## Student_management_programing
import json
import os

jsonResult = []

def ask_path():
    ask = input("안녕하세요! 학생 주소록 관리 프로그램을 시작합니다. 경로에 파일이 없습니다. \n 1. 경로를 입력합니다.  2. 기본 경로로 생성하겠습니다.\n 메뉴를 선택하세요 : ")
    if ask == '1':
        path = input("새로운 경로를 입력하세요 : ")
        print("새로운 경로에 저장합니다.")
        return path
    else:
        print("기본경로로 생성하겠습니다.")
        path = 'ITT_Student.json'
        return path

def main_intro():
    print("")
    print("<< json 기반 주소록 관리 프로그램 >>")
    print("  1. 학생 정보 입력")
    print("  2. 학생 정보 조회")
    print("  3. 학생 정보 수정")
    print("  4. 학생 정보 삭제")
    print("  5. 프로 그램 종료")

def student_ID_number():
    try:
        if not os.path.isfile("ITT_Student.json"):
            with open('count.txt','w') as file:
                counter = '1'
                file.write(counter)
            student_id = "ITT" + counter.zfill(3)
            return  student_id
        else:
            with open('count.txt','r') as file:
                counter = file.readline()
                counter = int(counter) + 1
                student_id = "ITT" + str(counter).zfill(3)

            with open('count.txt', 'w') as file:
                file.write(str(counter))
            return student_id

    except FileNotFoundError:
        if len(jsonResult) == 0:
            counter = '1'
            student_id = "ITT" + counter.zfill(3)
            with open("count.txt",'w') as file:
                file.write(counter)
            return  student_id
        else:
            counter = str(len(jsonResult) + 1)
            with open('count.txt', 'w') as file:
                file.write(counter)
            student_id = "ITT" + counter.zfill(3)
            return student_id

def info_insert():
    student_dic = {}
    recent_info_list = []
    student_dic['name'] = input("이름을 입력하세요 : ")
    student_dic['age'] = str(input("나이를 입력하세요 : "))
    student_dic['address'] = input("주소를 입력하세요 : ")
    student_dic['past_record'] = input("과거 수강 횟수를 입력하세요 : ")
    while True:
        select = input("현재 강의 정보를 추가하시겠습니까? (y/n) : ")
        if select == 'y':
            recent_info_list.append(info_insert_course())
            student_dic['recent_info'] = recent_info_list
            continue
        else:
            break
    student_dic['student_ID'] = student_ID_number()
    jsonResult.append(student_dic)
    print("--------- 학생 정보가 입력되었습니다 ---------")

def info_insert_course():
    recent_info = {}
    recent_info['강의코드'] = input("현재 수강 과목 코드를 기입하세요 : ")
    recent_info['강의명'] = input("강의명을 입력하세요 : ")
    recent_info['강사명'] = input("강사명을 입력하세요 : ")
    recent_info['개강일'] = input("개강일을 입력하세요 : ")
    recent_info['종료일'] = input("종료일을 입력하세요 : ")
    return recent_info

def info_input():
    print("")
    print("--------- 학생 정보 조회를 시작합니다 ---------")
    print("1. 전체 항목 대상 조회")
    print("\t검색 조건 선택\t")
    print("2. 학생 이름")
    print("3. 학생 나이")
    print("4. 학생 주소")
    print("5. 학생 ID")
    print("6. 과거 수강 횟수")
    print("7. 강의명")
    print("8. 강사명")
    print("9. 강의코드")
    print("10. 이전화면으로 되돌아갑니다")
    print("")
    condition = int(input("검색 조건을 선택하세요."))
    return condition

def info_search(element, search_index):
    result = []
    for i in range(len(jsonResult)):
        if not element in jsonResult[i]["recent_info"] :
            if jsonResult[i][element] == search_index:
                result.append(jsonResult[i])
            elif search_index in jsonResult[i][element]:
                result.append(jsonResult[i])
        else:
            for j in range(len(jsonResult[i]["recent_info"])):
                if jsonResult[i]["recent_info"][j][element] == search_index:
                    result.append(jsonResult[i])
                elif search_index in jsonResult[i]["recent_info"][j][element]:
                    result.append(jsonResult[i])
    return result

def info_show_indiviual(result):
    print("")
    for i in range(len(result)):
        print("==================== 학생 회원 정보 ====================")
        print("이름 (예 : 홍길동) : %s " % result[i]['name'])
        print("나이 (예 : 22) : %s " % result[i]['age'])
        print("주소 (예 : 한양시 종로구 우리집) : %s " % result[i]['address'])
        print("학생ID (예 : ITT001) : %s " % result[i]['student_ID'])
        print("과거 수강 횟수 (예 : 1) : %s " % result[i]['past_record'])
        print("==================== 현재 수강 정보 ====================")
        for j in range(len(result[i].get('recent_info'))):
            print("강의코드 : %s"  % result[i].get('recent_info')[j]['강의코드'])
            print("강의명   : %s"  % result[i].get('recent_info')[j]['강의명'])
            print("강사     : %s"  % result[i].get('recent_info')[j]['강사명'])
            print("개강일   : %s"  % result[i].get('recent_info')[j]['개강일'])
            print("종료일   : %s"  % result[i].get('recent_info')[j]['종료일'])
            print("---------------------------------------------------------")
    print("---------------- 회원 정보 조회 성공!! -----------------")

