import urllib.request
import datetime
import json
import threading
from bs4 import BeautifulSoup
import ctypes

# HK Comment] 기술적인 융합 보다 비즈니스적인 융합을 좀 더 고민해보세요.

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False # 건축법 시행령에 따라 베란다가 아닌 폐쇄형 발코니가 정확한 표현
g_Door = False # 출입문
g_humidifier = False # 가습기
g_dehumidifier = False # 제습기
g_air_cleaner = False # 공기청정기
g_AI_Mode = False
g_Date="20180101"
g_Time="0600"
g_AI_Mode_ON_OFF_check = False

g_MAX_humidity = 75
g_MIN_humidity = 35
g_standard_time = 45

def update_scheduler(AI_name="집사"):
    
    check_45min_fir_exec = False # Flag => first_45_start_flag
    while True:
        if g_AI_Mode == True:  # 매~시 45분에 1시간 간격으로 데이터 읽기!
            global g_Balcony_Windows,g_Date, g_Time
            current_time = datetime.datetime.now() # HK Comment] 시간 보정 필요 없음
            if current_time.minute == g_standard_time and check_45min_fir_exec==False :  # 45분이고 초와 시간이 다르면.. 45분을 기준으로 1시간이 됐을 것이다?
                weather_data=Get_RealTime_Weather_Info(g_Date,g_Time) # 시간보정 필요없음
                air_pollution_data = Get_RealTime_Air_Pollution_Info('대구', '13')  # 대기오염 데이터 정보 받아와서
                
                safety_state = AI_Control_Pow(weather_data)  # 낙뢰에 따른 기기 전원 종료 -> 낙뢰 위험 감지시 기기에 대한 작동 off
                if safety_state == False:
                    AI_Control_Window(weather_data) # 창문제어
                    AI_Control_Humidifier(weather_data) # 가습기제어
                    AI_Control_Dehumidifier(weather_data) # 제습기제어                
                    AI_Control_Air_Pollution(air_pollution_data)
                    if g_Balcony_Windows == True:print("인공지능 스피커 %s : 화창한 날씨가 예상되어 창문을 열었어요."%AI_name)
                    else: print("인공지능 스피커 %s : 3시간 이내 비가 올 예정이므로 창문을 닫았어요."%AI_name)
                    if g_air_cleaner == True: print("인공지능 스피커 %s : 미세먼지 농도가 나쁘므로 공기청정기를 가동했어요."%AI_name)
                    else: print("인공지능 스피커 %s : 공기가 좋습니다 공기청정기를 켜지 않아도 될 것 같아요."%AI_name)
                    if g_humidifier == True: print("인공지능 스피커 %s : 건조한 날씨가 예상되어 가습기를 틀었어요."%AI_name)
                    else: print("인공지능 스피커 %s : 가습기를 꺼도 될 것 같아요."%AI_name)
                    if g_dehumidifier == True : print("인공지능 스피커 %s : 불쾌지수가 높을걸로 예상되어 제습기를 틀었어요."%AI_name)
                    else: print("인공지능 스피커 %s : 제습기를 꺼도 될 것 같아요."%AI_name)
                    if g_Radiator == True: print("인공지능 스피커 %s : 쌀쌀한 날씨가 예상되어 온풍기를 가동할게요"%AI_name)
                    else: print("인공지능 스피커 %s : 온풍기를 꺼도 될 것 같아요."%AI_name)

                else:
                    print("인공지능 스피커 %s : 낙뢰우려로 인한 전자제품 작동을 중지합니다."%AI_name)

                check_45min_fir_exec=True
            if current_time.minute != g_standard_time:
                check_45min_fir_exec=False

def Print_Main_Menu():
    print("1. 기기 상태 확인")
    print("2. 기기 제어")
    print("3. 스마트 모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료\n")

def Device_status(Device,Devcie_Status,ON_message='작동',OFF_message='정지'):
    print("%s 상태: "%Device, end="")
    if Devcie_Status == True : print(ON_message)
    elif Devcie_Status == False : print(OFF_message)

