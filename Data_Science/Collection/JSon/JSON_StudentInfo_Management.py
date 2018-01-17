import json
#        'student_ID':'ITT001',
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
"""
g_json_bigdata = [
    {
        'student_ID':'ITT001',
        'student_name':'김기정',
        'student_age':31,
        'address':'대구광역시 파티마 병원 옆 포시즌 302호',
        'total_course_info':{
            'num_of_course_learned':2,
            'learning_course_info':[
                    {
                        'course_code':'IB171106',
                        'course_name':'IoT 빅데이터 실무반',
                        'teacher':'이현구',
                        'open_date':'2017-11-06',
                        'close_date':'2018-09-05'
                     }
            ]
        }
     },
    {
        'student_ID':'ITT002',
        'student_name':'전수범',
        'student_age':29,
        'address':'대구광역시 달서구 성지로 14안길 17',
        'total_course_info':{
            'num_of_course_learned':1,
            'learning_course_info':[
                    {
                        'course_code':'IB171106',
                        'course_name':'IoT 빅데이터 실무반',
                        'teacher':'이현구',
                        'open_date':'2017-11-06',
                        'close_date':'2018-09-05',
                     },
                    {
                        'course_code':'OB171106',
                        'course_name':'오픈소스기반 빅데이터 실무반',
                        'teacher':'이현구',
                        'open_date':'2018-01-06',
                        'close_date':'2018-08-05'
                     }
            ]

        }
     }
]
"""

def print_initial_menu():
    print("\n           << JSON기반 학생 정보 관리 프로그램 >>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료반")
    print("메뉴를 선택하세요:",end=" ")

def create_student_ID():
    return "ITT003"

def input_student_info():
    input_menu_message = [
        "이름 (예: 홍길동 ): ",
        "나이 (예: 29): ",
        "주소 (예: 대구광역시 동구 아양로 135): ",
        "과거 수강 횟수 (예: 1): ",
        "현재 수강 과목이 있습니까? (예: 예/아니오)",
        "강의코드 (예: IB171106, OB0104 ..): ",
        "강의명 (예: IOT 빅데이터 실무반): ",
        "강사 (예: 이현구): ",
        "개강일 (예: 2017-11-06): ",
        "종료일 (예: 2018-09-05): ",
    ]

    c_student_id = create_student_ID()
    i_student_name = input(input_menu_message[0])
    i_student_age = input(input_menu_message[1])
    i_address = input(input_menu_message[2])
    i_number_of_course_learned = input(input_menu_message[3])
    i_is_learning = input(input_menu_message[4])
    if(i_is_learning == "예" ):
        i_course_code = input(input_menu_message[5])
        i_course_name = input(input_menu_message[6])
        i_teacher = input(input_menu_message[7])
        i_open_date = input(input_menu_message[8])
        i_close_date = input(input_menu_message[9])

    g_json_bigdata.append(
        {
            g_student_id:c_student_id,
            g_student_name:i_student_name,
            g_student_age:i_student_age,
            g_address:i_address,
            g_total_course_info:{
                g_num_of_course_learned:i_number_of_course_learned,
                g_learning_course_info:[
                    {
                        g_course_code:i_course_code,
                        g_course_name:i_course_name,
                        g_teacher:i_teacher,
                        g_open_date:i_open_date,
                        g_close_date:i_close_date
                    }
                ]
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
    print("7. 과거 수강 횟수 검색")
    print("8. 과거 수강 횟수 검색")
    print("9. 과거 수강 횟수 검색")
    print("메뉴를 선택하세요: ", end=" ")

def print_entire_student_info():
    print("\n- 전체 학생 정보 출력 -")
    for student_data in g_json_bigdata:
        print("\n* 학생 ID: ", student_data.get(g_student_id))
        print("* 이름: ", student_data.get(g_student_name))
        print("* 나이: ", student_data.get(g_student_age))
        print("* 주소: ",student_data.get(g_address))
        print("* 수강 정보")
        print(" + 과거 수강 횟수: ",student_data.get(g_total_course_info).get(g_num_of_course_learned))

        if( g_learning_course_info in student_data.get(g_total_course_info).keys()):
            print(" + 현재 수강 과목")
            for learning_course_data in (student_data.get(g_total_course_info)).get(g_learning_course_info):
                print("  강의 코드: ", learning_course_data.get(g_course_code))
                print("  강의명: ", learning_course_data.get(g_course_name))
                print("  강사: ", learning_course_data.get(g_teacher))
                print("  개강일: ", learning_course_data.get(g_open_date))
                print("  종료일: \n", learning_course_data.get(g_close_date))

def read_student_info():
    print_read_student_info_menu()

    menu_num = int(input())

    if menu_num == 1:
        print_entire_student_info()

def update_student_info():
    print_update_student_info_menu()

def save_student_info():
    try:
        with open(g_file_name_saved, 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('%s is saved ' % g_file_name_saved)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    menu_num = 0

    try:
        with open(g_file_name_saved, encoding='UTF8') as json_file: json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_bigdata = json.loads(json_string)
    except Exception as e:
        print(e)

    while True:
        print_initial_menu()
        menu_num = int(input())

        if menu_num == 1:
            student_info = input_student_info()
            #insert_student_info(student_info)
            print("학생 정보를 등록하였습니다.")
        elif menu_num == 2:
            read_student_info()
        elif menu_num == 3:
            update_student_info()
        elif menu_num == 5:
            save_student_info()
            break

    print("학생 정보 관리 프로그램을 종료합니다.")