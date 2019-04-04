# -*- coding:utf-8 -*-

#from eunjeon import Mecab
import mecab
import re
import json
import pymysql

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
        if type(req) == str:
            req_body = json.loads(req)
        else:
            req_body = req

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

        # DB 교체
        self.dm = self.get_DM_from_DB()

        # 사용자 발화에서 pin 을 찾는 코드
        # pin이 아닐 경우, False 가 저장됨
        self.pin = self.__get_pin__()

        # 사용자 발화에서 intention 을 찾는 코드
        # intention 찾기에 실패한 경우, False 가 저장됨
        # 현재 pin 이나 온도가 입력될 경우 False 가 저장되고 있음
        self.intention = self.__get_intention__()

        ## 응답 형식

    ## 미완성
    def make_response(self):
        # DB 연결
        connection = pymysql.connect(
            host='127.0.0.1',
            user='hmc',
            password='mediazen',
            db='hmc_chatbot',
        )

        with connection.cursor() as user_cursor:
            user_sql = 'SELECT * FROM tb_user_info WHERE kakao_info=%s'
            user_cursor.execute(user_sql, (self.user_key))

            user_info = user_cursor.fetchone()

            if not user_info:
                return self.dm["Intentions"]



    def get_responseForm(self, response_text_row_in_db):
        # column name and index matching
        # domain            :   0
        # intention         :   1
        # chatbot_status    :   2
        # response_type     :   3
        # response_text     :   4
        # response_object1  :   5
        # response_object2  :   6

        #print(response_text_row_in_db)

        responseForm = {
            "type": response_text_row_in_db[3],
            "text": response_text_row_in_db[4],
            "object1": response_text_row_in_db[5],
            "object2": response_text_row_in_db[6]
        }

        return responseForm

    def str2obj(self, rulestr):
        # string: ooo/NNN,qqq/SSS
        # object: {('ooo', 'NNN'), ('qqq', 'SSS')}
        if not rulestr is None:
            splitted_morph = rulestr.split(',')

            result = []
            for morph_tag in splitted_morph:
                result.append(tuple(morph_tag.split('/')))
            return set(result)
        else:
            return "NaN"

    # DB 에서 DM 정보를 불러오는 함수
    ### DB 에 필요한 필드
    # 'Buttons': 버튼 입력 목록 (* FROM tb_user_input WHERE intention=button)
    # 'Intentions': 의도와 필수형태소 객체 (* FROM tb_rule WHERE intention, rule)
    # 'Errors': 에러 반응 텍스트 (* FROM tb_user_input WHERE intention=error)
    # 'Pin': PIN 입력 후 대화 반응 (삭제 예정)
    def get_DM_from_DB(self):
        # DB 연결
        connection = pymysql.connect(
            host='127.0.0.1',
            user='hmc',
            password='mediazen',
            db='hmc_chatbot',
        )

        with connection.cursor() as cursor:
            ## Buttons 채우기
            sql = 'SELECT * FROM tb_response_text WHERE intention="Button"'
            cursor.execute(sql)

            # key: button label
            # value: response form
            buttons = {}
            for row in cursor:
                # setting response form
                # response form example
                # {
                #   "type": ..,
                #   "text": ..,
                #   "buttons": ..,
                #   ..
                # }
                buttons[row[2]] = self.get_responseForm(row)

            ## Buttons 완성: 변수명 buttons

            ## Errors 채우기
            sql = 'SELECT * FROM tb_response_text WHERE intention="Error"'
            cursor.execute(sql)

            # key: error number (string)
            # value: response form
            errors = {}
            for row in cursor:
                errors[row[2]] = self.get_responseForm(row)

            ## Errors 완성: 변수명 errors

            ## Intentions 채우기
            intentions = {}
            # 의도 목록이 필요함
            sql = 'SELECT * FROM tb_user_input'
            cursor.execute(sql)
            intention_list = []
            for row in cursor:
                intention_list.append(row[1])
            intention_set = list(set(intention_list))

            # 의도 목록 intention_set
            # 의도 목록을 기준으로 Rule과 Response를 정리함
            for intention in intention_set:
                # 규칙 가져오기
                rule_sql = 'SELECT * FROM tb_rule WHERE intention=%s'
                nrows = cursor.execute(rule_sql, (intention))
                if nrows == 0:
                    continue

                rule_result = cursor.fetchone()

                rule_temp = []
                for col in rule_result:
                    if col in ['Control_Car', 'FAQ', 'SmallTalk', intention]:
                        continue

                    rule = self.str2obj(col)
                    if rule == "NaN":
                        continue
                    rule_temp.append(rule)

                # 규칙 가져오기 끝: 변수명 rule_temp

                # 응답 가져오기
                res_sql = 'SELECT * FROM tb_response_text WHERE intention=%s'
                cursor.execute(res_sql, (intention))

                res_temp = {}
                for status_row in cursor:
                    res_temp[status_row[2]] = self.get_responseForm(status_row)

                # 응답 가져오기 끝: 변수명 res_temp

                # 의도 채우기
                intentions[intention] = {
                    'Rule': rule_temp,
                    'Response': res_temp
                }

            ## Intentions 완성: 변수명 intentions

            ## Pin은 삭제

        # DB 닫기
        connection.close()

        # 결과
        dm = {
            'Buttons': buttons,
            'Errors': errors,
            'Intentions': intentions,
        }

        return dm


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
            # 추측도 불가능한 발화의 경우, Fail 을 반환
            else:
                intention = self.__get_intention_from_lm__()

                if intention:
                    return intention
                else:
                    return "Fail"

    # Rule 과 비교하여 intention 을 찾는 함수
    def __get_intention_from_lm__(self):
        # Searching in intentions
        for key in self.dm['Intentions'].keys():
            matched_case = 0
            for necset in self.dm['Intentions'][key]['Rule']:
                # There are set of morphs
                print("Intention:", key)
                print("Morph set:", necset)
                matched = necset & set(self.pos)
                if not matched:
                    continue
                else:
                    matched_case += 1

            if (matched_case == len(self.dm['Intentions'][key]['Rule'])) and matched_case:
                # This case, the utterance is in this intention
                return key

        return "Fail"

    # 코퍼스에서 입력 발화를 검색하는 함수
    def __get_intention_from_corpus__(self):
        # DB 연결
        connection = pymysql.connect(
            host='127.0.0.1',
            user='hmc',
            password='mediazen',
            db='hmc_chatbot',
        )

        with connection.cursor() as cur:
            sql = 'SELECT * FROM tb_user_input'
            cur.execute(sql)

            for row in cur:
                if self.utt == row[2]:
                    return row[1]

        return None


if __name__ == '__main__':
    req = {
        'user_key': 'sf1234dsf',
        'utt': '17도로 시동 켜줘',
        'code': 7000,
        'intention': '',
        'options': 0
    }

    m = Model(req)

    print(m.intention)