def Naver_Pop_Search_Word():
    html = urllib.request.urlopen('https://www.naver.com/')
    soup = BeautifulSoup(html, 'html.parser')

    search_word = soup.findAll('span', attrs={'class': 'ah_k'})
    rank_data = soup.findAll('span', attrs={'class': 'ah_r'})

    try:
        rank = int(input("검색어 1위부터 몇위까지 가져올까요?(최대 20위까지) : "))
        if rank>20:
            rank=20
        elif rank<1:
            rank=1
    except:
        rank = 10

    for i in range(rank):
        print("%2s위 %s"%(rank_data[i].text, search_word[i].text))
    print()

def Check_Device_Status():
    print()
    Device_status('난방기',g_Radiator) # 전역변수를 함수 파라미터로 사용했지만 값의 변경은 없으므로.
    Device_status('가스밸브', g_Gas_Valve,'열림','잠김')
    Device_status('발코니(베란다) 창문', g_Balcony_Windows,'열림','닫김')
    Device_status('출입문', g_Door,'열림','닫김')
    Device_status('가습기',g_humidifier)
    Device_status('제습기',g_dehumidifier)
    Device_status('공기청정기',g_air_cleaner)
    print()

def Print_Device_Menu():
    print("상태 변경할 기기를 선택하세요")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다) 창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")
    print("7. 공기청정기")

def Control_Device_Manual():
    global g_Radiator , g_Gas_Valve , g_Balcony_Windows , g_Door, g_humidifier, g_dehumidifier, g_air_cleaner
    Check_Device_Status()
    Print_Device_Menu()
    menu_num = input("번호를 입력하세요 : ")
    status_change_true = True
    
    if menu_num == '1': g_Radiator = not g_Radiator
    elif menu_num == '2': g_Gas_Valve = not g_Gas_Valve
    elif menu_num == '3': g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == '4': g_Door = not g_Door
    elif menu_num == '5': g_humidifier = not g_humidifier# 가습기
    elif menu_num == '6': g_dehumidifier = not g_dehumidifier# 제습기
    elif menu_num == '7': g_air_cleaner = not g_air_cleaner
    else :
        print("잘못된 입력")
        status_change_true = False

    if status_change_true == True:
        Check_Device_Status()

def get_request_url(url):
    # url - 사용자 입장 / req - 프로토콜 레벨에서 채워질 값들이 들어감
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:  # status code가 200인 경우 (정상 호출)
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as err_message:
        print(err_message)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def Date_and_Time_Correction(): # HK Comment] 시간 보정은 사용자가 원할 경우에만 하도록 변경
    global g_Date, g_Time
    current_time = datetime.datetime.now()
    g_Date = str(current_time.year) + str(current_time.month).zfill(2) + str(current_time.day).zfill(2)

    if current_time.minute < g_standard_time: # n시 0~44분 -> n-1시 30분으로 처리
        g_Time = str(current_time.hour-1).zfill(2) + str(30)
        if current_time.hour == 0 :
            g_Date = str(current_time.year) + str(current_time.month).zfill(2) + str(current_time.day-1).zfill(2)
            g_Time = str(23) + str(30)
        print("단기예보에 등록된 데이터를 읽기 위해 %s시 %s분으로 보정되었습니다 " % (g_Time[:2], g_Time[2:]))
    else:
        g_Time = str(current_time.hour).zfill(2) + str(current_time.minute).zfill(2)

    return g_Date+","+g_Time

