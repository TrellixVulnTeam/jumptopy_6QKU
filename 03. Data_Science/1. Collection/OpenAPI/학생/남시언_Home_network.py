import urllib.request
import datetime
import json
import threading
# HK Comment] 공통 사항
# 1. 변수명은 최대한 가독성 높게 (나쁜 예: dt ..)
# 2. 실시간 Update 할 떄나 인공지능 모드에 의해서 Scheduling 작업시 기상정보 가져온후
#    발코니창이 문닫는 조건이 된다면 문 닫는 로직 추가
# 시뮬레이션 데이터는 필요한 데이터만 저장하던지 아니면 실제 response 데이터를 조작하던지 할것
# 실시간 기상 정보 Update하면 장비제어와 관련된 기상정보는 따로 출력한다.

# 실제 홈네트워크 시스템처럼 한번 가동되면 꺼지지 않게.( 따라서 재시작에 대한 고려는 일단 X)
g_Radiator = False # 전역변수 지역변수 변수명에 표시( 회사에서 꼭 쓴다고 함. )
g_Gas_Valve = False
g_Balcony_Windows = False # 건축법 시행령에 따라 베란다가 아닌 폐쇄형 발코니가 정확한 표현
g_Door = False # 출입문
g_humidifier = False # 가습기
g_dehumidifier = False # 제습기
g_AI_Mode = False
g_Date="20180101"
g_Time="0600"

def update_scheduler():
    check_45min_fir_exec = False  # Flag => first_45_start_flag
    while True:
        if g_AI_Mode == True:  # 매~시 45분에 1시간 간격으로 데이터 읽기!
            global g_Balcony_Windows, g_Date, g_Time
            current_time = datetime.datetime.now()  # HK Comment] 시간 보정 필요 없음
            # time.sleep(3600)

            if current_time.minute == 45 & check_45min_fir_exec == False:  # 45분이고 초와 시간이 다르면.. 45분을 기준으로 1시간이 됐을 것이다?
                weather_data = Get_RealTime_Weather_Info(g_Date, g_Time)  # 45분으로 리퀘스트 날려도 찰떡같이 30분으로 준다
                Auto_Control_Window(weather_data)  # 창문제어
                Auto_Control_Humidifier(weather_data)  # 가습기제어
                Auto_Control_Dehumidifier(weather_data)  # 제습기제어
                check_45min_fir_exec = True
            if current_time.minute != 45:
                check_45min_fir_exec = False

def Print_Main_Menu():
    print("1. 기기 상태 확인")
    print("2. 기기 제어")
    print("3. 스마트 모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료\n")

def Device_status(Device, Devcie_Status, ON_message='작동', OFF_message='정지'):
    print("%s 상태: " % Device, end="")
    if Devcie_Status == True:
        print(ON_message)
    elif Devcie_Status == False:
        print(OFF_message)

def Check_Device_Status():
    print()
    Device_status('난방기', g_Radiator)  # 전역변수를 함수 파라미터로 사용했지만 값의 변경은 없으므로.
    Device_status('가스밸브', g_Gas_Valve, '열림', '잠김')
    Device_status('발코니(베란다) 창문', g_Balcony_Windows, '열림', '닫김')
    Device_status('출입문', g_Door, '열림', '닫김')
    Device_status('가습기', g_humidifier)
    Device_status('제습기', g_dehumidifier)
    print()

def Print_Device_Menu():
    print("상태 변경할 기기를 선택하세요")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다) 창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기\n")

def Control_Device_Manual():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_humidifier, g_dehumidifier
    Check_Device_Status()
    Print_Device_Menu()
    menu_num = input("번호를 입력하세요 : ")
    status_change_true = True

    if menu_num == '1':
        g_Radiator = not g_Radiator
    elif menu_num == '2':
        g_Gas_Valve = not g_Gas_Valve
    elif menu_num == '3':
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == '4':
        g_Door = not g_Door
    elif menu_num == '5':
        g_humidifier = not g_humidifier  # 가습기
    elif menu_num == '6':
        g_dehumidifier = not g_dehumidifier  # 제습기
    else:
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

