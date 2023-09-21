'''
1. 이 소스 코드는 hgtk 라이브러리를 필요로 하기 때문에 hgtk 라이브러리를 설치해야 합니다 (pip install hgtk)
2. 한글의 창작 원리인 자음 체계표와 모음 체계표를 사용해 시를 변환했습니다. 가장 한글의 아름다움을 보여줄 수 있는 방법이라고 생각했습니다.
'''

import hgtk

RESET = "\033[0m"
BOLD = "\033[1m"

constant_char = {
  "파열": {
    "양순": {
      "예사": "ㅂ",
      "된": "ㅃ",
      "거센": "ㅍ"
    },
    "치조": {
      "예사": "ㄷ",
      "된": "ㄸ",
      "거센": "ㅌ"
    },
    "연구개": {
      "예사": "ㄱ",
      "된": "ㄲ",
      "거센": "ㅋ"
    }
  },
  "파찰": {
    "경구개": {
      "예사": "ㅈ",
      "된": "ㅉ",
      "거센": "ㅊ"
    }
  },
  "마찰": {
    "치조": {
      "예사": "ㅅ",
      "된": "ㅆ",
    },
    "후": "ㅎ"
  },
  "비음": {
    "양순": "ㅁ",
    "치조": "ㄴ",
    "연구개": "ㅇ"
  },
  "유음": {
    "치조": "ㄹ"
  }
}
vowels_char = {
  "전설": {
    "평순": {
      "고": "ㅣ",
      "중": "ㅔ",
      "저": "ㅐ"
    },
    "원순": {
      "고": "ㅟ",
      "중": "ㅚ"
    }
  },
  "후설": {
    "평순": {
      "고": "ㅡ",
      "중": "ㅓ",
      "저": "ㅏ"
    },
    "원순": {
      "고": "ㅜ",
      "중": "ㅗ"
    }
  },
}

