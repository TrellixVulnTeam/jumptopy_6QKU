# HKComment] 특정시간대에 결함이 발생할 수 있는 요소 점검
# 레시피 정보는 냉장고 디바이스를 만들어서 표시
# 검색정보를 수신하는 디바이스를 선택하여 표시할 수 있도록 추천
## [ver6]과 동일

######################################## Smart Home Network ########################################

import urllib.request                       ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup               ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
import datetime
import time
import json
import threading

g_Radiator = False              ## 난방기
g_Airconditioner = False        ## 에어컨
g_Aircleaner = False            ## 공기청정기
g_Humidifier = False            ## 가습기
g_Dehumidifier = False          ## 제습기
g_Gas_Valve = False             ## 가스밸브
g_Balcony_Windows = False       ## 발코니(베란다) 창문
g_Door = False                  ## 출입문
g_AI_Mode = False               ## 인공지능 모드
g_Ventilation_Mode = False      ## 환기 모드

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"   ## 기상정보 / 대기환경정보 service_key
json_weather_result = []        ## request 날린 기상정보를 담는 리스트
json_atmosphere_result = []     ## request 날린 대기환정보를 담는 리스트
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
last_thrid = "30"       ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
######## x_coodinate / y_coodinate는 기상 정보를 알아볼 위치 89 /91은 신암동
x_coodinate = "89"      ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
y_coodinate = "91"      ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
numofrows = "100"       ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 request 날릴 때, 항목
sidoname = "대구"       ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 request 날릴 때, 항목
stationname = "신암동"  ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 request 날릴 때, 항목
ver_info = "1.3"        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 request 날릴 때, 항목

client_id = "R1JCmA0iVfg4x_ecHHkN"                  ## 요리 레시피 / 맛집 검색 ID
client_secret = "EycJ4UgDEA"                        ## 요리 레시피 / 맛집 검색 Secret
display_recipe = "10"                               ## 검색 결과 출력 건수 지정 - 10 ~ 100
sort_recipe = "sim"                                 ## 정렬 옵션 : sim (유사도순), date (날짜순)
restaurant_local = "신암동"       ## "신암동" - 신암동 요리 맛집 json 파일 request 날릴 때, 항목
good_restaurant = "맛집"          ## "맛집" - 신암동 요리 맛집 json 파일 request 날릴 때, 항목


######################################## Check_Control_Device ########################################
def Print_Device_fir_Status(device_name, devcie_status):    ## 장비 상태 출력 함수 1-1
    print(">> %s 상태: " % device_name, end="")
    if devcie_status == True: print("작동")
    else: print("정지")

def Print_Device_snd_Status(device_name, devcie_status):    ## 장비 상태 출력 함수 1-2
    print(">> %s 상태: " % device_name, end="")
    if devcie_status == True: print("열림")
    else: print("닫힘")

def Check_Device_Status():      ## 장비 상태 확인 함수
    print("")
    print("===================================")
    Print_Device_fir_Status('난방기', g_Radiator)
    Print_Device_fir_Status('에어컨', g_Airconditioner)
    Print_Device_fir_Status('공기청정기', g_Aircleaner)
    Print_Device_fir_Status('가습기', g_Humidifier)
    Print_Device_fir_Status('제습기', g_Dehumidifier)
    Print_Device_snd_Status('가스밸브', g_Gas_Valve)
    Print_Device_snd_Status('발코니(베란다) 창문', g_Balcony_Windows)
    Print_Device_snd_Status('출입문', g_Door)
    print("===================================")
    print("")

def Control_Device():       ## 장비 제어 함수
    ## 전역 변수를 비교나 어사인 하려면 함수 안에서 global을 설정해 줘야 해!!
    global  g_Radiator, g_Airconditioner, g_Aircleaner, g_Humidifier, g_Dehumidifier, g_Gas_Valve, g_Balcony_Windows, g_Door

    Check_Device_Status()
    menu_num = int(input("<<상태 변경할 기기의 번호를 입력하세요>>\n"
                         "1. 난방기\n2. 에어컨\n3. 공기청정기\n4. 가습기\n5. 제습기\n"
                         "6. 가스밸브\n7. 발코니(베란다)창\n8. 출입문\n-> "))

    if menu_num == 1:
        g_Radiator = not g_Radiator
    elif menu_num == 2:
        g_Airconditioner = not g_Airconditioner
    elif menu_num == 3:
        g_Aircleaner = not g_Aircleaner
    elif menu_num == 4:
        g_Humidifier = not g_Humidifier
    elif menu_num == 5:
        g_Dehumidifier = not g_Dehumidifier
    elif menu_num == 6:
        g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 7:
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 8:
        g_Door = not g_Door
    print("")

    Check_Device_Status()

