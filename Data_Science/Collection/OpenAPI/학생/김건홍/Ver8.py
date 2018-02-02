import urllib.request
import time
import json
import datetime
import os

# 실시간업데이트를 하여 RN1 값이 있고 발코니 창이 열려 있는 경우 발코니 창을 닫도록 구현
# pageNo=1,2 두번 호출해서 RN1과 습도값을 모두 처리하세요.

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
g_humidifier = False
g_dehumidifier = False

access_key = "zKXKKnSlFbzQlSo3VGM7RSWUTndjwM0szSJhbK%2F85hKnvtPxU6zBzaudnzPFNNHf5j1azPl%2B7p4IfYMW8%2Bi4lg%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL request Success" %datetime.datetime.now())
            return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None

def getForecastTimeDataResponse(base_date,base_time,nx,ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    parameters = "?base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += "&_type=json&serviceKey=" + access_key
    parameters += "&pageNo=2"

    url = end_point+parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    try:
        jsonResult = []
        base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        base_time = time.strftime("%H%M", time.localtime(time.time()))
        nx = "89"
        ny = "91"
        jsonData = getForecastTimeDataResponse(base_date,base_time,nx,ny)
        if (jsonData['response']['header']['resultMsg'] == 'OK'):
            for i in (jsonData['response']['body']['items']['item']):
                jsonResult.append({'baseDate':i['baseDate'],'baseTime':i['baseTime'],'category':i["category"],'fcstDate':i['fcstDate'],'fcstTime':i['fcstTime'],'fcstValue':i['fcstValue'],'nx':i['nx'],'ny':i['ny']})

        print("%s_%s_Weather.json" %(base_date,base_time))

        with open("%s_%s_Weather.json" %(base_date,base_time),'w',encoding='utf8')as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
            outfile.write(retJson)
    except TypeError:
        jsonResult = []
        base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        base_time = time.strftime("%H%M", time.localtime(time.time()))
        base_Time = int(base_time) - 100
        nx = "89"
        ny = "91"
        jsonData = getForecastTimeDataResponse(base_date,str(base_Time),nx,ny)

        if (jsonData['response']['header']['resultMsg'] == 'OK'):
            for i in (jsonData['response']['body']['items']['item']):
                jsonResult.append({'baseDate':i['baseDate'],'baseTime':i['baseTime'],'category':i["category"],'fcstDate':i['fcstDate'],'fcstTime':i['fcstTime'],'fcstValue':i['fcstValue'],'nx':i['nx'],'ny':i['ny']})

        print("%s_%s_Weather.json" % (base_date,base_Time))

        with open("%s_%s_Weather.json" % (base_date,base_Time),'w',encoding='utf8')as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
            outfile.write(retJson)

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료")

def print_device_status(device_name,devcie_status):
    print("%s 상태: " % device_name, end="")
    if devcie_status == True: print("작동")
    else: print("정지")

def print_device_status1(device_name,devcie_status1):
    print("%s 상태: " % device_name, end="")
    if devcie_status1 == True: print("열림")
    else: print("닫힘")

def check_device_status():
    print_device_status('\n난방기', g_Radiator)
    print_device_status1('가스밸브', g_Gas_Valve)
    print_device_status1('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status1('출입문', g_Door)
    print_device_status('가습기', g_humidifier)
    print_device_status('제습기', g_dehumidifier)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_humidifier, g_dehumidifier
    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))
    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_humidifier = not g_humidifier
    if menu_num == 6: g_dehumidifier = not g_dehumidifier
    check_device_status()

