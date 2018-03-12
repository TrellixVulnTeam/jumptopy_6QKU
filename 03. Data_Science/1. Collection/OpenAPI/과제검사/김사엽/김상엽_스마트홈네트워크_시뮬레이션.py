import time
import json
import ctypes
import datetime
import threading
import urllib.request

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_Dehumidifier = False
g_Humidifier = False
g_AI_Mode = False
g_Air_Conditioner = False
g_Air_Cleaner = False
g_LCD_Panel = False
g_Speaker = False
g_air_con_max = 28
g_air_con_min = 20
g_dehumidi = 70
g_humidi = 40
g_Now_temperature = 0
g_Now_Humidity = 0
g_jsonResult_forecast = []
g_jsonResult_now = []
g_category = {"T1H" : "기온", "RN1" : "1시간 강수량", "SKY" : "하늘상태", "REH" : "습도", "PTY" : "강수형태", "LGT" : "낙뢰", "WSD" : "풍속"}
g_category_value = {"하늘상태" : {1 : "맑음", 2 : "구름조금", 3 : "구름많음", 4 : "흐림"},
                    "강수형태" : {0 : "없음", 1 : "비", 2 : "진눈개비", 3 : "눈"},
                    "낙뢰" : { 0 : "확률없음", 1 : "낮음", 2 : "보통", 3 : "높음"}}
g_function_dic = {"열림" : True, "닫힘" : False, "작동" : True, "정지" : False}
# g_disaster = {"01001" : "태풍", "01002" : "홍수", "01003" : "호우", "01004" : "강풍", "01005" : "대설", "01006" : "한파", "01007" : "풍랑",
#               "01008" : "황사", "01009" : "폭염", "01010" : "가뭄", "01011" : "지진", "01012" : "지진해일", "01013" : "해일",
#               "01014" : "산사태", "01015" : "화산폭발"}

accesskey = "DthpXT7YzG6wllvd7zn6DyNRVJJGmVR2EGEs5UWg%2BeVXHyMkw%2FxNO2WcSwTZc9RX0sJzCK5d3bNOxD16Etj0%2Fg%3D%3D"

def get_request_url(url) :

    req = urllib.request.Request(url)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Successed" %datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e :
        print(print("[%s] Url Request Failed" % datetime.datetime.now()))
        print(e)
        return None

def get_weather_forecast_info(x_coordinate, y_coordinate, base_date, base_time, page_num) :

    basic_request_url_forecast = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json"
    parameters += "&ServiceKey=" + accesskey
    parameters += "&nx=" + x_coordinate
    parameters += "&ny=" + y_coordinate
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&pageNo=" + str(page_num)

    final_request_url_forecast = basic_request_url_forecast + parameters
    retData_forecast = get_request_url(final_request_url_forecast)

    if retData_forecast == None : return None
    else : return json.loads(retData_forecast)

def get_control_signal() :
    url = "https://m.blog.naver.com/PostList.nhn?permalink=permalink&blogId=calmstalker"
    temp_dic = {}

    try:
        response_1 = urllib.request.urlopen(url)
        retData = response_1.read().decode("utf-8")
        print("Successed")
    except Exception as e:
        print(e)
        print("Failed")

    temp_1 = retData.split('<meta property="og:description" content=\"')
    temp_2 = temp_1[1].split('\"')[0].split(',')
    for x in temp_2:
        splited_x = x.split(':')
        temp_dic[splited_x[0]] = splited_x[1]


    return temp_dic

# def get_manual_for_disaster() :
#
#     D_url = "http://openapi.safekorea.go.kr/openapi/service/behaviorconductKnowHow/naturaldisaster/list"
#     for disaster in list(g_disaster.keys()) :
#         parameters = "?safety_cate=" + disaster
#         parameters += "&serviceKey=" + accesskey
#
#         final_url = D_url + parameters
#         retData_D_manual = get_request_url(final_url)
#         file_name = "국민행동요령(자연재해-%s).json" %g_disaster[disaster]
#
#         if retData_D_manual == None : pass
#         else :
#             save_weather_info(retData_D_manual, file_name )
#             print("%s저장완료" %file_name)

