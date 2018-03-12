import time
import json
import datetime
import os
import urllib.request

# HKlee Comment] 시뮬레이션 모드 한번에 작동되도록
# 가습기, 제습기 추가할 것!

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

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

    url = end_point+parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    jsonResult = []
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))
    nx = "89"
    ny = "91"
    jsonData = getForecastTimeDataResponse(base_date,base_time,nx,ny)

    # HK Comment] JSON 데이터 분석하는 코드를 작성할 것

    print("%s_%s_Weather.json" %(base_date,base_time))

    with open("%s_%s_Weather.json" %(base_date,base_time),'w',encoding='utf8')as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료")

def print_device_status(device_name,devcie_status):
    print("%s 상태: "% device_name, end="")
    if devcie_status == True: print("열림")  # 장비에 맞는 상태 메세지를 출력할 것
    else: print("닫힘")                      # 힌트] 메세지와 관련된 파라메터 추가

def print_device_status1(device_name,devcie_status1):
    print("%s 상태: "% device_name, end="")
    if devcie_status1 == True: print("작동")
    else: print("정지")

def check_device_status():
    print_device_status1('\n난방기',g_Radiator)
    print_device_status1('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door
    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))
    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    check_device_status()

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

    else:
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
    global g_Balcony_Windows
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

    else:
        if(retJson[0]['category']) == 'REH':
            print("REH//fcstValue = " + str(retJson[0]['fcstValue']))
            if retJson[0]['fcstValue'] > 80:
                if g_Balcony_Windows == True:
                    print("\n***습도가 높으므로 열려 있는 창문을 닫고, 제습기를 가동하겠습니다.***")
                    g_Balcony_Windows = not g_Balcony_Windows
                    check_device_status()
                else:
                    print("***습도가 높으므로 제습기를 가동하겠습니다.***")

def Dry_forecast_simulation():
    global g_Balcony_Windows
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

    else:
        if(retJson[0]['category']) == 'REH1':
            print("REH//fcstValue = " + str(retJson[0]['fcstValue']))
            if retJson[0]['fcstValue'] < 40:
                if g_Balcony_Windows == True:
                    print("\n***습도가 낮으므로 열려 있는 창문을 닫고, 가습기를 가동하겠습니다.***")
                    g_Balcony_Windows = not g_Balcony_Windows
                    check_device_status()
                else:
                    print("***습도가 낮으므로 가습기를 가동하겠습니다.***")

def Sunny_Day_simulation():
    global g_Balcony_Windows
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

    if not os.path.isfile('Rain_simulator.json'):
        with open('Sunny_Day_simulator.json','w',encoding='UTF8') as outfile:
            readable_result = json.dumps(retJson,indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('Sunny_Day_simulator.json SAVED')

    else:
        if(retJson[0]['category']) == 'SKY':
            print("SKY//fcstValue = " + str(retJson[0]['fcstValue']))
            if retJson[0]['fcstValue'] <= 2:
                if g_Balcony_Windows == False:
                    print("\n***화창한 날씨입니다^^ 닫힌 창문을 열고,제습기와 가습기 작동을 정지합니다.***")
                    g_Balcony_Windows = not g_Balcony_Windows
                    check_device_status()
                else:
                    print("\n***화창한 날씨입니다^^ 제습기와 가습기 작동을 정지합니다.***")

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:  # check_device_status() HK Comment] 장비 상태 출력하는 함수를 작성할 것
        check_device_status()

    elif menu_num == 2:
        control_device()

    elif menu_num == 3:
        smart_mode()

    elif menu_num == 4:
        simulation_mode()

    else: break