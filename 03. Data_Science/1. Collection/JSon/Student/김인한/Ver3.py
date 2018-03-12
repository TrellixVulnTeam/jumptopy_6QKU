import json

student_result = []
student_information = []

try:
    with open('ITT_Student.json', 'r', encoding='utf8') as outfile:
        json_object = json.load('ITT_Student.json')
        json_string = json.dumps(json_object)
        readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
except FileNotFoundError:
    file_maker = input('''경로에 파일이 없습니다. 어떻게 하시겠습니까?
    1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
    메뉴를 선택하세요 : ''')
    if file_maker == '1':
        address = input("경로를 입력해주세요 : ")
        with open(address + 'ITT_Student.json',encoding='utf8') as outfile:
            json_object = json.load(outfile)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)

    elif file_maker == '2':
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print("파일 생성완료.")

while True:
    student_management = input("""<< json기반 주소록 관리 프로그램 >>
1. 학생 정보입력
2. 학생 정보조회
3. 학생 정보수정
4. 학생 정보삭제
5. 프로그램 종료
    입력 : """)
    if student_management == '5':
        break
    elif student_management == '1':
            with open('ITT_Student.json',encoding='utf8') as outfile:
                json_object = json.load(outfile)
                json_string = json.dumps(json_object)
                json_big_data = json.loads(json_string)

                student_information = [
                    {
                    'student_ID': "ITT" + '{:0=3}'.format(len(student_information)+1),
                    'name': input("성함은? : "),
                    'age': input("나이는? : "),
                    'address': input("주소는? : "),
                    'lecture_information':
                        {
                        'past_lecture_subject': input("과거수강횟수는? : "),
                        'recent_lecture_subject':
                            [
                            {
                            'lecture_code':input("강의코드는? : "),
                            'lecture_name':input("강의명? : "),
                            'teacher':input("강사는? : "),
                            'start_day':input("개강일은? : "),
                            'close_day':input("종료일은? : ")
                            }
                            ]
                        }
                    }
                ]
                student_result = student_information
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
                    # outfile.write(readable_result)