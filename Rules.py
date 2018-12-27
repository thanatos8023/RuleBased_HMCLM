# -*- coding:utf-8 -*-

#from eunjeon import Mecab
import mecab
import re
import json
import os
import glob
import pickle
import random


class Model(object):
    def __init__(self, req):
        ###################################
        # Request form
        # 'utt': User input utterance
        # 'code': Status Code
        #   API Server Code
        #   '7000': first input
        #   '7001': No necessery slots (Control_Engine_Start only)
        #   '8000': After pin input, yet processed previous command
        #
        #   Bluelink Server Code
        #   '200': Vehicle control Successed
        #   '4002': Invalid Request Body
        #   '4003': Invalid pin
        #   '4004': Duplicate request
        #   '4005': Unsupported control request
        #   '4011': Invalid access token
        #   '4081': Request timeout
        #   '5001': Internal Server Error
        #   '5031': Service Temporary Unavailable
        #   '5041': Gateway timeout
        # 'user_key': Identifier for users
        ####################################

        # 형태소 분석기 Mecab 불러오기
        self.mecab = mecab.MeCab()

        # API 서버에서 요청은 json 형식으로 전달된다.
        # 전달된 json을 parsing 해서 dictionary로 활용함
        # json 모듈 활용
        print(req)
        req_body = json.loads(req)

        # API 서버에서 받은 요청을 활용하기 쉽도록 개별 변수에 저장한다.
        # utt: 사용자 입력 발화
        # code: 현재 상태를 나타내는 Status 코드 자세한 내용은 위의 주석 참조
        # user_key: 발화를 입력한 사용자를 구분하기 위한 id. 암호화 되어있음
        self.utt = req_body['utt']
        self.code = req_body['code']
        self.user_key = req_body['user_key']

        # 대화의 Depth 가 깊어질 경우,
        # 보존해야하는 정보가 발생함
        # (예, 시동 걸기 시에 온도 정보는 pin 입력 시까지 보존할 필요가 있음)
        # 이 정보는 req['options']에 저장됨
        # options 목록
        # 1. 실내 온도 ('temp')
        self.options = req_body['options']

        # LM Rule을 확인하기 위해서는 형태소 분석이 필요하다.
        # 사용자 입력 발화를 형태소 분석하는 코드
        # 이렇게 분석된 발화는 다음과 같은 형태를 가지게 된다.
        # (예)
        # 입력 발화: 시동 걸어
        # pos: [
        #   ('시동', 'NNG'),
        #   ('걸', 'VV'),
        #   ('어', 'EC'),
        # ]
        self.pos = self.mecab.pos(self.utt)

        # LM Rule 및 Response form 이 정리된 파일 불러오기
        # 이후로 DB 로 대체도 가능
        # 불러온 정보는 dictionary 형식으로 저장됨
        # 자세한 형식은 make_rule.py 참조
        with open('dm.pickle', 'rb') as f:
            self.dm = pickle.load(f)

        # 사용자 발화에서 pin 을 찾는 코드
        # pin이 아닐 경우, False 가 저장됨
        self.pin = self.__get_pin__()

        # 사용자 발화에서 intention 을 찾는 코드
        # intention 찾기에 실패한 경우, False 가 저장됨
        # 현재 pin 이나 온도가 입력될 경우 False 가 저장되고 있음
        if req_body['intention']:
            self.intention = req_body['intention']
        else:
            self.intention = self.__get_intention__()

    # 사용자 입력 발화에서 pin을 찾는 함수
    def __get_pin__(self):
        # 정규식을 활용함
        # 4자리 숫자를 입력할 경우, pin으로 간주함
        pin = re.match('\d\d\d\d', self.utt)
        if not pin:
            return False
        else:
            return pin.group()

    # 사용자 입력 발화에서 온도를 찾는 함수
    def get_temperature_from_utterance(self):
        # 정규식을 활용함
        # 숫자의 연쇄를 찾아서, 이를 숫자로 변환하고, 온도로 반환
        temp_match = re.match('\d+', self.utt)

        # 숫자가 없을 경우도 고려함
        # '최대', '최고' 등이 발화 안에 있는 경우, 자동으로 32도로 설정
        # '최소', '최저' 등이 발화 안에 있는 경우, 자동으로 16도로 설정
        # '적당' 등이 발화 안에 있는 경우, 자동으로 24도로 설정
        if not temp_match:
            max_match = {('최대', 'NNG'), ('최고', 'NNG')} & set(self.pos)
            min_match = {('최소', 'NNG'), ('최저', 'NNG')} & set(self.pos)
            mid_match = {('적당', 'XR')} & set(self.pos)

            if max_match:
                return 32
            elif min_match:
                return 16
            elif mid_match:
                return 24
            # 숫자도 없고, 앞서 제시한 형태소들도 보이지 않을 시, -1을 반환
            else:
                return -1
        # 숫자가 있을 경우
        else:
            temp = int(temp_match.group())
            # 이 숫자가 적절한 온도의 범위 안에 있을 경우에만 온도를 반환
            if 15 < temp < 33:
                return temp
            # 숫자는 있는데 온도의 범위를 벗어난 경우에는 -273을 반환
            else:
                return -273

    # intention 반환 함수
    # intention 탐색 순서: 버튼인가? -> 코퍼스에 등록된 발화인가? -> Rule에 맞는 발화인가?
    def __get_intention__(self):
        # 버튼일 경우,
        # 바로 'Buttons'를 반환하고 종료
        if self.utt in self.dm['Buttons'].keys():
            return 'Buttons'
        else:
            # 버튼이 아닐 경우,
            # 먼저 코퍼스 탐색함
            # 코퍼스에 있는 발화일 경우, 코퍼스 이름(intention)이 반환됨
            # 없는 발화일 경우, False 가 반환됨
            intention = self.__get_intention_from_corpus__()

            # 코퍼스에 해당 발화가 있을 경우,
            # intention 을 반환하고 바로 종료
            if intention:
                return intention
            # 코퍼스에 해당 발화가 없을 경우,
            # Rule 을 이용해서 intention 을 추측함.
            # 추측도 불가능한 발화의 경우, None 을 반환
            else:
                intention = self.__get_intention_from_lm__()

                if intention:
                    return intention
                else:
                    return None

    # Rule 과 비교하여 intention 을 찾는 함수
    def __get_intention_from_lm__(self):
        # Searching in intentions
        for key in self.dm['Intentions'].keys():
            matched_case = 0
            for necset in self.dm['Intentions'][key]['Rule']:
                # There are set of morphs
                # matched
                matched = necset & set(self.pos)
                if not matched:
                    break
                else:
                    matched_case += 1

            if matched_case == len(self.dm['Intentions'][key]['Rule']):
                # This case, the utterance is in this intention
                return key

        return None

    # 코퍼스에서 입력 발화를 검색하는 함수
    def __get_intention_from_corpus__(self):
        # corpus loading
        filelist = glob.glob('corpus/*.txt')
        for file in filelist:
            # searching file by file (= intention by intention)
            with open(file, 'r', encoding='utf-8') as f:
                corpus_intention = os.path.basename(file).replace('.txt', '')
                corpus_raw = f.read().split('\n')

            for raw_sent in corpus_raw:
                if raw_sent == self.utt:
                    return corpus_intention

        return None


