import pickle
import json

name = "name"
age = "age"
address = "address"
class_info = "class_info"
p_registration = "p_registration"
attending_class = "attending_class"
c_name = "c_name"
c_tutor = "c_tutor"
c_open = "c_open"
c_close = "c_close"

def input_student_info_form_of_dic(primary_index_list) :
    primary_key = primary_index_list.pop()
    student_name = input("학생의 이름을 입력하십시오.\ne.g)김상엽 : ")
    student_age = input("학생의 나이를 입력하십시오.\ne.g)30 : ")
    student_address = input("학생의 주소를 입력하십시오.\ne.g)경북 경산시 조영동 297-2 : ")
    student_past_registration_times = input("학생의 과거 수강 횟수를 입력하십시오. : ")
    returned_result = \
        {
            primary_key:
                {
                    name: student_name, age: student_age, address: student_address,
                    class_info:
                        {
                            p_registration: student_past_registration_times,
                            attending_class: {}
                        }
                }
        }
    while 1 :
        order_1 = input("현재 수강 과목 정보를 추가하시겠습니까?(1:입력 2:무시) : ")
        if order_1 == '2' : break
        elif order_1 == '1' :
            student_attending_class_code = input("학생이 수강중인 강의코드를 입력하십시오.(강의코드 알파벳 2자리 + 개강 년월일 6자리)\n\
e.g)IB171106 : ")
            student_attending_class_name = input("학생이 수강중인 강의명을 입력하십시오.\n\
e.g)IoT 빅데이터 실무반 : ")
            student_attending_class_tutor = input("학생이 수강중인 강의의 강사명을 입력하십시오.\n\
e.g)이현구 : ")
            student_attending_class_open_date = input("학생이 수강중인 강의의 개강날짜들을 입력하십시오.\n\
e.g)2017-11-06 : ")
            student_attending_class_close_date = input("학생이 수강중인 강의의 종강날짜들을 입력하십시오.\n\
e.g)2018-09-05 : ")
            returned_result[primary_key][class_info][attending_class][student_attending_class_code] = \
            {
                "c_name" : student_attending_class_name,
                "c_tutor" : student_attending_class_tutor,
                "c_open" : student_attending_class_open_date,
                "c_close" : student_attending_class_close_date
            }
    return returned_result

def add_attending_class(list_index, primary_key_value) :
    new_student_attending_class_code = input("학생이 수강중인 강의코드를 입력하십시오.(강의코드 알파벳 2자리 + 개강 년월일 6자리)\n\
e.g)IB171106 : ")
    new_student_attending_class_name = input("학생이 수강중인 강의명을 입력하십시오.\n\
e.g)IoT 빅데이터 실무반 : ")
    new_student_attending_class_tutor = input("학생이 수강중인 강의의 강사명을 입력하십시오.\n\
e.g)이현구 : ")
    new_student_attending_class_open_date = input("학생이 수강중인 강의의 개강날짜들을 입력하십시오.\n\
e.g)2017-11-06 : ")
    new_student_attending_class_close_date = input("학생이 수강중인 강의의 종강날짜들을 입력하십시오.\n\
e.g)2018-09-05 : ")
    json_big_data[list_index][primary_key_value][class_info][attending_class][new_student_attending_class_code] = \
        {
            "c_name": new_student_attending_class_name,
            "c_tutor": new_student_attending_class_tutor,
            "c_open": new_student_attending_class_open_date,
            "c_close": new_student_attending_class_close_date
        }

