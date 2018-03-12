import json

student_result = []

try:
    with open('E:\python.warkspace\Guri\openAPI\ITT_Student.json', 'r', encoding='utf8') as outfile:
        json_object = json.load('ITT_Student.json')
        json_string = json.dumps(json_object)
        readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
except FileNotFoundError:
    file_maker = input('''경로에 파일이 없습니다. 어떻게 하시겠습니까?
    1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
    메뉴를 선택하세요 : ''')
    if file_maker == '1':
        address = input("경로를 입력해주세요 : ")
        with open(address + 'ITT_Student.json',encoding='utf8') as outfile:
            json_object = json.load(outfile)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
    elif file_maker == '2':
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)