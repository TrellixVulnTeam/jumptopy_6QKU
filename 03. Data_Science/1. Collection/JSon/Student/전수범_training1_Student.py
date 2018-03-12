import json
import os


def Start_Student(json_big_data):
    while True:
        student_data = {}
        total_course_info = {}
        now_course_info_list = []
        now_course_info_dict = {}

        print("<<json기반 주소록 관리 프로그램>>".center(33))  ## .center(30) 하면 총 글자 수 30칸에서 가운데 정렬
        initial_number = int(input("===원하는 서비스의 번호를 눌러주세요~ 찡긋;)===\n1. 학생 정보 입력\n2. 학생 정보 조회\n3. 학생 정보 수정"
                                  "\n4. 학생 정보 삭제\n5. 프로그램 종료\n-> "))
        if initial_number == 1:      ## 학생 정보 입력
            print("<<학생 정보 입력을 진행하겠습니다.>>".center(30))
            student_name = input("이름을 입력해 주세요 : ")
            student_data["이름"] = student_name
            student_age = int(input("나이를 입력해 주세요 : "))
            student_data["나이"] = student_age
            student_address = input("주소를 입력해 주세요 : ")
            student_data["주소"] = student_address
            Class_Code(json_big_data, student_data, total_course_info, now_course_info_list, now_course_info_dict)  ## 강의 코드 - 강의명 - 강사 이름 - 개강일 - 종료일.. 입력 함수

        elif initial_number == 2:        ## 학생 정보 조회
            student_name_count = 0
            instructor_name_count = 0
            class_name_count = 0
            print("<<학생 정보를 조회하겠습니다.>>".center(30))
            search_student = input("조회를 원하는 학생의 정보를 입력해 주세요 : ")
            for search_info in json_big_data:       ## ID 조회
                if search_info.get('student_ID') == search_student:
                    Student_Info(search_student, json_big_data)

            for search_info in json_big_data:       ## 이름 or 강사 이름 or 강의명 카운트_ 중복 확인
                if search_info.get('이름') == search_student:
                    student_name_count += 1
                for now_course_info in search_info.get('수강 정보').get('현재 수강 과목'):
                    if now_course_info.get('강사 이름') == search_student:
                        instructor_name_count += 1
                    elif now_course_info.get('강의명') == search_student:
                        class_name_count += 1

            if student_name_count > 1:      ## 학생 이름 중복 시 ID만 출력
                mul_count = 0
                for search_info in json_big_data:
                    if search_info.get('이름') == search_student:
                        mul_count += 1
                        print("조회한 학생의 ID : %s" % search_info.get('student_ID'))
                print("'%s' 이름을 가진 학생은 %s명입니다." % (search_student, mul_count))
            elif student_name_count == 1:   ## 중복이 없을 시 학생 정보 출력
                Student_Info(search_student, json_big_data)

            if instructor_name_count > 1:       ## 강사 이름 중복 시 ID만 출력
                mul_count = 0
                for search_info in json_big_data:
                    for now_course_info in search_info.get('수강 정보').get('현재 수강 과목'):
                        if now_course_info.get('강사 이름') == search_student:
                            mul_count += 1
                            print("조회한 학생의 ID : %s" % search_info.get('student_ID'))
                print("'%s' 강사님의 수업을 듣는 학생은 %s명입니다." % (search_student, mul_count))
            elif instructor_name_count == 1:
                Student_Info(search_student, json_big_data)

            if class_name_count > 1:        ## 강의명 중복 시 ID만 출력
                mul_count = 0
                for search_info in json_big_data:
                    for now_course_info in search_info.get('수강 정보').get('현재 수강 과목'):
                        if now_course_info.get('강의명') == search_student:
                            mul_count += 1
                            print("조회한 학생의 ID : %s" % search_info.get('student_ID'))
                print("'%s' 강의를 듣는 학생은 %s명입니다." % (search_student, mul_count))
            elif class_name_count == 1:
                Student_Info(search_student, json_big_data)

        elif initial_number == 3:        ## 학생 정보 수정
            search_id = input("정보 수정을 원하는 학생의 ID를 입력해 주세요 : ")
            for search_id_info in json_big_data:       ## ID 조회
                if search_id_info.get('student_ID') == search_id:
                    Student_Update(search_id_info)

        elif initial_number == 4:
            delete_info = input("정보 삭제를 원하는 학생의 ID를 입력해 주세요 : ")
            Delete_Student(json_big_data, delete_info)


        elif initial_number == 5:
            print("이용해 주셔서 감사합니다! 또 놀러 오세요~")
            break


