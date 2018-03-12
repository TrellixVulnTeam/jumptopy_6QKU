import json
import os

student_ITT = []
input_student = {}

if os.path.isfile('ITT_Student.json'):
    try:
        with open('ITT_Student.json', encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            student_ITT = json.loads(json_string)
    except: pass
else:
    ITT = int(input(""" 경로에 파일이 없습니다. 어떻게 하시겠습니까?
1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
메뉴를 선택하세요: """))
    if ITT == 1:
        load = input("경로를 입력하세요: ")
        delimiter = "\\"
        try:
            with open(load+delimiter+'ITT_Student.json', encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                json_big_data = json.loads(json_string)
        except:
            print("경로를 잘못입력하였습니다.")

    elif ITT == 2:
        with open('ITT_Student.json','w',encoding='UTF8') as outfile:
            readable_result = json.dumps(student_ITT,indent=4, sort_keys=True, ensure_ascii=False)
            outfile.close()
            print('ITT_Student.json SAVED')

while 1:
    print("    << json기반 주소록 관리 프로그램 >>")
    content = int(input("""1) 학생 정보 입력)
2) 학생 정보 조회)
3) 학생 정보 수정)
4) 학생 정보 삭제)
5) 프로그램 종료"""))

    if content == 1:
        print("<학생정보>")
        input_student = {
            'student_id': "ITT" + '{:0=3}'.format(len(student_ITT)+1),
            'student_name': input("이름을 입력해주세요: "),
            'student_age': input("나이를 입력해주세요: "),
            'student_address': input("주소를 입력해주세요: "),
            'total_course_info':{
                    'num_of_course_learned': input("과거 수강 횟수를 입력해주세요: "),
                    'learning_course_info':[
                    {
                        'course_code': input("강의코드를 입력해주세요: "),
                        'course_name': input("강의명을 입력해주세요: "),
                        'teacher': input("강사명을 입력해주세요: "),
                        'start_date': input("개강일을 입력해주세요: "),
                        'finish_date': input("종료일을 입력해주세요: ")
                    }
                ]
            }
        }
        student_ITT.append(input_student)
        print(student_ITT)
    elif content == 2:
        with open('ITT_Student.json','r',encoding='UTF8') as outfile:
            readable_result = json.dumps(student_ITT, indent=4, sort_keys=True, ensure_ascii=False)
        cheak = int(input("학생정보를 조회하시겠습니까? 1)네 2)돌아가기"))
        if cheak == 1:
                print("<학생정보조회>")
                print("아이디 : "+ student_ITT[0]['student_id'])
                print("이름 : "+ student_ITT[0]['student_name'])
                print("나이 : "+ student_ITT[0]['student_age'])
                print("주소 : "+ student_ITT[0]['student_address'])
                print("횟수 : "+ student_ITT[0]['total_course_info']['num_of_course_learned'])
                print("강의코드 : "+ student_ITT[0]['total_course_info']['learning_course_info'][0]['course_code'])
                print("강의명 : "+ student_ITT[0]['total_course_info']['learning_course_info'][0]['course_name'])
                print("강사명 : "+ student_ITT[0]['total_course_info']['learning_course_info'][0]['teacher'])
                print("개강일 : "+ student_ITT[0]['total_course_info']['learning_course_info'][0]['start_date'])
                print("종료일 : "+ student_ITT[0]['total_course_info']['learning_course_info'][0]['finish_date'])
        else:
            continue

with open('ITT_Student.json','w',encoding='UTF8') as outfile:
    readable_result = json.dumps(student_ITT, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)
    print('ITT_Student.json SAVED')