poem_sentence_1 = [
  # 기본 
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파열"]["양순"]["예사"],
    vowels_char["후설"]["원순"]["중"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 자음자
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["연구개"],          
    vowels_char["후설"]["평순"]["고"],    
    constant_char["비음"]["양순"],          
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["저"]
  ],
  "space",
  "17",
  # 개
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["저"],
  ]
]
poem_sentence_2 = [
  # 기본 
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파열"]["양순"]["예사"],
    vowels_char["후설"]["원순"]["중"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 모음자
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["비음"]["연구개"],          
    vowels_char["후설"]["평순"]["고"],    
    constant_char["비음"]["양순"],          
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["저"]
  ],
  "space",
  "11",
  # 개가
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["저"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  "space",
  #  만나
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
  ],
]
poem_sentence_3 = [
  #스물여덟
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["고"],
  ],
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["원순"]["고"],
    constant_char["유음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],    
    "ㅕ"
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["중"],
    "ㄼ" 
  ],
  "space",
  # 글자로
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["저"]
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  # 태어난
  [
    constant_char["파열"]["치조"]["거센"],
    vowels_char["전설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["연구개"], 
    vowels_char["후설"]["평순"]["중"]
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 너
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
  ],
  "!"
]
poem_sentence_4 = [
  # 누구나
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["원순"]["고"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["원순"]["고"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
  ],
  "space",
  # 쉽게
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["원순"]["고"],
    constant_char["파열"]["양순"]["예사"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  # 익힐
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["파열"]["연구개"]["예사"],
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  "space",
  # 수
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["고"]
  ],
  "space",
  # 있는
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["마찰"]["치조"]["된"]
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 너
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
  ],
  "!"
]
poem_sentence_5 = [
  #과학적이고
  [
    constant_char["파열"]["연구개"]["예사"],
    "ㅘ"
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["파열"]["연구개"]["예사"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["파열"]["연구개"]["예사"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  # 실용적인
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    "ㅛ",
    constant_char["비음"]["연구개"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["파열"]["연구개"]["예사"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 너
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
  ],
  "!"
]
poem_sentence_6 = [
  # 577돌이
  "577",
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
    constant_char["유음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
  ],
  "space",
  # 지나도록
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
    constant_char["파열"]["연구개"]["예사"],
  ],
  "space",
  # 빛나는
  [
    constant_char["파열"]["양순"]["예사"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["파찰"]["경구개"]["거센"]
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 너
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
  ],
  "!"
]
poem_sentence_7 = [
  # 0과 1만으로
  "0",
  [
    constant_char["파열"]["연구개"]["예사"],
    'ㅘ'
  ],
  "space",
  "1",
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["평순"]["고"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  # 표현하는
  [
    constant_char["파열"]["양순"]["거센"],
    "ㅛ",
  ],
  [
    constant_char["마찰"]["후"],
    "ㅕ",
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 컴퓨터 세상에서도
   [
    constant_char["파열"]["연구개"]["거센"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["비음"]["양순"],
  ],
  [
    constant_char["파열"]["양순"]["거센"],
    "ㅠ"
  ],
  [
    constant_char["파열"]["치조"]["거센"],
    vowels_char["후설"]["평순"]["중"],
  ],
  "space",
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["연구개"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["중"],
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["중"],
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ]
]
poem_sentence_8 = [
  # 24자라는 유한한
  "24",
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  [
    constant_char["비음"]["연구개"],
    "ㅠ"
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 수의 기호만으로
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["고"],
  ],
  [
    constant_char["비음"]["연구개"],
    'ㅢ'
  ],
  "space",
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["평순"]["고"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
  ]
]
poem_sentence_9 = [
  # 무한에 가까운
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["원순"]["고"],
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["파열"]["연구개"]["된"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["원순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 천지자연의
  [
    constant_char["파찰"]["경구개"]["거센"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["연구개"],
    "ㅕ",
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    "ㅢ"
  ],
  "space",
  # 소리를 만드는 너!
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  "space",
  [
    constant_char["비음"]["양순"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["고"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  # 너
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
  ],
  "!"
]
poem_sentence_10 = [
  # 네 덕분에
  [
    constant_char["비음"]["치조"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["파열"]["연구개"]["예사"],
  ],
  [
    constant_char["파열"]["양순"]["예사"],
    vowels_char["후설"]["원순"]["고"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  # 디지털 원주민인 우리는
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파열"]["치조"]["거센"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["유음"]["치조"],
  ],
  "space",
  [
    constant_char["비음"]["연구개"],
    "ㅝ",
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["원순"]["고"],
  ],
  [
    constant_char["비음"]["양순"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  "space",
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["원순"]["고"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
]
poem_sentence_11 = [
  # 컴퓨터로도
  [
    constant_char["파열"]["연구개"]["거센"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["비음"]["양순"],
  ],
  [
    constant_char["파열"]["양순"]["거센"],
    "ㅠ"
  ],
  [
    constant_char["파열"]["치조"]["거센"],
    vowels_char["후설"]["평순"]["중"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  # 휴대전화로도
  [
    constant_char["마찰"]["후"],
    "ㅠ"
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["저"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["마찰"]["후"],
    'ㅘ',
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["원순"]["고"],
    constant_char["파열"]["양순"]["예사"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  # 의사소통한다네
  [
    constant_char["비음"]["연구개"],
    "ㅢ"
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["파열"]["치조"]["거센"],
    vowels_char["후설"]["원순"]["중"],
    constant_char["비음"]["연구개"],
  ],
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["파열"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "."
]
poem_sentence_12 = [
  # 이런
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["비음"]["치조"],
  ],
  "space",
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["중"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["중"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  # 찬사를 보내지
  [
    constant_char["파찰"]["경구개"]["거센"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  "space",
  [
    constant_char["파열"]["양순"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["전설"]["평순"]["저"],
  ],
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["전설"]["평순"]["고"],
  ],
  "space",
  # 않을 리가
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["평순"]["저"],
    "ㄶ"
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  "space",
  [
    constant_char["유음"]["치조"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  "space",
  # 있겠는가
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
    constant_char["마찰"]["치조"]["된"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["중"],
    constant_char["마찰"]["치조"]["된"],
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  "."
]
poem_sentence_13 = [
  # 한류열풍을
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["치조"],
  ],
  [
    constant_char["유음"]["치조"],
    "ㅠ"
  ],
  [
    constant_char["비음"]["연구개"],
    "ㅕ",
    constant_char["유음"]["치조"],
  ],
  [
    constant_char["파열"]["양순"]["거센"],
    vowels_char["후설"]["원순"]["고"],
    constant_char["비음"]["연구개"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  "space",
  # 타고 전 세계로
  [
    constant_char["파열"]["치조"]["거센"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  [
    constant_char["파찰"]["경구개"]["예사"],
    vowels_char["후설"]["평순"]["중"],
    constant_char["비음"]["치조"],
  ],
  "space",
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    "ㅖ"
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
  ],
  "space",
  # 펼처나가
  [
    constant_char["파열"]["양순"]["거센"],
    'ㅕ',
    constant_char["유음"]["치조"],
  ],
  [
    constant_char["파찰"]["경구개"]["거센"],
    'ㅕ'
  ],
  [
    constant_char["비음"]["치조"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["후설"]["평순"]["저"],
  ],
  "space",
  # 세상을 이롭게 하세
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["후설"]["평순"]["저"],
    constant_char["비음"]["연구개"],
  ],
  [
    constant_char["비음"]["연구개"],
    vowels_char["후설"]["평순"]["고"],
    constant_char["유음"]["치조"],
  ],
  "space",
  [
    constant_char["비음"]["연구개"],
    vowels_char["전설"]["평순"]["고"],
  ],
  [
    constant_char["유음"]["치조"],
    vowels_char["후설"]["원순"]["중"],
    constant_char["파열"]["양순"]["예사"],
  ],
  [
    constant_char["파열"]["연구개"]["예사"],
    vowels_char["전설"]["평순"]["중"],
  ],
  "space",
  [
    constant_char["마찰"]["후"],
    vowels_char["후설"]["평순"]["저"],
  ],
  [
    constant_char["마찰"]["치조"]["예사"],
    vowels_char["전설"]["평순"]["중"]
  ],
  "."
]

def print_word(characters):
  print(hgtk.letter.compose(*characters), end="")

def print_sentence(words):
  for word in words:
    if word == "space":
      print(" ", end="")
    elif type(word) == str:
      print(word, end="")
    else:
      print_word(word)

  print(" ")

print(f"\n{BOLD}<< 예술이니? 과학이니? >>{RESET}")

print_sentence(poem_sentence_1)
print_sentence(poem_sentence_2)
print_sentence(poem_sentence_3)
print("\n")
print_sentence(poem_sentence_4)
print_sentence(poem_sentence_5)
print_sentence(poem_sentence_6)
print("\n")
print_sentence(poem_sentence_7)
print_sentence(poem_sentence_8)
print_sentence(poem_sentence_9)
print("\n")
print_sentence(poem_sentence_10)
print_sentence(poem_sentence_11)
print("\n")
print_sentence(poem_sentence_12)
print_sentence(poem_sentence_13)