# def get_weather_now_info(x_coordinate, y_coordinate, base_date, base_time, page_num):
#
#     basic_request_url_now = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib"
#
#     parameters = "?_type=json"
#     parameters += "&ServiceKey=" + accesskey
#     parameters += "&nx=" + x_coordinate
#     parameters += "&ny=" + y_coordinate
#     parameters += "&base_date=" + base_date
#     parameters += "&base_time=" + base_time
#     parameters += "&pageNo=" + str(page_num)
#
#     final_request_url_now = basic_request_url_now + parameters
#     retData_now = get_request_url(final_request_url_now)
#
#     if retData_now == None:
#         return None
#     else:
#         return json.loads(retData_now)

def process_weather_info(forecast_or_now) :

    now_page = 1
    now_date = datetime.datetime.now()
    base_date = str(now_date.year) + "{0:0>2}".format(str(now_date.month)) + "{0:0>2}".format(str(now_date.day))

    if now_date.minute >= 45 :
        base_time = "{0:0>2}".format(str(now_date.hour)) + "{0:0>2}".format(str(now_date.minute))
    else :
        base_time = "{0:0>2}".format(str(now_date.hour - 1)) + "{0:0>2}".format(str(now_date.minute))

    while 1 :

        if forecast_or_now == "forecast" :
            jsonData = get_weather_forecast_info("89", "91", base_date, base_time, now_page)
        # elif forecast_or_now == "now" :
        #     jsonData = get_weather_now_info("89", "91", base_date, base_time, now_page)

        if jsonData["response"]["header"]["resultMsg"] == "OK" :
            for item in jsonData["response"]["body"]["items"]["item"] :
                name_of_coordinate = "대구광역시 동구 신암4동"
                g_jsonResult_forecast.append({"name" : name_of_coordinate,
                                   "base_date" : item["baseDate"],
                                   "base_time" : item["baseTime"],
                                   "weather" : item["category"],
                                   "forecast_date" : item["fcstDate"],
                                   "forecast_time" : item["fcstTime"],
                                   "weather_value" : item["fcstValue"]})

        now_page += 1
        max_pageNo = int(jsonData["response"]["body"]["totalCount"] / jsonData["response"]["body"]["numOfRows"])

        if max_pageNo - now_page == -1 : break

    return None

def save_weather_info(data, name = "우리동내_초단기_예보조회.json") :

    with open(name, 'w', encoding="utf-8") as outfile :
        retJson = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    return  None

def print_main_menu():

    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 일기예보 출력")
    print("5. 시뮬레이션 모드")
    print("6. 프로그램 종료")

def check_device_status():

    print("\n---------------<디바이스 상태>---------------")
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문', g_Door)
    print_device_status("가습기", g_Humidifier)
    print_device_status("제습기", g_Dehumidifier)
    print_device_status("에어컨", g_Air_Conditioner)
    print_device_status("공기청정기", g_Air_Cleaner)
    print_device_status("LCD패널", g_LCD_Panel)
    print_device_status("스피커", g_Speaker)

def print_device_status(device_name,devcie_status):

    print("%s 상태: "%device_name, end="")

    if devcie_status == True :
        if device_name == "난방기" or device_name == "가습기" or device_name == "제습기" or device_name == "에어컨" or\
device_name == "공기청정기" or device_name == "LCD패널" or device_name == "스피커" :
            print("작동")
        elif device_name == "발코니(베란다) 창문" or device_name == "출입문" or device_name == "가스밸브" :
            print("열림")

    else :
        if device_name == "난방기" or device_name == "가습기" or device_name == "제습기" or device_name == "에어컨" or\
device_name == "공기청정기" or device_name == "LCD패널" or device_name == "스피커"  :
            print("정지")
        elif device_name == "발코니(베란다) 창문" or device_name == "출입문" or device_name == "가스밸브" :
            print("닫힘")

def print_device_menu():
    print("\n---------------<상태 변경할 기기를 선택하세요>---------------")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")
    print("7. 에어컨")
    print("8. 공기청정기")
    print("9. LCD패널")
    print("10. 스피커")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_Humidifier, g_Dehumidifier, g_Air_Cleaner, g_Air_Conditioner,\
g_LCD_Panel, g_Speaker
    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))
    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_Humidifier = not g_Humidifier
    if menu_num == 6: g_Dehumidifier = not g_Dehumidifier
    if menu_num == 7: g_Air_Conditioner = not g_Air_Conditioner
    if menu_num == 8: g_Air_Cleaner = not g_Air_Cleaner
    if menu_num == 9: g_LCD_Panel = not g_LCD_Panel
    if menu_num == 10: g_Speaker = not g_Speaker
    check_device_status()