def Date_and_Time_Correction():  # HK Comment] 시간 보정은 사용자가 원할 경우에만 하도록 변경
    global g_Date, g_Time
    current_time = datetime.datetime.now()
    g_Date = str(current_time.year) + str(current_time.month).zfill(2) + str(current_time.day).zfill(2)

    if current_time.minute < 45:  # n시 0~44분 -> n-1시 30분으로 처리
        g_Time = str(current_time.hour - 1).zfill(2) + str(30)
        if current_time.hour == 0 :
            g_Date = str(current_time.year) + str(current_time.month).zfill(2) + str(current_time.day-1).zfill(2)
            g_Time = str(23) + str(30)
    else:
        g_Time = str(current_time.hour).zfill(2) + str(current_time.minute).zfill(2)
    # 시간보정에서 0시 정각인 경우 전날의 23시대로 바꾸고 전날로 넘어갔는데 달이 바뀌거나 년도가 바뀌는 경우에 대한 처리 X
    # 이런 경우 저장해놓은 데이터를 읽어서 처리?
    print("단기예보에 등록된 데이터를 읽기 위해 %s시 %s분으로 보정되었습니다 " % (g_Time[:2], g_Time[2:]))
    return g_Date+","+g_Time

def Short_term_forecast_save(Json_Data, File_name):
    with open(File_name, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(Json_Data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def Auto_Control_Window(Json_Data):
    global g_Balcony_Windows
    rain_flag = False
    for i in range(len(Json_Data['response']['body']['items']['item'])):
        if Json_Data['response']['body']['items']['item'][i]['category'] == 'RN1':  # 강수형태= PTY
            if 0 != Json_Data['response']['body']['items']['item'][i]['fcstValue']:
                rain_flag = True  # 창문닫는 작업, 맑은 날씨가 아닌것으로 예상되는 시간이 1시간이라도 있다면
                break

    if rain_flag == True:  # 비온다
        g_Balcony_Windows = False
    else:  # 비 안온다
        g_Balcony_Windows = True

def Auto_Control_Humidifier(Json_Data):
    global g_humidifier
    high_humidity = False
    for i in range(len(Json_Data['response']['body']['items']['item'])):
        if Json_Data['response']['body']['items']['item'][i]['category'] == 'REH':  # 습도재는 데이터가 있다면
            if Json_Data['response']['body']['items']['item'][i]['fcstValue'] <= 30:
                high_humidity = True  # 가습기 틀어야 되겠네
                break

    if high_humidity == True:
        g_humidifier = True
    else:
        g_humidifier = False

def Auto_Control_Dehumidifier(Json_Data):
    global g_dehumidifier
    low_humidity = False
    for i in range(len(Json_Data['response']['body']['items']['item'])):
        if Json_Data['response']['body']['items']['item'][i]['category'] == 'REH':
            if Json_Data['response']['body']['items']['item'][i]['fcstValue'] >= 70:
                low_humidity = True
                break

    if low_humidity == True:
        g_dehumidifier = True
    else:
        g_dehumidifier = False

def Get_RealTime_Weather_Info(date, time):  # open API가 들어갈 부분
    Access_Key = "iIhsixEf18XxhFwut8lRVPkptX44Z0E2kGCTBl8%2BBnOUU%2BNX5QoSpXcwZ1J14NbOB1s2cxLv9Uuf%2F%2FkjnHzysQ%3D%3D"
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + Access_Key
    parameters += "&base_date=" + date
    parameters += "&base_time=" + time  ############ 06시 30분 발표(30분 단위) -매시각 45분 이후 호출
    parameters += "&numOfRows=" + "30"  # 30개 데이터 동시에 긁어오게
    parameters += "&nx=" + "89"  # 대구광역시 동구 신암4동의 x좌표
    parameters += "&ny=" + "91"  # 대구광역시 동구 신암4동의 y좌표

    url = end_point + parameters
    retData = get_request_url(url)
    JsonData = json.loads(retData)

    if JsonData != None:
        if JsonData['response']['header']['resultMsg'] == 'OK':
            Short_term_forecast_save(JsonData, "초단기예보_가장최근_데이터.json")
            return JsonData
        else:
            print("허용된 요청 초과로 기상데이터를 읽을 수 없는 상태입니다.")
            return None

def Smart_Mode():
    global g_AI_Mode, g_Date, g_Time
    print("1. 인공지능 모드 상태 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update\n")
    menu_num = input("메뉴를 선택하세요 : ")

    if menu_num == '1':  # 확인만
        Device_status("현재 인공지능 모드", g_AI_Mode)
    elif menu_num == '2':  # 이게 켜지면 30분 간격으로 계속 데이터 수집해야함(자동 업데이트)
        g_AI_Mode = not g_AI_Mode
        Device_status("현재 인공지능 모드", g_AI_Mode)  # 바꾼걸 바로 확인하자
    elif menu_num == '3':  # 수동으로 데이터를 수집해서 업데이트함 -> 제어까지 동시에
        g_Date, g_Time = Date_and_Time_Correction().split(",")  # 시간 체크 및 보정
        weather_data = Get_RealTime_Weather_Info(g_Date, g_Time)
        ##########################################################################################
        # 강수량, 습도 등에 대한 정보를 따로 보여주고 원형을 보여줘라
        ##########################################################################################
        print(weather_data)  # 긁어온 원형 데이터 보여줌
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

    for i in range(len(exam_data['response']['body']['items']['item'])):
        if exam_data['response']['body']['items']['item'][i]['category']=='RN1': # 비오는지 안오는지 체크
            if exam_data['response']['body']['items']['item'][i]['fcstValue'] != 0: # 0이 아니면 1mm 이상 비가 온다
                g_Balcony_Windows= False # 창문 꼭 닫자
                Device_status("발코니(베란다)",g_Balcony_Windows,'열림','닫김')
                break

    Short_term_forecast_save(exam_data,"비오는날_시뮬레이션.json")

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

    for i in range(len(exam_data['response']['body']['items']['item'])):
        if exam_data['response']['body']['items']['item'][i]['category'] == 'REH':  # 습도재는 정보가 맞는지 체크
            if exam_data['response']['body']['items']['item'][i]['fcstValue'] <= 30:  # 겨울철 적정습도는 40%
                g_humidifier = True  # 가습기 켜자
                Device_status("가습기", g_humidifier)
                break

    Short_term_forecast_save(exam_data, "건조한_날_시뮬레이션.json")

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

    for i in range(len(exam_data['response']['body']['items']['item'])):
        if exam_data['response']['body']['items']['item'][i]['category'] == 'REH':  # 습도재는 정보가 맞는지 체크
            if exam_data['response']['body']['items']['item'][i]['fcstValue'] >= 70:  # 여름철 적정습도는 60%
                g_dehumidifier = True  # 제습기 켜자
                Device_status("제습기", g_dehumidifier)
                break

    Short_term_forecast_save(exam_data, "습한_날_시뮬레이션.json")

def Fresh_Simulator(): # 상쾌한 날 시뮬
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

    for i in range(len(exam_data['response']['body']['items']['item'])):
        if exam_data['response']['body']['items']['item'][i]['category'] == 'REH':  # 습도재는 정보가 맞는지 체크
            if 30 < exam_data['response']['body']['items']['item'][i]['fcstValue'] < 70:  # 습도가 31~69%라면
                g_humidifier = False  # 가습기 꺼라
                g_dehumidifier = False  # 제습기 꺼라
                Device_status("가습기", g_dehumidifier)
                Device_status("제습기", g_dehumidifier)
                break

    Short_term_forecast_save(exam_data, "상쾌한_날_시뮬레이션.json")

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

ai_thread = threading.Thread(target=update_scheduler)
ai_thread.daemon = True
ai_thread.start()

while True:
    Print_Main_Menu()
    menu_num = input("메뉴를 선택하세요. : ")

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