#HKComment] 다른 PC 환경에서 인터페이스 이식성 확인해 볼것
from bs4 import BeautifulSoup
import os
import sys
import urllib.request
import threading
import datetime
import time
import json
import delivary_tracking
import ctypes

os.system("mode con cols=100 lines=50")

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_mode = False
g_humidifier = False
g_dehumidifier = False
g_aircleaner = False
g_heater = False
g_delivary_alarm = False

access_key="PUjPcu22uUk09DaNdDl6mkVTDoMG2QJWGhxwAeQVqybmmJfBDw%2F2kb0ziRxy0smbezEH77TXCv%2BfCYGP7OkDfw%3D%3D"


def cls(n=0):
    if n == 0:
        os.system('cls')
    else:
        sys.stdout.write('\b' * n)

def display(a):
    sys.stdout.write(a)
    return len(a)

def terminate_thread(thread):
    """Terminates a python thread from another thread.
    :param thread: a threading.Thread instance
    """
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def my_thread_terminate():
    while t.is_alive():
        try:
            terminate_thread(t)
        except:
            pass

def get_request_url(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        return response.read().decode('utf-8')
    else:print("접속안대...")

def realtime_weather_info():
    global time1

    end_point='http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData'

    times = datetime.datetime.now()
    if int(times.strftime('%M')) < 45:
        time1 = times+datetime.timedelta(minutes=-30)
    elif int(times.strftime('%M')) >= 45:
        time1 = times
    parameters = "?&_type=json&serviceKey="+access_key
    parameters += '&base_date=' + times.strftime("%Y%m%d")
    parameters += '&base_time='+ time1.strftime('%H%M')
    parameters += '&nx='+ str(89)
    parameters += '&ny='+ str(91)
    parameters += '&numOfRows='+str(100)

    url=end_point+parameters
    retData = get_request_url(url)

    if(retData == None):return None
    else:return json.loads(retData)

def realtime_dust_info():

    end_point='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

    parameters = "?serviceKey="+access_key
    parameters +="&sidoName="+ urllib.request.quote('대구')
    parameters +='&ver='+'1.3'
    parameters += '&numOfRows='+str(100)

    url=end_point+parameters
    retData = get_request_url(url)
    soup = BeautifulSoup(retData, 'lxml')

    if(retData == None):return None
    else: return soup

def main():
    global g_Balcony_Windows,g_humidifier,g_dehumidifier,g_aircleaner
    global jsonResult

    jsonResult = {}
    jsonData = realtime_weather_info()
    soup = realtime_dust_info()
    if int(datetime.datetime.now().strftime('%M')) < 30:
        hours = time1 + datetime.timedelta(hours=2)
    elif int(datetime.datetime.now().strftime('%M')) >= 30:
        hours = time1 + datetime.timedelta(hours=1)

    after_hour = hours.strftime("%H") + '00'
    for i in jsonData['response']['body']['items']['item']:
        if after_hour == str(i['fcstTime']):
            jsonResult['예측시간'] = str(i['fcstTime'])[:2] + ':' + str(i['fcstTime'])[2:]
            if i['category'] =='LGT':
                jsonResult['낙뢰'] =i['fcstValue']
            elif i['category'] == 'PTY':
                jsonResult['강수형태'] = i['fcstValue']
            elif i['category'  ] == 'RN1':
                jsonResult['1시간강수량'] = i['fcstValue']
            elif i['category'] =='SKY':
                jsonResult['하늘상태'] = i['fcstValue']
            elif i['category'] == 'T1H':
                jsonResult['기온'] = i['fcstValue']
            elif i['category'] == 'REH':
                jsonResult['습도'] = i['fcstValue']

    dust_info = {}
    dust_data = soup.find_all('item')
    for i in dust_data:
        if list(i.strings)[1] == '신암동':
            dust_info['측정시간'] = list(i.strings)[5]
            dust_info['측정위치'] =list(i.strings)[1]
            dust_info['미세먼지'] = list(i.strings)[-2]
            dust_info['초미세먼지'] = list(i.strings)[-4]
    jsonResult['미세먼지정보'] = dust_info


    print()
    print('{0:^95}'.format("<< 날씨 예보 정보 >>"))
    for i in list(jsonResult.items()):
        if i[0] != '미세먼지정보':
            print('\t\t\t\t          %s : %s'%(i[0],str(i[1])))
    print()
    print('{0:^95}'.format("<< 미세먼지 정보 >>"))
    for i in list(jsonResult['미세먼지정보'].items()):
        print('\t\t\t\t     %s : %s' % (i[0], str(i[1])))

    with open('Home_Network_Data/기상정보&미세먼지정보_업데이트.json','w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(readable_result)
        print('\n'+'{0:^78}'.format('[기상정보&미세먼지정보_업데이트.json] 저장되었습니다.'))

    if  os.path.isfile('Home_Network_Data/배송정보.txt'):
        delivary_tracking.read_code()
        delivary_tracking.total_delivery()
        delivary_tracking.save_delivary()
        print('\n\t\t\t\t[최신배송상태 추적.json] 저장되었습니다.')
    else :
        print('\n\t\t    택배 알리미를 이용하기위해서는 우선 배송정보를 등록해주세요.')
        delivary_tracking.delivary_main()

    print('\n\t\t\t\t       업데이트를 완료했습니다.')

    # if int(jsonResult['강수형태']) > 0:
    #     if g_Balcony_Windows == False:
    #         g_Balcony_Windows = True
    #         print("\n<< 예상 강수형태[%s] 30분 내로 비 겁나 온다네요...문을 닫습니당 >>"%jsonResult['강수형태'])
    #     else: pass
    # elif int(jsonResult['강수형태']) ==0:
    #     if g_Balcony_Windows == True:
    #         g_Balcony_Windows = False
    #
    # if int(jsonResult['습도']) < 45:
    #     if g_humidifier == False:
    #         g_humidifier = True
    #         print("\n<< 예상습도[%s%%] 습도가 낮을거라네요... 가습기를 켭니다 >>"%jsonResult['습도'])
    #     if g_dehumidifier == True:
    #         g_dehumidifier = False
    #
    # elif int(jsonResult['습도']) > 55 :
    #     if g_dehumidifier == True:
    #         g_dehumidifier = False
    #         print('\n<< 예상습도[%s%%] 습도가 높을거라네요... 제습기를 켭니다 >>'%jsonResult['습도'])
    #     if g_humidifier == True:
    #         g_humidifier = False
    #
    # elif 45 <= int(jsonResult['습도']) <= 55:
    #     print('\n<< 예상습도[%s%%] 쾌적할거 같습니다 >>' % jsonResult['습도'])
    #
    # if int(jsonResult['미세먼지정보']['미세먼지']) > 2 or int(jsonResult['미세먼지정보']['초미세먼지']) > 2:
    #     if g_aircleaner == False:
    #         g_aircleaner = True
    #         print('\n<< 미세먼지[%s],초미세먼지[%s] 미세먼지 지수가 높습니다 공기청정기를 켭니다 >>'%(jsonResult['미세먼지정보']['미세먼지'],jsonResult['미세먼지정보']['초미세먼지']))
    #     else: pass
    # elif int(jsonResult['미세먼지정보']['미세먼지']) or int(jsonResult['미세먼지정보']['초미세먼지']) <= 2:
    #     if g_aircleaner == True:
    #         g_aircleaner = False
    #     if g_Balcony_Windows == True:
    #         g_Balcony_Windows = False

def main2():
    global g_Balcony_Windows,g_humidifier,g_dehumidifier,g_delivary_alarm,g_aircleaner
    global jsonResult

    jsonResult = {}
    jsonData = realtime_weather_info()
    soup = realtime_dust_info()

    if int(datetime.datetime.now().strftime('%M')) < 30:
        hours = time1 + datetime.timedelta(hours=2)
    elif int(datetime.datetime.now().strftime('%M')) >= 30:
        hours = time1 + datetime.timedelta(hours=1)
    after_hour = hours.strftime("%H") + '00'

    for i in jsonData['response']['body']['items']['item']:

        if after_hour == str(i['fcstTime']):
            if i['category'] == 'LGT':
                jsonResult['낙뢰'] = i['fcstValue']
            elif i['category'] == 'PTY':
                jsonResult['강수형태'] = i['fcstValue']
            elif i['category'] == 'RN1':
                jsonResult['1시간강수량'] = i['fcstValue']
            elif i['category'] == 'SKY':
                jsonResult['하늘상태'] = i['fcstValue']
            elif i['category'] == 'T1H':
                jsonResult['기온'] = i['fcstValue']
            elif i['category'] == 'REH':
                jsonResult['습도'] = i['fcstValue']
        jsonResult['예측시간'] = str(i['fcstTime'])[:2] + ':' + str(i['fcstTime'])[2:]

    dust_info = {}
    dust_data = soup.find_all('item')
    for i in dust_data:
        if list(i.strings)[1] == '신암동':
            dust_info['측정시간'] = list(i.strings)[5]
            dust_info['측정위치'] = list(i.strings)[1]
            dust_info['미세먼지'] = list(i.strings)[-2]
            dust_info['초미세먼지'] = list(i.strings)[-4]
    jsonResult['미세먼지정보'] = dust_info

    with open('Home_Network_Data/기상정보&미세먼지정보_업데이트.json', 'w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

    if int(jsonResult['강수형태']) > 0:
        if g_Balcony_Windows == False:
            g_Balcony_Windows = True
            delivary_tracking.speaker("비가 올 예정입니다. 발코니창을 닫겠습니다.")
        else:delivary_tracking.speaker("비가 올 예정입니다. 발코니창은 닫혀 있습니다.")
    if int(jsonResult['강수형태']) == 0:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass
    #가습
    if int(jsonResult['습도']) < 45:
        if g_humidifier == False:
            g_humidifier = True
            delivary_tracking.speaker("예상습도는 %s%% 입니다. 건조할것 같네요. 가습기가 작동됩니다." % jsonResult['습도'])
        else :delivary_tracking.speaker("예상습도는 %s%% 입니다. 가습기가 이미 가동중입니다."%jsonResult['습도'])
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass
        if g_dehumidifier == True:
            g_dehumidifier = False


    elif int(jsonResult['습도']) > 55:
        if g_dehumidifier == False:
            g_dehumidifier = True
            delivary_tracking.speaker("예상습도는 %s%% 입니다. 축축할거 같네요. 제습기가 작동됩니다." % jsonResult['습도'])
        else:delivary_tracking.speaker("예상습도는 %s%% 입니다. 제습기가 이미 가동중입니다."%jsonResult['습도'])
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass
        if g_humidifier == True:
            g_humidifier = False

    if int(jsonResult['미세먼지정보']['미세먼지']) > 2 or int(jsonResult['미세먼지정보']['초미세먼지']) > 2:
        if g_aircleaner == False:
            g_aircleaner = True
            delivary_tracking.speaker("현재 미세먼지 수치는 %s이고, 초미세먼지 수치는%s 입니다. 기관지에 안좋을거 같네요. 창문을 닫고 공기청정기가 작동됩니다." % (
            jsonResult['미세먼지정보']['미세먼지'], jsonResult['미세먼지정보']['초미세먼지']))

        else :delivary_tracking.speaker("현재 미세먼지 수치는 %s이고, 초미세먼지 수치는%s 입니다. 공기청정기가 이미 작동중입니다." % (
            jsonResult['미세먼지정보']['미세먼지'], jsonResult['미세먼지정보']['초미세먼지']))
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False

    elif int(jsonResult['미세먼지정보']['미세먼지']) or int(jsonResult['미세먼지정보']['초미세먼지']) <= 2:
        if g_aircleaner == True:
            g_aircleaner = False

    g_delivary_alarm = True
    try:delivary_tracking.smart_delivary_speaker()
    except:
        delivary_tracking.speaker("스마트모드 택배 알리미를 이용하기 위해서는 우선 배송정보를 입력해주셔야 해요.")
        g_delivary_alarm = False


def realtime_check():
    global  jsonResult,g_Balcony_Windows,g_humidifier,g_dehumidifier,g_aircleaner,g_delivary_alarm

    if int(jsonResult['강수형태']) > 0:
        if g_Balcony_Windows == False:
            g_Balcony_Windows = True
        else:pass
    if int(jsonResult['강수형태']) == 0:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass
    #가습
    if int(jsonResult['습도']) < 45:
        if g_humidifier == False:
            g_humidifier = True
        if g_dehumidifier == True:
            g_dehumidifier = False
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass


    elif int(jsonResult['습도']) > 55:
        if g_dehumidifier == False:
            g_dehumidifier = True
        if g_humidifier == True:
            g_humidifier = False
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass

    if int(jsonResult['미세먼지정보']['미세먼지']) > 2 or int(jsonResult['미세먼지정보']['초미세먼지']) > 2:
        if g_aircleaner == False:
            g_aircleaner = True
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        if g_Balcony_Windows == True:
            g_Balcony_Windows = False
        else:pass
    elif int(jsonResult['미세먼지정보']['미세먼지']) or int(jsonResult['미세먼지정보']['초미세먼지']) <= 2:
        if g_aircleaner == True:
            g_aircleaner = False

    if g_delivary_alarm == False:
        g_delivary_alarm = True


def simulation(x):
    global g_Balcony_Windows,g_humidifier,g_dehumidifier,g_aircleaner,g_delivary_alarm

    soup = realtime_dust_info()
    jsonData = realtime_weather_info()
    if int(datetime.datetime.now().strftime('%M')) < 30:
        hours = time1 + datetime.timedelta(hours=2)
    elif int(datetime.datetime.now().strftime('%M')) >= 30:
        hours = time1 + datetime.timedelta(hours=1)

    after_hour = hours.strftime("%H") + '00'

    jsonResult = {}
    for i in jsonData['response']['body']['items']['item']:
        if after_hour == str(i['fcstTime']):
            jsonResult['예측시간'] = str(i['fcstTime'])[:2] + ':' + str(i['fcstTime'])[2:]
            if i['category'] =='LGT':
                jsonResult['낙뢰'] =i['fcstValue']
            elif i['category'] == 'PTY':
                jsonResult['강수형태'] = i['fcstValue']
            elif i['category'  ] == 'RN1':
                jsonResult['1시간강수량'] = i['fcstValue']
            elif i['category'] =='SKY':
                jsonResult['하늘상태'] = i['fcstValue']
            elif i['category'] == 'T1H':
                jsonResult['기온'] = i['fcstValue']
            elif i['category'] == 'REH':
                jsonResult['습도'] = i['fcstValue']


            if x == '1':jsonResult['강수형태'] = '1'
            elif x =='2':jsonResult['습도'] = '26'
            elif x =='3':jsonResult['습도'] = '70'
            elif x =='5':
                g_Balcony_Windows = True
                g_humidifier = True
                g_dehumidifier = True

                jsonResult['습도'] = '50'
                jsonResult['강수형태'] = '0'

    dust_info = {}
    dust_data = soup.find_all('item')
    for i in dust_data:
        if list(i.strings)[1] == '신암동':
            dust_info['측정시간'] = list(i.strings)[5]
            dust_info['측정위치'] = list(i.strings)[1]
            dust_info['미세먼지'] = '3'
            dust_info['초미세먼지'] = '4'
    jsonResult['미세먼지정보'] = dust_info

    check_device_status()

    print()
    print('{0:^95}'.format("<< 날씨 예보 정보 >>"))
    for i in list(jsonResult.items()):
        if i[0] != '미세먼지정보':
            print('\t\t\t\t          %s : %s' % (i[0], str(i[1])))

    print()
    print('{0:^95}'.format("<< 미세먼지 정보 >>"))
    for i in list(jsonResult['미세먼지정보'].items()):
        print('\t\t\t\t     %s : %s' % (i[0], str(i[1])))

    with open('Home_Network_Data/기상정보_시뮬레이션.json', 'w',encoding='utf8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print('\n'+'{0:^85}'.format('가상정보_시뮬레이션.json 이 저장되었습니다.'))
        print('\n' + '{0:^85}'.format('시뮬레이션 환경이 조성되었습니다.'))

    if x == '1':
        if int(jsonResult['강수형태']) > 0:
            print("\n"+'{0:^75}'.format("<< 예상 강수상태[%s] 30분 내로 비 겁나 온다네요...발코니 창을 닫겠습니다 >>" % jsonResult['강수형태']))
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else:
                pass

        elif int(jsonResult['강수형태']) == 0:
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else:pass

    elif x =='2':
        if int(jsonResult['습도']) < 45:
            print("\n"+'{0:^75}'.format("<< 예상습도[%s%%] 습도가 낮을거라네요... 가습기가 작동됩니다 >>" % jsonResult['습도']))
            if g_humidifier == False:
                g_humidifier = True
            else:pass
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else:pass
        elif int(jsonResult['습도']) > 55:
            if g_humidifier == True:
                g_humidifier = False
        elif 45 <= int(jsonResult['습도']) <=55 :
            print('\n'+'{0:^75}'.format('<< 예상습도[%s%%] 쾌적할것 같습니다 >>' % jsonResult['습도']))

    elif x =='3':
        if int(jsonResult['습도']) > 55:
            print("\n"+'{0:^75}'.format("<< 예상습도[%s%%] 습도가 높을거라네요... 제습기가 작동됩니다 >>" % jsonResult['습도']))
            if g_dehumidifier == False:
                g_dehumidifier = True
            else:pass
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else:pass
        elif int(jsonResult['습도']) < 55:
            if g_dehumidifier == True:
                g_dehumidifier = False
        elif 45 <= int(jsonResult['습도']) <=55 :
            print('\n'+'{0:^75}'.format('<< 예상습도[%s%%] 쾌적할것 같습니다 >>' % jsonResult['습도']))

    elif x =='4':
        if int(jsonResult['미세먼지정보']['미세먼지']) > 2 or int(jsonResult['미세먼지정보']['초미세먼지']) > 2:
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else: pass
            if g_aircleaner == False:
                g_aircleaner = True
                print('\n'+'{0:^64}'.format('<< 미세먼지[%s],초미세먼지[%s] 미세먼지 지수가 높습니다 발코니창을 닫고 공기청정기을 작동합니다 >>' % (
                jsonResult['미세먼지정보']['미세먼지'], jsonResult['미세먼지정보']['초미세먼지'])))
            else:pass
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            else:pass
        elif int(jsonResult['미세먼지정보']['미세먼지']) or int(jsonResult['미세먼지정보']['초미세먼지']) <= 2:
            if g_aircleaner == True:
                g_aircleaner = False

    elif x =='5':
        if 45 <= int(jsonResult['습도']) <=55 :
            print('\n'+'{0:^75}'.format('<< 예상습도[%s%%] 쾌적할것 같습니다 모든 관련제품을 끄겠습니다 >>' % jsonResult['습도']))
            if g_Balcony_Windows == True:
                g_Balcony_Windows = False
            if g_dehumidifier == True:
                g_dehumidifier = False
            if g_humidifier == True:
                g_humidifier = False
            if g_aircleaner == True:
                g_aircleaner = False
    else:
        print('\n\t\t\t\t       < 옳은값을 입력하세요 >')


    if x == '6':
        delivary_tracking.example_total_delivary()


def print_main_menu():
    upline = '\n\t\t\t\t        ┏' + '━' * 18 + '┓'
    downline = '\t\t\t\t        ┗' + '━' * 18 + '┛'
    print(upline + "\n\t\t\t\t        ┃ 1. 장비상태 확인 ┃\n\t\t\t\t        ┃ 2. 장비제어      ┃\n\t\t\t\t        ┃ 3. 스마트모드    ┃\n\t\t\t\t        ┃ 4. 시뮬레이션모드┃\n\t\t\t\t        ┃ 5. 종료          ┃\n" + downline)

def print_device_status(device_name,devcie_status):
    if devcie_status == True : print("\t\t\t\t┃ %s 상태 : [작동]"%device_name+' '*int(((21-len('┃ '+device_name+' 상태 : [작동]'))*2))+'┃')
    else :   print("\t\t\t\t┃ %s 상태 : [정지]"%device_name+' '*int(((21-len('┃ '+device_name+' 상태 : [정지]'))*2))+'┃')


def print_device_status2(device_name,device_status):
    if device_status == True: print("\t\t\t\t┃ %s 상태 : [열림]"%device_name+' '*int(((21-len('┃ '+device_name+' 상태 : [열림]'))*2))+'┃')
    else : print("\t\t\t\t┃ %s 상태 : [닫힘]"%device_name+' '*int(((21-len('┃ '+device_name+' 상태 : [잠김]'))*2))+'┃')


def check_device_status():
    print('\n\t\t\t\t┏' + '━' * 33 + '┓')
    print_device_status('난방기',g_Radiator)
    print_device_status2('가스밸브', g_Gas_Valve)
    print_device_status2('발코니(베란다)창문', g_Balcony_Windows)
    print_device_status2('출입문', g_Door)
    print_device_status('가습기', g_humidifier)
    print_device_status('제습기',g_dehumidifier)
    print_device_status('공기청정기',g_aircleaner )
    print_device_status('택배알리미', g_delivary_alarm)
    print('\t\t\t\t┗' + '━' * 33 + '┛')


def print_device_menu():
    upline = '\t\t\t\t    ┏' + '━' * 25 + '┓'
    downline = '\t\t\t\t    ┗' + '━' * 25 + '┛'
    print("\n\t\t\t\t  < 상태 변경할 기기를 선택하세요 >\n")
    print(upline + '\n\t\t\t\t    ┃' + "{0:^22}".format("1. 난방기") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^21}".format("2. 가스밸브") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^18}".format("3. 발코니(베란다)창") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^22}".format("4. 출입문") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^22}".format("5. 가습기") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^22}".format("6. 제습기") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^20}".format("7. 공기청정기") + '┃\n' + downline)
    print(upline + '\n\t\t\t\t    ┃' + "{0:^20}".format("8. 택배알리미") + '┃\n' + downline)



def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door,g_humidifier,g_dehumidifier,g_aircleaner,g_delivary_alarm

    check_device_status()
    print_device_menu()
    try:
        menu_num = int(input("\n\t\t\t\t\t번호를 입력하세요: "))
    except:
        print('\n\t\t\t\t       < 옳은값을 입력하세요 >')
        return control_device()

    if menu_num == 1: g_Radiator = not g_Radiator
    elif menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    elif menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 4: g_Door = not g_Door
    elif menu_num == 5: g_humidifier = not g_humidifier
    elif menu_num == 6: g_dehumidifier = not g_dehumidifier
    elif menu_num == 7: g_aircleaner  = not g_aircleaner
    elif menu_num == 8:
        if g_delivary_alarm == False:
            g_delivary_alarm = True
            delivary_tracking.delivary_main()
        else:
            print("\n\t\t\t\t      택배알리미 상태 : [작동]")
            a = int(input("\n\t\t\t\t      1. 이용하기 2. 끄기 : "))
            if a == 1:
                delivary_tracking.delivary_main()
            else: g_delivary_alarm = not g_delivary_alarm

    else:
        print('\n\t\t\t\t       < 옳은값을 입력하세요 >')
        return control_device()

    check_device_status()

def smart_mode():
    global g_AI_mode,t
    upline = '\n\t\t\t\t   ┏' + '━' * 28 + '┓'
    downline = '\t\t\t\t   ┗' + '━' * 28 + '┛'
    print(upline + '\n\t\t\t\t   ┃ 1. 인공지능 모드 상태 조회 ┃\n' + downline)
    print(upline + '\n\t\t\t\t   ┃ 2. 인공지능 모드 상태 변경 ┃\n' + downline)
    print(upline + '\n\t\t\t\t   ┃ 3. 실시간 정보 업데이트    ┃\n' + downline)

    try:
        menu_num = int(input('\n\t\t\t\t\t메뉴를 선택하세요 : '))
    except:
        print("\n\t\t\t\t       < 옳은값을 입력하세요 >")
        return smart_mode()

    if menu_num ==1:
        print('\n\t\t\t\t     현재 인공지능 모드: ', end='')
        if g_AI_mode == True: print('[작동]')
        else : print('[정지]')

    elif menu_num == 2:
        g_AI_mode = not g_AI_mode
        print('\n\t\t\t\t     현재 인공지능 모드: ', end='')
        if g_AI_mode == True:
            t = threading.Thread(target=update_scheduler)
            t.daemon = True
            t.start()
            print('[작동]')

        else :
            my_thread_terminate()
            print('[정지]')

    elif menu_num ==3:
        main()
    else:
        print('\n\t\t\t\t       < 옳은값을 입력하세요 >')
        return smart_mode()

def update_scheduler():
    global g_AI_mode,jsonResult
    stop1 = True
    stop2 = True
    while True:
        if g_AI_mode == False:
            continue
        else:
            if stop1 == True:
                delivary_tracking.speaker("안녕하세요. 인공지능모드가 활성화 되었습니다.")
                main2()
                stop1 = False
            else: pass
            realtime_check()
            if datetime.datetime.now().strftime("%M%S") == '4501':
                if stop2 == True:
                    stop2 = False
                    main2()
                    realtime_check()
                    time.sleep(3598)
                else: pass
            else: pass


if __name__=='__main__':

    t = threading.Thread(target=update_scheduler)
    t.daemon = True

    try:os.mkdir("Home_Network_Data")
    except:pass

    if getattr(sys, 'frozen', False):
        path = os.path.join(sys._MEIPASS, 'jake')
    else:path = 'jake'

    for i in range(9):
        for i in range(1, 31):
            n=0
            a = ''
            f = open(path+"\\new %s.txt" % str(i), 'r')
            line = f.readlines()
            for i in line:
                a += i
            time.sleep(0.01)
            cls(n)
            n = display(a)

    f = open(path+"\\new 31.txt")
    line = f.readlines()
    n = 0
    a=''
    for i in line:
        a += i
    time.sleep(0.01)
    os.system('cls')
    sys.stdout.write(a)
    cls(n)
    n = display(a)

    print('\n\n')
    print("\t\t\t<< 스마트 홈네트워크 시뮬레이션 프로그램 ver 2.0 >>")
    time.sleep(0.5)
    print("\t\t\t                                       - 이창현 -")
    time.sleep(0.5)
    while True:
        print_main_menu()
        try:
            menu_num = int(input("\n\t\t\t\t\t메뉴를 선택하세요 : "))
        except:
            print('\n\t\t\t\t       < 옳은값을 입력하세요 >')
            continue

        if(menu_num == 1):
            check_device_status()
        elif(menu_num ==2):
            control_device()
        elif(menu_num == 3):
            smart_mode()
        elif(menu_num ==4):
            upline = '                          ┏' + '━' * 43 + '┓'
            downline = '                          ┗' + '━' * 43 + '┛'
            print(upline + "\n                          ┃ 1. 비오는날 시뮬레이션(발코니창 제어)     ┃\n" + downline + '\n' + upline +
                  "\n                          ┃ 2. 건조한날 시뮬레이션(가습기 제어)       ┃\n" + downline + '\n' + upline +
                  "\n                          ┃ 3. 습한날 시뮬레이션(제습기 제어)         ┃\n" + downline + '\n' + upline +
                  "\n                          ┃ 4. 먼지 많은날 시뮬레이션(공기청정기 제어)┃\n" + downline + '\n' + upline +
                  "\n                          ┃ 5. 상쾌한날 시뮬레이션(제습기/가습기 제어)┃\n" + downline + '\n' + upline +
                  "\n                          ┃ 6. 택배추적 시뮬레이션(택배알리미 제어)   ┃\n" + downline +
                  "\n\t\t\t\t\t메뉴를 선택하세요 : ", end='')

            simulation(input())

        elif(menu_num ==5):
            if getattr(sys, 'frozen', False):
                path = os.path.join(sys._MEIPASS, 'bonobono')
            else:path = 'bonobono'

            for i in range(0, 18):
                n=0
                a = ''
                f = open(path + "\\%s.txt" % str(i), 'r')
                line = f.readlines()
                for i in line:
                    a += i
                time.sleep(0.01)
                cls(n)
                n = display(a)

            f = open(path + "\\18.txt")
            line = f.readlines()
            n = 0
            a = ''
            for i in line:
                a += i
            time.sleep(0.01)
            cls(n)
            n = display(a)
            time.sleep(1)
            break
        else:
            print("\n\t\t\t\t       < 옳은값을 입력하세요 >")

    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)
