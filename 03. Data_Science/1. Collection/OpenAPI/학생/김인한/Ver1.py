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
g_AI_Mode = False

access_key = "fgNUbFNWdrPsUqf6WsEPlsKYxDQ%2BgzRO2LIXFxVCeb7zMpjnDnIGiVINYnTenSQdMMseq9GIWW4Bkh5%2B7ZNXKA%3D%3DABC"

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("0. 프로그램 종료")

def check_device_status():
    print("\n난방기 상태: ",end='')
    if(g_Radiator == True): print("작동")
    elif(g_Radiator == False): print("정지")

    print("가스밸브 상태: ",end='')
    if(g_Gas_Valve == True): print("작동")
    elif(g_Gas_Valve == False): print("정지")

    print("발코니 창문 상태: ",end='')
    if(g_Balcony_Windows == True): print("작동")
    elif(g_Balcony_Windows == False): print("정지")

    print("출입문 상태: ",end='')
    if(g_Door == True): print("작동")
    elif(g_Door == False): print("정지")

def print_device_menu():
    print("상태 변경할 기기를 선택하세요. ")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(배란다) 창문")
    print("4. 출입문")

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None

def getweather(base_date,base_time,nx,ny):
    pass
    # 메뉴얼을 보고 기상정보 수집하는 코드를 직접 작성할 것

def get_realtime_weather_info():
    jsonresult = []
    basedate = time.strftime("%Y%m%d", time.localtime(time.time()))
    basetime = time.strftime("%H%M", time.localtime(time.time()))
    basetime = int(basetime) - 100
    basetime = str(basetime)
    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)

    # HK Comment] jsondata 저장 하는 코드를 직접 작성할것 (관광지 정보 코드 참조가능)

    print("%s_%s_날씨정보"%(basedate, basetime))
    with open('%s_%s_날씨정보.json' % (basedate, basetime), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def update_scheduler():
    global g_Balcony_Windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            AI_time = time.localtime(time.time())
            if AI_time[4] == 45 and AI_time[5] == 30:
                with open('weather.json', encoding='utf8') as outfile:
                    json_object = json.load(outfile)
                    json_string = json.dumps(json_object)
                    json_big_data = json.loads(json_string)

                weather_div = json_big_data[0]
                rain_AI_system = int(weather_div['fcstValue'])
                if rain_AI_system == 0 and g_Balcony_Windows == False:
                    print("창문을 열겠습니다.")
                    g_Balcony_Windows = True
                elif rain_AI_system > 0 and g_Balcony_Windows == True:
                    print("비가와요! 문닫아요!")
                    g_Balcony_Windows = False
                time.sleep(1)
t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

def smart_mode():
    global g_AI_Mode
    global g_Balcony_Windows
    print("\n1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태변경")
    print("3. 실시간 기상정보 Update")
    print("4. 시뮬레이션 모드")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("정지")
    elif menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동")
            update_scheduler()
        else: print("중지")

    elif menu_num == 3:
        get_realtime_weather_info()

    elif menu_num == 4:
        simulation_number = int(input("""1. 비오는날 시뮬레이션 (발코니창 제어)
2. 습한날 시뮬레이션 (제습기 제어)
3. 건조한날 시뮬레이션 (가습기 제어)
4. 상쾌한날 시뮬레이션 (제습기/가습기 제어)
    입력하세요: """))
        if simulation_number == 1:
            real_weather_list = []
            real_weather = {"baseDate": 20180129,
                            "baseTime": 1430,
                            "category": "RN1",
                            "fcstDate": 20180129,
                            "fcstTime": time.strftime("%H%M", time.localtime(time.time())),
                            "fcstValue": random.randint(1, 100), # 변경가능 0으로 강수량 없음으로
                            "nx": 89,
                            "ny": 91
                            }
            real_weather_list.append(real_weather)
            weather_div = real_weather_list[0]
            rain_AI_system = int(weather_div['fcstValue'])
            if rain_AI_system == 0 and g_Balcony_Windows == False:
                print("창문을 열겠습니다.")
                g_Balcony_Windows = True
            elif rain_AI_system > 0 and g_Balcony_Windows == True:
                print("강수량 :",rain_AI_system," 비가와요! 문닫아요!")
                g_Balcony_Windows = False
            with open('weather.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(real_weather_list, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)

        # elif simulation_number == 2:


def control_device():
    global g_Radiator
    global g_Gas_Valve
    global g_Balcony_Windows
    global g_Door
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1:
        if g_Radiator == True:
            g_Radiator = False
            print("난방기 정지")
        elif g_Radiator == False:
            g_Radiator = True
            print("난방기 작동")
    elif menu_num == 2:
        if g_Gas_Valve == True:
            g_Gas_Valve = False
            print("가스밸브 잠금")
        elif g_Gas_Valve == False:
            g_Gas_Valve = True
            print("가스밸브 오픈")
    elif menu_num == 3:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
            print("창문 닫음")
        elif g_Balcony_Windows == False:
            g_Balcony_Windows = True
            print("창문 개방")
    elif menu_num == 4:
        if g_Door == True:
            g_Door = False
            print("출입문 닫음")
        elif g_Door == False:
            g_Door = True
            print("출입문 개방")

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 0): break