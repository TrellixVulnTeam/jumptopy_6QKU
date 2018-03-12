import re
#requests 설치
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import json

client_id = "vwGbSmYZkjUG9IzrVEtb"  # 애플리케이션 등록시 발급 받은 값 입력
client_secret = "kfR8irTyY5"  # 애플리케이션 등록시 발급 받은 값 입력

def get_movie_top_list():
    url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    move_list = soup.find_all('div', 'tit3')
    count = 1
    for m in move_list:
        title = m.find('a')
        print (count, '위:', re.search('title=".+"', str(title)).group()[7:-1])
        count += 1
        if count == 11:
            break

def get_movie_search(name):
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText + "&display=3&sort=count"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
#
def get_movie_info(name):
    movie_info_list = []
    movie_data = get_movie_search(name)
    movie_data_loads = json.loads(movie_data)
    if len(movie_data_loads['items']) == 1:
        for data in movie_data_loads["items"]:
            movie_info_list.append({'영화이름':data.get('title'),'개봉년도':data.get('pubDate'),
                      '감독':data.get('director'), '주연배우':data.get('actor'),'평점':data.get('userRating')})

        print("")

        for key, value in movie_info_list[0].items():
            print("<<"+key+">>")
            value = value.replace('<b>', '')
            value = value.replace('</b>', '')
            value = value.replace('|', ' ')
            print("-"+ value)
            print("")

        print("관련된 영화 정보 Youtube 링크입니다")
        with open("movie_ai_list.txt", 'a') as data:
            data.write(name+"\n")
        youtube_search(name)

    elif len(movie_data_loads['items']) > 1:
            overlap_movie_list = []
            print("'"+name+"'"+"과 관련된 영화가 여러개 있습니다")
            for i, value in enumerate (movie_data_loads["items"],1):
                print("="*40)
                print(i,".","영화제목")
                value_nm = value.get('title')
                value_nm = value_nm.replace('<b>', '')
                value_nm = value_nm.replace('</b>', '')
                print("\t"+value_nm)
                print("\t"+"영화감독")
                value_dir = value.get('director')
                value_dir = value_dir.replace('|', ' ')
                print("\t" + value_dir)
                print("\t"+"개봉년도")
                print('\t'+value.get('pubDate'))
                print("\t"+"주연배우")
                print('\t'+value.get('actor'))
                print("\t"+"평점")
                print('\t'+value.get('userRating'))
                print("=" * 40)
                overlap_movie_list += [[value_nm,value_dir]]
            choice_num = int(input("원하시는 영화의 번호를 입력하십시요.\n>>"))
            num = choice_num
            print("")
            print("관련된 영화 정보 Youtube 링크입니다")
            try:
                with open("movie_ai_list.txt", 'a') as data:
                    data.write(overlap_movie_list[num-1][0]+"\n")
                youtube_search(overlap_movie_list[num-1][0]+" "+overlap_movie_list[num-1][1])
            except IndexError:
                youtube_search(overlap_movie_list[num - 1][0])
            print("")

def youtube_search(name):
    query_string = urllib.parse.urlencode({"search_query" : name+"예고편"})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])

