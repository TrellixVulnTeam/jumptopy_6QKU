import json

student_result = []
student_list = []
student_information = []

try:
    with open('test.json', encoding='utf8') as outfile:
        json_object = json.load(outfile)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        student_list = json_big_data
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
        student_result.append(student_information)

with open('test.json', 'w', encoding='utf8') as outfile:
    student_list += student_result
    readable_result = json.dumps(student_list, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)