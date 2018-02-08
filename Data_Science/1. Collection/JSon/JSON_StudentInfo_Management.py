import json
import os

g_student_id_index = 0
g_file_name_saved = 'ITT_Student.json'
g_student_id = 'student_ID'
g_student_name = 'student_name'
g_student_age = 'student_age'
g_address = 'address'
g_total_course_info = 'total_course_info'
g_num_of_course_learned = 'num_of_course_learned'
g_learning_course_info = 'learning_course_info'
g_course_code = 'course_code'
g_course_name = 'course_name'
g_teacher = 'teacher'
g_open_date = 'open_date'
g_close_date = 'close_date'
g_json_bigdata = []

def print_initial_menu():
    print("\n           << JSON기반 학생 정보 관리 프로그램 >>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")
    print("메뉴를 선택하세요:",end=" ")

def create_student_ID():
    global g_student_id_index
    g_student_id_index = g_student_id_index+1
    student_id = "ITT" + str(g_student_id_index).zfill(3)
    return student_id

def get_learning_course_info_list():
    temp_learning_course_list=[]

    while True:
        temp_learning_course={
            g_course_code: input("강의코드 (예: IB171106, OB0104 ..): "),
            g_course_name: input("강의명 (예: IOT 빅데이터 실무반): "),
            g_teacher: input("강사 (예: 이현구): "),
            g_open_date: input("개강일 (예: 2017-11-06): "),
            g_close_date: input("종료일 (예: 2018-09-05): ")
        }
        temp_learning_course_list.append(temp_learning_course)

        if(input("현재 수강하는 과목이 더 있습니까? (y/n) ") == 'n' ):
            break

    return temp_learning_course_list

def input_student_info():
    c_student_id = create_student_ID()
    i_student_name = input("이름 (예: 홍길동 ): ")
    i_student_age = input("나이 (예: 29): ")
    i_address = input("주소 (예: 대구광역시 동구 아양로 135): ")
    i_number_of_course_learned = input("과거 수강 횟수 (예: 1): ")
    learning_course_info_list = []

    if(input("현재 수강 과목이 있습니까? (예: y/n) ") == "y" ):
        learning_course_info_list = get_learning_course_info_list()

    g_json_bigdata.append(
        {
            g_student_id:c_student_id,
            g_student_name:i_student_name,
            g_student_age:i_student_age,
            g_address:i_address,
            g_total_course_info:{
                g_num_of_course_learned:i_number_of_course_learned,
                g_learning_course_info:learning_course_info_list
            }
        }
    )

def print_read_student_info_menu():
    print("\n아래 메뉴를 선택하세요.")
    print("1. 전체 학생정보 조회")
    print(" 검색 조건 선택")
    print("2. ID 검색")
    print("3. 이름 검색")
    print("4. 나이 검색")
    print("5. 주소 검색")
    print("6. 과거 수강 횟수 검색")
    print("7. 현재 강의를 수강중인 학생")
    print("8. 현재 수강 중인 강의명")
    print("9. 현재 수강 강사")
    print("10. 이전 메뉴")

    print("메뉴를 선택하세요: ", end=" ")

def print_matched_student_info(student_data):
    print("\n* 학생 ID: ", student_data.get(g_student_id))
    print("* 이름: ", student_data.get(g_student_name))
    print("* 나이: ", student_data.get(g_student_age))
    print("* 주소: ", student_data.get(g_address))
    print("* 수강 정보")
    print(" + 과거 수강 횟수: ", student_data.get(g_total_course_info).get(g_num_of_course_learned))

    if (g_learning_course_info in student_data.get(g_total_course_info).keys()):
        print(" + 현재 수강 과목")
        for learning_course_data in (student_data.get(g_total_course_info)).get(g_learning_course_info):
            print("  강의 코드: ", learning_course_data.get(g_course_code))
            print("  강의명: ", learning_course_data.get(g_course_name))
            print("  강사: ", learning_course_data.get(g_teacher))
            print("  개강일: ", learning_course_data.get(g_open_date))
            print("  종료일: ", learning_course_data.get(g_close_date))

def print_entire_student_info():
    print("\n- 전체 학생 정보 출력 -")
    for student_data in g_json_bigdata:
        print_matched_student_info(student_data)

