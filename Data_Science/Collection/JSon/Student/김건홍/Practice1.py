import json
import os
"""
프로그램 시작시 소스코드가 있는 경로에 'ITT_Student.json' 파일이 있다면 읽어들인다.
없으면 아래와 같이 물어본다.

경로에 파일이 없습니다. 어떻게 하시겠습니까?
1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
메뉴를 선택하세요: 

1번을 선택하면 'ITT_Student.json' 파일이 있는 경로를 물어봐서 읽어들인다
2번을 선택하면 'ITT_Student.json' 을 생성한다.
"""
if os.path.isfile('ITT_Student.json'):
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)

else:
    ITT = int(input(""" 경로에 파일이 없습니다. 어떻게 하시겠습니까?
1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
메뉴를 선택하세요: """))
    if ITT == 1:
        load = input("경로를 입력하세요: ")
        delimiter ="\\"
        try:
            with open(load+delimiter+'ITT_Student.json', encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)

        except:
            print("경로를 잘못입력하였습니다.")
    elif ITT == 2:




print("프로그램을 종료합니다.")
