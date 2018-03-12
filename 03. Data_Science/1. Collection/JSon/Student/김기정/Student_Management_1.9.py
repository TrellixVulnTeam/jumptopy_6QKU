from collections import OrderedDict
import json
import os
import sys

os_delimeter = "\\"
st_count = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
key_list = ["이름","나이","주소"]
key_list_2 = ["강의코드","강의명","강사"]

def tree_maker():
    for x in range(1, 10 * 2, 2):
        print((" " * ((10 * 2 - 1 - x) // 2)) + ("*" * x))
    for y in range(1, 4):
        print(" " * (10 - 2) + "***")


def st_ID_Generator():
    try:
        with open(os.getcwd() + os_delimeter + st_count, "r") as data:
            count_n = data.readline()
            st_ID = "ITT" + count_n
            int_count_n = int("%01d" % int(count_n))
            int_count_n += 1
        with open(os.getcwd() + os_delimeter + st_count, "w") as count:
            three_digit_n = "%03d" % int_count_n
            count.write(three_digit_n)
            return st_ID
    except FileNotFoundError:
        with open(os.getcwd() + os_delimeter + st_count, "w") as file:
            file.write("002")
            st_initID = "ITT" + "001"
            return st_initID


def open_json_file():
    with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        return json_big_data

def check_value_ID(input_data,key_data):
    index = 0
    while True:
        store = []
        if index < len(open_json_file()):
            for dic_data in open_json_file():
                if input_data in dic_data[key_data]:
                    store.append(dic_data[key_data])
                    index += 1
        return (store)

def check_value_student(input_data,key_data):
    index = 0
    while True:
        store = []
        if index < len(open_json_file()):
            for dic_data in open_json_file():
                if input_data in dic_data["학생정보"][key_data]:
                    store.append(dic_data["학생정보"][key_data])
                    index += 1
        return (store)

def check_value_academy(input_data,key_data):
    index = 0
    while True:
        store = []
        if index < len(open_json_file()):
            for dic_data in open_json_file():
                if input_data in dic_data["수강정보"][key_data]:
                    store.append(dic_data["수강정보"][key_data])
                    index += 1
        return (store)


def check_value_class(input_data,key_data):
    index = 0
    while True:
        store = []
        if index < len(open_json_file()):
            for dic_data in open_json_file():
                for x in range(len(dic_data["수강정보"]) - 1):
                    if input_data in dic_data["수강정보"]["강좌"+str(x)][key_data]:
                        store.append(dic_data["수강정보"]["강좌"+str(x)][key_data])
        return (store)

def fix_json_file():
    print("변경된 데이터를 저장 중입니다")
    with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
        readable_result = json.dumps(open_json_file(), indent=4, ensure_ascii=False)
        make_file.write(readable_result)
        print('저장이 완료되었습니다')

def output_personel_information(personal_sentence):
    if len(personal_sentence) == 1:  #
        for i in range(len(open_json_file())):
            for p in personal_sentence:
                if p == open_json_file()[i]["학생ID"] or p == open_json_file()[i]["학생정보"]["이름"] or p == open_json_file()[i]["학생정보"]["나이"] or p == open_json_file()[i]["학생정보"]["주소"]:
                    print("\n")
                    print((("\t" * 13) + "학생ID: %s\n" % open_json_file()[i]["학생ID"]) + "\n" +
                          (("\t" * 12) + "이름: %s" % open_json_file()[i]["학생정보"]["이름"]) + "\n" +
                          (("\t" * 12) + "나이: %s" % open_json_file()[i]["학생정보"]["나이"]) + "\n" +
                          (("\t" * 12) + "주소: %s" % open_json_file()[i]["학생정보"]["주소"]) + "\n\n" +
                          (("\t" * 13) + "과거수강횟수: %s" % open_json_file()[i]["수강정보"]["과거수강횟수"]) + "\n")
                    for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                        print((("\t" * 14) + "강좌" + str(x + 1)) + "\n\n" +
                              (("\t" * 13) + "강의코드" + str(x + 1) + ": " + "%s" %
                               open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n" +
                              (("\t" * 13) + "강의명" + str(x + 1) + ": " + "%s" %
                               open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의명"]) + "\n" +
                              (("\t" * 13) + "강사" + str(x + 1) + ": " + "%s" %
                               open_json_file()[i]["수강정보"]["강좌" + str(x)]["강사"]) + "\n" +
                              (("\t" * 13) + "개강일" + str(x + 1) + ": " + "%s" %
                               open_json_file()[i]["수강정보"]["강좌" + str(x)]["개강일"]) + "\n" +
                              (("\t" * 13) + "종료일" + str(x + 1) + ": " + "%s" %
                               open_json_file()[i]["수강정보"]["강좌" + str(x)]["종료일"]) + "\n")
                        continue
    if len(personal_sentence) >= 2:
        print("-" * 140)
        print(("중복된 값으로 인한 학생ID 요약").center(110))
        print("-" * 140)
        for i in range(len(open_json_file())):
            for x in personal_sentence:
                if x == open_json_file()[i]["학생ID"] or x == open_json_file()[i]["학생정보"]["이름"] or x == open_json_file()[i]["학생정보"]["나이"] or x == open_json_file()[i]["학생정보"]["주소"]:
                    print("")
                    print((("\t" * 13) + "학생이름: %s" % open_json_file()[i]["학생정보"]["이름"]))
                    print((("\t" * 13) + "학생ID: %s" % open_json_file()[i]["학생ID"]))
                    break
        print("")
        print("-" * 140)

def output_institute_information(institute_sentence):
    if len(institute_sentence) == 1:
        for p in institute_sentence:  #
            for i in range(len(open_json_file())):
                for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                    if p == open_json_file()[i]["수강정보"][
                            "과거수강횟수"] or p == open_json_file()[i]["수강정보"]["강좌" + str(x)][
                            "강의코드"] or p == open_json_file()[i]["수강정보"]["강좌" + str(x)][
                            "강의명"] or p == open_json_file()[i]["수강정보"]["강좌" + str(x)][
                            "강사"]:
                        print("\n")
                        print((("\t" * 13) + "학생ID: %s\n" % open_json_file()[i]["학생ID"]) + "\n" +
                                  (("\t" * 12) + "이름: %s" % open_json_file()[i]["학생정보"]["이름"]) + "\n" +
                                  (("\t" * 12) + "나이: %s" % open_json_file()[i]["학생정보"]["나이"]) + "\n" +
                                  (("\t" * 12) + "주소: %s" % open_json_file()[i]["학생정보"]["주소"]) + "\n\n" +
                                  (("\t" * 13) + "과거수강횟수: %s" % open_json_file()[i]["수강정보"]["과거수강횟수"]) + "\n")
                        print((("\t" * 14) + "강좌" + str(x + 1)) + "\n\n" +
                                  (("\t" * 13) + "강의코드" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n" +
                                  (("\t" * 13) + "강의명" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의명"]) + "\n" +
                                  (("\t" * 13) + "강사" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강사"]) + "\n" +
                                  (("\t" * 13) + "개강일" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["개강일"]) + "\n" +
                                  (("\t" * 13) + "종료일" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["종료일"]) + "\n")
                        break
                    continue
                continue
            break

    if len(institute_sentence) >= 2:
        print("-" * 140)
        print(("중복된 값으로 인한 학생ID 요약").center(110))
        print("-" * 140)
        for i in range(len(open_json_file())):
            for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                for p in institute_sentence:
                    if p == open_json_file()[i]["수강정보"][
                        "과거수강횟수"] or p == open_json_file()[i]["수강정보"]["강좌" + str(x)][
                        "강의코드"] or p == open_json_file()[i]["수강정보"]["강좌" + str(x)][
                        "강의명"] or p == open_json_file()[i]["수강정보"]["강좌" + str(x)][
                        "강사"]:
                        print("")
                        print((("\t" * 13) + "학생이름: %s" % open_json_file()[i]["학생정보"]["이름"]))
                        print((("\t" * 13) + "학생ID: %s" % open_json_file()[i]["학생ID"]))
                    break


def check_del_save():
    with open(os.getcwd() + os_delimeter + json_file_name, 'w',
              encoding="utf-8") as make_file:
        readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
        make_file.write(readable_result)
        print('저장되었습니다.')

st_database = OrderedDict()
student_info = OrderedDict()
class_info = OrderedDict()
class_past_info = OrderedDict()
jsonData = OrderedDict()
lecture_info = OrderedDict()

while True:
    print("-" * 140)
    print("<<Json기반 주소록 관리 프로그램>>".center(115))
    print("-" * 140)
    print("1. 학생 정보입력".center(115))
    print("2. 학생 정보조회".center(115))
    print("3. 학생 정보수정".center(115))
    print("4. 학생 정보삭제".center(115))
    print("5. 프로그램 종료".center(115))
    print("-" * 140)
    pg_selection = int(input(">>"))
    if pg_selection == 1:  # 학생 ID는 ITT00X 순서대로 부여
        print("-" * 140)
        print(("등록하실 학생 정보를 입력하시오").center(115))
        print("-" * 140)
        print("뒤로가기(0)")
        print("\n\n")
        st_name = str(input("이름 : \n"))
        print("")
        student_info["이름"] = st_name
        st_old = str(input("나이 : \n"))
        print("")
        student_info["나이"] = st_old
        st_address = str(input("주소 :\n"))
        print("")
        student_info["주소"] = st_address
        print("수강 정보 입력")
        class_past_count = str(input("과거 수강 횟수 :\n"))
        print("")
        class_info["과거수강횟수"] = class_past_count
        lecture_number = 0
        while True:
            class_code = str(input("강의 코드 :\n"))
            print("")
            lecture_info["강의코드"] = class_code
            class_name = str(input("강의명 :\n"))
            print("")
            lecture_info["강의명"] = class_name
            class_teacher = str(input("강사 :\n"))
            print("")
            lecture_info["강사"] = class_teacher
            class_start = str(input("개강일 :\n"))
            print("")
            lecture_info["개강일"] = class_start
            class_end = str(input("종료일 :\n"))
            print("")
            lecture_info["종료일"] = class_end
            aggrement = str(input("강의를 추가하시겠습니까? Y/N\n>>"))
            if aggrement == "y" or aggrement == "Y":
                class_info["강좌" + str(lecture_number)] = lecture_info
                lecture_number = lecture_number + 1
                lecture_info = OrderedDict()
                continue
            if aggrement == "n" or aggrement == "N":
                class_info["강좌" + str(lecture_number)] = lecture_info
                break
            if not aggrement == "n" or aggrement == "N" or aggrement == "y" or aggrement == "Y":
                print("잘못입력하셨습니다. 기존 데이터를 저장하고 초기화면으로 넘어갑니다")
                class_info["강좌" + str(lecture_number)] = lecture_info
                break

        print("-" * 140)
        st_ID = st_ID_Generator()
        st_database["학생ID"] = st_ID
        st_database["학생정보"] = student_info
        st_database["수강정보"] = class_info
        jsonData = [st_database]

        try:
            with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                json_big_data = json.loads(json_string)
                total_json_data = json_big_data + jsonData
            with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                readable_result = json.dumps(total_json_data, indent=4, ensure_ascii=False)
                make_file.write(readable_result)
                print('등록된 정보가 저장되었습니다.')
                continue

        except FileNotFoundError:
            with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                readable_result = json.dumps(jsonData, indent=4, ensure_ascii=False)
                make_file.write(readable_result)
                print('등록된 정보가 저장되었습니다.')
                continue

    if pg_selection == 2:  # 학생 정보 조회
        try:
            while True:
                print("-" * 140)
                print(("조회하실 학생 정보를 선택하시오").center(115))
                print("-" * 140)
                print("\n\n\n" + ("\t" * 5) + "<<인적사항조회>>" + ("\t" * 5) + "<<전체학생조회>>" + ("\t" * 5) + "<<수강정보조회>>")
                print(("\t" * 6) + "  -1-" + ("\t" * 7) + "      -2-" + ("\t" * 8) + "   -3-")
                print("\n" * 2)
                print("-" * 140)
                print("뒤로가기(0)")
                input_sentence = str(input(">>"))
                if input_sentence == "0":
                    break
                if input_sentence == "전체학생조회" or input_sentence == "2":
                    for i in range(len(open_json_file())):
                        print("\n")
                        print((("\t" * 13) + "학생ID: %s\n" % open_json_file()[i]["학생ID"]) + "\n" +
                              (("\t" * 12) + "이름: %s" % open_json_file()[i]["학생정보"]["이름"]) + "\n" +
                              (("\t" * 12) + "나이: %s" % open_json_file()[i]["학생정보"]["나이"]) + "\n" +
                              (("\t" * 12) + "주소: %s" % open_json_file()[i]["학생정보"]["주소"]) + "\n\n" +
                              (("\t" * 13) + "과거수강횟수: %s" % open_json_file()[i]["수강정보"]["과거수강횟수"]) + "\n")
                        for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                            print((("\t" * 14) + "강좌" + str(x + 1)) + "\n\n" +
                                  (("\t" * 13) + "강의코드" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n" +
                                  (("\t" * 13) + "강의명" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의명"]) + "\n" +
                                  (("\t" * 13) + "강사" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강사"]) + "\n" +
                                  (("\t" * 13) + "개강일" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["개강일"]) + "\n" +
                                  (("\t" * 13) + "종료일" + str(x + 1) + ": " + "%s" %
                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["종료일"]) + "\n")
                            continue
                    print("조회하신 정보를 출력하였습니다")
                    aggrement_yn = str(input("초기화면으로 넘어가시겠습니까? Y/N\n>>"))
                    if aggrement_yn == "y" or aggrement_yn == "Y":
                        break
                    if aggrement_yn == "n" or aggrement_yn == "N":
                        continue

                if input_sentence == "인적사항조회" or input_sentence == "1":
                    while True:
                        print("-" * 140)
                        print("\n1.ID로 조회")
                        print("\n2.학생정보로 조회")
                        print("")
                        print("-" * 140)
                        print("뒤로가기(0번)")
                        input_sentence_2 = str(input(">>"))
                        if input_sentence_2 == "0":
                            break
                        if input_sentence_2 == "1":
                            print("-" * 140)
                            personal_sentence = str(input("학생ID를 입력하시오: \n"))
                            print("-" * 140)
                            output_personel_information(check_value_ID(personal_sentence, "학생ID"))
                        if input_sentence_2 == "2":
                            print("-" * 140)
                            personal_sentence = str(input("이름, 나이, 주소 중 한가지를 입력하시오: \n"))
                            print("-" * 140)
                            for key in key_list:
                                output_personel_information(check_value_student(personal_sentence, key))

                if input_sentence == "수강정보조회" or input_sentence == "3":
                    while True:
                        print("-" * 140)
                        print("\n1.과거수강횟수로 조회")
                        print("\n2.강의정보로 조회")
                        print("")
                        print("-" * 140)
                        print("뒤로가기(0번)")
                        input_sentence_3 = str(input(">>"))
                        if input_sentence_3 == "0":
                            break
                        if input_sentence_3 == "1":
                            print("-" * 140)
                            print("과거수강횟수를 입력하시오")
                            print("-" * 140)
                            institute_sentence = str(input(">>"))
                            output_institute_information(check_value_academy(institute_sentence, "과거수강횟수"))
                        if input_sentence_3 == "2":
                            print("-" * 140)
                            print("강의코드, 강의명, 강사 중 한가지를 입력하세요")
                            print("-" * 140)
                            institute_sentence = str(input(">>"))
                            for key_2 in key_list_2:
                                output_institute_information(check_value_class(institute_sentence, key_2))

        except FileNotFoundError:
            print("파일이 없습니다")

    if pg_selection == 3:  # 학생 정보 수정
        with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
        print("-" * 140)
        print("수정하실 학생의 ID나 이름을 입력하시오(뒤로가기 0번)")
        print("-" * 140)
        input_value = str(input(":"))
        if input_value == 0:
            break
        else:
            for i in range(len(json_big_data)):
                for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                    if input_value == (json_big_data[i]["학생정보"]["이름"]) or input_value == (json_big_data[i]["학생ID"]):
                        while True:
                            print("-" * 140)
                            print("")
                            print(("수정하실 항목을 선택하시오").center(110))
                            print("")
                            print(("1.학생 정보").center(115))
                            print(("2.수강 정보").center(115))
                            print(("3.뒤로 가기").center(115))
                            print("")
                            print("-" * 140)
                            print("")
                            fix_sentence = str(input(":"))
                            if fix_sentence == "1" or fix_sentence == "학생 정보" or fix_sentence == "학생정보":
                                while True:
                                    print("-" * 140)
                                    print("")
                                    print(("수정하실 학생 정보를 선택하시오").center(110))
                                    print("")
                                    print(("1.이름").center(112))
                                    print(("2.나이").center(112))
                                    print(("3.주소").center(112))
                                    print(("4.뒤로가기").center(114))
                                    print("")
                                    print("-" * 140)
                                    st_fix_num = int(input(":"))
                                    if st_fix_num == 1:
                                        print("-" * 140)
                                        print("이름을 선택하셨습니다")
                                        print("현재 이름은", "<", (json_big_data[i]["학생정보"]["이름"]), ">", "입니다")
                                        print("-" * 140)
                                        input_name = str(input("수정 이름\n:"))
                                        (json_big_data[i]["학생정보"]["이름"]) = input_name
                                        print("-", (json_big_data[i]["학생정보"]["이름"]), "-", "로 수정되었습니다")
                                        continue
                                    if st_fix_num == 2:
                                        print("-" * 140)
                                        print("나이를 선택하셨습니다")
                                        print("현재 나이는", "<", (json_big_data[i]["학생정보"]["나이"]), ">", "입니다")
                                        print("-" * 140)
                                        input_old = str(input("수정 나이\n:"))
                                        (json_big_data[i]["학생정보"]["나이"]) = input_old
                                        print("-", (json_big_data[i]["학생정보"]["나이"]), "-", "로 수정되었습니다")
                                        continue
                                    if st_fix_num == 3:
                                        print("-" * 140)
                                        print("주소를 선택하셨습니다")
                                        print("현재 주소는", "<", (json_big_data[i]["학생정보"]["주소"]), ">", "입니다")
                                        print("-" * 140)
                                        input_address = str(input("수정 주소\n:"))
                                        (json_big_data[i]["학생정보"]["주소"]) = input_address
                                        print("-", (json_big_data[i]["학생정보"]["주소"]), "-", "로 수정되었습니다")
                                        continue
                                    if st_fix_num == 4:
                                        print("변경된 사항을 저장하겠습니다")
                                        with open(os.getcwd() + os_delimeter + json_file_name, 'w',
                                                  encoding="utf-8") as make_file:
                                            readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                            make_file.write(readable_result)
                                            print('저장되었습니다')
                                            break

                            if fix_sentence == "2" or fix_sentence == "수강 정보" or fix_sentence == "수강정보":
                                while True:
                                    print("-" * 140)
                                    print("")
                                    print(("수정하실 수강 정보를 선택하시오").center(110))
                                    print("")
                                    print(("1.과거수강횟수").center(115))
                                    print(("2.강의목록").center(113))
                                    print(("3.뒤로가기").center(113))
                                    print("")
                                    print("-" * 140)
                                    ins_fix_num = int(input(":"))
                                    if ins_fix_num == 1:
                                        print("-" * 140)
                                        print("과거 수강 횟수를 선택하셨습니다")
                                        print("현재 과거 수강 횟수는", "<", (json_big_data[i]["수강정보"]["과거수강횟수"]), ">", "입니다")
                                        print("-" * 140)
                                        input_name = str(input("수정 과거 수강 횟수\n>>"))
                                        (json_big_data[i]["수강정보"]["과거수강횟수"]) = input_name
                                        print(("-", json_big_data[i]["수강정보"]["과거수강횟수"]), "-", "로 수정되었습니다")
                                        continue
                                    if ins_fix_num == 2:
                                        print("-" * 140)
                                        print("")
                                        print(("수정하실 수강 정보를 선택하시오").center(110))
                                        print("")
                                        print(("1.강의코드").center(113))
                                        print(("2.강의명").center(113))
                                        print(("3.강사").center(112))
                                        print(("4.개강일").center(113))
                                        print(("5.종료일").center(113))
                                        print(("6.뒤로가기").center(114))
                                        print("")
                                        print("-" * 140)
                                        select_num = int(input(":"))
                                        if select_num== 1:
                                            print("-" * 140)
                                            print("강의코드를 선택하셨습니다")
                                            print("현재 강의코드는", "<", (json_big_data[i]["수강정보"]["강좌" + str(x)]["강의코드"]), ">",
                                                  "입니다")
                                            print("-" * 140)
                                            input_name = str(input("수정 강의 코드\n>>"))
                                            (json_big_data[i]["수강정보"]["강좌" + str(x)]["강의코드"]) = input_name
                                            print("-", (json_big_data[i]["수강정보"]["강좌" + str(x)]["강의코드"]), "-", "로 수정되었습니다")
                                            continue
                                        if select_num == 2:
                                            print("-" * 140)
                                            print("강의명를 선택하셨습니다")
                                            print("현재 강의명은", "<", (json_big_data[i]["수강정보"]["강좌" + str(x)]["강의명"]), ">",
                                                  "입니다")
                                            print("-" * 140)
                                            input_name = str(input("수정 강의 명\n:"))
                                            (json_big_data[i]["수강정보"]["강좌" + str(x)]["강의명"]) = input_name
                                            print("-", (json_big_data[i]["수강정보"]["강좌" + str(x)]["강의명"]), "-", "로 수정되었습니다")
                                            continue
                                        if select_num == 3:
                                            print("-" * 140)
                                            print("강사를 선택하셨습니다")
                                            print("현재 강사는", "<", (json_big_data[i]["수강정보"]["강좌" + str(x)]["강사"]), ">",
                                                  "입니다")
                                            print("-" * 140)
                                            input_name = str(input("수정 강사\n:"))
                                            (json_big_data[i]["수강정보"]["강좌" + str(x)]["강사"]) = input_name
                                            print("-", (json_big_data[i]["수강정보"]["강좌" + str(x)]["강사"]), "-", "로 수정되었습니다")
                                            continue
                                        if select_num == 4:
                                            print("-" * 140)
                                            print("개강일를 선택하셨습니다")
                                            print("현재 개강일은", "<", (json_big_data[i]["수강정보"]["강좌" + str(x)]["개강일"]), ">",
                                                  "입니다")
                                            print("-" * 140)
                                            input_name = str(input("수정 개강일\n:"))
                                            (json_big_data[i]["수강정보"]["강좌" + str(x)]["개강일"]) = input_name
                                            print("-", (json_big_data[i]["수강정보"]["강좌" + str(x)]["개강일"]), "-", "로 수정되었습니다")
                                            continue
                                        if select_num == 5:
                                            print("-" * 140)
                                            print("종료일를 선택하셨습니다")
                                            print("현재 종료일은", "<", (json_big_data[i]["수강정보"]["강좌" + str(x)]["종료일"]), ">",
                                                  "입니다")
                                            print("-" * 140)
                                            input_name = str(input("수정 종료일\n:"))
                                            (json_big_data[i]["수강정보"]["강좌" + str(x)]["종료일"]) = input_name
                                            print("-", (json_big_data[i]["수강정보"]["강좌" + str(x)]["종료일"]), "-", "로 수정되었습니다")
                                            continue
                                        if select_num == 6:
                                            print("변경된 사항을 저장하겠습니다")
                                            with open(os.getcwd() + os_delimeter + json_file_name, 'w',
                                                      encoding="utf-8") as make_file:
                                                readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                                make_file.write(readable_result)
                                                print('저장되었습니다.')
                                                continue
                                    if  ins_fix_num == 3:
                                        print("변경된 사항을 저장하겠습니다")
                                        with open(os.getcwd() + os_delimeter + json_file_name, 'w',
                                                  encoding="utf-8") as make_file:
                                            readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                            make_file.write(readable_result)
                                            print('저장되었습니다')
                                            break
                            if fix_sentence == "3" or fix_sentence == "뒤로가기" or fix_sentence == "뒤로가기":
                                break
                            break

    if pg_selection == 4:  # 학생 정보 삭제
        with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
        print("-" * 140)
        print("삭제할 학생의 ID를 입력하시오(뒤로가기 0번):")
        print("-" * 140)
        input_value = str(input(":"))
        if input_value == 0:
            break
        else:
            for i in range(len(json_big_data)):
                for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                    if input_value == (json_big_data[i]["학생ID"]):
                        while True:
                            print("-" * 140)
                            print("")
                            print(("삭제할 항목을 선택하시오").center(110))
                            print("")
                            print(("1.전체항목").center(113))
                            print(("2.수강정보").center(113))
                            print(("3.뒤로가기").center(113))
                            print("")
                            print("-" * 140)
                            del_number = int(input(":"))
                            if del_number == 1:
                                del_agree = str(input("전체 항목을 삭제하시겠습니까? Y/N"))
                                if del_agree == "Y" or del_agree == "y":
                                    del (json_big_data[i])
                                    print("-" * 140)
                                    print("전체 항목을 삭제하였습니다")
                                    print("-" * 140)
                                if del_agree == "N" or del_agree == "n":
                                    print("취소하였습니다")
                                    break
                            if del_number == 2:
                                print("-" * 140)
                                print(("해당된 ID의 수강정보 입니다").center(110))
                                print("-" * 140)
                                print("")
                                for i in range(len(open_json_file())):
                                    if input_value == open_json_file()[i]["학생ID"]:
                                        for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                                            print(((("\t" * 12) + "강좌" + str(x + 1)) + " - " + "강의코드" + str(x + 1) + ": " + "%s" %
                                                   open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n")
                                            continue
                                print("-" * 140)
                                print("삭제할 강좌의 강의 코드를 입력하세요(강좌 전체 삭제:ALL,뒤로가기:0)")
                                del_code = str(input(":"))
                                if del_code == "ALL" or del_code == "all" or del_code == "All" or del_code == "aLL":
                                    del_agree = str(input("수강 정보를 삭제하시겠습니까? Y/N"))
                                    if del_agree == "Y" or del_agree == "y":
                                        del (json_big_data[i]["수강정보"])
                                        print("수강 정보를 삭제하였습니다")
                                        check_del_save()
                                    if del_agree == "N" or del_agree == "n":
                                        print("취소하였습니다")
                                        continue
                                if del_code == "0":
                                    continue
                                if del_code == open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]:
                                    del_agree = str(input("수강 정보를 삭제하시겠습니까? Y/N"))
                                    if del_agree == "Y" or del_agree == "y":
                                        del (json_big_data[i]["수강정보"]["강좌" + str(x)])
                                        print("수강 정보를 삭제하였습니다")
                                        check_del_save()
                                    if del_agree == "N" or del_agree == "n":
                                        print("취소하였습니다")
                                        continue
                            if del_number == 3:
                                print("변경된 사항을 저장하겠습니다")
                                with open(os.getcwd() + os_delimeter + json_file_name, 'w',
                                          encoding="utf-8") as make_file:
                                    readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                    make_file.write(readable_result)
                                    print('저장되었습니다.')
                                    break

    if pg_selection == 5:  # 프로그램 종료
        print("")
        print(("종료되었습니다").center(114))
        print("")
        break

    #
    #     with open(os.getcwd() + os_delimeter +'ITT_Student.json', 'w', encoding='utf8') as outfile:
    #         readable_result = json.dumps(st_datebase, indent=4, sort_keys=True, ensure_ascii=False)
    #         outfile.write(readable_result)
    #         print('ITT_Student.json SAVED')
    #         break