def Json_Data_Save(Json_Data,File_name):
    with open(File_name, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(Json_Data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print("%s saved"%File_name)

def AI_Control_Window(Json_Data):
    global g_Balcony_Windows
    rain_flag = False
    for item_key in Json_Data['response']['body']['items']['item']:
        if item_key['category'] == 'RN1':  # 강수형태= PTY
            if 0 != item_key['fcstValue']:
                rain_flag = True # 창문닫는 작업, 맑은 날씨가 아닌것으로 예상되는 시간이 1시간이라도 있다면
                break

    if rain_flag == True: # 비온다
        g_Balcony_Windows = False
    else: # 비 안온다
        g_Balcony_Windows = True

def AI_Control_Humidifier(Json_Data):
    global g_humidifier
    high_humidity = False
    for item_key in Json_Data['response']['body']['items']['item']:
        if item_key['category'] == 'REH':  # 습도재는 데이터가 있다면
            if item_key['fcstValue'] <= g_MIN_humidity:
                high_humidity = True # 가습기 틀어야 되겠네
                break

    if high_humidity == True:
        g_humidifier = True
    else:
        g_humidifier = False

def AI_Control_Dehumidifier(Json_Data):
    global  g_dehumidifier
    low_humidity = False
    for item_key in Json_Data['response']['body']['items']['item']:
        if item_key['category'] == 'REH':
            if item_key['fcstValue'] >= g_MAX_humidity:
                low_humidity = True
                break

    if low_humidity == True:
        g_dehumidifier = True
    else:
        g_dehumidifier = False

def AI_Control_Pow(Json_Data):
    global g_Radiator,g_Balcony_Windows,g_humidifier,g_dehumidifier

    for item_key in Json_Data['response']['body']['items']['item']:
        if item_key['category']=='LGT':
            if item_key['fcstValue'] >= 2: # 0 확률없음 1 낮음 2 보통 3 높음
                g_Radiator = False # 온풍기 끄자
                g_Balcony_Windows = False # 창문 닫자
                g_humidifier = False # 가습기 끄자
                g_dehumidifier = False # 제습기 끄자
                return True
    return False

def AI_Control_Air_Pollution(Json_Data,local_name="신암동"): #대기오염
    global g_Balcony_Windows,g_air_cleaner

    for item_key in Json_Data['list']:
        if item_key['stationName'] == local_name:
            if item_key['pm10Grade'] =="3" or item_key['pm10Grade'] =="4" : # 나쁨~매우나쁨이라면
                g_Balcony_Windows = False # 닫아버린다.
                g_air_cleaner = True # 공기청정기는 켜야지
                break

def RealTime_Info_load(file_name): # 저장된 json 파일을 읽어들이는 함수
    with open(file_name, encoding='utf8') as infile:
        json_object = json.load(infile)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
    return json_big_data

def Get_RealTime_Air_Pollution_Info(local_name="대구",Row_len="13"):
    # 이 리퀘스트는 날짜 정보를 입력하지 않아도 당일(+현재시간대) 정보를 자동으로 리스폰스로 날려줌
    Access_Key = "iIhsixEf18XxhFwut8lRVPkptX44Z0E2kGCTBl8%2BBnOUU%2BNX5QoSpXcwZ1J14NbOB1s2cxLv9Uuf%2F%2FkjnHzysQ%3D%3D"
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=json&serviceKey=" + Access_Key
    parameters += "&sidoName=" + urllib.request.quote(local_name) # parse = request 결과는 같음 내부동작의 차이는?
    parameters += "&numOfRows=13"

    url = end_point + parameters # url은 분명히 정상임. 리퀘스트 날리면 리스폰스가 잘 날아온다.
    retData = get_request_url(url)
    JsonData = json.loads(retData)

    if retData != None:
        Json_Data_Save(JsonData, "실시간_미세먼지_가장최근_데이터.json")
        return JsonData
    else:
        print("기상 데이터가 현재 비어있습니다. 저장되어 있던 자료로 분석하겠습니다.")
        JsonData = RealTime_Info_load("실시간_미세먼지_가장최근_데이터.json")
        return JsonData

def Get_RealTime_Weather_Info(date,time): # open API가 들어갈 부분.. 실시간 보다는 초단기예보 (+ 시간 보정)
    Access_Key = "iIhsixEf18XxhFwut8lRVPkptX44Z0E2kGCTBl8%2BBnOUU%2BNX5QoSpXcwZ1J14NbOB1s2cxLv9Uuf%2F%2FkjnHzysQ%3D%3D"
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + Access_Key
    parameters += "&base_date=" + date
    parameters += "&base_time=" + time ############ 06시 30분 발표(30분 단위) -매시각 45분 이후 호출
    parameters += "&numOfRows=" + "30" # 30개 데이터 동시에 긁어오게
    parameters += "&nx=" + "89" # 대구광역시 동구 신암4동의 x좌표
    parameters += "&ny=" + "91" # 대구광역시 동구 신암4동의 y좌표

    url= end_point + parameters
    retData = get_request_url(url)
    JsonData = json.loads(retData)

    if JsonData != None:
        if JsonData['response']['header']['resultMsg'] == 'OK':
            '''
            for item_key in (JsonData['response']['body']['items']['item']):
                if item_key['category']=='T1H':
                    item_key['category'] = '기온'
                    item_key['fcstValue'] = str(item_key['fcstValue']) + '도'
                elif item_key['category']=='RN1':
                    item_key['category'] = '1시간 강수량'
                    item_key['fcstValue'] = str(item_key['fcstValue']) +'mm' # 정확히는 범위를 나타낼 뿐 강수량은 각각 다르다.
                elif item_key['category'] =='REH':
                    item_key['category'] = '습도'
                    item_key['fcstValue'] = str(item_key['fcstValue']) + '%'
                elif item_key['category'] == 'PTY':
                    item_key['category'] = '강수형태'
                    if item_key['fcstValue'] == 0 : 
                        item_key['fcstValue'] = '맑음'
                    elif item_key['fcstValue'] == 1 :
                        item_key['fcstValue'] = '비'
            '''
            Json_Data_Save(JsonData,"초단기예보_가장최근_데이터.json")
            return JsonData
        else:
            print("기상데이터를 읽을 수 없는 상태입니다.")
            return None
    else:
        print("기상데이터가 현재 비어있습니다.")
        return None

def Smart_Mode():
    global g_AI_Mode, g_Date, g_Time, g_AI_Mode_ON_OFF_check
    print("1. 인공지능 모드 상태 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 네이버 실시간 검색어")
    print("4. 실시간 기상정보 Update")
    print("5. 실시간 대기정보 Update\n")
    menu_num = input("메뉴를 선택하세요 : ")

    if menu_num == '1': # 확인만
        Device_status("현재 인공지능 모드",g_AI_Mode)
    elif menu_num == '2': # 이게 켜지면 30분 간격으로 계속 데이터 수집해야함(자동 업데이트)
        g_AI_Mode = not g_AI_Mode
        Device_status("현재 인공지능 모드", g_AI_Mode) # 바꾼걸 바로 확인하자
        g_AI_Mode_ON_OFF_check = True
    elif menu_num == '3': # 네이버 실시간 검색어 순위를 보여줌
        Naver_Pop_Search_Word()
    elif menu_num == '4': # 수동으로 데이터를 수집해서 업데이트함 -> 제어까지 동시에
        g_Date,g_Time=Date_and_Time_Correction().split(',') # 시간 체크 및 보정
        weather_data=Get_RealTime_Weather_Info(g_Date,g_Time)
        print(weather_data)# 긁어온 원형 데이터 보여줌
    elif menu_num == '5':
        air_pollution_data=Get_RealTime_Air_Pollution_Info()
        print(air_pollution_data) # 긁어온 원형 데이터 보여줌
    else:
        print("잘못된 입력")

def Window_Simulator():
    exam_data = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "baseDate": 20180130,
                        "baseTime": 1130,
                        "category": "RN1",
                        "fcstDate": 20180130,
                        "fcstTime": 1200,
                        "fcstValue": 20,
                        "nx": 89,
                        "ny": 91
                    }
                ]
            },
            "numOfRows": 30,
            "pageNo": 1,
            "totalCount": 40
        },
        "header": {
            "resultCode": "0000",
            "resultMsg": "OK"
        }
    }
}
    global g_Balcony_Windows

    for item_key in exam_data['response']['body']['items']['item']:
        if item_key['category']=='RN1' : # 비오는지 안오는지 체크
            if item_key['fcstValue'] !=0: # 0이 아니면 1mm 이상 비가 온다
                g_Balcony_Windows= False
                Device_status("발코니(베란다)", g_Balcony_Windows, '열림', '닫김')
                break

