import json
import os

def open_json_file(json_address):
    with open(json_address + json_file_name, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            return json_object

def make_json_file():
    with open(now_cwd + os_delimeter + json_file_name,'w', encoding='UTF8') as json_file:
            readable_result = json.dumps(json_default, indent=4, ensure_ascii=False)
            json_file.write(readable_result)
            print("기본 경로로 생성합니다")
            print("파일 생성 완료!")



now_cwd = os.getcwd()
os_delimeter = "\\"
count_file = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
json_default = []