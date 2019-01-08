# -*- coding:utf-8 -*-

import pickle
import json

error_response = {
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
    '7000': json.dumps({
        'message': {
            'text': '명령 입력이 대기중이에요. Pin번호를 입력해주세요!'
        }
    }),

    '8000': json.dumps({
        'message': {
            'text': '명령을 수행 중이에요. 한 번에 하나의 명령만 처리할 수 있어요. 다른 명령을 더 하시려면 잠시 후에 다시 시도해주세요.'
        }
    }),

    '4002': json.dumps({
        'message': {
            'text': '(Error 4002) 관리자에게 문의 해주세요!'
        }
    }),

    '4003': json.dumps({
        'message': {
            'text': '잘못 된 핀번호를 입력하셨어요. 핀번호를 다시 입력 해주세요.'
        }
    }),

    '4004': json.dumps({
        'message': {
            'text': '중복 된 명령이에요! 잠시 후 다시 시도 해주세요.'
        }
    }),

    '4005': json.dumps({
        'message': {
            'text': '(Error 4005) 내부 서버 오류에요.. 관리자에게 문의 해주세요!'
        }
    }),

    '4011': json.dumps({
        'message': {
            'text': '(Error 4011) 사용자 정보 기한이 만료되었어요. 사용자 정보 삭제 후 재 등록 해주세요. 계속 오류가 발생하면 관리자에게 문의 해주세요!'
        }
    }),

    '4081': json.dumps({
        'message': {
            'text': '(Error 4081) 내부 서버 오류에요.. 관리자에게 문의 해주세요!'
        }
    }),

    '5001': json.dumps({
        'message': {
            'text': '(Error 5001) 내부 서버 오류에요.. 관리자에게 문의 해주세요!'
        }
    }),

    '5031': json.dumps({
        'message': {
            'text': '(Error 5031) 서비스가 일시적으로 중단 되었어요.. 빠른 시일 내에 재개하겠습니다!'
        }
    }),

    '5041': json.dumps({
        'message': {
            'text': '(Error 5041) 관리자에게 문의하세요.'
        }
    })
}

