import json
from pprint import pprint

total_news = []
with open("이명박_naver_news.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    total_news = json.loads(json_string)

for change_str in total_news:
    if '&quot;' in change_str.get('title') or '&lt;' in change_str.get('title') or '&gt;' in change_str.get('title') or '<b>' in change_str.get(
            'title') or '</b>' in change_str.get('title'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
        change_str['title'] = change_str.get('title').replace("&quot;", "'")
        change_str['title'] = change_str.get('title').replace("&lt;", "<")
        change_str['title'] = change_str.get('title').replace("&gt;", ">")
        change_str['title'] = change_str.get('title').replace("<b>", "")
        change_str['title'] = change_str.get('title').replace("</b>", "")
    if '&quot;' in change_str.get('description') or '&lt;' in change_str.get('description') or '&gt;' in change_str.get(
            'description') or '<b>' in change_str.get('description') or '</b>' in change_str.get(
            'description'):  ## 따옴표가 &quot;로 출력돼서 다시 따옴표로 바꿔주는 작업
        change_str['description'] = change_str.get('description').replace('&quot;', "'")
        change_str['description'] = change_str.get('description').replace('&lt;', "<")
        change_str['description'] = change_str.get('description').replace('&gt;', ">")
        change_str['description'] = change_str.get('description').replace('<b>', "")
        change_str['description'] = change_str.get('description').replace('</b>', "")

with open('change_이명박_naver_news.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(total_news, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

address_ls = []
for address_get in total_news:
    address = address_get.get('org_link')
    point_address = address.split('/')
    if len(point_address) >= 3:
        address_ls.append(point_address[2])

address_number  = []
only_one = set()
for check_address in address_ls:
    each_ls = []
    each_ls.append(address_ls.count(check_address))
    each_ls.append(check_address)
    address_number.append(each_ls)
    only_one.add(check_address)

final_ls = []
for check_mul in only_one:
    for mul in address_number:
        if check_mul in mul:
            final_ls.append(mul)
            break

final_ls.sort()
final_ls.reverse()

news_count = 0
for prnt in final_ls:
    news_count += prnt[0]
    print(">> '%s' : %s 건" % (prnt[1], prnt[0]))
print("\n>> 실제 뉴스 총 건수 : %s" % len(address_number))     ## 받아들인 뉴스가 모아져 있는 리스트 내의 갯수를 통해
print(">> 검색한 뉴스 총 건수 : %s" % news_count)   ## 중복 도메인의 수의 총합을 통해 확인