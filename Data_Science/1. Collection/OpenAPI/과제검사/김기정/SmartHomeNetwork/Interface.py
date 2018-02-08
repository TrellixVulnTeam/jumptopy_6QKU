
def output_humidity():
    data_list = []
    import GetWeatherInfo
    weather_data = GetWeatherInfo.main()
    for data in weather_data:
        if data.get("category") == "REH":
            data_list.append(data.get("fcstValue"))
    return data_list[0]

def output_temperature():
    data_list = []
    import GetWeatherInfo
    weather_data = GetWeatherInfo.main()
    for data in weather_data:
        if data.get("category") == "T1H":
            data_list.append(data.get("fcstValue"))
    return data_list[0]

def main_interface():
    print("┌"+"─"*17+"┐" + "\t" * 6 +  "─" * 20 + "\t" + "┌" + "─" * 2 +"┐" + "║".rjust(42))
    print("│"+ "                 │" + "\t" * 5 + "／" + "\t" * 6 + "  ＼" + "│" + "  │"+ "║".rjust(42))
    print("│"+" 1. 장비수동제어 "+"│"+ "\t" * 4 + " ／" + "\t" * 8 + " ＼" + "│" + "║".rjust(42))
    print("│"+" 2. 인공지능모드 "+"│"+ "\t" * 3 + "  ／" + "\t"*3 + "☀"+ "\t"* 3+" ☔"+"\t" * 3 +"＼" + "║".rjust(40))
    print("│"+" 3. 미세먼지확인 "+"│" + "\t" * 2 + "   ／" + "\t" * 3 + " " + str(output_temperature()) +"°C"+ "\t"*3 + str(output_humidity())+"%"+"\t"* 3 +"   ＼" + "║".rjust(37))
    print("│"+" 4. 오늘의 추천 "+" │"+ "║".rjust(91))
    print("│"+" 5. 종료 "+"        │"+ "║".rjust(91))
    print("│"+ "                 │"  + "║".rjust(91))
    print("┖"+"─"*17+"┘"+ "║".rjust(91))

def control_device_interface():
    print("1. 가습기")
    print("2. 제습기")
    print("3. 공기청정기")
    print("4. 보일러")
    print("5. 에어컨")
    print("6. 창문")
    print("7. 뒤로가기")

def smart_mode_interface():
    print("=" * 50)
    print("1. 인공지능 모드 상태 확인")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print("4. 뒤로가기")
    print("=" * 50)