def Humidifier_Simulator(): #
    exam_data = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "baseDate": 20180130,
                        "baseTime": 1130,
                        "category": "REH",
                        "fcstDate": 20180130,
                        "fcstTime": 1200,
                        "fcstValue": 20,
                        "nx": 89,
                        "ny": 91
                    }
                ]
            },
            "numOfRows": 30,
            "pageNo": 1,
            "totalCount": 40
        },
        "header": {
            "resultCode": "0000",
            "resultMsg": "OK"
        }
    }
}
    global g_humidifier

    for item_key in exam_data['response']['body']['items']['item']:
        if item_key['category']=='REH' :  # 습도재는 정보가 맞는지 체크
            if item_key['fcstValue'] <=30: # 겨울철 적정습도는 40%
                g_humidifier = True  # 가습기 켜자
                Device_status("가습기", g_humidifier)
                break

def Dehumidifier_Simulator():
    exam_data = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "baseDate": 20170830,
                        "baseTime": 1130,
                        "category": "REH",
                        "fcstDate": 20170830,
                        "fcstTime": 1400,
                        "fcstValue": 85,
                        "nx": 89,
                        "ny": 91
                    }
                ]
            },
            "numOfRows": 30,
            "pageNo": 1,
            "totalCount": 40
        },
        "header": {
            "resultCode": "0000",
            "resultMsg": "OK"
        }
    }
}
    global g_dehumidifier # 제습기

    for item_key in exam_data['response']['body']['items']['item']:
        if item_key['category']=='REH' :  # 습도재는 정보가 맞는지 체크
            if item_key['fcstValue'] >= 70: # 겨울철 적정습도는 40%
                g_dehumidifier = True  # 가습기 켜자
                Device_status("제습기", g_dehumidifier)
                break