def insert_temperature_into_json(form_data, temp):
    # form_data = json
    # temp = {}.format
    form = json.loads(form_data)
    form['message']['text'] = form['message']['text'] % temp

    return json.dumps(form)


# 요청에 대한 응답을 만드는 함수
def make_response(model):
    response_template = {
        'status': '',
        'form': '',
        'user_key': '',
        'intention': '',
        'options': 0
    }
    # Step 1
    if model.pin and model.code == '7000':
        if model.intention == "Control_Engine_Start":
            response_template['form'] = insert_temperature_into_json(model.dm['Pin'][model.intention], model.options)
        else:
            response_template['form'] = model.dm['Pin'][model.intention]
        response_template['status'] = '8000'
        response_template['user_key'] = model.user_key
        response_template['intention'] = model.intention
        return response_template

    # Step 2
    if model.code in model.dm['Errors'].keys():
        response_template['form'] = model.dm['Errors'][model.code]
        response_template['status'] = '100'
        response_template['user_key'] = model.user_key
        response_template['intention'] = model.intention
        return response_template

    # Step 3
    if model.intention:
        if model.intention == 'Buttons':
            response_template['form'] = model.dm[model.intention][model.utt]
            response_template['status'] = '100'
            response_template['user_key'] = model.user_key
            response_template['intention'] = model.intention

        elif model.intention == 'Control_Engine_Start':
            temp = model.get_temperature_from_utterance()
            if temp == -1:
                response_template['status'] = '7001'
                response_template['form'] = model.dm['Intentions'][model.intention]['Response']['noTemp']
            elif temp == -273:
                response_template['status'] = '7001'
                response_template['form'] = model.dm['Intentions'][model.intention]['Response']['tempError']
            else:
                response_template['status'] = '7000'
                response_template['form'] = insert_temperature_into_json(model.dm['Intentions'][model.intention]['Response']['temp'], int(temp))
                response_template['options'] = temp

            response_template['user_key'] = model.user_key
            response_template['intention'] = model.intention

        else:
            response_template['form'] = model.dm['Intentions'][model.intention]['Response']
            if model.intention.find('Control') > -1 and not model.intention == 'Control_Door_Open':
                response_template['status'] = '8000'
            else:
                response_template['status'] = '100'
            response_template['user_key'] = model.user_key
            
            response_template['intention'] = model.intention

    else:
        response_template['form'] = json.dumps({
            'message': {
                'text': '죄송해요... 제가 잘 이해하지 못했어요.'
            }
        })
        response_template['status'] = '100'
        response_template['user_key'] = model.user_key
        response_template['intention'] = model.intention

    return response_template