######################################## URL_Request_Json_Read ########################################
def get_Request_URL(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)     ## request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):       ## (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=" + numofrows

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})

    with open('동구_%s_초단기예보조회_%s.json' % (stationname, yyyymmdd), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_%s_초단기예보조회_%s_%s.json SAVED\n' % (stationname, yyyymmdd, day_time))

def get_Realtime_Weather_Info():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = "{0:0>2}".format(day_hour_int) + last_thrid      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    return day_min_int

def Read_Weather_Json():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일을 불러오는(읽는) 함수
    total_weather = []
    with open("동구_%s_초단기예보조회_%s.json" % (stationname, yyyymmdd), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_weather = json.loads(json_string)

    return total_weather

def get_Atmosphere_URL():   ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) request 보내기 전, url 만드는 함수

    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=json&serviceKey=" + access_key
    parameters += "&sidoName=" + urllib.parse.quote(sidoname)
    parameters += "&ver=" + ver_info

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Atmosphere_Json():  ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일 생성하는 함수
    print("\n<<가장 최신 대기환경정보 업데이트를 실시합니다!!>>\n".center(30))
    jsonData = get_Atmosphere_URL()

    for prn_data in jsonData.get('list'):
        if prn_data.get('stationName') == stationname:      ## 신암동 정보만 뽑아내기 위해
            json_atmosphere_result.append({'stationName':prn_data.get('stationName'),
                           'dataTime':prn_data.get('dataTime'),
                           'pm10Value':prn_data.get('pm10Value'),       ## 10μm 이하의 미세먼지를 기준으로
                           'pm10Grade1h':prn_data.get('pm10Grade1h'),
                           'khaiValue':prn_data.get('khaiValue'),
                           'khaiGrade':prn_data.get('khaiGrade')})

    with open('동구_%s_통합대기환경정보_%s.json' % (stationname, yyyymmdd), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_atmosphere_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_%s_통합대기환경정보_%s.json SAVED\n' % (stationname, yyyymmdd))

def Read_Atmosphere_Json():        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) json 파일을 불러오는(읽는) 함수
    total_atmosphere = []
    with open("동구_%s_통합대기환경정보_%s.json" % (stationname, yyyymmdd), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_atmosphere = json.loads(json_string)

    return total_atmosphere

######################################## Smart_AI_Ventilation ########################################
def Update_Scheduler():     ## 인공지능 모드 ON일 경우, 매 시 45분 10초 마다 실시간 정보를 업데이트 하도록 하는 함수
    while True:
        if g_AI_Mode == False:
            continue
        else:   ## 인공지능 모드가 켜지면
            if time.strftime("%M%S") == "4510":     ## 매 시 45분 10초에
                print("<< 설정하신 45분이 되었습니다. 실시간 정보 업데이트를 시작합니다:) >>\n")
                get_Realtime_Weather_Info()     ## 실시간 기상정보를 업데이트 해라
                Make_Atmosphere_Json()          ## 실시간 대기환경정보를 업데이트 해라
                time.sleep(5)   ## 업데이트 하고는 5초간 잠재워라 -> 업데이트를 한 번만 하도록

def Window_Ventilation():   ## 환기 모드 작동 -> 2시간 창문 닫고 20분 창문 열도록(2시간마다 20분씩 창문 열어서 환기) 하는 함수
    global g_Balcony_Windows
    while True:
        if g_Ventilation_Mode == False:
            continue
        else:   ## 환기 모드가 켜지면
            print("<< 환기를 위해 20분 동안 창문을 엽니다:) >>\n")
            if g_Balcony_Windows == False:  ## 창문이 닫혀 있다면
                g_Balcony_Windows = not g_Balcony_Windows       ## 창문을 열어라
                time.sleep(1200)    ## 20분 동안
            else:   ## 창문이 열려 있다면
                time.sleep(1200)    ## 20분 동안 창문을 열어 놔라

            g_Balcony_Windows = not g_Balcony_Windows   ## 이제 창문을 닫아라
            print("<< 환기를 마쳤습니다. 2시간 동안 창문을 닫습니다:) >>\n")
            time.sleep(7200)        ## 2시간 동안

def AI_Mode_TurnOn():       ## 인공지능 모드가 꺼져 있는 상황에서, 켤 지 묻는 함수
    global g_AI_Mode

    switch_num = int(input("\n<< 인공지능 모드가 꺼져 있습니다. 켜시겠습니까? >>\n1. ON\n2. OFF\n\n-> "))
    if switch_num == 1:
        print("\n===============================")
        print("인공지능 모드를 가동합니다:)\n")
        print(">> 변경 전 인공지능 모드 : ", end="")
        if g_AI_Mode == False: print("정지")
        g_AI_Mode = not g_AI_Mode
        print(">> 현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        print("===============================\n")

        Devices_AI()

    elif switch_num == 2:
        print("\n======================================")
        print("인공지능 모드 정지 상태를 유지합니다:)")
        print("======================================\n")

def Ventilation_Mode():     ## 환기 모드가 꺼져 있는 상황에서, 켤 지 묻는 함수
    global g_Ventilation_Mode
    switch_num = int(input("\n<< 환기 모드를 켜시겠습니까? >>\n1. ON\n2. OFF\n\n-> "))
    if switch_num == 1:
        print("\n===============================")
        print("환기 모드를 가동합니다:)\n")
        print(">> 변경 전 환기 모드 : ", end="")
        if g_Ventilation_Mode == False: print("정지")
        g_Ventilation_Mode = not g_Ventilation_Mode
        print(">> 현재 환기 모드 : ", end="")
        if g_Ventilation_Mode == True: print("작동")
        print("\n2시간마다 20분씩 환기")
        print("===============================\n")

    elif switch_num == 2:
        print("\n======================================")
        print("환기 모드 정지 상태를 유지합니다:)")
        print("======================================\n")

def Control_Devices_AI(total_weather, total_atmosphere):        ## 인공지능 - 장비 제어 함수
    global g_Radiator, g_Airconditioner, g_Aircleaner, g_Balcony_Windows, g_Humidifier, g_Dehumidifier

    print("===============================================================================")

################################### 난방기 / 에어컨 인공지능 모드
    temperature_num = 0     ## 난방기 / 에어컨 인공지능 모드
    for temper in total_weather:
        if temper.get('category') == "T1H":     ## 항목(category)이 온도(T1H)이면
            temperature_num += temper.get('fcstValue')
            break

    print(" 현재 기온 : %s ℃ ".center(65) % temperature_num)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("* 난방기 작동 범위 : \n     1. 기온이 15도 미만\n     2. 기온이 15도 이상 20이하일 때, 이미 난방기가 작동 중인 상황")
    print("* 에어컨 작동 범위 : 기온이 33도 이상")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ################## 난방기 작동
    ## 겨울철 실내 적정 온도 : 18 ~ 20도
    if temperature_num < 15:    ## 기온이 15도 미만이면 난방기를 켜라
        if g_Radiator == True:  ## 난방기가 켜져 있으면, 그대로 유지
            print("기온이 15℃ 미만입니다. 작동 중인 난방기 상태를 유지합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == True: print("작동\n")
        else:   ## 난방기가 꺼져 있으면, 켜라
            g_Radiator = not g_Radiator
            print("기온이 15℃ 이하입니다. 정지된 난방기를 작동합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == True: print("작동\n")

    elif 15 <= temperature_num <= 20:       ## 기온이 15도 이상 20도 이하면 현재 난방기 상태 유지
        print("기온이 적정하여 현재 난방기 상태를 유지합니다:)")
        print(">> 난방기 상태 : ", end="")
        if g_Radiator == True: print("작동\n")
        else: print("정지\n")

    elif temperature_num > 20:      ## 기온이 20도 이상이면 난방기를 꺼라
        if g_Radiator == True:  ## 난방기가 켜져 있으면, 꺼라
            g_Radiator = not g_Radiator
            print("기온이 20℃ 초과입니다. 작동 중인 난방기를 정지합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == False: print("정지\n")
        else:   ## 난방기가 꺼져 있으면, 그대로 유지
            print("기온이 20℃ 초과입니다. 정지된 난방기 상태를 유지합니다:)")
            print(">> 난방기 상태 : ", end="")
            if g_Radiator == False: print("정지\n")

    ################## 에어컨 작동
    if temperature_num >= 33:   ## 기온이 33도 이상이면 에어컨을 켜라
        if g_Airconditioner == True:    ## 에어컨이 켜져 있으면, 그대로 유지
            print("기온이 33℃ 초과입니다. 작동 중인 에어컨 상태를 유지합니다:)")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == True: print("작동\n")
        else:   ## 에어컨이 꺼져 있으면, 켜라
            g_Airconditioner = not g_Airconditioner
            print("기온이 33℃ 초과입니다. 정지된 에어컨을 작동합니다.")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == True: print("작동\n")
    else:       ## 기온이 33도 미만이면 에어컨을 꺼라
        if g_Airconditioner == True:    ## 에어컨이 켜져 있으면, 꺼라
            g_Airconditioner = not g_Airconditioner
            print("기온이 33℃ 미만입니다. 작동 중인 에어컨을 정지합니다:)")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == False: print("정지\n")
        else:   ## 에어컨이 꺼져 있으면, 그대로 유지
            print("기온이 33℃ 미만입니다. 정지된 에어컨 상태를 유지합니다:)")
            print(">> 에어컨 상태 : ", end="")
            if g_Airconditioner == False: print("정지\n")

################################### 공기청정기 인공지능 모드
    atmosphere_num = 0
    for atmosphere_status in total_atmosphere:
        atmosphere_num += int(atmosphere_status.get('khaiValue'))        ## 통합대기환경 지수
        break

    print("================================".center(72))
    print(" 현재 통합대기환경 지수 : %s".center(60) % atmosphere_num)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("* 공기청정기 작동 범위 : 통합대기환경 지수 100 초과")  ## 통합대기환경 지수 101 ~ : 나쁨
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ################## 공기청정기 작동
    if atmosphere_num > 100:     ## 통합대기환경 지수가 100 초과이면 (대기환경이 나쁘면), 공기청정기 켜라
        if g_Aircleaner == True:    ## 공기청정기가 켜져 있으면
            print("대기환경이 나쁩니다. 작동 중인 공기청정기 상태를 유지합니다:)")      ## 그대로 유지
            print(">> 공기청정기 상태 : ", end="")
            if g_Aircleaner == True: print("작동\n")
        else:       ## 공기청정기가 꺼져 있으면
            g_Aircleaner = not g_Aircleaner     ## 켜라
        print("대기환경이 나쁩니다. 정지된 공기청정기를 작동합니다:)")
        print(">> 공기청정기 상태 : ", end="")
        if g_Aircleaner == True: print("작동\n")

    else:       ## 통합대기환경 지수가 100 이하이면 (대기환경이 나쁘지 않으면), 공기청정기 꺼라
        if g_Aircleaner == True:    ## 공기청정기가 켜져 있으면
            g_Aircleaner = not g_Aircleaner     ## 꺼라
            print("대기환경이 나쁘지 않습니다. 작동 중인 공기청정기를 정지합니다:)")
            print(">> 공기청정기 상태 : ", end="")
            if g_Aircleaner == False: print("정지\n")
        else:       ## 공기청정기가 꺼져 있으면
            print("대기환경이 나쁘지 않습니다. 정지된 공기청정기 상태를 유지합니다:)")     ## 그대로 유지
            print(">> 공기청정기 상태 : ", end="")
            if g_Aircleaner == False: print("정지\n")

################################### 창문 인공지능 모드
    rain_num = 0    ## rain_num > 0 : 비나 눈이 옴
    for window_status_wth in total_weather:
        if window_status_wth.get('category') == "PTY":      ## 항목(category)이 강수형태(PTY)이면
            rain_num += window_status_wth.get('fcstValue')     ## 강수 형태 (없음(0), 비(1), 비/눈(2), 눈(3))
            break

    atmosphere_num = 0    ## atmosphere_num > 100 : 나쁨
    for window_status_atm in total_atmosphere:
        atmosphere_num += int(window_status_atm.get('khaiValue'))      ## 통합대기환경지수
        break

    ######### 비가 오거나 난방기가 작동 중이거나 대기가 좋지 않으면, 창문을 닫아라
    if rain_num > 0 or g_Radiator == True or atmosphere_num > 100:
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            if rain_num > 0:    ## 비가 온다면
                g_Balcony_Windows = not g_Balcony_Windows   ## 창문을 닫아라
                print("비가 오고 있습니다. 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and atmosphere_num > 100:  ## 비는 오지 않고, 대기환경이 나쁘다면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("대기환경이 좋지 않습니다. 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and atmosphere_num <= 100 and g_Radiator == True:    ## 비는 오지 않고, 대기환경이 나쁘지 않고, 난방기가 작동 중이라면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("난방기가 작동 중입니다. 열린 창문을 닫습니다:)")
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")

        else:  ## 창문이 닫혀 있으면
            if rain_num > 0:    ## 비가 온다면
                print("비가 오고 있습니다. 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and g_Radiator == True:    ## 비는 오지 않고 난방기가 작동 중이라면
                print("난방기가 작동 중입니다. 닫힌 창문 상태를 유지합니다:)")    ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            elif rain_num == 0 and g_Radiator ==False and atmosphere_num > 100:   ## 비는 오지 않고, 난방기도 정지 중이고, 대기환경이 나쁘다면
                print("대기환경이 좋지 않습니다. 닫힌 창문 상태를 유지합니다:)")   ## 계속해서 창문을 닫아 놔라
                print(">> 발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")

    ######### 비도 오지 않고, 난방기도 정지 중이고, 대기도 나쁘지 않다면, 창문을 열어라
    elif rain_num == 0 and g_Radiator == False and atmosphere_num <= 100:
        if g_Balcony_Windows == True:  ## 창문이 열려 있으면
            print("대기 환경이 나쁘지 않은 강수 없는 날입니다. 열린 창문 상태를 유지합니다:)")
            print(">> 발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == True: print("열림\n")
        elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
            g_Balcony_Windows = not g_Balcony_Windows
            print("대기 환경이 나쁘지 않은 강수 없는 날입니다. 닫힌 창문을 엽니다:)")
            print(">> 발코니(베란다) 창문 상태 : ", end="")
            if g_Balcony_Windows == True: print("열림\n")

################################### 가습기 / 제습기 인공지능 모드
    humidity_status_num = 0
    for humidity_status in total_weather:
        if humidity_status.get('category') == "REH":     ## 항목(category)이 습도(REH)이면
            humidity_status_num += humidity_status.get('fcstValue')     ## 습도
            break

    print("====================".center(72))
    print(" 현재 습도 : %s %% ".center(70) % humidity_status_num)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("* 가습기 작동 범위 : 습도 45% 미만")    ## 실내 적정 습도 : 45 ~ 55%
    print("* 제습기 작동 범위 : \n     1. 습도가 55% 초과 70% 미만일 때, 이미 제습기가 작동 중인 상황\n     2. 습도 70% 이상")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ################## 가습기 작동
    if humidity_status_num < 45:  ## 습도가 45% 미만이면 가습기를 켜라
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            g_Humidifier = not g_Humidifier  ## 가습기 켜라
            print("습도가 45%% 미만입니다. 정지된 가습기를 작동합니다:)")
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == True: print("작동\n")
        else:  ## 가습기가 켜져 있으면
            print("습도가 45%% 미만입니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == True: print("작동\n")

    elif humidity_status_num >= 45:   ## 습도가 45% 이상이면 가습기를 꺼라
        if g_Humidifier == False:  ## 가습기가 꺼져 있으면
            print("습도가 45%% 이상입니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")
        else:  ## 가습기가 켜져 있으면
            g_Humidifier = not g_Humidifier
            print("습도가 45%% 이상입니다. 작동 중인 가습기를 정지합니다:)")  ## 가습기를 꺼라
            print(">> 가습기 상태 : ", end="")
            if g_Humidifier == False: print("정지\n")

    ################## 제습기 작동
    if humidity_status_num <= 55:      ## 습도가 55% 이하면 제습기를 꺼라
        if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
            print("습도가 55%% 이하입니다. 정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == False: print("정지\n")
        else:  ## 제습기가 켜져 있으면
            g_Dehumidifier = not g_Dehumidifier
            print("습도가 55%% 이하입니다. 작동 중인 제습기를 정지합니다:)")  ## 제습기를 꺼라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == False: print("정지\n")

    elif 55 < humidity_status_num < 70:      ## 습도가 55% 초과 70% 미만이면 제습기 상태를 그대로 유지
        print("습도가 적정하여 현재 제습기 상태를 유지합니다:)")
        print(">> 제습기 상태 : ", end="")
        if g_Dehumidifier == True: print("작동\n")    ## 켜져 있으면 그대로 켜 놓고
        else: print("정지\n")     ## 꺼져 있으면 그대로 꺼 놓고

    elif humidity_status_num >= 70:      ## 습도가 70% 이상이면 제습기를 켜라
        if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
            g_Dehumidifier = not g_Dehumidifier
            print("습도가 70%% 이상입니다. 정지된 제습기를 작동합니다:)")  ## 제습기를 켜라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == True: print("작동\n")
        else:  ## 제습기가 켜져 있으면
            print("습도가 70%% 이상입니다. 작동 중인 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
            print(">> 제습기 상태 : ", end="")
            if g_Dehumidifier == True: print("작동\n")

    print("===============================================================================")

    ################## 환기 모드 작동
    if rain_num == 0 and atmosphere_num <= 100:     ## 비가 안 오고, 대기환경이 나쁘지 않은 조건에서
        if g_Ventilation_Mode == False:         ## 환기 모드가 꺼져 있을 경우
            print("\n===============================")
            print(">> 현재 환기 모드 : ", end="")
            if g_Ventilation_Mode == False: print("정지")
            print("===============================")
            Ventilation_Mode()      ## 환기 모드가 꺼져 있는 상황에서, 켤 지 묻는 함수

def Devices_AI():   ## 실시간 업데이트 정보 request -> json 파일 만들고 -> 장비 제어하는 함수
    get_Realtime_Weather_Info()
    print("\n<<가장 최신 대기환경정보 업데이트를 실시합니다!!>>\n".center(30))
    Make_Atmosphere_Json()
    total_weather = Read_Weather_Json()  ## 기상정보 json 파일을 불러오는 함수 - 인공지능 모드를 위해 json 파일의 정보를 읽어 오는
    total_atmosphere = Read_Atmosphere_Json()  ## 대기환경정보 json 파일을 불러오는 함수 - 인공지능 모드를 위해 json 파일의 정보를 읽어 오는

    if 30 < get_Realtime_Weather_Info() <= 59:  ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
                                                ## get_Realtime_Weather_Info() 하면 return -> day_min_int

        Control_Devices_AI(total_weather, total_atmosphere)   ## 장비 제어 함수

    elif 0 <= get_Realtime_Weather_Info() <= 30:  ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = str(day_hour_int) + last_thrid

        Control_Devices_AI(total_weather, total_atmosphere)   ## 장비 제어 함수

def Smart_Mode():       ## 스마트 모드 메뉴 함수
    global g_AI_Mode, g_Ventilation_Mode
    print("")
    print("<< 스마트 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요 >>\n".center(45))
    menu_num = int(input("1. 인공지능 모드 조회\n2. 인공지능 모드 변경\n3. 환기 모드 조회\n4. 환기 모드 변경\n"
                         "5. 실시간 기상정보 Update\n6. 실시간 대기환경정보 Update\n\n-> "))

    if menu_num == 1:       ## 인공지능 모드 조회
        print("\n===============================")
        print(">> 현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("정지")
        print("===============================\n")

    elif menu_num == 2:     ## 인공지능 모드 상태 변경
        if g_AI_Mode == False:      ## 인공지능 모드가 꺼져 있을 경우
            AI_Mode_TurnOn()    ## 인공지능 모드가 꺼져 있는 상황에서, 켤 지 묻는 함수

        else:       ## 인공지능 모드가 켜져 있을 경우
            switch_num = int(input("\n<< 인공지능 모드가 켜져 있습니다. 끄시겠습니까? >>\n1. ON\n2. OFF\n-> "))
            if switch_num == 1:
                print("\n======================================")
                print("인공지능 모드 작동 상태를 유지합니다:)")
                print("======================================\n")
            elif switch_num == 2:
                print("\n===============================")
                print("인공지능 모드를 정지합니다:)\n")
                print(">> 변경 전 인공지능 모드 : ", end="")
                if g_AI_Mode == True: print("작동")
                g_AI_Mode = not g_AI_Mode
                print(">> 현재 인공지능 모드 : ", end="")
                if g_AI_Mode == False: print("정지")
                print("===============================\n")

    elif menu_num == 3:     ## 환기 모드 조회
        print("\n===========================")
        print(">> 현재 환기 모드 : ", end="")
        if g_Ventilation_Mode == True: print("작동")
        else: print("정지")
        print("===========================\n")

    elif menu_num == 4:     ## 환기 모드 상태 변경
        if g_Ventilation_Mode == False:     ## 환기 모드가 꺼져 있을 경우
            Ventilation_Mode()      ## 환기 모드가 꺼져 있는 상황에서, 켤 지 묻는 함수

        else:  ## 환기 모드가 켜져 있을 경우
            switch_num = int(input("\n<< 환기 모드가 켜져 있습니다. 끄시겠습니까? >>\n1. ON\n2. OFF\n-> "))
            if switch_num == 1:
                print("\n======================================")
                print("환기 모드 작동 상태를 유지합니다:)")
                print("======================================\n")
            elif switch_num == 2:
                print("\n===============================")
                print("환기 모드를 정지합니다:)\n")
                print(">> 변경 전 환기 모드 : ", end="")
                if g_Ventilation_Mode == True: print("작동")
                g_Ventilation_Mode = not g_Ventilation_Mode
                print(">> 현재 환기 모드 : ", end="")
                if g_Ventilation_Mode == False: print("정지")
                print("===============================\n")

    elif menu_num == 5:
        get_Realtime_Weather_Info()

        ## 실시간 정보 업데이트를 하는데, 인공지능 모드가 ON인 경우, 실시간 정보 업데이트 한 것을 토대로, 상황 분석 -> 장비 제어
        if g_AI_Mode == True:
            total_weather = Read_Weather_Json()  ## 기상정보 json 파일을 불러오는 함수
            total_atmosphere = Read_Atmosphere_Json()   ## 대기환경통합정보 json 파일을 불러오는 함수

            Control_Devices_AI(total_weather, total_atmosphere)  ## 장비 제어 함수

    elif menu_num == 6:
        Make_Atmosphere_Json()

        ## 실시간 정보 업데이트를 하는데, 인공지능 모드가 ON인 경우, 실시간 정보 업데이트 한 것을 토대로, 상황 분석 -> 장비 제어
        if g_AI_Mode == True:
            total_weather = Read_Weather_Json()  ## 기상정보 json 파일을 불러오는 함수
            total_atmosphere = Read_Atmosphere_Json()  ## 대기환경정보 json 파일을 불러오는 함수

            Control_Devices_AI(total_weather, total_atmosphere)  ## 장비 제어 함수

    print("")

##########################################################################################################
##########################################################################################################
################################### 인공지능 모드 - 1. 요리 레피시 / 맛집 검색
def Update_Json():  ## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업 + 링크 주소가 잘못 나와서 다시 조합하는 작업 함수
    food_blog_ls = []
    with open('%s_%s_%s.json' % (inp_want_food, item_type, yyyymmdd), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        food_blog_ls = json.loads(json_string)

    for change_str in food_blog_ls.get('items'):
        ########## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업
        if '&quot;' in change_str.get('title') or '&lt;' in change_str.get('title') or '&gt;' in change_str.get('title') or\
                        '<b>' in change_str.get('title') or '</b>' in change_str.get('title') or '&amp;' in change_str.get('title'):
            change_str['title'] = change_str.get('title').replace("&quot;", "'")
            change_str['title'] = change_str.get('title').replace("&lt;", "<")
            change_str['title'] = change_str.get('title').replace("&gt;", ">")
            change_str['title'] = change_str.get('title').replace("<b>", "")
            change_str['title'] = change_str.get('title').replace("</b>", "")
            change_str['title'] = change_str.get('title').replace("&amp;", "&")
        if '&quot;' in change_str.get('description') or '&lt;' in change_str.get('description') or '&gt;' in change_str.get(
            'description') or '<b>' in change_str.get('description') or '</b>' in change_str.get('description') or '&amp;' in change_str.get('description'):
            change_str['description'] = change_str.get('description').replace('&quot;', "'")
            change_str['description'] = change_str.get('description').replace('&lt;', "<")
            change_str['description'] = change_str.get('description').replace('&gt;', ">")
            change_str['description'] = change_str.get('description').replace('<b>', "")
            change_str['description'] = change_str.get('description').replace('</b>', "")
            change_str['description'] = change_str.get('description').replace('&amp;', "&")

        ########## 링크 주소가 잘못 나와서 다시 조합하는 작업
        ## "http://blog.naver.com/theboni?Redirect=Log&amp;logNo=221065338934"      ## 이렇게 없는 주소로 나와서
        ## -> "https://blog.naver.com/theboni/221065338934"                         ## -> 제대로 된 주소로 바꿔 줌
        ## "http://blog.naver.com/dngusghk?Redirect=Log&amp;logNo=221161588949"
        ## -> "https://blog.naver.com/dngusghk/221161588949"

        change_str['link'] += "z"  ## link에 나와 있는 마지막 12자리 숫자를 가져오기 위해 z를 마지막에 넣어 줌
        new_link = change_str.get('bloggerlink') + "/" + change_str.get('link')[-13:-1]  ## z가 없으면 마지막 숫자는 누락되니까(-1번째 자리는 포함 안 하니까)
        change_str['link'] = new_link  ## 새로운 link 주소를 입력해 줌

    with open('%s_%s_%s.json' % (inp_want_food, item_type, yyyymmdd), 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(food_blog_ls, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

    return food_blog_ls

def Recipe_Request_Json(url):       ## 요리 레시피 / 맛집을 당겨오기 위해 request 보내는 함수
    req = urllib.request.Request(url)

    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(req)
    rescode = response.getcode()

    if rescode == 200:
        json_recipe_result = json.loads(response.read().decode('utf-8'))

        with open('%s_%s_%s.json' % (inp_want_food, item_type, yyyymmdd), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(json_recipe_result, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
            print('\n%s_%s_%s.json SAVED' % (inp_want_food, item_type, yyyymmdd))

    else:
        print("Error Code:" + rescode)

    ## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업 + 링크 주소가 잘못 나와서 다시 조합하는 작업 함수
    Update_Json()

def get_Recipe_URL():       ## 요리 레시피 / 맛집을 당겨오기 위해 request 보내는 전, URL 만드는 함수

    end_point = "https://openapi.naver.com/v1/search/blog"

    parameters = "?query=" + research_food  ## 검색을 원하는 문자열로서 UTF-8로 인코딩
    parameters += "&display=" + display_recipe  ## 검색 결과 출력 건수 지정
    parameters += "&sim=" + sort_recipe  ## 정렬 옵션 : sim (유사도순), date (날짜순)

    url = end_point + parameters

    Recipe_Request_Json(url)    ## 요리 레시피 / 맛집을 당겨오기 위해 request 보내는 함수

def Food_recommendation():      ## 요리 레시피 / 맛집 추천해 주는 함수
    global inp_want_food, research_food, item_type        ## global을 안 써주면 get_Recipe_URL에서 research_food를 인식하지 못하는
                                                          ## Recipe_Request_Json에서는 inp_want_food를 인식하지 못하는
    print("")                                             ## -> get_Recipe_URL(research_food, inp_want_food) 를 넣어 줘야 하는!! global을 써주면 편하다!!
    print("<< 배고픔을 싹 날려~ 모드입니다:) >>\n".center(40))
    inp_want_food = input("드시고 싶은 요리 이름을 입력해 주세요 : ")

    ########################### 레시피 추천
    item_type = "recipe"
    want_food = urllib.parse.quote(inp_want_food)  ## 요리 레시피 json 파일 request 날릴 때, 항목
    recipe_food = urllib.parse.quote(" 레시피")  ## 요리 레시피 json 파일 request 날릴 때, 항목
    research_food = want_food + recipe_food  ## 요리 레시피 json 파일 request 날릴 때, 항목

    get_Recipe_URL()        ## 요리 레시피를 당겨오기 위해 request 보내는 전, URL 만드는 함수

    recipe_blog_ls = Update_Json()      ## json 파일에서 레시피 목록을 가져오는 변수
    print("")
    print("<< %s 레시피 추천 목록입니다:) 관심 있는 레시피는 바로 가기를 클릭해 주세요~ >>".center(55) % inp_want_food)
    for prn_recipe in recipe_blog_ls.get('items'):
        print("\n<<제목>>\n%s\n" % prn_recipe.get('title'))
        print("<<간략 소개>>\n%s\n" % prn_recipe.get('description'))
        print("바로 가기 ☞  %s\n" % prn_recipe.get('link'))
        print("=" * 150)

    ########################### 맛집 추천
    item_type = "restaurant"
    local_food = urllib.parse.quote(restaurant_local)         ## "신암동" - 신암동 요리 맛집 json 파일 request 날릴 때, 항목
    want_food = urllib.parse.quote(inp_want_food)             ## 신암동 요리 맛집 json 파일 request 날릴 때, 항목
    restaurant_food = urllib.parse.quote(good_restaurant)     ## "맛집" - 신암동 요리 맛집 json 파일 request 날릴 때, 항목
    research_food = local_food + want_food + restaurant_food  ## 신암동 요리 맛집 json 파일 request 날릴 때, 항목

    print("")
    print("=+" * 100)
    print("=+" * 100)
    get_Recipe_URL()  ## 신암동 요리 맛집을 당겨오기 위해 request 보내는 전, URL 만드는 함수

    restaurant_blog_ls = Update_Json()      ## json 파일에서 맛집 목록을 가져오는 변수

    print("")
    print("<< %s %s %s 추천 목록입니다:) 관심 있는 맛집은 바로 가기를 클릭해 주세요~ >>".center(55) % (restaurant_local, inp_want_food, good_restaurant))
    for prn_recipe in restaurant_blog_ls.get('items'):
        print("\n<<제목>>\n%s\n" % prn_recipe.get('title'))
        print("<<간략 소개>>\n%s\n" % prn_recipe.get('description'))
        print("바로 가기 ☞  %s\n" % prn_recipe.get('link'))
        print("=" * 150)

################################### 인공지능 모드 - 2. 현재 뉴스 상위 1~20위 / 3. 한 주간의 상위 1~20위 뉴스 / 4. 현재 연예 뉴스 상위 1~20위 / 5. 현재 스포츠 뉴스 상위 1~20위
def Print_News(each_today_news_info, news_num):      ## 현재 인기 뉴스 / 한 주간의 인기 뉴스 / 현재 인기 연예 뉴스 프린트 함수
    news_title_link = each_today_news_info.a    ## <li class="num1"> 에 포함되어 있는 <a> 소스코드를 가져오는
    print("<< %s 위 >>" % news_num)
    print("제목 : %s" % news_title_link['title'])     ## <li class="num1"> 에 포함되어 있는 <a> 에 포함되어 있는 title 속성을 가져오는
    print("바로 가기 ☞  http://news.naver.com%s\n" % news_title_link['href'])    ## <li class="num1"> 에 포함되어 있는 <a> 에 포함되어 있는 href 속성을 가져오는

    ######## 또는 news_title_link로 새롭게 변수 지정할 필요 없이
    # print("<< %s 위 >>" % news_num)
    # print("제목 : %s" % each_today_news_info.a['title'])      ## 바로 each_today_news_info.a['title']) 이렇게 뽑아 내도 됨
    # print("바로 가기 ☞ http://news.naver.com%s\n" % each_today_news_info.a['href'])

def Print_Sports_News(each_today_news_info, news_num):      ## 현재 인기 스포츠 뉴스 프린트 함수
    news_title_link = each_today_news_info.a    ## <li class="num1"> 에 포함되어 있는 <a> 소스코드를 가져오는
    print("<< %s 위 >>" % news_num)
    print("제목 : %s" % news_title_link['title'])     ## <li class="num1"> 에 포함되어 있는 <a> 에 포함되어 있는 title 속성을 가져오는
    print("바로 가기 ☞  %s\n" % news_title_link['href'])    ## <li class="num1"> 에 포함되어 있는 <a> 에 포함되어 있는 href 속성을 가져오는


def Response_News(soup, news_type):        ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수
    news_num = 0
    while True:
        news_num += 1
        each_today_news_info = soup.find('li', attrs={'class': 'num%s' % news_num})  ## <li class="num1"> 에 포함되어 있는 소스코드를 가져오는

        if news_type == 1:
            Print_News(each_today_news_info, news_num)              ## 현재 인기 뉴스 / 한 주간의 뉴스 프린트 함수
        elif news_type == 2:
            Print_Sports_News(each_today_news_info, news_num)       ## 현재 인기 스포츠 뉴스 프린트 함수

        if news_num == 3: break

    while True:
        news_num += 1
        each_today_news_info = soup.find('li', attrs={'class': 'gnum%s' % news_num})

        if news_type == 1:
            Print_News(each_today_news_info, news_num)          ## 현재 인기 뉴스 / 한 주간의 뉴스 프린트 함수
        elif news_type == 2:
            Print_Sports_News(each_today_news_info, news_num)   ## 현재 인기 스포츠 뉴스 프린트 함수

        if news_num == 20: break

def Today_Top_News():       ## 현재 인기 뉴스 상위 1~20위를 보여 주는 함수
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=000&date=%s' % yyyymmdd)
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 현재 인기 뉴스 상위 1 ~ 20위 목록입니다:) 관심 있는 뉴스는 바로 가기를 클릭해 주세요~ >>\n".center(75))

    news_type = 1   ## 현재 인기 뉴스 / 한 주간의 인기 뉴스 / 현재 인기 연예 뉴스의 타입은 '1' - 링크 주소가 달라서 구분
    Response_News(soup, news_type)     ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수

def Week_Top_News():        ## 한 주간의 상위 1~20위 뉴스를 보여 주는 함수
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularWeek.nhn?rankingType=popular_week&sectionId=000&date=%s' % yyyymmdd)
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 지난 한 주간의 인기 뉴스 상위 1 ~ 20위 목록입니다:) 관심 있는 뉴스는 바로 가기를 클릭해 주세요~ >>\n".center(75))

    news_type = 1   ## 현재 인기 뉴스 / 한 주간의 인기 뉴스 / 현재 인기 연예 뉴스의 타입은 '1' - 링크 주소가 달라서 구분
    Response_News(soup, news_type)     ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수

def Ent_Top_News():         ## 현재 인기 연예 뉴스 상위 1~20위를 보여 주는 함수
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=106')
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 현재 인기 연예 뉴스 상위 1 ~ 20위 목록입니다:) 관심 있는 뉴스는 바로 가기를 클릭해 주세요~ >>\n".center(75))

    news_type = 1   ## 현재 인기 뉴스 / 한 주간의 인기 뉴스 / 현재 인기 연예 뉴스의 타입은 '1' - 링크 주소가 달라서 구분
    Response_News(soup, news_type)         ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수

def Sports_Top_News():      ## 현재 인기 스포츠 뉴스 상위 1~20위를 보여 주는 함수
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=107&date=%s' % yyyymmdd)
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 현재 인기 스포츠 뉴스 상위 1 ~ 20위 목록입니다:) 관심 있는 뉴스는 바로 가기를 클릭해 주세요~ >>\n".center(75))

    news_type = 2   ## 현재 인기 스포츠 뉴스의 타입은 '2' - 링크 주소가 달라서 구분
    Response_News(soup, news_type)         ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수

################################### 인공지능 모드 - 6. 인기 클립 영상 시청
def Response_Video(soup):
    video_link_group = soup.findAll('a')     ## 링크가 포함되어 있는 <a>의 모든 정보 가져오기 - 1~3위 링크 뽑기 위해

    ## <div class="cds_type"> 에 포함되어 있는 소스코드를 가져오는 - 4~20위 링크 뽑기 위해
    ## 4~20위는 <a> 안에 주소가 2개 포함되어 있어 동일한 주소가 두 번씩 출력 되는
    ## 그래서 그 보다 하위인 <div class="cds_type"> 소스코드 모두 가져옴
    today_video_lowlink = soup.findAll('div', attrs={'class': 'cds_type'})    ## 1~3위랑 4~20위의 범위를 다르게 잡아 줌

    video_num = 0
    for each_video in video_link_group:             ## 1-3위 - 링크가 포함되어 있는 <a>의 모든 정보에서
        check_link = each_video.get('href')         ## 링크 부분인 'href'만 가져오기
        if "http://tv.naver.com/v/" in check_link:  ## 링크에 순위 동영상 외 다른 동영상 링크도 포함되어 있어, 순위 동영상 링크 가져오기
            video_num += 1                          ## 순위 동영상에는 "http://tv.naver.com/v/"이 포함되어 있음
            print("<< %s 위 >>" % video_num)
            print("제목 : %s" % each_video.img.get('alt'))  ## <a> 하위 <img alt="이세영, 이승기의 영혼 조정! 이제 영원히 날 지키게 될 거예요"> 에서 제목 뽑아내기
            print("바로 가기 ☞  %s\n" % check_link)        ## <a href="http://tv.naver.com/v/2659359/list/67096"> 에서 링크 뽑아내기
        if video_num == 3: break

    for each_video in today_video_lowlink:          ## 4~20위 - <div class="cds_type"> 소스코드를 하나씩 넣음
        check_link = each_video.a.get('href')
        if "http://tv.naver.com/v/" in check_link:
            video_num += 1
            print("<< %s 위 >>" % video_num)
            print("제목 : %s" % each_video.img.get('alt'))  ## <div class="cds_type"> 하위 <img alt="이세영, 이승기의 영혼 조정! 이제 영원히 날 지키게 될 거예요"> 에서 제목 뽑아내기
            print("바로 가기 ☞  %s\n" % check_link)        ## <dl class="cds_info"> 하위 <a href="http://tv.naver.com/v/2659232/list/67096"> 에서 링크 뽑아내기
        if video_num == 20: break

def Watch_Video():
    html = urllib.request.urlopen('http://tv.naver.com/r/')
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 현재 인기 클립 영상 상위 1 ~ 20위 목록입니다:) 관심 있는 영상은 바로 가기를 클릭해 주세요~ >>\n".center(75))

    Response_Video(soup)

################################### 인공지능 모드 - 7. 음악 듣기
def Listen_Music():      ## 음악 듣기 함수
    print("")
    print("<< 음악 감상 모드입니다:) >>\n".center(40))
    inp_want_music = input("듣고 싶은 노래 제목이나 가수 이름을 입력해 주세요 : ")

    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=%s' % urllib.parse.quote(inp_want_music))
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    ## 모든 소스코드에서 <h3 class="yt-lockup-title "> 하위 소스코드만 따오는
    music_info = soup.findAll('h3', attrs={'class': 'yt-lockup-title '})

    print("")
    print("<< '%s' 노래 목록입니다:) 원하시는 노래는 바로 가기를 클릭해 주세요~ >>\n".center(65) % inp_want_music)

    music_count = 0
    while True:
        music_count += 1

        ## music_info = soup.findAll('h3', attrs={'class': 'yt-lockup-title '})가 리스트로 이루어져 있음
        ## 리스트에서 하나씩 뽑아 <a aria-describedby="description-id-841094" class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link " data-sessionlink="itct=CFkQ3DAYACITCJXFm4jrjdkCFQRYYAodGLMBsSj0JFIG7J2066Oo" dir="ltr" href="/watch?v=QLAmTkqzSPs" rel="spf-prefetch" title="이루 - 흰눈">이루 - 흰눈</a>
        print("제목 : %s" % music_info[music_count].a.get('title'))  ## <a>에 포함되어 있는 title="이루 - 흰눈"을 뽑아라
        print("바로 가기 ☞  https://www.youtube.com%s\n\n" % music_info[music_count].a.get(
            'href'))  ## <a>에 포함되어 있는 href="/watch?v=QLAmTkqzSPs"를 뽑아라

        if music_count == 10: break  ## 노래 10개 추천하고 종료해라

######################################## AI_Mode ########################################
def Integrated_AI_Mode():       ## 인공지능 모드
    global g_AI_Mode
    if g_AI_Mode == False:  ## 인공지능 모드가 꺼져 있는 경우
        AI_Mode_TurnOn()  ## 켤 지 묻는 함수
    else:   ## 인공지능 모드가 켜져 있는 경우
        pass    ## 그냥 패스

    print("")
    print("<< 인공지능 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요 >>\n".center(50))
    menu_num = int(input("1. [Food] 나 배고파!!\n2. [News] 나 현재 소식이 궁금해!!\n3. [News] 나 한 주간의 핫한 소식이 궁금해!!\n"
                         "4. [Entertainment] 나 핫한 연예 소식이 궁금해!!\n5. [Sports] 나 핫한 스포츠 소식이 궁금해!!\n"
                         "6. [TV] 나 핫한 클립 영상 보고 싶어~\n7. [Music] 나 음악 듣고 싶어~\n-> "))

    if menu_num == 1:
        Food_recommendation()       ## 요리 레시피 / 맛집 추천해 주는 함수
    elif menu_num == 2:
        Today_Top_News()            ## 현재 인기 뉴스 상위 1~20위를 보여 주는 함수
    elif menu_num == 3:
        Week_Top_News()             ## 한 주간의 상위 1~20위 뉴스를 보여 주는 함수
    elif menu_num == 4:
        Ent_Top_News()              ## 현재 인기 연예 뉴스 상위 1~20위를 보여 주는 함수
    elif menu_num == 5:
        Sports_Top_News()           ## 현재 인기 스포츠 뉴스 상위 1~20위를 보여 주는 함수
    elif menu_num == 6:
        Watch_Video()               ## 인기 클립 영상 시청 함수
    elif menu_num == 7:
        Listen_Music()              ## 음악 듣기 함수


##########################################################################################################
##########################################################################################################
######################################## Simulation_Mode ########################################
def Simulation_Mode():      ## 시뮬레이션 모드 메뉴
    global g_Balcony_Windows, g_Humidifier, g_Dehumidifier
    print("<< 시뮬레이션 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요 >>".center(45))
    menu_num = int(input("1. 비오는 날 시뮬레이션\n2. 건조한 날 시뮬레이션\n3. 습한 날 시뮬레이션\n"
                         "4. 상쾌한 날 시뮬레이션\n-> "))

    get_Realtime_Weather_Info()     ## json 파일 만들기 전 함수

    total_weather = Read_Weather_Json()     ## json 파일을 불러오는 함수

################################### 비오는 날 시뮬레이션
    if menu_num == 1:
        rain_num = 0   ## 창문 인공지능 모드
        for window_status in total_weather:
            if window_status.get('category') == "PTY":
                rain_num += window_status.get('fcstValue')
                break
        rain_num = 0

        if rain_num == 0:  ## 강수 확률이 있으면 창문을 닫아라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("강수 확률이 있어 창문을 닫습니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            else:  ## 창문이 닫혀 있으면
                print("강수 확률이 있어 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
        else:  ## 강수 확률이 없으면 창문을 열어라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                print("햇살이 좋아 열린 창문 상태를 유지합니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")
            elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
                g_Balcony_Windows = not g_Balcony_Windows
                print("햇살이 좋아 창문을 엽니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")

################################### 건조한 날 시뮬레이션
    elif menu_num == 2:
        humidity_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        print("현재 습도 : %s%%" % humidity_status_num)

        if humidity_status_num < 45:  ## 평균 습도가 45% 이하면 가습기를 켜라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                g_Humidifier = not g_Humidifier  ## 가습기 켜라
                print("현재 습도가 낮습니다. 가습기를 작동시킵니다:)")
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")
            else:  ## 가습기가 켜져 있으면
                print("현재 습도가 낮습니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")

        elif humidity_status_num >= 45 and humidity_status_num <= 55:
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

        elif humidity_status_num > 55:  ## 평균 습도가 55% 이상이면 가습기를 꺼라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도 : %s%%" % humidity_status_num)
                print("현재 습도가 높습니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도 : %s%%" % humidity_status_num)
                print("현재 습도가 높습니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

################################### 습한 날 시뮬레이션
    elif menu_num == 3:
        humidity_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        humidity_status_num = 75
        print("현재 습도 : %s%%" % humidity_status_num)

        if humidity_status_num > 70:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("현재 습도가 높습니다. 제습기를 작동시킵니다:)")  ## 제습기를 켜라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")
            else:  ## 제습기가 켜져 있으면
                print("현재 습도가 높습니다. 작동된 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")

        elif humidity_status_num < 55:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("현재 습도가 제습기 작동 범위 이하입니다. 정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("현재 습도가 제습기 작동 범위 이하입니다. 제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")

################################### 상쾌한 날 시뮬레이션
    elif menu_num == 4:
        humidity_status_num = 0   ## 가습기 / 제습기 인공지능 모드
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        humidity_status_num = 50

        if 45 <= humidity_status_num and humidity_status_num <= 55:
            print("\n현재 습도 : %s%%\n" % humidity_status_num)
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")


######################################## Entry_Point!!!!! ########################################
while True:
    t = threading.Thread(target=Update_Scheduler)       ## 인공지능 모드 ON일 경우,
    t.daemon = True                 ## 매 시 45분 10초 마다 실시간 정보를 업데이트 하도록 하는 스레드
    t.start()

    t = threading.Thread(target=Window_Ventilation)     ## 환기 모드 작동
    t.daemon = True                 ## -> 2시간 창문 닫고 20분 창문 열도록(2시간마다 20분씩 창문 열어서 환기) 하는 스레드
    t.start()


    print("<< Smart Home Network Program >>\n".center(50))
    menu_num = int(input("1. 장비 상태 확인\n2. 장비 제어\n3. 스마트 모드\n4. 인공지능 모드\n5. 시뮬레이션 모드\n0. 프로그램 종료\n\n-> "))

    if menu_num == 1:
        Check_Device_Status()
    elif menu_num == 2:
        Control_Device()
    elif menu_num == 3:
        Smart_Mode()
    elif menu_num == 4:
        Integrated_AI_Mode()
    elif menu_num == 5:
        Simulation_Mode()
    elif menu_num == 0:
        break