def print_student_info_main_menu():
    print("\nUpdate 항목을 선택하세요.")
    print("1. 개인 정보")
    print("2. 현재 수강 중인 강의 정보")
    print("0. 이전 메뉴")
    print("메뉴 번호를 입력하세요: ",end=" ")

def print_student_personal_info_menu():
    print("1. 학생 이름")
    print("2. 나이")
    print("3. 주소")
    print("4. 과거 수강 횟수")
    print("5. 현재 수강 중인 강의 정보")
    print("0. 이전 메뉴")
    print("메뉴 번호를 입력하세요: ",end=" ")

def print_student_course_info_menu():
    print("1. 강의 코드")
    print("2. 강의명 ")
    print("3. 강사")
    print("4. 개강일")
    print("5. 종료일")
    print("0. 취소")
    print("메뉴 번호를 입력하세요: ",end=" ")

def print_delete_student_info_menu():
    print("삭제 할 대상을 선택하세요." )
    print("1. 학생 정보")

def search_student_info(menu_num, keyword):
    if menu_num == 2: dict_key=g_student_id
    elif menu_num == 3: dict_key=g_student_name
    elif menu_num == 4: dict_key=g_student_age
    elif menu_num == 5: dict_key=g_address
    elif menu_num == 6: dict_key=g_num_of_course_learned
    elif menu_num == 8: dict_key=g_course_name
    elif menu_num == 9: dict_key=g_teacher

    matched_index=[]
    search_index=0
    for student_info_element in g_json_bigdata:
        if menu_num >=2 and menu_num <=5: #dictionary depth 1
            if keyword in student_info_element[dict_key]:
                matched_index.append(search_index)
        elif menu_num == 6: # dictionary depth 2 (과거 수강 횟수 검색)
            if keyword in student_info_element[g_total_course_info][dict_key]:
                matched_index.append(search_index)
        elif menu_num >=8 and menu_num <=9: # dictionary depth 3 (과정명, 강사명)
            is_learning_course_matched=False
            for learning_course_element in student_info_element[g_total_course_info][g_learning_course_info]:
                if keyword in learning_course_element[dict_key]:
                    if is_learning_course_matched == False:
                        matched_index.append(search_index)
                    else:
                        is_learning_course_matched = True
                        break

        search_index +=1

    if len(matched_index) == 0:
        print("\n일치된 결과가 없습니다.")
    elif len(matched_index) == 1:
        print_matched_student_info(g_json_bigdata[matched_index[0]])
    else:
        print("\n복수 개의 결과가 검색되었습니다.\n\t\t----- 요약 결과 -----")
        for search_index in matched_index:
            matched_data_str = ">> 학생 ID: "+g_json_bigdata[search_index][g_student_id]+", 학생 이름: "+g_json_bigdata[search_index][g_student_name]
            print(matched_data_str)


def read_student_info():
    print_read_student_info_menu()

    menu_num = int(input())

    if menu_num == 1:
        print_entire_student_info()
    elif (menu_num >= 2 and menu_num <=6) or (menu_num >=8 and menu_num <=9) :
        keyword = input("검색어를 입력하세요: ")
        search_student_info(menu_num,keyword)
    elif menu_num == 10:
        return None
    else:
        print("번호를 잘못 선택하셨습니다. 0번에서 10번까지 입력하세요.")

def update_learning_course_info(student_element, key_in_course_info, value_to_be_changed):
   for learning_course_element in student_element[g_total_course_info] [g_learning_course_info]:
       learning_course_element[key_in_course_info] = value_to_be_changed

