import json
import os

def Start_Student(json_big_data):
    while True:
        print("<<json기반 주소록 관리 프로그램>>".center(33))  ## .center(30) 하면 총 글자 수 30칸에서 가운데 정렬
        initial_number = int(input("===원하는 서비스의 번호를 눌러주세요~ 찡긋;)===\n1. 학생 정보 입력\n2. 학생 정보 조회\n3. 학생 정보 수정"
                                  "\n4. 학생 정보 삭제\n5. 프로그램 종료\n-> "))
        if initial_number == 1:      ## 학생 정보 입력
            Create_Student(json_big_data)
        elif initial_number == 2:       ## 학생 정보 조회
            Select_Student(json_big_data)
        elif initial_number == 3:        ## 학생 정보 수정
            search_id = input("정보 수정을 원하는 학생의 ID를 입력해 주세요(예, ITT001) (돌아가기 : Enter)\n"
                              "-> ")
            if search_id == "":     ## 엔터시 '돌아가기' 기능
                continue
            else:
                Find_ID(search_id, json_big_data)   ## 학생 정보 수정 전, ID 조회 함수
                                                 ## 함수로 만들지 않고, 여기에 바로 적으면
                                                ## print("일치하는 ID가 없습니다. ID를 확인해 주세요!!\n")가 무조건 출력되는!!
        elif initial_number == 4:         ## 학생 정보 삭제
            delete_info = input("정보 삭제를 원하는 학생의 ID를 입력해 주세요 : ")
            Delete_Student(json_big_data, delete_info)
        elif initial_number == 5:           ## 프로그램 종료
            print("이용해 주셔서 감사합니다!! 찡긋;)")
            break
        else: print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")

def Create_Student(json_big_data):
    print("<<학생 정보 입력을 진행하겠습니다. (돌아가기 : Enter)>>".center(50))
    total_student_list = []
    create_student = {}         ## depth 1
    create_student['이름'] = input("이름을 입력해 주세요(예, 홍길동) : ")
    if create_student['이름'] == "": return None      ## 엔터시 '돌아가기' 기능
    create_student['나이'] = input("나이를 입력해 주세요(예, 29) : ")
    if create_student['나이'] == "": return None
    create_student['주소'] = input("주소를 입력해 주세요(예, 대구광역시 달서구 성지로 14안길 17) : ")
    if create_student['주소'] == "": return None
    create_student['수강 정보'] = create_student_course_info = {}       ## depth 2
    create_student_course_info['과거 수강 횟수'] = input("과거 수강 횟수를 입력해 주세요(예, 0) : ")
    if create_student_course_info['과거 수강 횟수'] == "": return None
    print("현재 수강 정보를 입력하시겠습니까? (y/n)")
    create_student_course_info_now = {}         ## depth 3
    create_student_course_info['현재 수강 과목'] = create_student_course_info_now_list = []
    while True:
        now_course_exist = input(" : ")
        if now_course_exist == 'Y' or now_course_exist == 'y':
            Create_Course(create_student_course_info_now, create_student_course_info_now_list, create_student, create_student_course_info, json_big_data)
            print("추가 수강 정보를 입력하시겠습니까? (y/n)")
        elif now_course_exist == 'N' or now_course_exist == 'n':
            if os.path.isfile("Student_ID_info.txt"):  ## 고유 아이디 생성 후 배정_아이디 배정 txt 파일이 있을 경우
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
                    create_student['student_ID'] = student_id
                    json_big_data.append(create_student)

                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("학생 정보 입력이 완료되었습니다!!\n")

            elif not os.path.isfile("Student_ID_info.txt"):     ## 아이디 배정 txt 파일이 없을 경우
                if len(json_big_data) > 0:      ## 입력값이 이미 있고, 추가로 작성할 경우
                    id_index_add = len(json_big_data)
                    with open('Student_ID_info.txt', 'w') as student_id_info:
                        student_id_info.write("ITT" + "{0:0>3}".format(str(len(json_big_data)+1)))
                    with open('Student_ID_info.txt', 'r') as student_id_info:
                        student_id = student_id_info.readline()
                        create_student['student_ID'] = student_id
                        json_big_data.append(create_student)
                    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                        outfile.write(readable_result)
                        print("학생 정보 입력이 완료되었습니다!!\n")
                else:       ## 처음부터 입력할 경우
                    with open('Student_ID_info.txt', 'w') as student_id_info:
                        student_id_info.write("ITT" + "001")
                    with open('Student_ID_info.txt', 'r') as student_id_info:
                        student_id = student_id_info.readline()
                        create_student['student_ID'] = student_id
                        json_big_data.append(create_student)
                    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                        outfile.write(readable_result)
                        print("학생 정보 입력이 완료되었습니다!!\n")
            break
        elif now_course_exist == "": return None
        else:
            print("입력을 잘못하셨습니다. Y 또는 N을 선택해 주세요:)")

