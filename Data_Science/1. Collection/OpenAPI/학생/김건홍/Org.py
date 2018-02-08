import urllib.request
import time
import json
import datetime

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

access_key = "VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D"

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

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for i in (jsonData['response']['body']['items']['item']):
            jsonResult.append({'baseDate':i['baseDate'],'baseTime':i['baseTime'],'category':i["category"],'fcstDate':i['fcstDate'],'fcstTime':i['fcstTime'],'fcstValue':i['fcstValue'],'nx':i['nx'],'ny':i['ny']})

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
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('\n난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

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
        dry_forecast_simulation()

    else:
        return None

def precipitation_forecast_simulation():
    global g_Balcony_Windows
    with open("Weather_info.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        retJson = json.loads(json_string)
        for retJson in retJson:
            if (retJson['category']) == 'RN1':
                print("RN1//fcstValue = "+str(retJson['fcstValue']))
                if retJson['fcstValue'] > 0:
                    if g_Balcony_Windows == True:
                        print("\n***비가 올 예정이오니 열려 있는 창문을 닫습니다.***")
                        g_Balcony_Windows = not g_Balcony_Windows
                        check_device_status()

def Damp_forecast_simulation():
    global g_Balcony_Windows
    with open("Weather_info.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        retJson = json.loads(json_string)
        for retJson in retJson:
            if (retJson['category']) == 'REH':
                print("REH//fcstValue = "+str(retJson['fcstValue']))
                if retJson['fcstValue'] < 0:
                    if g_Balcony_Windows == True:
                        print("\n***습도가 높으므로 제습기를 가동합니다.***")
                        g_Balcony_Windows = not g_Balcony_Windows
                        check_device_status()

def dry_forecast_simulation():
    global g_Balcony_Windows
    with open("Weather_info.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        retJson = json.loads(json_string)
        for retJson in retJson:
            if (retJson['category']) == 'REH':
                print("REH//fcstValue = "+str(retJson['fcstValue']))
                if retJson['fcstValue'] < 0:
                    if g_Balcony_Windows == True:
                        print("\n***습도가 높으므로 제습기를 가동합니다.***")
                        g_Balcony_Windows = not g_Balcony_Windows
                        check_device_status()

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