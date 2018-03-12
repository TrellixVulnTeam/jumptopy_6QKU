from operator import itemgetter, attrgetter
list = [1,3,4]
[
        {
            "link": "http://news.jtbc.joins.com/article/article.aspx?news_id=NB11580344",
            "name": "MB국정원, 대북 공작금도 빼돌린 정황…검찰 수사 착수",
            "shares": {
                "count": 28
            }
        }
]

my_list=[
    {
        "name":"AT01",
        "shares":3
    },
    {
        "name":"AT01",
        "shares":1
    },
    {
        "name":"AT01",
        "shares":2
    }
]
new_list = sorted(my_list,key=itemgetter('shares'))

print(new_list)