def info_show_plural(result):
    for i in range(len(result)):
        print(">>> %d, 학생이름 : %s, 학생 ID : %s" % (i + 1, result[i]['name'], result[i]["student_ID"]))

def info_revise(result):
    while True:
        print("---- 학생 정보를 수정하겠습니다 ----")
        print("1. 이름\t2. 나이\t2. 주소\t4. 과거 수강 횟수\t5. 강의명\t6. 강의코드\t7. 강사명\t8. 새로운 강의 추가하기\t9. 뒤로가기")
        number = int(input("메뉴를 선택하세요 :"))
        if number < 7:
            revise_value = input("수정할 정보를 입력하세요 :")
            if number == 1 :
                result[0]['name'] = revise_value
            elif number == 2:
                result[0]['age'] = revise_value
            elif number == 3:
                result[0]['address'] = revise_value
            elif number == 4:
                result[0]['past_record'] = revise_value
            elif number == 5 :
                result[0].get('recent_info')[0]['강의명'] = revise_value
            elif number == 6:
                result[0].get('recent_info')[0]['강의코드'] = revise_value
            elif number == 7:
                result[0].get('recent_info')[0]['강사명'] = revise_value
        elif number == 8:
            result[0].get('recent_info').append(info_insert_course())
        elif number == 9 :
            return number
        Quit = input("종료를 원하시면 '종료'라고 입력하세요. 계속 수정하시려면 엔터를 눌러주세요")
        if Quit == '종료':
            break
        else:
            continue

def info_delete():
    know_ask = input("학생ID를 정확하게 알고계십니까?? y/n : ")
    if know_ask == 'n':
        index_key = input("기억하고 있는 정보를 입력하세요 : ")
        info_show_plural(info_search("student_ID",index_key))
    if know_ask == 'y':
        index = input("학생ID를 입력하세요 : ")
        info_show_indiviual(info_search("student_ID",index))
        print('메뉴를 선택하세요')
        number = int(input("1. 학생ID 전체삭제       2. 현재 수강중인 강의삭제 :"))
        if number == 1:
            for element in jsonResult:
                if element['student_ID'] == index:
                    element_del = element
                    jsonResult.remove(element_del)
        elif number == 2:
            index_2 = input("원하시는 과목코드를 입력하세요 : ")
            for i in range(len(jsonResult)):
                if jsonResult[i]['student_ID'] == index:
                    for element_2 in jsonResult[i]['recent_info']:
                        if element_2['강의코드'] == index_2:
                            element_del = element_2
                            jsonResult[i]['recent_info'].remove(element_del)
    print("============= 안전하게 삭제되었습니다 =============")

def info_start(path):
    try:
        with open(path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            jsonResult_load = json.loads(json_string)
        return jsonResult_load

    except FileNotFoundError :
        with open(path, 'w', encoding='UTF8') as outfile:
            readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(str(readable_result))
        return jsonResult

def info_save():
    with open('ITT_Student.json', 'w', encoding='UTF8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(str(readable_result))

print(" \t\t\t\t학생 주소록 관리 프로그램을 실행합니다.\t\t\t\t")

try:
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        jsonResult = json.loads(json_string)

except FileNotFoundError:
     jsonResult = info_start(ask_path())
     print('ITT_Student.json SAVED')

while True :
    main_intro()
    option = int(input('메뉴을 선택해주세요 : '))
    try:
        if option == 1 :
            info_insert()
            index = input("지금까지의 정보 입력을 취소하시려면 'quit'를 입력하세요 :")
            if index == "quit": continue
            else:
                print("----------- 학생 정보 입력이 되었습니다 ----------")
                info_save()

        elif option == 2 :
            number = info_input()
            if number == 1:
                info_show_indiviual(jsonResult)
            elif 10 > number > 1:
                key_word = input("키워드를 입력하세요 : ")
                if number == 2 :
                    element = "name"
                elif number == 3 :
                    element = "age"
                elif number == 4:
                    element = "address"
                elif number == 5 :
                    element = "student_ID"
                elif number == 6 :
                    element = "past_record"
                elif number == 7 :
                    element = "강의명"
                elif number == 8 :
                    element = "강사명"
                elif number == 9 :
                    element = "강의코드"

                if len(info_search(element,key_word)) == 1:
                    info_show_indiviual(info_search(element,key_word))
                elif len(info_search(element,key_word)) > 1:
                    info_show_plural(info_search(element,key_word))
            elif number == 10:
                continue

        elif option == 3 :
            print("")
            print("------------- 학생 정보 수정을 시작합니다 -------------")
            print("!!!!! 학생ID는 수정이 불가합니다 !!!!!\n")
            while True:
                key_word = input("학생ID를 입력하세요 : ")
                if len(info_search("student_ID", key_word)) == 1:
                    info_show_indiviual(info_search("student_ID", key_word))
                    info_revise(info_search("student_ID", key_word))
                    break
                elif len(info_search("student_ID", key_word)) > 1:
                    info_show_plural(info_search("student_ID", key_word))
                    print("다시 입력하세요.")
                    continue
                info_show_indiviual(info_search("student_ID", key_word))
            info_save()

        elif option == 4 :
            info_delete()
            info_save()

        elif option == 5 :
            print("프로그램을 종료합니다.")
            break
    except:
        continue