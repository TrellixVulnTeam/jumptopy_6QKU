import json

json_big_data =[]
dic_data= {
        'key1':input("key1의 값을 입력하세요: ")
}
# 9~14라인 사이에 1줄만 추가하면 되요.
try:
    with open('test.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
except: pass
json_big_data.append(dic_data)

# 아래 코드를 절대로 바꾸지 말것
with open('test.json', 'w', encoding='UTF8') as outfile:
    readable_result = json.dumps(json_big_data ,indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)