def control_humidifier():
    global g_humidifier
    try:
        base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        base_time = time.strftime("%H%M", time.localtime(time.time()))
        with open("%s_%s_Weather.json" % (base_date,base_time), encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            retJson = json.loads(json_string)
    except FileNotFoundError:
        base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        base_time = time.strftime("%H%M", time.localtime(time.time()))
        base_Time = int(base_time)-100
        with open("%s_%s_Weather.json" % (base_date,base_Time), encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            retJson = json.loads(json_string)

    for retJson in retJson:
        if(retJson['category']) == 'REH':
            if retJson['fcstValue'] < 40:
                if g_humidifier == False:
                    print("\n***현재 습도(%s%%)가 적정습도 보다 낮으므로 가습기를 가동하겠습니다.***"%str(retJson['fcstValue']))
                    g_humidifier = not g_humidifier
                    check_device_status()
                    break
                elif g_humidifier == True:
                    print("***습도가 낮으므로(현재%s%%) 가습기가 작동중입니다.***"%str(retJson['fcstValue']))
                    check_device_status()
                    break

def control_dehumidifier():
    global g_dehumidifier
    try:
        base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        base_time = time.strftime("%H%M", time.localtime(time.time()))
        with open("%s_%s_Weather.json" % (base_date,base_time), encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            retJson = json.loads(json_string)
    except FileNotFoundError:
        base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        base_time = time.strftime("%H%M", time.localtime(time.time()))
        base_Time = int(base_time)-100
        with open("%s_%s_Weather.json" % (base_date,base_Time), encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            retJson = json.loads(json_string)

    for retJson in retJson:
        if(retJson['category']) == 'REH':
            if retJson['fcstValue'] > 70:
                if g_humidifier == False:
                    print("\n***현재 습도(%s%%)가 적정습도 보다 높으므로 제습기를 가동하겠습니다.***"%str(retJson['fcstValue']))
                    g_dehumidifier = not g_dehumidifier
                    check_device_status()
                    break
                elif g_dehumidifier == True:
                    print("***습도가 높으므로(현재%s%%) 제습기가 작동중입니다.***"%str(retJson['fcstValue']))
                    check_device_status()
                    break
# def control_window():


def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update 신청하기")
    print("4. 실시간 기상정보 Update 불러오기")
    menu_num = int(input("메뉴를 선택하세요: "))
    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("정지")

    elif menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("정지")

    elif menu_num == 3:
        print("실시간 기상정보 Update 신청하기")
        get_realtime_weather_info()
        control_humidifier()
        control_dehumidifier()
    else:
        print("\n실시간 기상정보 Update 불러오기")
        print("=" *50)
        get_weather_info()

def get_realtime_weather_info():
    if __name__ == '__main__':
        main()

def get_weather_info():
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))
    with open("%s_%s_Weather.json" %(base_date,base_time), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        retJson = json.loads(json_string)
        for retJson in retJson:
            print("['baseDate'] = " + str(retJson['baseDate']))
            print("['category'] = " + str(retJson['category']))
            print("['fcstDate'] = " + str(retJson['fcstDate']))
            print("['fcstTime'] = " + str(retJson['fcstTime']))
            print("['fcstValue'] = " + str(retJson['fcstValue']))
            print("['nx'] = " + str(retJson['nx']))
            print("['ny'] = " + str(retJson['ny']))
            print("=" *50)

def simulation_mode():
    print("\n1. Rain Day Simulation (발코니창 제어)")
    print("2. Damp Day Simulation (제습기 제어)")
    print("3. Dry Day Simulation (가습기 제어)")
    print("4. Sunny Day Simulation (제습기/가습기 제어)")
    menu_num = int(input("메뉴를 선택하세요: "))
    if menu_num == 1:
        precipitation_forecast_simulation()

    elif menu_num == 2:
        Damp_forecast_simulation()

    elif menu_num == 3:
        Dry_forecast_simulation()

    elif menu_num == 4:
        Sunny_Day_simulation()

def precipitation_forecast_simulation():
    global g_Balcony_Windows
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))

    retJson = []

    jsonResult ={
        "baseDate": base_date,
        "baseTime": base_time,
        "category": "RN1",
        "fcstDate": base_date,
        "fcstTime": base_time,
        "fcstValue": 10,
        "nx": 89,
        "ny": 91
    }
    retJson.append(jsonResult)

    if not os.path.isfile('Rain_simulator.json'):
        with open('Rain_simulator.json','w',encoding='UTF8') as outfile:
            readable_result = json.dumps(retJson,indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('Rain_simulator.json SAVED')
    if(retJson[0]['category']) == 'RN1':
        print("RN1//fcstValue = " + str(retJson[0]['fcstValue']))
        if retJson[0]['fcstValue'] > 0:
            if g_Balcony_Windows == True:
                print("\n***비가 올 예정이오니 열려 있는 창문을 닫습니다.***")
                g_Balcony_Windows = not g_Balcony_Windows
                check_device_status()
            else:
                print("***비가 올 예정이오니 창문 개방은 삼가하시기 바랍니다.***")

def Damp_forecast_simulation():
    global g_Balcony_Windows , g_dehumidifier
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))

    retJson = []

    jsonResult ={
        "baseDate": base_date,
        "baseTime": base_time,
        "category": "REH",
        "fcstDate": base_date,
        "fcstTime": base_time,
        "fcstValue": 90,
        "nx": 89,
        "ny": 91
    }
    retJson.append(jsonResult)

    if not os.path.isfile('Rain_simulator.json'):
        with open('Damp_simulator.json','w',encoding='UTF8') as outfile:
            readable_result = json.dumps(retJson,indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('Damp_simulator.json SAVED')

    if(retJson[0]['category']) == 'REH':
        print("REH//fcstValue = " + str(retJson[0]['fcstValue']))
        if retJson[0]['fcstValue'] > 80:
            if g_dehumidifier == False:
                print("\n***습도가 높으므로 제습기를 가동하겠습니다.***")
                g_dehumidifier = not g_dehumidifier
                check_device_status()
            elif g_dehumidifier == True:
                print("***습도가 높으므로 제습기가 가동중입니다.***")
                check_device_status()

def Dry_forecast_simulation():
    global g_humidifier
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))

    retJson = []

    jsonResult ={
        "baseDate": base_date,
        "baseTime": base_time,
        "category": "REH",
        "fcstDate": base_date,
        "fcstTime": base_time,
        "fcstValue": 30,
        "nx": 89,
        "ny": 91
    }
    retJson.append(jsonResult)

    if not os.path.isfile('Rain_simulator.json'):
        with open('Dry_simulator.json','w',encoding='UTF8') as outfile:
            readable_result = json.dumps(retJson,indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('Dry_simulator.json SAVED')

    if(retJson[0]['category']) == 'REH':
        print("REH//fcstValue = " + str(retJson[0]['fcstValue']))
        if retJson[0]['fcstValue'] < 40:
            if g_humidifier == False:
                print("\n***습도가 낮으므로 가습기를 가동하겠습니다.***")
                g_humidifier = not g_humidifier
                check_device_status()
            elif g_humidifier == True:
                print("***습도가 낮으므로 가습기가 작동중입니다.***")

def Sunny_Day_simulation():
    global g_Balcony_Windows, g_humidifier, g_dehumidifier
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))

    retJson = []

    jsonResult ={
        "baseDate": base_date,
        "baseTime": base_time,
        "category": "SKY",
        "fcstDate": base_date,
        "fcstTime": base_time,
        "fcstValue": 1,
        "nx": 89,
        "ny": 91
    }
    retJson.append(jsonResult)

    if not os.path.isfile('Sunny_Day_simulator.json'):
        with open('Sunny_Day_simulator.json','w',encoding='UTF8') as outfile:
            readable_result = json.dumps(retJson,indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('Sunny_Day_simulator.json SAVED')

    if(retJson[0]['category']) == 'SKY':
        print("SKY//fcstValue = " + str(retJson[0]['fcstValue']))
        if retJson[0]['fcstValue'] <= 2:
            if g_humidifier and g_dehumidifier == True:
                print("\n***화창한 날씨가 예상되므로 가습기와 제습기의 작동을 정지합니다..***")
                g_dehumidifier = not g_dehumidifier
                g_humidifier = not g_humidifier
                check_device_status()
            elif g_humidifier == True:
                print("***화창한 날씨입니다. 가습기의 작동을 정지하겠습니다.***")
                g_humidifier = not g_dehumidifier
                check_device_status()
            elif g_dehumidifier == True:
                print("***화창한 날씨입니다. 제습기의 작동을 정지하겠습니다.***")
                g_dehumidifier = not g_dehumidifier

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        check_device_status()

    elif menu_num == 2:
        control_device()

    elif menu_num == 3:
        smart_mode()

    elif menu_num == 4:
        simulation_mode()

    else: break