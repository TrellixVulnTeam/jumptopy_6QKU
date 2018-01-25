import json

news_domain_all_list = []
num_of_domain_info = {}
num_of_domain_info_list = []

with open("이명박_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)

for x in jsonResult:
    try: news_domain_all_list.append(x["org_link"].split('/')[2])
    except: print("'org_link'가 없는 기사를 발견했습니다.")

news_domain_unique_list=set(news_domain_all_list)

total_count=0
for one_of_unique in news_domain_unique_list:
    num_of_domain_info[one_of_unique]=0
    for one_of_all in news_domain_all_list:
        if one_of_all == one_of_unique:
            num_of_domain_info[one_of_unique] += 1
    num_of_domain_info_list.append(num_of_domain_info)
    total_count +=num_of_domain_info[one_of_unique]

print(total_count)

