from Environment import Check_Init_File
import os
import json

count_file = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
now_cwd = os.getcwd()
os_delimeter = "\\"

def check_file():
    if os.path.isfile(json_file_name):
        print("파일 로딩 완료!")
    else:
        print("경로에 파일이 없습니다. 어떻게 하시겠습니까?")
        print("1.경로를 입력합니다")
        print("2.기본 경로로 생성합니다")
        print("메뉴를 선택하세요")
        menu = int(input(":"))
        if menu == 1:
            try:
                print("경로를 입력하세요")
                print("ex) C:\\python\\")
                input_json_address()
                print("파일 로딩 완료!")
                Check_Init_File.open_json_file(input_json_address())
            except FileNotFoundError:
                print("지정된 곳에 파일이 없습니다")
                Check_Init_File.make_json_file()
        if menu == 2:
            Check_Init_File.make_json_file()


def input_json_address():
    json_address = str(input(": "))
    os.chdir(json_address + os_delimeter)
    return json_address

def save_json_file(object):
    with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        total_json_data = json_big_data + [dict(object)]
    with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
        readable_result = json.dumps(total_json_data, indent=4, sort_keys= False, ensure_ascii=False)
        make_file.write(readable_result)
        print('등록된 정보가 저장되었습니다.')

def load_json_file():
    with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        return json_big_data


