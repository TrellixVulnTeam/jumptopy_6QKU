import urllib.request
import time
import datetime
import json

access_key = "i4zXtlcTwh041E8W0qOyGPnIggToM4lqBePqd5ZR8v4uJQ6WcXACinkJgll%2Fk0PYSSinPNRJL%2B07OvnTXPcHaA%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url) # protocol 레벨(http 양식)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None

def getNatVisitor(base_date, base_time, nx, ny):
    end_point="http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += "&numOfRows=100"
    url = end_point + parameters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


def main():
    jsonResult = []
    category = []
    now = time.localtime()
    base_date= "%04d%02d%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
    base_time= "%02d%02d" % (now.tm_hour-1,now.tm_min)
    nx = "89"
    ny = "91"

    jsonData = getNatVisitor(base_date, base_time, nx, ny)


    for i in range(len(jsonData['response']['body']['items']['item'])):
        if(jsonData['response']['header']['resultMsg']=='OK'):
            baseDate = jsonData['response']['body']['items']['item'][i]["baseDate"]
            baseTime = jsonData['response']['body']['items']['item'][i]["baseTime"]
            category = jsonData['response']['body']['items']['item'][i]["category"]
            fcstDate = jsonData['response']['body']['items']['item'][i]["fcstDate"]
            fcstTime = jsonData['response']['body']['items']['item'][i]["fcstTime"]
            fcstValue = jsonData['response']['body']['items']['item'][i]["fcstValue"]
            nx = jsonData['response']['body']['items']['item'][i]["nx"]
            ny = jsonData['response']['body']['items']['item'][i]["ny"]

            jsonResult.append({'basedate':baseDate,'basetime':baseTime,'category':category,'fcstDate':fcstDate,'fcstTime':fcstTime,
                               'fcstValue':fcstValue,'fcs''nx':nx,'ny':ny})

    return jsonResult

if __name__ == '__main__':
    main()
