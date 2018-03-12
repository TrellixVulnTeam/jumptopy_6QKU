import json
import sys
import os
import time
import webbrowser
from SmartHomeNetwork import Interface, ControlDevice, SearchProgram, SaveJsonFile,GetPollutionInfo
from SmartHomeNetwork import SecurityProgram
from SmartHomeNetwork.SecurityProgram import password_list


g_Humidifier = False  # 가습기
g_Dehumidifier = False # 제습기
g_Air_Purifier = False # 공기청정기
g_Radiator = False # 보일러
g_Air_Conditioner = False # 에어컨
g_Balcony_Windows = False # 창문
g_AI_Mode = False # 04. AI 모드

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def loading():
    _print('■ ■ ■ ■ ■')
    time.sleep(0.5)
    _print(' ■ ■ ■ ■ ■')
    time.sleep(0.5)
    _print(' ■ ■ ■ ■ ■')
    time.sleep(0.5)
    _print(' 👌')
    time.sleep(0.5)
    print("")

def check_device_status():
    print("")
    ControlDevice.print_device_status('가습기', g_Humidifier)
    ControlDevice.print_device_status('제습기', g_Dehumidifier)
    ControlDevice.print_device_status('공기청정기', g_Air_Purifier)
    ControlDevice.print_device_status('난방기',g_Radiator)
    ControlDevice.print_device_status('에어콘', g_Air_Conditioner)
    ControlDevice.print_window_status('발코니(베란다) 창문', g_Balcony_Windows)

def control_device():
    while True:
        global g_Humidifier, g_Dehumidifier, g_Air_Purifier, g_Radiator, g_Air_Conditioner, g_Balcony_Windows
        menu_num = int(input("번호를 입력하세요: "))
        if menu_num == 1: g_Humidifier = not g_Humidifier
        elif menu_num == 2: g_Dehumidifier = not g_Dehumidifier
        elif menu_num == 3: g_Air_Purifier = not g_Air_Purifier
        elif menu_num == 4: g_Radiator = not g_Radiator
        elif menu_num == 5: g_Air_Conditioner = not g_Air_Conditioner
        elif menu_num == 6: g_Balcony_Windows = not g_Balcony_Windows
        elif menu_num == 7: break
        else:
            print("잘못 입력하셨습니다")
        check_device_status()
        return None

def smart_mode():
    while True:
        global  g_AI_Mode
        Interface.smart_mode_interface()
        if menu_num == 1:
            print("")
            print("현재 인공지능 모드: ", end="")
            if g_AI_Mode == True:
                print("작동")
                break
            else:
                print("정지")
                break
        elif menu_num == 2:
            g_AI_Mode = not g_AI_Mode
            print("")
            print("현재 인공지능 모드: ", end="")
            if g_AI_Mode == True:
                print("작동")
                print("")
                print("실시간 기상 정보 로딩 중")
                loading()
                print("기상 정보에 따른 디바이스 조정 중")
                loading()
                print("")
                try:
                    print("=" * 125)
                    SaveJsonFile.auto_save_weatherinfo()
                    SaveJsonFile.auto_save_pollutioninfo()
                    smart_mode_Balcony()
                    smart_mode_de_hu()
                    smart_mode_purifier()
                    print("=" * 125)
                    break
                except FileNotFoundError:
                    SaveJsonFile.auto_save_weatherinfo()
                    SaveJsonFile.auto_save_pollutioninfo()
                    print("=" * 125)
                    smart_mode_Balcony()
                    smart_mode_de_hu()
                    smart_mode_purifier()
                    print("=" * 125)
                    break
            else:
                print("정지")
                print("")
        elif menu_num == 3:
            SaveJsonFile.auto_save_weatherinfo()
            SaveJsonFile.auto_save_pollutioninfo()
            print("업데이트에 따른 디바이스 조정 중")
            loading()
            print("")
            if g_AI_Mode == True:
                print("=" * 125)
                smart_mode_Balcony()
                smart_mode_de_hu()
                smart_mode_purifier()
                print("=" * 125)
                break
            elif g_AI_Mode == False:
                print("04. AI 모드가 꺼져있어 디바이스를 조정할수없습니다.")
                break
        elif menu_num == 4:
            break

def smart_mode_Balcony():
    global g_Balcony_Windows
    weather_data = SaveJsonFile.auto_load_weatherinfo()
    pollution_data = SaveJsonFile.auto_load_pollutioninfo()
    value = 0
    category_count = 0
    for total_data in weather_data:
        if total_data.get("category") == "PTY":
            category_count += 1
            value += total_data.get("fcstValue")
    if value/category_count > 0:
        if g_Balcony_Windows == True:
            print("비가 예상됩니다. 창문을 닫겠습니다")
            g_Balcony_Windows = False
    elif value/category_count == 0:
        for data in pollution_data:
            if int(data.get("pm10Grade")) <= 2:
                if g_Balcony_Windows == False:
                    print("날씨가 계속 맑은 예정입니다. 창문을 열겠습니다")
                    g_Balcony_Windows = True
            elif int(data.get("pm10Grade")) > 2:
                if g_Balcony_Windows == True:
                    print("미세먼지가 많습니다. 창문을 닫겠습니다")
                    g_Balcony_Windows = False

