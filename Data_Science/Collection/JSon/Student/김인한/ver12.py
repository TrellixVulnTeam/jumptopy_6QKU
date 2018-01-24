import json

student_result = []
student_list = []
student_information = []

address_file = 'ITT_Student.json'
address = ''

try:
    with open(address_file, encoding='utf8') as outfile:
        json_object = json.load(outfile)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        student_list = json_big_data
except FileNotFoundError:
    file_maker = input('''경로에 파일이 없습니다. 어떻게 하시겠습니까?
    1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
    메뉴를 선택하세요 : ''')
    address_file = '\ITT_Student.json'
    if file_maker == '1':
        address = input("경로를 입력해주세요 : ")
        with open(address + address_file ,encoding='utf8') as outfile:
            json_object = json.load(outfile)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
    elif file_maker == '2':
        address_file = 'ITT_Student.json'
        address = ''

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
        student_information = {
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
        student_result.append(student_information)
    elif student_management == '2':
        student_list += student_result
        for i in range(len(student_list)):
            recent_lecture_list = student_list[i]['lecture_information']['recent_lecture_subject']
            print("학생ID : ",student_list[i]['student_ID'])
            print("이름 : ",student_list[i]['name'])
            print("나이 : ",student_list[i]['age'])
            print("주소 : ",student_list[i]['address'])
            print("과거수강횟수 : ",student_list[i]['lecture_information']['past_lecture_subject'])
            print("현재수강과목")
            print(" - 강의코드 : ",recent_lecture_list[0]['lecture_code'])
            print(" - 강의명 : ",recent_lecture_list[0]['lecture_name'])
            print(" - 강사 : ", recent_lecture_list[0]['teacher'])
            print(" - 개강일 : ", recent_lecture_list[0]['start_day'])
            print(" - 종강일 : ", recent_lecture_list[0]['close_day'])

with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
    student_list += student_result
    readable_result = json.dumps(student_list, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)