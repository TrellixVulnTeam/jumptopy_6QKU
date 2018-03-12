import urllib.request
import datetime
import json
import time
import threading
import random

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_humidity = False
g_humidifier = False
g_Blind = False
g_AI_Mode = False

g_Max_Acceptable_humidity_level = 60
g_Min_Acceptable_humidity_level = 50
temperature_max = 24
temperature_min = 18

access_key = "fgNUbFNWdrPsUqf6WsEPlsKYxDQ%2BgzRO2LIXFxVCeb7zMpjnDnIGiVINYnTenSQdMMseq9GIWW4Bkh5%2B7ZNXKA%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("\n[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None

def getweather(basedate, basetime, nx, ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key + "&numOfRows=100"
    parameters += "&base_date=" + basedate
    parameters += "&base_time=" + basetime
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny

    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_realtime_weather_info():
    jsonresult = []
    basedate = time.strftime("%Y%m%d", time.localtime(time.time()))
    basetime = time.strftime("%H%M", time.localtime(time.time()))
    basetime = int(basetime) - 100
    basetime = str(basetime)
    basetime = basetime.zfill(4)
    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        jsonresult = jsondata['response']['body']['items']['item']

    print("%s_%s_날씨정보" % (basedate, basetime))
    with open('%s_%s_날씨정보.json' % (basedate, basetime), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션모드")
    print("0. 프로그램 종료")

def print_device_status(device_name, devcie_status):
    print("%s 상태: " % device_name, end="")
    if devcie_status == True:
        print("작동")
    else:
        print("정지")

def print_device_status_2(device_name, devcie_status):
    print("%s 상태: " % device_name, end="")
    if devcie_status == True:
        print("열림")
    else:
        print("닫힘")

def check_device_status():
    print_device_status('\n난방기', g_Radiator)
    print_device_status_2('가스밸브', g_Gas_Valve)
    print_device_status_2('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status_2('출입문', g_Door)
    print_device_status('제습기', g_humidity)
    print_device_status('가습기', g_humidifier)
    print_device_status_2('블라인드', g_Blind)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요. ")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(배란다) 창문")
    print("4. 출입문")
    print("5. 제습기")
    print("6. 가습기")
    print("7. 블라인드")

def control_device():
    global g_Radiator
    global g_Gas_Valve
    global g_Balcony_Windows
    global g_Door
    global g_humidity
    global g_humidifier
    global g_Blind
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1:
        if g_Radiator == True:
            g_Radiator = False
            print("\n난방기 정지")
        elif g_Radiator == False:
            g_Radiator = True
            print("\n난방기 작동")
    elif menu_num == 2:
        if g_Gas_Valve == True:
            g_Gas_Valve = False
            print("\n가스밸브 닫힘")
        elif g_Gas_Valve == False:
            g_Gas_Valve = True
            print("\n가스밸브 열림")
    elif menu_num == 3:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
            print("\n창문 닫힘")
        elif g_Balcony_Windows == False:
            g_Balcony_Windows = True
            print("\n창문 열림")
    elif menu_num == 4:
        if g_Door == True:
            g_Door = False
            print("\n출입문 닫힘")
        elif g_Door == False:
            g_Door = True
            print("\n출입문 열림")
    elif menu_num == 5:
        if g_humidity == True:
            g_humidity = False
            print("\n제습기 정지")
        elif g_humidity == False:
            g_humidity = True
            print("\n제습기 작동")
    elif menu_num == 6:
        if g_humidifier == True:
            g_humidifier = False
            print("\n가습기 정지")
        elif g_humidifier == False:
            g_humidifier = True
            print("\n가습기 작동")
    elif menu_num == 7:
        if g_Blind == True:
            g_Blind = False
            print("\n블라인드 닫힘")
        elif g_Blind == False:
            g_Blind = True
            print("\n블라인드 열림")

def update_scheduler():
    global g_humidity
    global g_Balcony_Windows
    global g_humidifier
    while True:
        if g_AI_Mode == False:
            continue
        else:
            AI_time = time.localtime(time.time())
            if AI_time[4] == 45 and AI_time[5] == 59:
                AI_start_system()

def smart_mode():
    global g_AI_Mode
    global g_Balcony_Windows
    print("\n1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태변경")
    print("3. 실시간 기상정보 업데이트")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("\n현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동")
        else:
            print("정지")
    elif menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("\n현재인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동")
            AI_start_system()
        else:
            print("중지")
    elif menu_num == 3:
        get_realtime_weather_info()

def AI_start_system():
    global g_humidity
    global g_Balcony_Windows
    global g_humidifier
    global g_Blind
    global g_Radiator

    REH_number = []
    RN1_number = []
    T1H_number = []
    SKY_number = []
    basedate = time.strftime("%Y%m%d", time.localtime(time.time()))
    basetime = time.strftime("%H%M", time.localtime(time.time()))
    basetime = int(basetime) - 100
    basetime = str(basetime)
    basetime = basetime.zfill(4)
    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        jsonresult = jsondata['response']['body']['items']['item']
        AI_div = jsonresult
        AI_number_line = len(AI_div)
        for i in range(AI_number_line):
            if 'RN1' in AI_div[i]['category']:
                RN1_number_list = AI_div[i]['fcstValue']
                RN1_number.append(RN1_number_list)
            if 'REH' in AI_div[i]['category']:
                REH_number_list = AI_div[i]['fcstValue']
                REH_number.append(REH_number_list)
            if 'T1H' in AI_div[i]['category']:
                T1H_number_list = AI_div[i]['fcstValue']
                T1H_number.append(T1H_number_list)
            if 'SKY' in AI_div[i]['category']:
                SKY_number_list = AI_div[i]['fcstValue']
                SKY_number.append(SKY_number_list)

    Blind_AI_system_2 = SKY_number[0]
    if SKY_number[0] == 1:
        SKY_number[0] = "맑음"
    elif SKY_number[0] == 2:
        SKY_number[0] = "구름조금"
    elif SKY_number[0] == 3:
        SKY_number[0] = "구름많음"
    elif SKY_number[0] == 4:
        SKY_number[0] = "흐림"
    humidifier_AI_system = REH_number[0]
    humidity_AI_system = REH_number[0]
    Balcony_Windows_AI_system_2 = T1H_number[0]
    Balcony_Windows_AI_system = RN1_number[0]
    print("\n오늘의 날씨:",SKY_number[0],"\n현재기온:",Balcony_Windows_AI_system_2,'℃','\n현재습도:',humidity_AI_system,"%","\n강수량:",Balcony_Windows_AI_system,"%")
    Windows_temperature = int(input("\n난방기를 작동시킬 최저온도를 설정해주세요: "))
    if Balcony_Windows_AI_system > 0 and g_Balcony_Windows == True:
        print("창문을 닫겠습니다.")
        g_Balcony_Windows = False
    if Blind_AI_system_2 == 1 and Balcony_Windows_AI_system_2 in range(temperature_min,temperature_max) and g_Balcony_Windows == False:
        print("현재적정온도(18℃~24℃):",Windows_temperature,'℃ \n창문을 열겠습니다.')
        g_Balcony_Windows = True # 날씨 맑음에 적정온도, 창문이 닫혀있으면 창문을 연다.
    if humidity_AI_system > g_Max_Acceptable_humidity_level and g_humidity == False:
        print("제습기를 작동하겠습니다.")
        g_humidity = True
    if humidity_AI_system < g_Min_Acceptable_humidity_level and g_humidity == True:
        print("제습기를 정지하겠습니다.")
        g_humidity = False
    if humidifier_AI_system > g_Max_Acceptable_humidity_level and g_humidifier == True:
        print("가습기를 정지하겠습니다.")
        g_humidifier = False
    if humidifier_AI_system < g_Min_Acceptable_humidity_level and g_humidifier == False:
        print("가습기를 작동하겠습니다.")
        g_humidifier = True
    if Balcony_Windows_AI_system_2 < Windows_temperature and g_Radiator == False: # 실내온도를 측정해서로 바꿔야한다. (지금은 현재밖에 온도)
        print("난방기 작동시키겠습니다.")
        g_Radiator = True
    if Blind_AI_system_2 == 1 and g_Blind == False:
        Blind_Start = int(input("\n블라인드를 여시겠습니까? \n1.작동\n2.정지 \n입력해주세요: "))
        if Blind_Start == 1:
            print("블라인드를 열겠습니다.")
            g_Blind = True
        elif Blind_Start == 2:
            g_Blind = False
    time.sleep(1)

def simulation_mode():
    global g_Balcony_Windows
    simulation_number = int(input("""\n1. 비오는날 시뮬레이션 (발코니창 제어)
2. 습한날 시뮬레이션 (제습기 제어)
3. 건조한날 시뮬레이션 (가습기 제어)
4. 상쾌한날 시뮬레이션 (제습기/가습기 제어)
입력하세요: """))
    if simulation_number == 1:
        real_weather_list = []
        real_weather = {"baseDate": 20180131,
                        "baseTime": 1430,
                        "category": "RN1",
                        "fcstDate": 20180131,
                        "fcstTime": time.strftime("%H%M", time.localtime(time.time())),
                        "fcstValue": random.randint(1, 100),  # 변경가능 0으로 강수량 없음으로
                        "nx": 89,
                        "ny": 91
                        }
        real_weather_list.append(real_weather)
        weather_div = real_weather_list[0]
        rain_AI_system = int(weather_div['fcstValue'])
        if rain_AI_system > 0 and g_Balcony_Windows == True:
            print("강수량 :", rain_AI_system, " 비가와요! 문닫아요!")
            g_Balcony_Windows = False
        with open('weather.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(real_weather_list, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)

    elif simulation_number == 2:
        global g_humidity
        real_weather_list = []
        real_weather = {"baseDate": 20180131,
                        "baseTime": 1430,
                        "category": "REH",
                        "fcstDate": 20180131,
                        "fcstTime": time.strftime("%H%M", time.localtime(time.time())),
                        "fcstValue": random.randint(1, 100),  # 범위 변경가능
                        "nx": 89,
                        "ny": 91
                        }
        real_weather_list.append(real_weather)
        weather_div = real_weather_list[0]
        humidity_AI_system = int(weather_div['fcstValue'])
        if humidity_AI_system > g_Max_Acceptable_humidity_level and g_humidity == False:
            print("습도 :", humidity_AI_system, "%", "제습기 작동하겠습니다.")
            g_humidity = True
        elif humidity_AI_system < g_Min_Acceptable_humidity_level and g_humidity == True:
            print("습도 :", humidity_AI_system, "%", "입니다. 제습기를 정지합니다.")
            g_humidity = False
        elif humidity_AI_system in range(g_Min_Acceptable_humidity_level, g_Max_Acceptable_humidity_level + 1):
            print("습도 :", humidity_AI_system, "%", "아주 좋습니다. 유지하세요.")
        with open('weather.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(real_weather_list, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
    elif simulation_number == 3:
        global g_humidifier
        real_weather_list = []
        real_weather = {"baseDate": 20180131,
                        "baseTime": 1430,
                        "category": "REH",
                        "fcstDate": 20180131,
                        "fcstTime": time.strftime("%H%M", time.localtime(time.time())),
                        "fcstValue": random.randint(1, 100),  # 범위 변경가능
                        "nx": 89,
                        "ny": 91
                        }
        real_weather_list.append(real_weather)
        weather_div = real_weather_list[0]
        humidifier_AI_system = int(weather_div['fcstValue'])
        if humidifier_AI_system > g_Max_Acceptable_humidity_level and g_humidifier == True:
            print("습도 :", humidifier_AI_system, "%", "가습기 정지하겠습니다.")
            g_humidifier = False
        elif humidifier_AI_system < g_Min_Acceptable_humidity_level and g_humidifier == False:
            print("습도 :", humidifier_AI_system, "%", "입니다. 가습기를 작동합니다.")
            g_humidifier = True
        elif humidifier_AI_system in range(g_Min_Acceptable_humidity_level, g_Max_Acceptable_humidity_level + 1):
            print("습도 :", humidifier_AI_system, "%", "아주 좋습니다. 유지하세요.")
        with open('weather.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(real_weather_list, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
    elif simulation_number == 4:
        real_weather_list = []
        real_weather = {"baseDate": 20180131,
                        "baseTime": 1430,
                        "category": "REH",
                        "fcstDate": 20180131,
                        "fcstTime": time.strftime("%H%M", time.localtime(time.time())),
                        "fcstValue": random.randint(g_Min_Acceptable_humidity_level,
                                                    g_Max_Acceptable_humidity_level + 1),  # 범위 변경가능
                        "nx": 89,
                        "ny": 91
                        }
        real_weather_list.append(real_weather)
        weather_div = real_weather_list[0]
        nice_AI_system = int(weather_div['fcstValue'])
        if nice_AI_system in range(g_Min_Acceptable_humidity_level,
                                   g_Max_Acceptable_humidity_level + 1) and g_humidifier == True and g_humidity == True:
            g_humidifier = False
            g_humidity = False
            print("현재 습도:", nice_AI_system,"% 가습기, 제습기 정지합니다.")
        elif nice_AI_system in range(g_Min_Acceptable_humidity_level,
                                     g_Max_Acceptable_humidity_level + 1) and g_humidifier == True and g_humidity == False:
            g_humidifier = False
            print("현재 습도:", nice_AI_system,"% 가습기를 정지합니다.")
        elif nice_AI_system in range(g_Min_Acceptable_humidity_level,
                                     g_Max_Acceptable_humidity_level + 1) and g_humidifier == False and g_humidity == True:
            g_humidity = False
            print("현재 습도:", nice_AI_system,"% 제습기를 정지합니다.")
        else:
            print("현재 습도:", nice_AI_system, '% 이며, 가습기,제습기 정지상태입니다. 쾌적합니다.')

        with open('weather.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(real_weather_list, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)

t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if (menu_num == 1):
        check_device_status()
    elif (menu_num == 2):
        control_device()
    elif (menu_num == 3):
        smart_mode()
    elif (menu_num == 4):
        simulation_mode()
    elif (menu_num == 0):
        break