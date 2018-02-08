import json
import os

while 1:
    student_ITT = []
    input_student = {}
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

    if content == 2:
        terms = int(input(""" 어떤 조건으로 조회하시겠습니까?
    1)학생ID 2)이름 3)나이 4)주소 5)과거수강횟수 6)현재강의를 수강하는 학생 7)현재강의명 8)강사명 """))

    # if content == 3:

    if content == 4:
        with open('ITT_Student.json','r',encoding='UTF8')as outfile:
            readable_result = json.dumps(student_ITT, indent=4, sort_keys=True, ensure_ascii=False)
            student_ITT.clear()
            print("다지웠음ㅇㅇ")
    # else:
        break

# if not os.path.isdir('ITT_Student.json'):
#     with open('ITT_Student.json','a',encoding='UTF8') as outfile:
#         readable_result = json.dumps(student_ITT, indent=4, sort_keys=True, ensure_ascii=False)
#         outfile.write(readable_result)
#         print('ITT_Student.json SAVED')