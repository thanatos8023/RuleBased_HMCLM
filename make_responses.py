# -*- coding:utf-8 -*-
import json
import pickle


class Responses():
    def __init__(self):
        self.buttons = {

        }

        self.intentions = {
            'Control_Engine_Start': {
                'noTemp': {
                    'message': {
                        'text': '시동을 걸기 위해서는 온도 설정이 필요합니다. 온도를 몇 도로 설정할까요?'
                    }
                },
                'temp': {
                    'message': {
                        'text': '실내 온도를 %d 도로 설정합니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
                    }
                },
                'tempError': {
                    'message': {
                        'text': '잘못된 온도를 입력하셨습니다. 적절한 온도는 16 ~ 32 도 입니다.'
                    }
                }
            },
            'Control_Engine_Stop': {
                'message': {
                    'text': '시동을 끕니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
                }
            }
        }
        self.Control_Engine_Start = {
            'noTemp': {
                'message': {
                    'text': '시동을 걸기 위해서는 온도 설정이 필요합니다. 온도를 몇 도로 설정할까요?'
                }
            },
            'temp': {
                'message': {
                    'text': '실내 온도를 %d 도로 설정합니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
                }
            },
            'tempError': {
                'message': {
                    'text': '잘못된 온도를 입력하셨습니다. 적절한 온도는 16 ~ 32 도 입니다.'
                }
            }
        }

        self.Engine_Stop = {
            'message': {
                'text': '시동을 끕니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
            }
        }




def make_response(message_obj, btnlist, photo_obj):
    tmp = {}
    if not message_obj:
        tmp['message'] = {'text': '죄송하지만 잘 이해하지 못했어요.'}
    else:
        tmp['message'] = message_obj

        if photo_obj:
            tmp['message']['photo'] = photo_obj

        if btnlist:
            tmp['keyboard'] = {
                'type': 'buttons',
                'buttons': btnlist
            }

    return json.dumps(tmp)