def update_student_info():
    student_id = input("\n수정할 학생 ID를 입력하세요: ")
    print_student_personal_info_menu()
    menu_num = int(input())

    if menu_num == 0:
        return None
    elif menu_num != 5:
        value_to_be_changed = input("변경할 값을 입력하세요: ")

    for student_info_element in g_json_bigdata:
        if student_info_element[g_student_id] == student_id and menu_num == 1:
            student_info_element[g_student_name] = value_to_be_changed
        elif student_info_element[g_student_id] == student_id and menu_num == 2:
            student_info_element[g_student_age] = value_to_be_changed
        elif student_info_element[g_student_id] == student_id and menu_num == 3:
            student_info_element[g_address] = value_to_be_changed
        elif student_info_element[g_student_id] == student_id and menu_num == 4:
            student_info_element[g_total_course_info][g_num_of_course_learned] = value_to_be_changed
        elif student_info_element[g_student_id] == student_id and menu_num == 5:
            print_student_course_info_menu()
            sub_menu_num = int(input())
            if sub_menu_num == 0:
                break
            else:
                value_to_be_changed = input("변경할 값을 입력하세요: ")
            if sub_menu_num == 1:
                update_learning_course_info(student_info_element,g_course_code,value_to_be_changed)
            elif sub_menu_num == 2:
                update_learning_course_info(student_info_element,g_course_name,value_to_be_changed)
            elif sub_menu_num == 3:
                update_learning_course_info(student_info_element,g_teacher,value_to_be_changed)
            elif sub_menu_num == 4:
                update_learning_course_info(student_info_element,g_open_date,value_to_be_changed)
            elif sub_menu_num == 5:
                update_learning_course_info(student_info_element,g_close_date,value_to_be_changed)
            elif sub_menu_num == 0:
                break

def save_student_info():
    try:
        with open(g_file_name_saved, 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('%s is saved ' % g_file_name_saved)

    except Exception as e:
        print(e)

def delete_student_info():
    s_index = 0
    c_index = 0
    is_found = False

    student_id = input("\n삭제할 학생 ID를 입력하세요: ")
    print("삭제 유형을 선택하세요.")
    print("1. 전체 삭제")
    print("2. 현재 수강 중인 특정 과목정보 삭제")
    print("3. 이전 메뉴")
    menu_num = int(input("메뉴 번호를 선택하세요: "))

    if menu_num == 3:
        return None

    while s_index < len(g_json_bigdata):
        if student_id in g_json_bigdata[s_index][g_student_id]:
            is_found = True

            if menu_num == 1:
                if (input("정말로 삭제하시겠습니까? (y/n) ") == 'y'):
                    del g_json_bigdata[s_index]
                    break
            elif menu_num ==2:
                course_code = input("삭제할 과목 코드를 입력하세요: ")
                learning_course_info = g_json_bigdata[s_index][g_total_course_info][g_learning_course_info]

                while c_index < len(learning_course_info):
                    if course_code in learning_course_info[c_index][g_course_code]:
                        if (input("정말로 삭제하시겠습니까? (y/n) ") == 'y'):
                            del learning_course_info[c_index]
                            break
                    c_index += 1

        s_index += 1

    if is_found == False:
        print("해당 ID를 갖는 ID가 없습니다.")

if __name__ == '__main__':
    menu_num = 0

    try:
        with open(g_file_name_saved, encoding='UTF8') as json_file: json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_bigdata = json.loads(json_string)
    except:
        print("경로에 파일이 없습니다. 어떻게 하시겠습니까?\n1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.")
        if input("메뉴를 선택하세요: ") == '1':
            try:
                with open(input("경로를 입력하세요: "), encoding='UTF8') as json_file: json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                g_json_bigdata = json.loads(json_string)
            except:
                print("경로 확인 후 다시 프로그램을 시작하세요.")
                exit()

    if os.path.isfile("student_ID_index.txt"):
        with open('student_ID_index.txt', 'r') as id_data:
            id_index = id_data.readline()
            g_student_id_index = int(id_index[3:])
    else:
        with open('student_ID_index.txt', 'w') as id_data:
            id_data.write("ITT001")

    while True:
        print_initial_menu()
        menu_num = int(input())

        if menu_num == 1:
            student_info = input_student_info()
            #insert_student_info(student_info)
        elif menu_num == 2:
            read_student_info()
        elif menu_num == 3:
            update_student_info()
        elif menu_num == 4:
            delete_student_info()
        elif menu_num == 5:
            with open('student_ID_index.txt', 'w') as id_data:
                id_data.write("ITT" + str(g_student_id_index).zfill(3))
            save_student_info()
            break

    print("학생 정보 관리 프로그램을 종료합니다.")