def Create_Course(create_student_course_info_now, create_student_course_info_now_list, create_student, create_student_course_info, json_big_data):
    create_student_course_info_now = {}         ## depth 3
    create_student_course_info_now['강의 코드'] = input("강의 코드를 입력해 주세요(예, PY171106) : ")
    if create_student_course_info_now['강의 코드'] == "": return None       ## 엔터시 '돌아가기' 기능
    create_student_course_info_now['강의명'] = input("강의명을 입력해 주세요(예, 점프투 파이썬) : ")
    if create_student_course_info_now['강의명'] == "": return None
    create_student_course_info_now['강사명'] = input("강사명을 입력해 주세요(예, 이현구) : ")
    if create_student_course_info_now['강사명'] == "": return None
    create_student_course_info_now['개강일'] = input("개강일을 입력해 주세요(예, 2017-11-06) : ")
    if create_student_course_info_now['개강일'] == "": return None
    create_student_course_info_now['종료일'] = input("종료일을 입력해 주세요(예, 2018-09-05) : ")
    if create_student_course_info_now['종료일'] == "": return None
    create_student_course_info_now_list.append(create_student_course_info_now)
    create_student.get('수강 정보')['현재 수강 과목'] = create_student_course_info_now_list

def Select_Student(json_big_data):
    print("<<학생 정보 조회를 진행하겠습니다.>>".center(30))
    select_number = int(input("===원하는 조회 서비스의 번호를 눌러주세요~ 찡긋;)===\n"
                                  "1. 전체 학생 조회\n2. 개별 학생 조회\n0. 돌아가기\n-> "))
    if select_number == 1:
        Total_Student(json_big_data)
    elif select_number == 2:
        print("<<개별 학생 정보 조회합니다.>>".center(30))
        personal_select_number = int(input("===원하는 개별 학생 조회 서비스의 번호를 눌러주세요~ 찡긋;)===\n"
                                           "1. ID\n2. 이름\n3. 나이\n4. 주소\n5. 과거 수강 횟수\n6. 강의 코드\n7. 강의명\n"
                                           "8. 강사명\n0. 돌아가기\n-> "))
        if  personal_select_number == 1:
            personal_select_number = 'student_ID'
            print("<<ID를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 ID를 입력해 주세요 : ")      ## search_id 이런 개별 변수가 아닌 통합된 변수(key_name)로 받는 게 포인트!!
            Personal_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 2:
            personal_select_number = '이름'
            print("<<이름을 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 이름을 입력해 주세요 : ")
            Personal_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 3:
            personal_select_number = '나이'
            print("<<나이를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 나이를 입력해 주세요 : ")
            Personal_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 4:
            personal_select_number = '주소'
            print("<<주소를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 주소를 입력해 주세요 : ")
            Personal_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 5:
            personal_select_number = '과거 수강 횟수'
            print("<<과거 수강 횟수를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 과거 수강 횟수를 입력해 주세요 : ")
            Low_Persoanl_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 6:
            personal_select_number = '강의 코드'
            print("<<강의 코드를 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 강의 코드를 입력해 주세요 : ")
            Low_Persoanl_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 7:
            personal_select_number = '강의명'
            print("<<강의명을 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 강의명을 입력해 주세요 : ")
            Low_Persoanl_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 8:
            personal_select_number = '강사명'
            print("<<강사명을 통한 개별 학생 조회를 진행하겠습니다.>>".center(30))
            key_name = input("조회를 원하는 강사명을 입력해 주세요 : ")
            Low_Persoanl_Student(key_name, personal_select_number, json_big_data)
        elif personal_select_number == 0: return None
        else: print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")

    elif select_number == 0:
        return None
    else: print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")

def Total_Student(json_big_data):       ## 전체 학생 정보 조회하는 함수
    print("<<전체 학생 정보 조회합니다.>>".center(30))
    for total_print in json_big_data:
        Personal_Student_Print(total_print)     ## 각각의 학생들 정보 출력을 위해 Personal_Student_Print(total_print) 함수로

def Personal_Student(key_name, personal_select_number, json_big_data):     ## depth 1_ 개별 학생 정보 조회 함수
    search_index = []
    index_number = -1
    for search in json_big_data:
        index_number += 1
        if key_name in str(search.get(personal_select_number)):
            search_index.append(index_number)
    if len(search_index) == 1:
        Personal_Student_Index(personal_select_number, search_index, key_name, json_big_data)
    elif len(search_index) > 1:
        print("'%s'이/가 포함된 '%s'을/를 가진 학생은 %s명입니다." % (key_name, personal_select_number, len(search_index)))
        Mul_ID_Print(search_index, key_name, json_big_data)

