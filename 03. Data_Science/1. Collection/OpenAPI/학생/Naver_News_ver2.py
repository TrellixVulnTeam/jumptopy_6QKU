import json
from collections import OrderedDict
from pprint import pprint
with open("이명박_naver_news.json",encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    json_big_data = json.loads(json_data_string)

json_store =[]
for i in range(len(json_big_data)):
    json_link = json_big_data[i]["org_link"]
    json_link_del = json_link.replace("http://","")
    json_link_del = json_link_del.replace("https://", "")
    json_link_del = json_link_del.replace(":8080", "")
    json_split = json_link_del.split("/")
    json_store.append(json_split[0])

json_store_set = set(json_store)
json_store_set.remove('')

json_dict = OrderedDict()
print("[도메인별 기사 건수 분석]")
for i in json_store_set:
    global count
    count = 0
    for x in json_store:
        if i == x :
            count += 1
        else:
            continue
    json_dict[i] = count

json_dict_sorted = sorted(json_dict, key=lambda k:json_dict[k], reverse=True)
json_dict_init = 0
for i in json_dict_sorted:
    json_dict_init +=json_dict[i]
    print(">>"+i+" : "+ str(json_dict[i]))
    with open("test.txt", "a") as file:
        file.write(str(json_dict[i])+"\n")
print("-"*40)
print("총건수 : "+str(json_dict_init))