def Fresh_Simulator(): # 상쾌한 날 시뮬
    exam_data ={
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "baseDate": 20170830,
                        "baseTime": 1130,
                        "category": "REH",
                        "fcstDate": 20170830,
                        "fcstTime": 1200,
                        "fcstValue": 50,
                        "nx": 89,
                        "ny": 91
                    }
                ]
            },
            "numOfRows": 30,
            "pageNo": 1,
            "totalCount": 40
        },
        "header": {
            "resultCode": "0000",
            "resultMsg": "OK"
        }
    }
    }
    global g_humidifier,g_dehumidifier

    for item_key in exam_data['response']['body']['items']['item']:
        if item_key['category']=='REH' :  # 습도재는 정보가 맞는지 체크
            if 30 < item_key['fcstValue'] < 70: # 겨울철 적정습도는 40%
                g_humidifier = False  # 가습기 꺼라
                g_dehumidifier = False  # 제습기 꺼라
                Device_status("가습기", g_dehumidifier)
                Device_status("제습기", g_dehumidifier)
                break

def Simulator():
    print("\n1. 비 오는 날 시뮬레이션 (발코니창 제어)")
    print("2. 습한 날 시뮬레이션 (제습기 제어)")
    print("3. 건조한 날 시뮬레이션 (가습기 제어)")
    print("4. 상쾌한 날 시뮬레이션 (제습기/가습기 제어)\n")

    line_beautifully = True
    menu_num = input("메뉴를 선택하세요 : ")
    if menu_num == '1': # 강수예보 시뮬
        Window_Simulator()
    elif menu_num == '2':
        Dehumidifier_Simulator()
    elif menu_num == '3':
        Humidifier_Simulator()
    elif menu_num == '4':
        Fresh_Simulator()
    else:
        print("잘못된 입력")
        line_beautifully = False
    if line_beautifully == True:
        print()

def terminate_thread(thread):
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res= ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SEtAsyncExc failed")

def my_thread_terminate():
    while ai_thread.is_alive():
        try:
            terminate_thread(ai_thread)
        except:
            pass

ai_thread = threading.Thread(target=update_scheduler)
ai_thread.daemon = True  # 메인이 종료되면 따라 끝나겠다는 뜻
ai_thread.start()

while True:
    Print_Main_Menu()
    menu_num = input("메뉴를 선택하세요. : ")

    if g_AI_Mode==False & g_AI_Mode_ON_OFF_check==True:
        my_thread_terminate()
        g_AI_Mode_ON_OFF_check=False
        ai_thread = threading.Thread(target=update_scheduler)
        ai_thread.daemon = True  # 메인이 종료되면 따라 끝나겠다는 뜻
        ai_thread.start()

    current_time = datetime.datetime.now()

    if menu_num == '1': # 장비 상태 확인
        Check_Device_Status()
    elif menu_num == '2': # 장비 제어(수동)
        Control_Device_Manual()
    elif menu_num == '3': # 스마트 모드
        Smart_Mode()
    elif menu_num == '4': # 시뮬레이션 모드
        Simulator()
    elif menu_num == '5': # 종료
        break
    else:
        print("잘못된 입력")