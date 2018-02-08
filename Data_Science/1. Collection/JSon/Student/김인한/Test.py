import json

address = input("경로를 입력해주세요 : ")
with open(address + 'ITT_Student.json', encoding='utf8') as outfile:
    json_object = json.load(outfile)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)


with open(address + 'ITT_Student.json',encoding='utf8') as outfile:
    json_object = json.load(outfile)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)