def Class_Code(json_big_data, student_data, total_course_info, now_course_info_list, now_course_info_dict):           ## 수강 정보 입력 함수
    student_past_class = int(input("과거 수강 횟수를 입력해 주세요 : "))         ## 과거 수강 횟수 입력
    total_course_info["과거 수강 횟수"] = student_past_class
    while True:
        print("현재 수강 중인 과목 코드를 입력해 주세요:)\n입력을 모두 다 하셨으면 '종료'를 입력해 주세요!!")       ## 현재 수강 과목 입력
        class_code = input(" : ")
        if class_code != '종료':
            now_course_info_dict = {}           ## 중요!! 이거 없으면 2개 이상 작성할 시, 새롭게 작성하는 걸 이전에 작성한 거 위에 덮어 씀!!
            now_course_info_dict['강의 코드'] = class_code
            class_name = input("강의명을 입력해 주세요 : ")
            now_course_info_dict['강의명'] = class_name
            instructor_name = input("강사 이름을 입력해 주세요 : ")
            now_course_info_dict['강사 이름'] = instructor_name
            open_day = input("개강일을 입력해 주세요 : ")
            now_course_info_dict['개강일'] = open_day
            close_day = input("종료일을 입력해 주세요 : ")
            now_course_info_dict['종료일'] = close_day
            now_course_info_list.append(now_course_info_dict)
        elif class_code == '종료':
            total_course_info['현재 수강 과목'] = now_course_info_list
            student_data['수강 정보'] = total_course_info

            if os.path.isfile("Student_ID_info.txt"):                   ## 고유 아이디 배정
                with open('Student_ID_info.txt', 'r') as numbering:
                    id_number = numbering.readline()
                    split_numbering = id_number[3:]
                    int_split_numbering = int(split_numbering)
                    int_split_numbering += 1
                with open('Student_ID_info.txt', 'w') as student_id_info:
                    student_id_info.write("ITT" + "{0:0>3}".format(str(int_split_numbering)))
                    ## p.65 글자수 3, 오른쪽 정렬, 나머지 0으로
                with open('Student_ID_info.txt', 'r') as student_id_info:
                    student_id = student_id_info.readline()
                    student_data['student_ID'] = student_id
                    json_big_data.append(student_data)

                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("ITT_Student.json SAVED")

            elif not os.path.isfile("Student_ID_info.txt"):
                with open('Student_ID_info.txt', 'w') as student_id_info:
                    student_id_info.write("ITT" + "001")
                with open('Student_ID_info.txt', 'r') as student_id_info:
                    student_id = student_id_info.readline()
                    student_data['student_ID'] = student_id
                    json_big_data.append(student_data)
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("ITT_Student.json SAVED")

            break

def Student_Info(search_student, json_big_data):      ## 학생 정보 조회 출력 함수 1-1
    for search_info in json_big_data:       ## 입력값으로 ID를 받았을 때
        now_course_info = []
        if search_info.get('student_ID') == search_student:
            print("ID '%s'를 가진 학생의 정보는 다음과 같습니다." % search_student)
            Student_Info_Print(search_student, json_big_data, search_info, now_course_info)

    for search_info in json_big_data:       ## 입력값으로 학생 이름을 받았을 때
        now_course_info = []
        if search_info.get('이름') == search_student:
            print("'%s' 학생의 정보는 다음과 같습니다." % search_student)
            Student_Info_Print(search_student, json_big_data, search_info, now_course_info)

    for search_info in json_big_data:   ## 입력값으로 강사 이름 or 강의명을 받았을 때
        for now_course_info in search_info.get('수강 정보').get('현재 수강 과목'):
            if now_course_info.get('강사 이름') == search_student:      ## 입력값으로 강사 이름을 받았을 때
                print("'%s' 강사님의 수업을 듣는 학생 정보는 다음과 같습니다." % search_student)
                Student_Info_Print(search_student, json_big_data, search_info, now_course_info)
            elif now_course_info.get('강의명') == search_student:      ## 입력값으로 강의명을 받았을 때
                print("'%s' 강의를 듣는 학생 정보는 다음과 같습니다." % search_student)
                Student_Info_Print(search_student, json_big_data, search_info, now_course_info)


def Student_Info_Print(search_student, json_big_data, search_info, now_course_info):        ## 학생 정보 조회 출력 함수 1-2
    print("ID : %s" % search_info.get('student_ID'))
    print("이름 : %s" % search_info.get('이름'))
    print("나이 : %s" % search_info.get('나이'))
    print("주소 : %s" % search_info.get('주소'))
    print("")       ## 한 줄 띄어쓰기 위해
    print("과거 수강 횟수 : %s" % search_info.get('수강 정보').get('과거 수강 횟수'))
    print("")       ## 한 줄 띄어쓰기 위해
    print("현재 수강 과목은 다음과 같습니다.")
    for now_course_info in search_info.get('수강 정보').get('현재 수강 과목'):
        print("강사 이름 : %s" % now_course_info.get('강사 이름'))
        print("강의 코드 : %s" % now_course_info.get('강의 코드'))
        print("강의명 : %s" % now_course_info.get('강의명'))
        print("개강일 : %s" % now_course_info.get('개강일'))
        print("종료일 : %s" % now_course_info.get('종료일'))
        print("")       ## 한 줄 띄어쓰기 위해

