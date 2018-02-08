import re
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

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
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

def youtube_search():
    query_string = urllib.parse.urlencode({"search_query" : input()})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])