buttons_response = {
    '블루핸즈 정비 예약 안내': {
        'message': {
            'text': '아래 전화번호를 누르시면 바로 예약 하실 수 있어요.\n1899-0600\n가까운 블루핸즈를 검색을 하시려면 아래 링크를 누르세요.',
            'message_button': {
                'label': '가까운 블루핸즈 검색',
                'url': 'https://www.hyundai.com/kr/ko/customer-service/service-network/service-reservation-search'
            }
        }
    },

    '처음으로 돌아가기': {
        'message': {
            'text': '원하는 기능이나 차에 대해 궁금하신 점을 말씀해주세요.\n예) 내차 23도로 시동 걸어줘'
        }
    },

    '차량 제어 도움말': {
        'message': {
            'text': "원격으로 시동/공조, 문닫기, 배터리 충전, 경적/비상등 제어를 할 수 있어요. 원격시동/공조 기능은 공조를 미리 제어하기 위해 시동이 함께 필요한 서비스이므로 따로 사용이 불가능해요."
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['원격 시동/공조 제어', '자동차 문 제어', '원격 충전 제어', '경적/비상등 제어']
        }
    },

    '원격 시동/공조 제어': {
        'message': {
            'text': '원격으로 시동을 켜고 끌 수 있어요. 원격시동/공조 기능은 공조를 미리 제어하기 위해 시동이 함께 필요한 서비스이므로 따로 사용이 불가능해요.'
        }
    },

    '자동차 문 제어': {
        'message': {
            'text': '원격으로 문을 잠글 수 있어요. 보안 문제로 문열기는 할 수 없어요.'
        }
    },

    '원격 충전 제어': {
        'message': {
            'text': '원격으로 배터리 충전을 시작하거나 멈출 수 있어요.'
        }
    },

    '경적/비상등 제어': {
        'message': {
            'text': '원격으로 경적을 울리고 비상등을 켜서 차 위치를 쉽게 찾을 수 있어요.'
        }
    },

    '블루링크 도움말': {
        'message': {
            'text': '블루링크를 이용할 때 궁금한 점을 물어보실 수 있어요. 블루링크 가입, 컨시어지, 긴급출동, 이용 요금 안내 등 궁금한 사항을 물어보세요.'
        }
    },

    '블루링크 가입': {
        'message': {
            'text': '차종/고객 유형에 따른 가입방법은 홈페이지의 \'서비스 가입\' 페이지에서 확인하실 수 있어요. 아래 링크를 클릭해주세요.',
            'message_button': {
                'label': '블루핸즈 FAQ',
                'url': 'http://m.bluelink.hyundai.com/support/faq_01.html'
            }
        }
    },

    '인증 비밀번호 변경': {
        'message': {
            'text': '블루링크 센터 또는 블루멤버스 홈페이지를 통해 변경이 가능해요.\n\n블루링크 센터\n - 전화 1899-0606\n - 업무시간: 평일 09:00 ~ 18:00(토/일요일 및 공휴일 휴무)'
        }
    },

    '블루링크 가입 정보 변경': {
        'message': {
            'text': '블루링크 센터를 통해 가입 정보를 변경하실 수 있어요.\n\n블루링크 센터\n - 전화 1899-0606\n - 업무시간: 평일 09:00 ~ 18:00(토/일요일 및 공휴일 휴무)'
        }
    },

    '블루링크 전화번호 확인': {
        'message': {
            'text': '내비게이션 홈 화면에서 [전체 메뉴] 선택 ▶[블루링크] 선택▶[블루링크 설정] 선택▶[모뎀 정보] 선택 후 \'전화번호\'에서 확인하실 수 있어요.\n***차종에 따라 확인 방법이 일부 상이할 수 있습니다.'
        }
    },

    '이용 요금 안내': {
        'message': {
            'text': '''블루링크는 차종에 따라 일정 기간 동안 기본 서비스(원격제어, 안전보안, 차량관리, 길안내)가 무료로 제공됩니다.
차종에 따른 기본 서비스 무료 제공 기간은 블루링크 홈페이지의 '요금제 안내'에서 확인하실 수 있습니다.
단, 신차 구매 후 최초 가입 고객에 한해 기본 서비스 무료 이용이 가능하며, 중고차 구매 후 가입을 하실 경우 유료로 제공됩니다.
컨시어지 서비스는 기본 서비스 무료 제공 기간과 상관없이 유료로 제공됩니다.
부가 서비스인 '컨시어지'에 가입하신 후 이용하실 수 있습니다.'''
        }
    },

    '그래, 한번 해보자': {
        'message': {
            'text': '제가 먼저 시작할게요. 우라늄! 제가 이겼죠!?'
        }
    },

    '아니, 됐어': {
        'message': {
            'text': '네, 필요하면 언제든지 또 불러주세요.'
        }
    },

    '시작하기': {
        'message': {
            'text': '안녕하세요! 차량을 쉽게 제어하도록 도와주는 차량 제어 봇이에요. 원하는 기능이나 차에 대해 궁금하신 점을 말씀해주세요.\n예) 내차 23도로 시동 걸어줘'
        }
    },

    #'제어 결과 확인': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    #),
    #'계속 제어하기': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #   photo_obj={}
    #),
    #'네': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    #),
    #'아니요': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    #),

    #'추천 해주세요!': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    #),
    #'괜찮아요~': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    #),
}

intention_response = {
    'Control_Charge_Start': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Charge_Stop': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Door_Close': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Door_Open': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Engine_Start': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Engine_Stop': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Horn_On': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Light_On': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Control_Only_Temp': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Call': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Conciousy': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_CryaneAccount': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Dismiss': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_DrivingControlError': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_EmergencyAccount': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_EmergencyGas': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_FamilyUse': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Miss': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_OnlyEngine': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Paycheck': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_PWChange': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Regist': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_RegularCheck': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_Riss': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'FAQ_UpdateUserInfo': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Help_AirCon': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Help_Can': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Help_Conversation': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Help_EngineOil': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Help_OnlyQuestion': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'Help_Repair': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_AgeRU': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Bye': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_DoingWhat': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Emoticon': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Fun': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Fword': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Gloomy': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Hello': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Hungry': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_LetsPlay': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_RUThere': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Thanks': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_Tired': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
    'SmallTalk_WhoRU': make_response(
        message_obj={},
        btnlist=[],
        photo_obj={}
    ),
}

if __name__ == '__main__':
    with open('response.pickle', 'wb') as f:
        pickle.dump(buttons_response, f)