def Student_Update(search_id_info):       ## 학생 정보 수정 함수
    print("입력하신 ID의 학생 정보는 다음과 같습니다.")
    print(search_id_info)
    update_code = input("수정을 원하시는 부분을 입력해 주세요 : ")
    update_content = input("수정을 원하는, 수정 후 내용을 입력해 주세요 : ")
    if update_code == '이름':
        search_id_info['이름'] = update_content
    elif update_code == '나이':
        search_id_info['나이'] = int(update_content)
    elif update_code == '주소':
        search_id_info['주소'] = update_content
    elif update_code == '과거 수강 횟수':
        update_name = search_id_info['수강 정보']
        update_name['과거 수강 횟수'] = int(update_content)
    elif update_code == '강사 이름':
        change_instructor_name = input("수정을 원하는, 수정 전 강사 이름을 입력해 주세요 : ")
        update_name = search_id_info['수강 정보'].get('현재 수강 과목')
        for search_instructor in update_name:
            if search_instructor['강사 이름'] == change_instructor_name:
                search_instructor['강사 이름'] = update_content
    elif update_code == '강의 코드':
        change_code = input("수정을 원하는, 수정 전 강의 코드를 입력해 주세요 : ")
        update_code_name = search_id_info['수강 정보'].get('현재 수강 과목')
        for search_instructor in update_code_name:
            if search_instructor['강의 코드'] == change_code:
                search_instructor['강의 코드'] = update_content
    elif update_code == '강의명':
        change_class_name = input("수정을 원하는, 수정 전 강의명을 입력해 주세요 : ")
        update_class_name = search_id_info['수강 정보'].get('현재 수강 과목')
        for search_instructor in update_class_name:
            if search_instructor['강의명'] == change_class_name:
                search_instructor['강의명'] = update_content
    elif update_code == '개강일':
        change_open_day = input("수정을 원하는, 수정 전 개강일을 입력해 주세요 : ")
        update_open_day = search_id_info['수강 정보'].get('현재 수강 과목')
        for search_instructor in update_open_day:
            if search_instructor['개강일'] == change_open_day:
                search_instructor['개강일'] = update_content
    elif update_code == '종료일':
        change_close_day = input("수정을 원하는, 수정 전 종료일을 입력해 주세요 : ")
        update_close_day = search_id_info['수강 정보'].get('현재 수강 과목')
        for search_instructor in update_close_day:
            if search_instructor['종료일'] == change_close_day:
                search_instructor['종료일'] = update_content

    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print("ITT_Student.json UPDATED")

def Delete_Student(json_big_data, delete_info):
    del_index = -1
    for del_info in json_big_data:
        del_index += 1
        if del_info.get('student_ID') == delete_info:
            del_number = int(input("%s 학생의 삭제 내용을 선택해 주세요\n1. 모든 정보를 삭제한다.\n2. 수강 강의 정보만 삭제한다.\n : " % delete_info))
            if del_number == 1:
                del json_big_data[del_index]
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("ITT_Student.json DELETED")
            elif del_number == 2:
                del_class_code = input("삭제를 원하시는 수강 강의 코드를 입력해 주세요 : ")
                class_code_list = del_info.get('수강 정보').get('현재 수강 과목')
                code_list_index = -1
                for del_code in class_code_list:
                    code_list_index += 1
                    if del_code['강의 코드'] == del_class_code:
                        del class_code_list[code_list_index]
                        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                            readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                            outfile.write(readable_result)
                            print("ITT_Student.json DELETED")



json_big_data = []
if os.path.isfile("ITT_Student.json"):      ## 프로그램 시작 시 소스코드가 있는 경로에 'ITT_Student.json' 파일을 읽어 들인다
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        Start_Student(json_big_data)
elif not os.path.isfile("ITT_Student.json"):        ## 파일이 없을 시
    path_number = int(input("파일이 존재하지 않습니다.\n경로를 선택하려면 1번, 신규 생성하려면 2번을 눌러주세요\n-> "))
    if path_number == 1:
        path_path = input("파일 경로를 입력해 주세요 : ")
        with open("%s\\ITT_Student.json" % path_path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
            Start_Student(json_big_data)
    elif path_number == 2:
        Start_Student(json_big_data)