def smart_mode():
    global g_AI_Mode, t
    print("\n---------------<인공지능 모드 설정>---------------")
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상예보 Update")
    print("4. control signal 받기")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("---------------<디바이스 상태>---------------")
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else:print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("---------------<디바이스 상태>---------------")
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동\n우리동내 초단기예보 자동갱신 시작")
            t.start()
        else :
            print("중지")
            my_thread_terminate(t)
            print("자동갱신도 종료합니다.")
    elif menu_num == 3:
        process_weather_info("forecast")
        save_weather_info(g_jsonResult_forecast)
        if g_AI_Mode == True :
            print("---------------<디바이스 제어 상태>---------------")
            radiator_control(g_jsonResult_forecast)
            humidifier_control(g_jsonResult_forecast)
            dehumidifier_control(g_jsonResult_forecast)
            air_conditioner_control(g_jsonResult_forecast)
    elif menu_num == 4 :
        global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_Humidifier, g_Dehumidifier, g_Air_Cleaner, g_Air_Conditioner, \
g_LCD_Panel, g_Speaker
        signal = get_control_signal()
        g_Radiator = g_function_dic[signal["난방기"]]
        g_Gas_Valve = g_function_dic[signal["가스밸브"]]
        g_Balcony_Windows = g_function_dic[signal["발코니창"]]
        g_Door = g_function_dic[signal["현관문"]]
        g_Dehumidifier = g_function_dic[signal["제습기"]]
        g_Humidifier = g_function_dic[signal["가습기"]]
        g_Air_Conditioner = g_function_dic[signal["에어컨"]]
        g_Air_Cleaner = g_function_dic[signal["공기청정기"]]
        g_LCD_Panel = g_function_dic[signal["LCD패널"]]
        g_Speaker = g_function_dic[signal["스피커"]]
        check_device_status()



def get_realtime_weather_info_countinusly() :
    temp = datetime.datetime.now()
    while 1 :
        if temp.minute >= 45 and temp.minute < 46 :
            if g_AI_Mode == True :
                process_weather_info("forecast")
                save_weather_info(g_jsonResult_forecast)
            else : pass
            time.sleep(60)
        elif temp.minute < 45 :
            sleep_time_2 = (45 - temp.minute) * 60 - temp.second
            time.sleep(sleep_time_2)
        elif temp.minute >= 46 :
            sleep_time_1 = (60 - temp.minute) * 60 - temp.second
            time.sleep(sleep_time_1)

t = threading.Thread(target=get_realtime_weather_info_countinusly)
t.daemon = True

def terminate_thread(thread):
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def my_thread_terminate(t):
    while t.is_alive():
        try:
            terminate_thread(t)
        except:
            pass


def show_weather_info(jsonData) :
    global g_LCD_Panel
    num_of_forecast = int(len(jsonData) / 10)
    if g_LCD_Panel == True :
        print("-------------------------------------------------")
        print("\tforecast_date : %s" %jsonData[0]["forecast_date"])
        for time_line in range(num_of_forecast) :
            print("\tforecast_time : %s" %jsonData[time_line]["forecast_time"])
            for weather_line in range(10) :
                if jsonData[time_line + weather_line * num_of_forecast]["weather"] == "SKY"\
or jsonData[time_line + weather_line * num_of_forecast]["weather"] == "PTY"\
or jsonData[time_line + weather_line * num_of_forecast]["weather"] == "LGT" :
                    try :
                        print("\t%s : %s " % (g_category[jsonData[time_line + weather_line * num_of_forecast]["weather"]],
g_category_value\
    [g_category[jsonData[time_line + weather_line * num_of_forecast]["weather"]]]\
    [jsonData[time_line + weather_line * num_of_forecast]["weather_value"]]))
                    except KeyError : pass
                else :
                    try:
                        print("\t%s : %s " %(g_category[jsonData[time_line + weather_line * num_of_forecast]["weather"]],
                                             jsonData[time_line + weather_line * num_of_forecast]["weather_value"]))
                    except KeyError : pass
        print("-------------------------------------------------")
    else : print("LCD패널이 꺼져있습니다.")

def air_conditioner_control(json_data) :
    global g_Air_Conditioner
    for item in json_data:
        if item["weather"] == "T1H" and item["weather_value"] >= g_air_con_max and g_Radiator == False:
            print("20도 이상이 예상되어 에어컨을 켭니다.")
            g_Air_Conditioner = not g_Air_Conditioner
            break
        elif item["weather"] == "T1H" and item["weather_value"] < g_air_con_min and g_Radiator == True:
            print("20도 미만이 예상되어 에어컨을 끕니다.")
            g_Air_Conditioner = not g_Air_Conditioner
            break