def show_student_info(saved_primary_key_index, saved_primary_key) :
    print("<학생정보>")
    print("-학생아이디 : %s" % list(json_big_data[saved_primary_key_index].keys())[0])
    print("-학생이름 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][name])
    print("-학생나이 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][age])
    print("-학생주소 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][address])
    print("-수강정보")
    print(">>과거수강횟수 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][p_registration])
    temp_attending_class_keys_list = list(json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class].keys())
    for y in temp_attending_class_keys_list:
        print(">>현재수강과목코드 : %s" % y)
        print(">>현재수강강의이름 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_name])
        print(">>현재수강강의교사 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_tutor])
        print(">>현재수강강의개강 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_open])
        print(">>현재수강강의종강 : %s" % json_big_data[saved_primary_key_index][saved_primary_key][class_info][attending_class][y][c_close])
        print()

def get_student_primary_key_list() :
    temp_student_primary_key_list = []
    for x in range(len(json_big_data)):
        temp_student_primary_key_list.append([x, list(json_big_data[x].keys())[0]])
    return temp_student_primary_key_list

def show_all() :
    for x in student_primary_key_list :
        show_student_info(x[0], x[1])
        print("------------------------------------------------------------------------")
    return None

def check_codition(stored_data, input_data) :
    divide_stored_data = list(str(stored_data))
    divide_inputted_data = list(str(input_data))
    append_or_not = '0'
    starting_index = -1
    for x in range(len(divide_stored_data)) :
        if divide_stored_data[x] == divide_inputted_data[0] :
            starting_index = x
            break
    if starting_index == -1 : return append_or_not
    elif starting_index != -1 :
        for x in range(len(divide_inputted_data)) :
            try :
                if divide_stored_data[starting_index+x] == divide_inputted_data[x] : append_or_not = '1'
                else :
                    append_or_not = '0'
                    return append_or_not
            except :
                append_or_not = '0'
                return append_or_not
        return append_or_not

def search_with_student_primary_key(primary_key) :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if check_codition(x[1], primary_key) == '1' :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1 : show_student_info(searched_student_name_list[0][0],
                                                                searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1 :
        print("2개 이상의 결과가 검색되어 아이디와 이름만만 보여줍니다.")
        for x in searched_student_name_list :
            print("아이디 : %s    이름 : %s " %(x[1], json_big_data[x[0]][x[1]][name]))
    return None

def search_into_one_depth(input_data_category, input_data) :
    searched_student_name_list = []
    for x in student_primary_key_list:
        if check_codition(json_big_data[x[0]][x[1]][input_data_category], input_data) == '1':
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0][0],
                          searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1:
        print("2개 이상의 결과가 검색되어 아이디와 이름만 보여줍니다.")
        for x in searched_student_name_list:
            print("아이디 : %s    이름 : %s " %(x[1], json_big_data[x[0]][x[1]][name]))
    return None

def search_with_past_registrarion(student_ragistrantion) :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if check_codition(json_big_data[x[0]][x[1]][class_info][p_registration], student_ragistrantion) == '1' :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1 : show_student_info(searched_student_name_list[0][0],
                                                                searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1 :
        print("2개 이상의 결과가 검색되어 아이디와 이름만만 보여줍니다.")
        for x in searched_student_name_list:
            print("아이디 : %s    이름 : %s " %(x[1], json_big_data[x[0]][x[1]][name]))
    return None

def search_with_now_studying() :
    searched_student_name_list = []
    for x in student_primary_key_list :
        if list(json_big_data[x[0]][x[1]][class_info][attending_class].keys()) != [] :
            searched_student_name_list.append(x)
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0][0],
                          searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1:
        print("2개 이상의 결과가 검색되어 아이디와 이름만만 보여줍니다.")
        for x in searched_student_name_list:
            print("아이디 : %s    이름 : %s " %(x[1], json_big_data[x[0]][x[1]][name]))
    elif searched_student_name_list == [] : print("수강중인 학생이 없습니다.")
    return None

def search_into_two_depth(input_data_category, input_data) :
    searched_student_name_list = []
    for x in student_primary_key_list:
        student_class_code_list = list(json_big_data[x[0]][x[1]][class_info][attending_class].keys())
        for y in student_class_code_list:
            if check_codition(json_big_data[x[0]][x[1]][class_info][attending_class][y][input_data_category], input_data) == '1':
                searched_student_name_list.append(x)
                break
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0][0],
                          searched_student_name_list[0][1])
    elif len(searched_student_name_list) > 1:
        print("2개 이상의 결과가 검색되어 아이디와 이름만만 보여줍니다.")
        for x in searched_student_name_list:
            print("아이디 : %s    이름 : %s " %(x[1], json_big_data[x[0]][x[1]][name]))
    elif searched_student_name_list == []:
        print("수강중인 학생이 없습니다.")
    return None

def delet_with_student_primary_key(primary_key) :
    for x in student_primary_key_list :
        if primary_key == x[1] :
            del(json_big_data[x[0]])
            left_primary_key_index_list.append(primary_key)
            return None

def update_student_info(primary_key) :
    for x in student_primary_key_list :
        if primary_key == x[1] :
            while 1 :
                print("선택하신 아이디의 정보는 아래와 같습니다.")
                print("1:학생이름 : %s" % json_big_data[x[0]][x[1]][name])
                print("2:학생나이 : %s" % json_big_data[x[0]][x[1]][age])
                print("3:학생주소 : %s" % json_big_data[x[0]][x[1]][address])
                print("-수강정보")
                print("4:과거수강횟수 : %s" % json_big_data[x[0]][x[1]][class_info][p_registration])
                temp_attending_class_keys_list = list(json_big_data[x[0]][x[1]][class_info][attending_class].keys())
                print("5:현재수강강의 코드 : ", end = '')
                print(temp_attending_class_keys_list)
                print("6:현재수강강의 추가 : ")
                print("7:수정 끝")
                order_1 = input("바꾸려는 정보를 선택하십시오. : ")
                if order_1 == '7' : break
                elif order_1 == '1' :
                    new_name = input("이름을 입력하십시오.\ne.g)김상엽 : ")
                    json_big_data[x[0]][x[1]][name] = new_name
                elif order_1 == '2' :
                    new_age = input("나이를 입력하십시오.\ne.g)30 : ")
                    json_big_data[x[0]][x[1]][age] = new_age
                elif order_1 == '3' :
                    new_address = input("주소를 입력하십시오.\ne.g)경북 경산시 조영동 : ")
                    json_big_data[x[0]][x[1]][address] = new_address
                elif order_1 == '4' :
                    new_p_registration = input("과거수강횟수를 입력하십시오.\ne.g)0 : ")
                    json_big_data[x[0]][x[1]][class_info][p_registration] = new_p_registration
                elif order_1 == '5' :
                    c_code_from = input("바꾸려는 강의를 코드를 입력하십시오. : ")
                    print(">>현재수강강의이름 : %s" %json_big_data[x[0]][x[1]][class_info][attending_class][c_code_from][c_name])
                    print(">>현재수강강의교사 : %s" %json_big_data[x[0]][x[1]][class_info][attending_class][c_code_from][c_tutor])
                    print(">>현재수강강의개강 : %s" %json_big_data[x[0]][x[1]][class_info][attending_class][c_code_from][c_open])
                    print(">>현재수강강의종강 : %s" %json_big_data[x[0]][x[1]][class_info][attending_class][c_code_from][c_close])
                    order_2 = input("현재 수강 과목 정보를 수정하시겠습니까?(1:예 2:아니오 3:삭제) : ")
                    if order_2 == '2' : pass
                    elif order_2 == '1' :
                        print()
                        del(json_big_data[x[0]][x[1]][class_info][attending_class][c_code_from])
                        add_attending_class(x[0], x[1])
                    elif order_2 == '3' : del(json_big_data[x[0]][x[1]][class_info][attending_class][c_code_from])
                elif order_1 == '6' :
                    print()
                    add_attending_class(x[0], x[1])
    return None

def main_function() :
    global student_primary_key_list
    print("학생 정보 관리 프로그램입니다.".center(30))
    while 1 :
        order_1 = input("\n동작을 선택해 주십시오.\n\
1:학생 정보입력\n2:학생 정보조회\n3:학생 정보수정\n4:학생 정보삭제\n5:프로그램 종료\n동작입력 : ")
        if order_1 == '5' : break
        elif order_1 == '1' :
            print()
            while 1 :
                print()
                json_big_data.append(input_student_info_form_of_dic(left_primary_key_index_list))
                student_primary_key_list = get_student_primary_key_list()
                order_2 = input("계속 하시겠습니까?(1:예 2:아니오) : ")
                if order_2 == '2' : break
                elif order_2 == '1' : continue
        elif order_1 == '2' :
            print()
            while 1 :
                order_2 = input("\n1:전체정보출력\n2:ID로조회\n3:이름으로조회\n4:나이로조회\n5:주소로조회\n6:과거수강횟수로조회\n\
7:현재강의를수강하는학생으로조회\n8:현재수강과목의강의명으로조회\n9:현재수강과목의강사로조회\n10:상위메뉴로\n동작입력 : ")
                if order_2 == '10' : break
                elif order_2 == '1' :
                    print()
                    show_all()
                elif order_2 == '2' :
                    print()
                    input_data = input("아이디를 입력하세요. : ")
                    search_with_student_primary_key(input_data)
                elif order_2 == '3' :
                    print()
                    input_data = input("이름을 입력하세요. : ")
                    search_into_one_depth(name, input_data)
                elif order_2 == '4' :
                    print()
                    input_data = input("나이를 입력하세요. : ")
                    search_into_one_depth(age, input_data)
                elif order_2 == '5' :
                    print()
                    input_data = input("주소를 입력하세요. : ")
                    search_into_one_depth(address, input_data)
                elif order_2 == '6' :
                    print()
                    input_data = input("과거수강횟수를 입력하세요. : ")
                    search_with_past_registrarion(input_data)
                elif order_2 == '7' :
                    print()
                    search_with_now_studying()
                elif order_2 == '8' :
                    print()
                    input_data = input("현재수강과목의강의명을 입력하세요. : ")
                    search_into_two_depth(c_name, input_data)
                elif order_2 == '9' :
                    print()
                    input_data = input("현재수강과목의강사명을 입력하세요. : ")
                    search_into_two_depth(c_tutor, input_data)
        elif order_1 == '3' :
            print()
            input_data = input("수정하려는 아이디를 입력하십시오. : ")
            update_student_info(input_data)
            student_primary_key_list = get_student_primary_key_list()
        elif order_1 == '4' :
            print()
            input_data = input("삭제하려는 아이디를 입력하십시오. : ")
            delet_with_student_primary_key(input_data)
            student_primary_key_list = get_student_primary_key_list()
    return None
########################################################################################################################

json_file_name = "ITT_Student.json"
primary_code_index_file_name = "json_primary_code_sort.txt"
json_big_data = []
left_primary_key_index_list = []
student_primary_key_list = []

try :
    with open(json_file_name, encoding='UTF8') as json_file :
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        student_primary_key_list = get_student_primary_key_list()
    with open(primary_code_index_file_name, 'rb') as json_index :
        left_primary_key_index_list = pickle.load(json_index)
    main_function()
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        jsonResult = json_big_data
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
    with open(primary_code_index_file_name, 'wb') as json_index :
        pickle.dump(left_primary_key_index_list, json_index)

except FileNotFoundError :
    file_not_found = input("%s파일이 없습니다. 다음 동작을 선택해 주십시오.(1:신규생성 2:경로설정) : " %json_file_name)
    if file_not_found == '2' :
        path = input("경로를 입력해 주십시오.\ne.g)D:\\Pycharm_projects\\Emigration\\Jason_Practice\\ : ")
        try :
            with open(path + json_file_name, encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                json_big_data = json.loads(json_string)
            with open(path + primary_code_index_file_name, 'rb') as index_file :
                left_primary_key_index_list = pickle.load(index_file)
            main_function()
            with open(path + json_file_name, 'w', encoding='utf8') as outfile:
                jsonResult = json_big_data
                readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
            with open(path + primary_code_index_file_name, 'wb') as json_index:
                pickle.dump(left_primary_key_index_list, json_index)
        except :
            print("해당 경로에도 파일이 없습니다. 기본 경로에서 신규생성을 합니다.")
            file_not_found = '1'

    if file_not_found == '1' :
        with open(primary_code_index_file_name, 'wb') as index_file:
            temp_str = ""
            for x in range(1, 1000):
                temp_str += "ITT" + "{0:0>3}".format(str(x)) + '\n'
            left_primary_key_index_list = list(reversed(temp_str[:-1].split('\n')))
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                json_big_dict = []
                while 1 :
                    order_1 = input("학생정보를 추가하시겠습니까?(1:예 2:아니오) : ")
                    if order_1 == '2' : break
                    elif order_1 == '1' : json_big_dict.append(input_student_info_form_of_dic(left_primary_key_index_list))
                jsonResult = json_big_dict[:]
                readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')
            pickle.dump(left_primary_key_index_list, index_file)
        main_function()
    else :
        print("동작 선택 좀 똑디 하소.")
print("프로그램 종료")