def Low_Persoanl_Student(key_name, personal_select_number, json_big_data):     ## depth 2_ 개별 학생 정보 조회 함수
    search_index = []
    index_number = -1
    if personal_select_number == '과거 수강 횟수':        ## 과거 수강 횟수 조회
        for search in json_big_data:
            index_number += 1
            if key_name in str(search.get('수강 정보').get(personal_select_number)):
                search_index.append(index_number)
        if len(search_index) == 1:
            Personal_Student_Index(personal_select_number, search_index, key_name, json_big_data)
        elif len(search_index) > 1:
            print("'%s'이/가 포함된 '%s'을/를 가진 학생은 %s명입니다." % (key_name, personal_select_number, len(search_index)))
            Mul_ID_Print(search_index, key_name, json_big_data)
    else:       ## depth 3_ 현재 수강 과목(강의 코드, 강의명, 강사명) 조회
        for search in json_big_data:
            index_number += 1
            for now_course in search.get('수강 정보').get('현재 수강 과목'):
                if key_name in now_course.get(personal_select_number):
                    search_index.append(index_number)
                    break
        if len(search_index) == 1:
            Personal_Student_Index(personal_select_number, search_index, key_name, json_big_data)
        elif len(search_index) > 1:
            print("'%s'이/가 포함된 '%s'을/를 가진 학생은 %s명입니다." % (key_name, personal_select_number, len(search_index)))
            Mul_ID_Print(search_index, key_name, json_big_data)

def Personal_Student_Index(personal_select_number, search_index, key_name, json_big_data):     ## 학생 정보 조회 -> ID가 하나일 경우 출력 전 함수
    total_print = json_big_data[search_index[0]]
    print("'%s'에 '%s'이/가 포함된 학생의 정보는 다음과 같습니다." % (personal_select_number, key_name))
    Personal_Student_Print(total_print)                             # 출력을 위해 Personal_Student_Print(total_print) 함수로

def Mul_ID_Print(search_index, key_name, json_big_data):       ## 학생 정보 조회 -> ID 중복일 경우, ID와 이름만 출력하는 함수
    for idx in search_index:
        print("ID : %s      이름 : %s" %(json_big_data[idx].get('student_ID'), json_big_data[idx].get('이름')))
    print("")

def Personal_Student_Print(total_print):        ## 학생 정보 출력 함수
    print("학생 ID : %s" % total_print.get('student_ID'))
    print("이름 : %s" % total_print.get('이름'))
    print("나이 : %s" % total_print.get('나이'))
    print("주소 : %s" % total_print.get('주소'))
    print("수강 정보")
    print("  >> 과거 수강 횟수 : %s" % total_print.get('수강 정보').get('과거 수강 횟수'))
    if total_print.get('수강 정보').get('현재 수강 과목'):
        print("  >> 현재 수강 과목")
        for now_course in total_print.get('수강 정보').get('현재 수강 과목'):
            print("    +강의 코드 : %s" %now_course.get('강의 코드'))
            print("    +강의명 : %s" %now_course.get('강의명'))
            print("    +강사명 : %s" %now_course.get('강사명'))
            print("    +개강일 : %s" %now_course.get('개강일'))
            print("    +종료일 : %s \n" %now_course.get('종료일'))
    print("")

def Find_ID(search_id, json_big_data):      ## 학생 정보 수정 전, ID 조회 함수
    for total_print in json_big_data:  ## ID 조회
        if total_print.get('student_ID') == search_id:
            Update_Student(total_print, json_big_data)
            return None
    print("일치하는 ID가 없습니다. ID를 확인해 주세요!!\n")  ## ID 조회 -> 일치하는 ID가 없을 경우

