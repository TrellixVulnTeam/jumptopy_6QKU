from operator import itemgetter
from itertools import groupby

row= {
        "학생ID": "ITT001",
        "수강정보": {
            "강좌1": {
                "강의코드": "1",
                "강의명": "1",
                "강사": "1",
                "개강일": "1",
                "종료일": "1"
            },
            "강좌2": {
                "강의코드": "2",
                "강의명": "2",
                "강사": "2",
                "개강일": "2",
                "종료일": "2"
            }
        },
        "과거수강횟수": "1",
        "개인정보": {
            "이름": "1",
            "나이": "1",
            "주소": "1"
        }
    }



t = "ITT001"
p1 = {key:value for key,value in row.items() if value == t}
print(p1)