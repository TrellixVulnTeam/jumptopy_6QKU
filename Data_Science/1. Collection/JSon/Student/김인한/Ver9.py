import json

student_result = []
student_result_1 = []
student_result_2 = []

try:
    with open('ITT_Student.json', encoding='utf8') as outfile:
        json_object = json.load(outfile)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
except FileNotFoundError:
    pass

while True:
    student_management = input("""<< json기반 주소록 관리 프로그램 >>
1. 학생 정보입력
5. 프로그램 종료
    입력 : """)
    if student_management == '5':
        break
    elif student_management == '1':
        student_information = {
            'name': input("성함은? : "),
            }
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            student_result_2.append(student_information)
            readable_result = json.dumps(student_result_2, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)