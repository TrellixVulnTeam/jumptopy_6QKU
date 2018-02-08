from Register import Student_Register
from Register import Class_Register
from Environment import Numbering
from Environment import Interface
from collections import ChainMap
from Search import Partial_Value
import Checkfile

count_file = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
class_dict = {}
main_dict = {}

Checkfile.check_file()
Numbering.id_generator()

while True:
    Interface.main_interface()
    pg_selection = int(input(">>"))
    if pg_selection == 1:  # 학생 ID는 ITT00X 순서대로 부여
        print(("등록하실 학생 정보를 입력하시오"))
        main_dict["학생ID"] = Numbering.id_check()
        main_dict.update(Student_Register.student_return_info())
        main_dict.update(Class_Register.past_class_info())
        count = 1
        total_class = Class_Register.institute_return_info(count)
        while True:
            class_number = int(input("추가하실려면 1, 취소하실려면 2"))
            if class_number == 1:
                total_class = ChainMap(total_class, Class_Register.institute_return_info(count+1))
                count += 1
                continue
            class_dict["수강정보"] = dict(total_class)
            if class_number == 2:
                class_dict["수강정보"] = dict(total_class)
                break
        json_data = ChainMap(main_dict,class_dict)
        json_data = json_data
        Checkfile.save_json_file(json_data)

    if pg_selection == 2:
        Interface.second_interface()
        input_sentence = int(input(">>"))
        if input_sentence == 1:
            id = str(input("ID 입력"))
            print(Partial_Value.check_value(id,"학생ID"))
        elif input_sentence == 2:
            name = str(input("이름 입력"))
            print(Partial_Value.check_value_student(name, "이름"))
        elif input_sentence == 3:
            old = str(input("나이 입력"))
            print(Partial_Value.check_value_student(old, "나이"))
        elif input_sentence == 4:
            address = str(input("주소 입력"))
            print(Partial_Value.check_value_student(address, "주소"))
        elif input_sentence == 5:
            code = str(input("강의코드 입력"))
            print(Partial_Value.check_value_student(code, "강의코드"))
        elif input_sentence == 6:
            class_name = str(input("강의명 입력"))
            print(Partial_Value.check_value_student(class_name, "강의명"))
        elif input_sentence == 7:
            teacher = str(input("강사 입력"))
            print(Partial_Value.check_value_student(teacher, "강사"))
        elif input_sentence == 8:
            print("전체출력")


# 1. 번호 2.학생정보 3. 수강정보
#         -이름,나이,주소 - 과거수강횟수 - 강의(n)
#                                          -강의코드, 강의명, 강사, 개강일, 종료일