import urllib.request
import datetime
import json

access_key = "i4zXtlcTwh041E8W0qOyGPnIggToM4lqBePqd5ZR8v4uJQ6WcXACinkJgll%2Fk0PYSSinPNRJL%2B07OvnTXPcHaA%3D%3D"


def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None

def getNatVisitor():
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    parameters = "?_returnType=json&ServiceKey=" + access_key
    parameters += "&sidoName=" +urllib.request.quote("대구")
    parameters += "&ver=1.3"
    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)


def main():
    jsonResult = []
    jsonData = getNatVisitor()

    for data in jsonData['list']:
        if data.get('stationName') == "신암동":
            jsonResult.append({'stationName':data.get('stationName'),'dataTime':data.get('dataTime'),
                                   'so2Value':data.get('so2Value'),'coValue':data.get('coValue'),
                               'o3Value':data.get('o3Value'),'no2Value':data.get('no2Value'),'pm10Value':data.get('pm10Value'),
                               'pm25Value':data.get('pm25Value'),'khaiGrade': data.get('khaiGrade'), 'so2Grade': data.get('so2Grade'),
                               'coGrade': data.get('coGrade'),'o3Grade': data.get('o3Grade'), 'no2Grade': data.get('no2Grade'),
                               'pm10Grade': data.get('pm10Grade'), 'pm25Grade': data.get('pm25Grade')})

    return jsonResult
    # with open('날씨예보정보.json', 'w', encoding='utf8') as outfile:
    #     retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    #     outfile.write(retJson)