buttons_response = {
    '블루핸즈 정비 예약 안내': json.dumps({
        'message': {
            'text': '아래 전화번호를 누르시면 바로 예약 하실 수 있어요.\n1899-0600\n가까운 블루핸즈를 검색을 하시려면 아래 링크를 누르세요.',
            'message_button': {
                'label': '가까운 블루핸즈 검색',
                'url': 'https://www.hyundai.com/kr/ko/customer-service/service-network/service-reservation-search'
            }
        }
    }),

    '처음으로 돌아가기': json.dumps({
        'message': {
            'text': '원하는 기능이나 차에 대해 궁금하신 점을 말씀해주세요.\n예) 내차 23도로 시동 걸어줘'
        }
    }),

    '차량 제어 도움말': json.dumps({
        'message': {
            'text': "원격으로 시동/공조, 문닫기, 배터리 충전, 경적/비상등 제어를 할 수 있어요. 원격시동/공조 기능은 공조를 미리 제어하기 위해 시동이 함께 필요한 서비스이므로 따로 사용이 불가능해요."
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['원격 시동/공조 제어', '자동차 문 제어', '원격 충전 제어', '경적/비상등 제어']
        }
    }),

    '원격 시동/공조 제어': json.dumps({
        'message': {
            'text': '원격으로 시동을 켜고 끌 수 있어요. 원격시동/공조 기능은 공조를 미리 제어하기 위해 시동이 함께 필요한 서비스이므로 따로 사용이 불가능해요.'
        }
    }),

    '자동차 문 제어': json.dumps({
        'message': {
            'text': '원격으로 문을 잠글 수 있어요. 보안 문제로 문열기는 할 수 없어요.'
        }
    }),

    '원격 충전 제어': json.dumps({
        'message': {
            'text': '원격으로 배터리 충전을 시작하거나 멈출 수 있어요.'
        }
    }),

    '경적/비상등 제어': json.dumps({
        'message': {
            'text': '원격으로 경적을 울리고 비상등을 켜서 차 위치를 쉽게 찾을 수 있어요.'
        }
    }),

    '블루링크 도움말': json.dumps({
        'message': {
            'text': '블루링크를 이용할 때 궁금한 점을 물어보실 수 있어요. 블루링크 가입, 컨시어지, 긴급출동, 이용 요금 안내 등 궁금한 사항을 물어보세요.'
        }
    }),

    '블루링크 가입': json.dumps({
        'message': {
            'text': '차종/고객 유형에 따른 가입방법은 홈페이지의 \'서비스 가입\' 페이지에서 확인하실 수 있어요. 아래 링크를 클릭해주세요.',
            'message_button': {
                'label': '블루핸즈 FAQ',
                'url': 'http://m.bluelink.hyundai.com/support/faq_01.html'
            }
        }
    }),

    '인증 비밀번호 변경': json.dumps({
        'message': {
            'text': '블루링크 센터 또는 블루멤버스 홈페이지를 통해 변경이 가능해요.\n\n블루링크 센터\n - 전화 1899-0606\n - 업무시간: 평일 09:00 ~ 18:00(토/일요일 및 공휴일 휴무)'
        }
    }),

    '블루링크 가입 정보 변경': json.dumps({
        'message': {
            'text': '블루링크 센터를 통해 가입 정보를 변경하실 수 있어요.\n\n블루링크 센터\n - 전화 1899-0606\n - 업무시간: 평일 09:00 ~ 18:00(토/일요일 및 공휴일 휴무)'
        }
    }),

    '블루링크 전화번호 확인': json.dumps({
        'message': {
            'text': '내비게이션 홈 화면에서 [전체 메뉴] 선택 ▶[블루링크] 선택▶[블루링크 설정] 선택▶[모뎀 정보] 선택 후 \'전화번호\'에서 확인하실 수 있어요.\n***차종에 따라 확인 방법이 일부 상이할 수 있습니다.'
        }
    }),

    '이용 요금 안내': json.dumps({
        'message': {
            'text': '''블루링크는 차종에 따라 일정 기간 동안 기본 서비스(원격제어, 안전보안, 차량관리, 길안내)가 무료로 제공됩니다.
차종에 따른 기본 서비스 무료 제공 기간은 블루링크 홈페이지의 '요금제 안내'에서 확인하실 수 있습니다.
단, 신차 구매 후 최초 가입 고객에 한해 기본 서비스 무료 이용이 가능하며, 중고차 구매 후 가입을 하실 경우 유료로 제공됩니다.
컨시어지 서비스는 기본 서비스 무료 제공 기간과 상관없이 유료로 제공됩니다.
부가 서비스인 '컨시어지'에 가입하신 후 이용하실 수 있습니다.'''
        }
    }),

    '그래, 한번 해보자': json.dumps({
        'message': {
            'text': '제가 먼저 시작할게요. 우라늄! 제가 이겼죠!?'
        }
    }),

    '아니, 됐어': json.dumps({
        'message': {
            'text': '네, 필요하면 언제든지 또 불러주세요.'
        }
    }),

    '시작하기': json.dumps({
        'message': {
            'text': '안녕하세요! 차량을 쉽게 제어하도록 도와주는 차량 제어 봇이에요. 원하는 기능이나 차에 대해 궁금하신 점을 말씀해주세요.\n예) 내차 23도로 시동 걸어줘'
        }
    }),

    # '제어 결과 확인': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    # ),
    # '계속 제어하기': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #   photo_obj={}
    # ),
    # '네': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    # ),
    # '아니요': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    # ),

    # '추천 해주세요!': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    # ),
    # '괜찮아요~': make_response(
    #    message_obj={
    #        'text': ''
    #    },
    #    btnlist=[],
    #    photo_obj={}
    # ),
}