def smart_mode_de_hu():
    global g_Humidifier, g_Dehumidifier
    weather_data = SaveJsonFile.auto_load_weatherinfo()
    for total_data in weather_data:
        if total_data.get("category") == "REH":
            if total_data.get("fcstValue") <= 30:
                if g_Humidifier == False:
                    print("실내가 건조합니다. 가습기를 작동합니다 ")
                    g_Humidifier = True
                elif g_Dehumidifier == True:
                    print("실내가 건조합니다 제습기를 중지합니다")
                    g_Dehumidifier = False
                break

            elif total_data.get("fcstValue") >= 70:
                if g_Dehumidifier == False:
                    print("실내가 습합니다. 제습기를 작동합니다")
                    g_Dehumidifier = True
                elif g_Humidifier == True:
                    print("실내가 건조합니다 가습기를 중지합니다")
                    g_Humidifier = False
                break

            elif 30 < total_data.get("fcstValue") < 70:
                print("")
                print("쾌적한 환경입니다. 제,가습기를 가동하지 않아도 됩니다.")
                print("")
                break

def smart_mode_purifier():
    global g_Air_Purifier
    pollution_data = SaveJsonFile.auto_load_pollutioninfo()
    for data in pollution_data:
        if float(data.get("so2Value")) > 0.05 or float(data.get("coValue")) > 9 or float(data.get("o3Value")) > 0.09 or float(data.get("no2Value")) > 0.06 or int(data.get("pm10Value")) > 50 or int(data.get("pm25Value")) > 25:
            if g_Air_Purifier == False:
                print("오염수치가 높습니다. 공기청정기를 작동합니다")
                g_Air_Purifier = True
        else:
            if g_Air_Purifier == True:
                print("오염수치가 낮습니다. 공기청정기를 작동하지않습니다")
                g_Air_Purifier = False

def data_graph(value):
    if value == "1":
        return ("■ □ □ □ □" , "😍" , "최고")
    elif value == "2":
        return ("■ ■ □ □ □" , "😊" , "좋음")
    elif value == "3":
        return ("■ ■ ■ □ □" , "😔" , "보통")
    elif value == "4":
        return ("■ ■ ■ ■ □" , "😡" , "나쁨")
    elif value == "5":
        return ("■ ■ ■ ■ ■" , "😷" , "최악")

def pollution_data_to_graph():
    pollution_data = GetPollutionInfo.main()
    print("")
    print("미세먼지", data_graph(pollution_data[0].get("pm10Grade")))
    print("초미세먼지", data_graph(pollution_data[0].get("pm25Grade")))
    print("일산화탄소" , data_graph(pollution_data[0].get("coGrade")))
    print("이산화질소", data_graph(pollution_data[0].get("no2Grade")))
    print("아황산가스", data_graph(pollution_data[0].get("so2Grade")))
    print("오존", data_graph(pollution_data[0].get("o3Grade")))
    print("")


dir_name = time.strftime("%m%d", time.localtime(time.time()))
dir_weather = "weather"
dir_pollution = "pollution"
dir_movie = "movie"
file_delimeter = "//"

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)
if not os.path.isdir(dir_name + file_delimeter + dir_weather):
    os.mkdir(dir_name + file_delimeter + dir_weather)
if not os.path.isdir(dir_name + file_delimeter + dir_pollution):
    os.mkdir(dir_name + file_delimeter + dir_pollution)
if not os.path.isdir(dir_name + file_delimeter + dir_movie):
    os.mkdir(dir_name + file_delimeter + dir_movie)

SecurityProgram.mainloop()
password = ("".join([num for num in password_list]))
if password == "1111":
    print("")
    print("<<비밀번호 인증에 성공하셨습니다>>".center(85))
    print("")
    while True:
        print("▣"*110)
        Interface.main_interface()
        print("▣"*110)
        main_menu = int(input("→"))
        if main_menu == 1:
            loading()
            check_device_status()
            control_device()

        elif main_menu == 2:
            loading()
            Interface.smart_mode_interface()
            menu_num = int(input("메뉴를 선택하세요: "))
            smart_mode()

        elif main_menu == 3:
            loading()
            print("\n<<오늘의 미세먼지 지수입니다>>")
            pollution_data_to_graph()

        elif main_menu == 4:
            loading()
            print("")
            print("="*125)
            print("현재 인기있는 영화 리스트입니다")
            SearchProgram.get_movie_top_list()
            print("=" * 125)
            print("검색하고 싶은 영화를 입력하세요")
            movie_name = str(input(">>"))
            SearchProgram.get_movie_info(movie_name)
            print("영화를 예매 하시겠습니까?\nyes=1,no=2")
            menu_num = int(input(">>"))
            if menu_num == 1:
                url = "http://ticket.movie.naver.com/Ticket/Reserve.aspx"
                webbrowser.open(url)
            elif menu_num == 2:
                break

        elif main_menu == 5:
            break

        else:
            print("잘못 입력하셨습니다")
else:
    print("")
    print("<<비밀번호 인증에 실패하셨습니다>>".center(85))