def Update_Student(total_print, json_big_data):     ## 학생 정보 수정 함수
    print("입력하신 ID의 학생 정보는 다음과 같습니다.")
    Personal_Student_Print(total_print)
    update_code = int(input("수정을 원하는 서비스의 번호를 입력해 주세요\n1. 이름\n2. 나이\n3. 주소\n4. 수강 정보\n0. 돌아가기\n-> "))
    if update_code == 1 or update_code == 2 or update_code == 3:
        if update_code == 1:
            update_content = input("현재 이름은 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print['이름'])
            total_print['이름'] = update_content
        elif update_code == 2:
            update_content = input("현재 나이는 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print['나이'])
            total_print['나이'] = int(update_content)
        elif update_code == 3:
            update_content = input("현재 주소는 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print['주소'])
            total_print['주소'] = update_content
    elif update_code == 4:
            update_class_info = int(input("수정을 원하는 수강 정보의 번호를 입력해 주세요\n"
                                      "1. 과거 수강 횟수\n2. 현재 수강 과목\n0. 돌아가기\n-> "))
            if update_class_info == 1:
                update_content = int(input("현재 과거 수강 횟수는 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % total_print.get('수강 정보').get('과거 수강 횟수')))
                total_print.get('수강 정보')['과거 수강 횟수'] = int(update_content)
            elif update_class_info == 2:
                update_class_code = input("수정을 원하는 수강 과목의 강의 코드를 입력해 주세요 : ")
                class_index = -1
                for idx_class in total_print.get('수강 정보').get('현재 수강 과목'):
                    class_index += 1
                    if idx_class.get('강의 코드') == update_class_code:
                        print("입력하신 강의 코드의 과목 내용은 다음과 같습니다.")
                        print("강의 코드 : %s" % idx_class.get('강의 코드'))
                        print("강의명 : %s" % idx_class.get('강의명'))
                        print("강사명 : %s" % idx_class.get('강사명'))
                        print("개강일 : %s" % idx_class.get('개강일'))
                        print("종료일 : %s \n" % idx_class.get('종료일'))
                        update_class_content_number = int(input("수정을 원하는 과목 내용의 번호를 입력해 주세요\n"
                                                     "1. 강의 코드\n2. 강의명\n3. 강사명\n0. 돌아가기\n-> "))
                        if update_class_content_number == 1:
                            update_class_content = input("현재 강의 코드는 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % idx_class.get('강의 코드'))
                            idx_class['강의 코드'] = update_class_content
                        elif update_class_content_number == 2:
                            update_class_content = input("현재 강의명은 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % idx_class.get('강의명'))
                            idx_class['강의명'] = update_class_content
                        elif update_class_content_number == 3:
                            update_class_content = input("현재 강사명은 '%s'입니다. 무엇으로 바꾸시겠습니까? : " % idx_class.get('강사명'))
                            idx_class['강사명'] = update_class_content
                        elif update_class_content_number == 0:
                            return None
                        else:
                            print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                            return None
                        break
            elif update_class_info == 0:
                return None
            else:
                print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
                return None
    elif update_code == 0:
        return None
    else:
        print("입력을 잘못하셨습니다. 다시 입력해 주세요!!\n")
        return None

    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print("학생 정보 입력이 수정되었습니다!!\n")

def Delete_Student(json_big_data, delete_info):         ## 학생 정보 삭제 함수
    del_index = -1
    for del_info in json_big_data:
        del_index += 1
        if del_info.get('student_ID') == delete_info:
            print("입력하신 ID의 학생 정보는 다음과 같습니다.")
            for total_print in json_big_data:  ## ID 조회
                if total_print.get('student_ID') == delete_info:
                    Personal_Student_Print(total_print)     ## 입력한 ID의 학생 정보 출력
            del_number = int(input("'%s' 학생의 삭제 내용을 선택해 주세요\n1. 모든 정보 삭제\n2. 수강 강의 정보만 삭제\n0. 돌아가기\n-> " % delete_info))
            if del_number == 1:
                del json_big_data[del_index]
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print("ID '%s' 학생 정보가 모두 삭제 되었습니다!!\n" % delete_info)
                    return None
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
                            print("ID '%s' 학생의 수강 강의 중 '%s' 강의가 삭제되었습니다!!\n" % (delete_info, del_class_code))
                            return None
            elif del_number == 0:
                return None

    else:
        print("일치하는 ID가 없습니다. ID를 확인해 주세요!!\n")
        return None


## Entry Point~~
json_big_data = []
if os.path.isfile("ITT_Student.json"):      ## 프로그램 시작 시 소스코드가 있는 경로에 'ITT_Student.json' 파일을 읽어 들인다
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        Start_Student(json_big_data)
elif not os.path.isfile("ITT_Student.json"):        ## 파일이 없을 시
    path_number = int(input("<<파일이 존재하지 않습니다.>>\n1. 경로 선택\n2. 신규 생성\n-> "))
    if path_number == 1:
        path_path = input("파일 경로를 입력해 주세요 : ")
        with open("%s\\ITT_Student.json" % path_path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
            Start_Student(json_big_data)
    elif path_number == 2:
        Start_Student(json_big_data)
    else:
        print("입력을 잘못하셨습니다. 프로그램을 종료합니다:)\n")