def evaluation():
    req = {
        'utt': '',
        'code': 7000,
        'user_key': 'asdfqew52',
        'intention': '',
        'options': 0
    }

    while True:
        message = input('사용자 입력: ')

        if message == '나가기':
            break
        else:
            req['utt'] = message

        m = Model(json.dumps(req))

        res = make_response(m)

        res_dict_form = json.loads(res['form'])
        ###################################
        # Response form
        # 'form': json form for sending to chatting API
        # 'status': code for processing dialog
        # 'user_key': identification for user
        ####################################

        if res['status'] == '100':
            req['code'] = ''
            req['intention'] = ''
        else:
            req['code'] = res['status']
            req['intention'] = res['intention']
            req['options'] = res['options']

        print(res_dict_form['message']['text'])


def get_score():
    filelist = glob.glob('corpus/Control*.txt')
    raw = []
    for filename in filelist:
        with open(filename, 'r', encoding='utf-8') as f:
            raw += f.read().split('\n')

    random.shuffle(raw)
    test = raw[:1000]

    n = 0

    correction = []
    incorrect = []

    for sent in test:
        req = {
            'utt': sent,
            'code': 7000,
            'user_key': 'asdfqew52',
            'intention': '',
            'options': 0
        }

        m = Model(json.dumps(req))

        if m.intention:
            correction.append((sent, m.intention))
        else:
            incorrect.append((sent, m.intention))

    for i in range(100):
        print("{} ---> {}".format(correction[i][0], correction[i][1]))

    print("Correction: ", len(correction) / len(test))

    if not incorrect == []:
        print('-'*30)
        print('Incorrection')
        for i in range(5):
            print("{} ---> {}".format(incorrect[i][0], incorrect[i][1]))


if __name__ == '__main__':
    #evaluation()
    get_score()