def radiator_control(json_data) :
    global g_Radiator
    for item in json_data:
        if item["weather"] == "T1H" and item["weather_value"] >= g_air_con_min and g_Radiator == True:
            print("20도 이상이 예상되어 난방기를 끕니다.")
            g_Radiator = not g_Radiator
            break
        elif item["weather"] == "T1H" and item["weather_value"] < g_air_con_min and g_Radiator == False:
            print("20도 미만이 예상되어 난방기를 켭니다.")
            g_Radiator = not g_Radiator
            break

def window_control(json_data) :
    global g_Balcony_Windows
    for item in json_data:
        if item["weather"] == "PTY" and item["weather_value"] != 0 and g_Balcony_Windows == True:
            print("기상상황이 좋지 않다 예상되어 창문을 닫습니다.")
            g_Balcony_Windows = not g_Balcony_Windows
            break
        # elif item["weather"] == "PTY" and item["weather_value"] == 0 and g_Balcony_Windows == False:
        #     print("날이 좋을 것으로 예상되어 창문이 닫혀 있으니 엽니다.")
        #     g_Balcony_Windows = not g_Balcony_Windows
        #     break

def dehumidifier_control(json_data) :
    global g_Dehumidifier
    for item in json_data :
        if item["weather"] == "REH" and item["weather_value"] > g_dehumidi and g_Dehumidifier == False:
            print("습도가 70%초과라 예상되어 제습기를 켭니다.")
            g_Dehumidifier = not g_Dehumidifier
            break
        elif item["weather"] == "REH" and item["weather_value"] <= g_dehumidi and g_Dehumidifier == True:
            print("습도가 70%이하라 예상되어 제습기를 끕니다.")
            g_Dehumidifier = not g_Dehumidifier
            break

def humidifier_control(json_data) :
    global g_Humidifier
    for item in json_data :
        if item["weather"] == "REH" and item["weather_value"] < g_humidi and g_Humidifier == False:
            print("습도가 40%미만이라 예상되어 가습기를 켭니다.")
            g_Humidifier = not g_Humidifier
            break
        elif item["weather"] == "REH" and item["weather_value"] >= g_humidi and g_Humidifier == True:
            print("습도가 40%이상이라 예상되어 가습기를 끕니다.")
            g_Humidifier = not g_Humidifier
            break

def simulation_mode() :
    global g_Balcony_Windows
    global g_Humidifier
    global g_Dehumidifier

    json_simulation_data = [
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_date": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "PTY",
            "weather_value": 1
        },
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_date": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "REH",
            "weather_value": 80
        }
    ]

    json_simulation_data_good_weather = [
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_date": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "PTY",
            "weather_value": 0
        },
        {
            "base_date": 20180130,
            "base_time": "0930",
            "forecast_date": 20180130,
            "forecast_time": 1000,
            "name": "대구광역시 동구 신암4동",
            "weather": "REH",
            "weather_value": 50
        }
    ]

    save_weather_info(json_simulation_data, "시뮬레이션용날씨.json")
    save_weather_info(json_simulation_data_good_weather, "시뮬레이션용날씨_좋은날.json")
    # HK Comment] 시뮬레이션 작업후  JSON 파일 저장할 것 (다른 이름으로)
    order_1 = input("1.비오는날 시뮬레이션(발코니창 제어)\n2.습한날 시뮬레이션(제습기 제어)\n3.건조한날 시뮬레이션(가습기 제어)\n\
4.상쾌한날 시뮬레이션\n동작입력 : ")
    if order_1 == '1' :
        window_control(json_simulation_data)

    elif order_1 == '2' :
        dehumidifier_control(json_simulation_data)

    elif order_1 == '3' :
        humidifier_control(json_simulation_data)

    elif order_1 == '4' :
        window_control(json_simulation_data_good_weather)
        dehumidifier_control(json_simulation_data_good_weather)
        humidifier_control(json_simulation_data_good_weather)

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 2.0>")
print("                                   - 김상엽 -")
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))
    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif menu_num == 4 :
        show_weather_info(g_jsonResult_forecast)
    elif(menu_num == 5) :
        simulation_mode()
    elif(menu_num == 6):
        break