target_syl = {
    'Control_Engine_Start': {
        'Rule': [
            {
                ('시동', 'NNG'),
                ('공조', 'NNG'),
                ('에어컨', 'NNG'),
                ('히터', 'NNG'),
                ('온도', 'NNG')
            },
            {
                ('켜', 'VV'),
                ('걸', 'VV'),
                ('켜', 'VV+EC'),
                ('맞춰', 'VV+EC'),
                ('맞춰라', 'VV+EC'),
                ('맞춰요', 'VV+EF'),
                ('걸어라', 'VV+EC'),
                ('맞', 'VV'),
                ('설정', 'NNG'),
                ('조절', 'NNG'),
                ('온', 'NNG'),
                ('온', 'VV+ETM'),
                ('on', 'SL')
            }
        ],
        'Response': {
            'noTemp': json.dumps({
                'message': {
                    'text': '시동을 걸기 위해서는 온도 설정이 필요합니다. 온도를 몇 도로 설정할까요?'
                }
            }),
            'temp': json.dumps({
                'message': {
                    'text': '실내 온도를 {} 도로 설정합니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
                }
            }),
            'tempError': json.dumps({
                'message': {
                    'text': '잘못된 온도를 입력하셨습니다. 적절한 온도는 16 ~ 32 도 입니다.'
                }
            })
        }
    },

    'Control_Engine_Stop': {
        'Rule': [
            {
                ('시동', 'NNG'),
                ('공조', 'NNG'),
                ('에어컨', 'NNG'),
                ('히터', 'NNG'),
                ('차', 'NNG')
            },
            {
                ('꺼', 'VV+EC'),
                ('끄', 'VV'),
                ('꺼라', 'VV+EC'),
                ('꺼', 'VV'),
                ('꺼', 'NNB+VCP'),
                ('오프', 'NNG'),
                ('off', 'SL')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '시동을 끕니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
            }
        })
    },

    'Control_Door_Open': {
        'Rule': [
            {
                ('문', 'NNG'),
                ('차문', 'NNG'),
                ('도어', 'NNG'),
                ('어', 'IC')
            },
            {
                ('열', 'VV')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '문 잠김을 입력하시면 원격으로 문을 잠글 수 있어요. 그렇지만 보안 문제로 문 열기는 할 수 없어요.'
            }
        })
    },

    'Control_Door_Close': {
        'Rule': [
            {
                ('문', 'NNG'),
                ('차문', 'NNG'),
                ('도어', 'NNG'),
                ('어', 'IC')
            },
            {
                ('닫', 'VV'),
                ('잠궈', 'VV+EC')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '문을 잠급니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
            }
        })
    },

    'Control_Horn_On': {
        'Rule': [
            {
                ('경적', 'NNG'),
                ('크락', 'NNP'),
                ('션', 'NNG'),
                ('션', 'NNP')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '경적을 켭니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
            }
        })
    },

    'Control_Light_On': {
        'Rule': [
            {
                ('깜빡이', 'NNG'),
                ('비상', 'NNG'),
                ('등', 'NNB')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '비상등을 켭니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
            }
        })
    },

    'Control_Charge_Start': {
        'Rule': [
            {
                ('충전', 'NNG')
            }
        ],
        'Response': json.dumps({
            'text': '충전을 시작합니다. 기능 수행을 위해 Pin 번호를 입력해주세요.'
        })
    },

    'Control_Charge_Stop': {
        'Rule': [
            {
                ('충전', 'NNG')
            },
            {
                ('멈춰', 'VV+EC'),
                ('그만', 'MAG'),
                ('그만', 'XR'),
                ('종료', 'NNG'),
                ('중지', 'NNG'),
            },
        ],
        'Response': json.dumps({
            'message': {
                'text': '충전을 중단합니다. 기능 수행을 위해 Pin 번호를 입력하세요.'
            }
        })
    },

    'Help_AirCon': {
        'Rule': [
            {
                ('에어컨', 'NNG'),
                ('에어', 'NNP'),
                ('콘', 'NNG')
            },
            {
                ('냄새', 'NNG')
            },
        ],
        'Response': json.dumps({
            "message": {
                "text": '에어컨 탈취제를 사용하시면 일시적으로는 개선될수 있어요. 하지만, 정확한 원인 확인을 위해 블루핸즈에 방문해 보시는 것이 좋겠어요. 방문 예약을 진행할까요?\n방문예약을 원하시면 1899-0600으로 연락주세요.',
                "message_button": {
                  "label": "가까운 블루핸즈 검색",
                  "url": 'https://www.hyundai.com/kr/ko/customer-service/service-network/service-reservation-search'
                }
            }
        })
    },

    'Help_Can': {
        'Rule': [
            {
                ('할', 'VV+ETM')
            },
            {
                ('수', 'NNB'),
                ('줄', 'NNB')
            },
        ],
        'Response': json.dumps({
            "message": {
                "text": '저는 차를 원격으로 제어하고 궁금한 것들에 대해 답변을 드릴 수 있어요.'
            },
            "keyboard": {
                "type": 'buttons',
                'buttons': ['차량 제어 도움말', '블루링크 도움말', '블루핸즈 정비 예약 안내']
            }
        })
    },

    'Help_Conversation': {
        'Rule': [
            {
                ('상담', 'NNG')
            }
        ],
        'Response': json.dumps({
            "message": {
                "text": '채팅 상담을 원하시면 아래 링크를 클릭해 주세요. 전화 상담을 원하시면 아래 전화번호를 눌러주세요.\n1899-0600',
                "message_button": {
                    "label": "현대 블루핸즈",
                    "url": 'https://www.hyundai.com/kr/ko/customer-service/service-network/service-reservation-search'
                }
            }
        })
    },

    'Help_EngineOil': {
        'Rule': [
            {
                ('엔진오일', 'NNP'),
                ('엔진', 'NNG'),
                ('오', 'NR'),
                ('일', 'NNBC')
            },
            {
                ('교체', 'NNG'),
                ('교환', 'NNG'),
                ('갈', 'VV'),
                ('갈지', 'VV+EC'),
                ('갈', 'VV+ETM')
            },
            {
                ('주기', 'NNG'),
                ('언제', 'MAG'),
                ('때', 'NNG'),
            }
        ],
        'Response': json.dumps({
            "message": {
                "text": '엔진오일 교환 주기는 통상/가혹 조건에 따라 교환해주시면 되는데, 통상조건으로는 매 15,000㎞(또는 12개월), 가혹조건으로는 매 7,500㎞(또는 6개월)마다 교환해 주시면 좋을것 같습니다.\n\n ※단, 차종 및 엔진별 엔진오일 교환주기는 다르기 때문에, 취급설명서내 정기점검 주기표를 참고 바랍니다. 그랜저 정기 점검 주기표',
                "photo": {
                    "url": "http://13.125.73.118:3000/image/igoil.jpg",
                    "width": 640,
                    "height": 480
                }
            },
            "keyboard": {
                "type": 'buttons',
                'buttons': ['블루핸즈 정비 예약 안내', '처음으로']
            }
        })
    },

    'Help_OnlyQuestion': {
        'Rule': [
            {
                ('이상', 'NNG')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '이상한 부분이 어딘지 알려 주시겠어요?'
            }
        })
    },

    'Help_Repair': {
        'Rule': [
            {
                ('정비', 'NNG'),
                ('핸즈', 'NNP')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '아래 전화번호를 누르시면 바로 예약 하실 수 있어요.\n1899-0600\n가까운 블루핸즈를 검색을 하시려면 아래 링크를 누르세요.',
                'message_button': {
                    'label': '가까운 블루핸즈 검색',
                    'url': 'https://www.hyundai.com/kr/ko/customer-service/service-network/service-reservation-search'
                }
            }
        })
    },

    'SmallTalk_AgeRU': {
        'Rule': [
            {
                ('살', 'NNBC'),
                ('짤', 'VV+ETM')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '저는 이제 한 살이에요. 아직 배울 게 많답니다.'
            }
        })
    },

    'SmallTalk_Bye': {
        'Rule': [
            {
                ('바이', 'NNG'),
                ('갈게', 'VV+EC'),
                ('빠이', 'IC'),
                ('가', 'VV+EC'),
            }
        ],
        'Response': json.dumps({
            'text': '네~필요한 게 있으면 언제든지 찾아 주세요.'
        })
    },

    'SmallTalk_DoingWhat': {
        'Rule': [
            {
                ('뭐', 'IC'),
                ('머', 'NP'),
            },
            {
                ('해', 'VV+EC'),
                ('해', 'VV+EF'),
                ('있', 'VX'),
                ('냐', 'EF'),
                ('냐', 'EC')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '음, 그랜저에 대해 생각하고 있었어요. 아무리 생각해도 참 좋은 차인 것같아요.'
            }
        })
    },

    #'SmallTalk_Emoticon': {
    #    'Necessary': [
    #    ],
    #    'Special': {}
    #},

    'SmallTalk_Fun': {
        'Rule': [
            {
                ('얘기', 'NNG'),
                ('유머', 'NNG'),
                ('이야기', 'NNG'),
                ('재밌', 'VA'),
                ('재미있', 'VA'),
                ('웃겨', 'VV+EC'),
                ('웃기', 'VV')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '제가 개그에 소질은 없지만 최선을 다해볼게요. 바나나한테 반하나?'
            }
        })
    },

    #'SmallTalk_Fword': {},

    'SmallTalk_Gloomy': {
        'Rule': [
            {
                ('우울', 'NNG'),
                ('울적', 'NNG'),
                ('슬퍼', 'VA+EC')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '저는 우울할 땐 경치 좋은 곳으로 드라이브를 가곤 해요. 주변에 드라이브 하기 좋은 곳 몇군데를 추천해드릴까요?'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['추천 해주세요!', '괜찮아요~']
            }
        })
    },

    'SmallTalk_Hello': {
        'Rule': [
            {
                ('안녕', 'NNG'),
                ('하이', 'NNG'),
                ('헬로', 'NNP'),
                ('방가', 'NNG'),
                ('안녕', 'IC'),
                ('뇽', 'UNKNOWN'),
                ('반가워', 'VA+EC'),
                ('헬로우', 'IC'),
                ('hi', 'SL'),
                ('hello', 'SL')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '안녕하세요 ^^'
            }
        })
    },

    'SmallTalk_Hungry': {
        'Rule': [
            {
                ('배고파', 'VA+EC'),
                ('배고프', 'VA'),
                ('출출', 'XR')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '어서 식사를 하시는 게 좋겠어요. 주변에 맛집을 몇 개 추천해드릴까요?'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['추천 해주세요!', '괜찮아요~']
            }
        })
    },

    'SmallTalk_LetsPlay': {
        'Rule': [
            {
                ('심심', 'NNG'),
                ('심심', 'XR'),
                ('놀', 'VV')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '저랑 끝말잇기 하실래요?'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['그래', '괜찮아요~']
            }
        })
    },

    'SmallTalk_RUThere': {
        'Rule': [
            {
                ('여보세요', 'IC'),
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '네?'
            }
        })
    },

    'SmallTalk_Thanks': {
        'Rule': [
            {
                ('고마워', 'VA+EC'),
                ('기특', 'XR'),
                ('좋', 'VA'),
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '제가 도움이 되었다니 기뻐요.'
            }
        })
    },

    'SmallTalk_Tired': {
        'Rule': [
            {
                ('잠', 'NNG'),
                ('피곤', 'NNG'),
                ('지침', 'NNG'),
                ('졸려', 'VA+EC'),
                ('졸린다', 'VV+EC'),
                ('지쳐', 'VV+EC'),
                ('지쳤', 'VV+EP'),
                ('자', 'VV'),
                ('잠자', 'VV'),
                ('힘들', 'VA'),
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '휴식을 조금 취하시는 게 좋겠어요. 당장 휴식을 할 수 없다면 스트레칭과 커피가 졸음 깨는데 도움이 된답니다.'
            }
        })
    },

    'SmallTalk_WhoRU': {
        'Rule': [
            {
                ('누구', 'NP')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '저는 당신의 이동을 스마트하게 도와주는 그랜저 비서에요.'
            }
        })
    },

    'FAQ_Call': {
        'Rule': [
            {
                ('번호', 'NNG')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '내비게이션 홈 화면에서 [전체 메뉴] 선택 ▶[블루링크] 선택▶[블루링크 설정] 선택▶[모뎀 정보] 선택 후 \'전화번호\'에서 확인하실 수 있어요.\n *차종에 따라 확인 방법이 일부 상이할 수 있습니다.'
            }
        })
    },
    'FAQ_Conciousy': {
        'Rule': [
            {
                ('컨', 'NNP')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '컨시어지 서비스는 룸미러의 b버튼을 눌러 블루링크 센터 상담원 연결 후 이용하실 수 있어요. 컨시어지 서비스 이용을 위해서는 유료 부가 서비스인 \'컨시어지\'에 먼저 가입하셔야 해요. *컨시어지 사입시 월 9,00원(부가세 포함)이 부과되면, 블루링크 폰(음성통화) 사용시 2.09원/초(부가세 포함)의 통화료가 발생합니다. 단, 상담원 길안내는 통화료 별도로 부과되지 않습니다.'
            }
        })
    },
    'FAQ_Dismiss': {
        'Rule': [
            {
                ('해지', 'NNG')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '블루링크 센터를 통해 서비스를 해지하실 수 있어요.\n블루링크 센터\n- 전화: 1899-0606\n- 업무시간: 평일 09:00 ~ 18:00 (토/일요일 및 공휴일 휴무)\n자세한 내용은 아래 링크를 참조하세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['현대 블루링크']
            }
        })
    },
    'FAQ_CryaneAccount': {
        'Rule': [
            {
                ('견인', 'NNG')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '도로를 이탈하거나 장애물 등으로 인해 자력 주행이 불가능하여 구난이 필요하면 긴급구난 서비스가 제공됩니다. 그러나 이 경우 별도의 구난장비 없이 견인차(렉카)로 구난이 가능한 경우에 한하며, 별도의 구난장비가 필요하거나 작업 난이도에 따라 추가비용을 지급해야 합니다. 또한 구난작업 30분 초과시(현장도착에서 완료까지의 시가) 별도의 비용을 부담하여야 합니다.'
            }
        })
    },
    'FAQ_DrivingControlError': {
        'Rule': [
            {
                ('주행', 'NNG'),
            },
            {
                ('조작', 'NNG'),
                ('움직이', 'VV')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '안전한 운행을 위해 주행 중에는 단말기 조작을 제한하고 있으며, 기어가 P단일 경우만 조작이 가능해요. 시스템 조작을 통해 서비스를 이용하시려면 차량을 잠시 정차해주세요. 단, 조작이 간단한 일부 서비스는 주행 중에도 사용이 가능해요.'
            }
        })
    },
    'FAQ_EmergencyAccount': {
        'Rule': [
            {
                ('긴급', 'NNG')
            },
            {
                ('출동', 'NNG')
            }
        ],
        'Response': json.dumps({
            'message': {
                'text': '현대 긴급출동의 경우, 보증수리 대상은 출동비가 무상이지만 보증수리 초과 차량의 출동비는 현장에서 청구됩니다. 보증수리 차량도 출동비는 무상이지만 소요된 부품 등에 대해서는 고객이 비용을 지급해야 해요.'
            }
        })
    },
    'FAQ_EmergencyGas': {
        'Rule': [
            {
                ('주유', 'NNG'),
                ('급유', 'NNG')
            },
        ],
        'Response': json.dumps({
            'message': {
                'text': '현대 긴급출동의 경우, 보증수리 대상은 출동비가 무상이지만 보증수리 초과 차량의 출동비는 현장에서 청구됩니다. 보증수리 차량도 출동비는 무상이지만 소요된 부품 등에 대해서는 고객이 비용을 지급해야 해요.'
            }
        })
    }
}

pin_response = {
    'Control_Engine_Start': json.dumps({
        'message': {
            'text': '차량 내부 온도 {} 도로 원격 시동을 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),

    'Control_Engine_Stop': json.dumps({
        'message': {
            'text': '원격 시동을 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),

    'Control_Door_Close': json.dumps({
        'message': {
            'text': '원격 문 잠금을 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),

    'Control_Light_On': json.dumps({
        'message': {
            'text': '원격 비상등 켜기를 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),

    'Control_Horn_On': json.dumps({
        'message': {
            'text': '원격 경적 켜기를 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),

    'Control_Charge_Start': json.dumps({
        'message': {
            'text': '원격 충전을 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),

    'Control_Charge_Stop': json.dumps({
        'message': {
            'text': '원격 충전을 요청했어요. 차량 상태는 블루링크 앱에서 확인해주세요.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['제어 결과 확인', '처음으로']
        }
    }),
}

dm = {
    'Buttons': buttons_response,
    'Intentions': target_syl,
    'Errors': error_response,
    'Pin': pin_response
}


if __name__ == '__main__':
    with open('dm.pickle', 'wb') as f:
        pickle.dump(dm, f)