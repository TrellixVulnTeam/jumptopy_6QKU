import json
import datetime
import requests
import time
import pygame.mixer
import os
import threading
from gtts import gTTS


def requests_url(url):
    req = requests.get(url, headers={'Accept' : 'application/json;charset=UTF-8'})
    response = req.text
    return response

def realtime_delivery_company_info():
    access_key = 'QPZSmqhXiTqklpnS8sUl3Q'
    end_point='http://info.sweettracker.co.kr/api/v1/companylist'
    parameters = "?t_key="+access_key
    url=end_point+parameters
    retData = requests_url(url)

    if (retData == None):return None
    else:return json.loads(retData)

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("Home_Network_Data/test.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(open("Home_Network_Data/test.mp3","rb"))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.stop()


def realtime_delivery_info():
    global tcode,tinvoice
    access_key = 'QPZSmqhXiTqklpnS8sUl3Q'
    end_point='http://info.sweettracker.co.kr/api/v1/trackingInfo'
    parameters = "?t_key=" + access_key
    parameters +="&t_code="+ str(tcode)
    parameters +="&t_invoice="+str(tinvoice)
    url = end_point + parameters

    retData = requests_url(url)
    if (retData == None):
        return None
    else:return json.loads(retData)

def delivery_company_list():
    jsonResult = realtime_delivery_company_info()
    print()
    for i in jsonResult["Company"]:
        print('\t\t\t\t    '+i['Code']+' : '+ i['Name'])

def selcet_delivery_company():
    jsonResult = realtime_delivery_company_info()
    for i in jsonResult["Company"]:
        if tcode == i["Code"]:
            tcompany = i['Name']
            print("\n택배회사는 %s 입니다."%tcompany)

def total_delivery():
    global delivary_result
    delivary_result = realtime_delivery_info()
    print('\n'+'{0:^85}'.format('< 현재까지 진행된 배송상황을 알려드립니다 >'))
    print('\n\t\t\t\t    발송자 : ' + delivary_result['senderName'])
    print('\t\t\t\t    수령인 : ' + delivary_result['receiverName'])

    for i in delivary_result['trackingDetails']:
        print()
        print('\t\t\t\t    시간 : '+i['timeString'])
        print('\t\t\t\t    위치 : '+i['where'])
        print('\t\t\t\t    상태 : '+i['kind'])


def save_delivary():
    global delivary_result,tcode,tinvoice
    delivary_result = realtime_delivery_info()
    with open('Home_Network_Data/최신배송상태 추적.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(delivary_result['trackingDetails'][-1], indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)


def resent_delivery():
    global delivary_result
    delivary_result = realtime_delivery_info()
    print('\n<< 현재 위치 >>')

    print('발송자 : ' + delivary_result['senderName'])
    print('수령인 : ' + delivary_result['receiverName'])
    print()
    print('시간 : ' + delivary_result['trackingDetails'][-1]['timeString'])
    print('위치 : ' + delivary_result['trackingDetails'][-1]['where'])
    print('상태 : ' + delivary_result['trackingDetails'][-1]['kind'])
    save_delivary()

def resent_speaker():
    global delivary_result
    speaker('실시간 배송 추적상태를 알려드립니다.')
    if delivary_result['trackingDetails'][-1]['kind'] == '접수':
        speaker('현재 주문하신 상품은 %s에 %s 되었습니다루다루다람쥐' % (delivary_result['trackingDetails'][-1]['where'], delivary_result['trackingDetails'][-1]['kind']))

    elif delivary_result['trackingDetails'][-1]['kind'] == '도착':
        speaker('현재 주문하신 상품은 %s에 %s 했습니다루다루다람쥐' % (delivary_result['trackingDetails'][-1]['where'], delivary_result['trackingDetails'][-1]['kind']))

    elif delivary_result['trackingDetails'][-1]['kind'] == '발송':
        speaker('현재 주문하신 상품은 %s에서 %s 되었습니다루다루다람쥐' % (delivary_result['trackingDetails'][-1]['where'], delivary_result['trackingDetails'][-1]['kind']))

    elif delivary_result['trackingDetails'][-1]['kind'] == '배달준비':
        speaker('현재 주문하신 상품은 %s에서 %s 중입니다루다루다람쥐' % (delivary_result['trackingDetails'][-1]['where'], delivary_result['trackingDetails'][-1]['kind']))

    elif delivary_result['trackingDetails'][-1]['kind'] == '배달완료':
        speaker('현재 주문하신 상품은 %s 되었습니다루다루다람쥐' % (delivary_result['trackingDetails'][-1]['kind']))
    else:
        speaker('현재 주문하신 상품은 %s에서 %s 중입니다루다루다람쥐' % (delivary_result['trackingDetails'][-1]['where'], delivary_result['trackingDetails'][-1]['kind']))


def comparison_delivary():
    global delivary_result
    delivary_result = realtime_delivery_info()

    if os.path.isfile('Home_Network_Data/최신배송상태 추적.json'):
        with open('Home_Network_Data/최신배송상태 추적.json', encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            ex_delivary_spot = json.loads(json_string)

        if delivary_result['trackingDetails'][-1]['kind'] == '배달완료':
            print('\n<< 실시간 배송 추적상태를 알려드립니다 >>')
            speaker('실시간 배송 추적상태를 알려드립니다.')
            print('\n<< 주문하신 상품은 배달완료 되었습니다 >>')
            speaker('주문하신 상품은 배달완료 되었습니다')

        else:
            resent_speaker()
            save_delivary()
    else:
        save_delivary()
        resent_speaker()


def smart_delivary_speaker():
    global delivary_result, tcode, tinvoice
    with open('Home_Network_Data/배송정보.txt') as lfile:
        line = lfile.readline()
    tcode, tinvoice = line.split(' ')
    delivary_result = realtime_delivery_info()

    if delivary_result['trackingDetails'][-1]['kind'] == '배달완료':
        speaker('실시간 배송 추적상태를 알려드립니다.')
        speaker('주문하신 상품은 배달완료 되었습니다')
    else:
        resent_speaker()
        save_delivary()


def read_code():
    global tcode,tinvoice
    with open('Home_Network_Data/배송정보.txt') as lfile:
        line = lfile.readline()
    tcode, tinvoice = line.split(' ')


def delivary_main():
    global tcode,tinvoice
    print('\n\t\t\t\t  << 택배추적 알리미 시작합니다 >>')
    upline = '\t\t\t\t      ┏'+'━'*21+'┓'
    downline = '\t\t\t\t      ┗'+'━'*21+'┛'
    sel = input('\n'+upline+'\n\t\t\t\t      ┃ 1. 배송정보 입력하기┃\n'+downline+
                '\n'+upline+'\n\t\t\t\t      ┃ 2. 배송조회         ┃\n'+downline+
                '\n'+'\n\t\t\t\t\t      입력 : ')
    if sel == '1':
        delivery_company_list()
        try:
            tcode= int(input("\n\t\t\t\t    택배사 코드를 입력하세요 : "))
        except:
            print('\n\t\t\t       < 택배사 코드는 숫자로 입력해주세요 >')
            return delivary_main()
        selcet_delivery_company()
        try:
            tinvoice=int(input("\n\t\t\t\t  운송장 번호를 입력하세요 : "))
        except:
            print('\n\t\t\t\t< 운송장 번호는 숫자로 입력해주세요 >')
            return delivary_main()
        savefile = input('\n\t\t\t\t      저장하시겠습니까? (y/n):')
        if savefile == 'y':
            print('\n\t\t\t\t      저장 되었습니다 감사합니다')
            with open('Home_Network_Data/배송정보.txt', 'w') as sfile:
                sfile.write(str(tcode)+' '+str(tinvoice))
        elif savefile =='n':
            print('\n\t\t\t\t      < 취소되었습니다 >')

        return delivary_main()

    elif sel == '2':
        try:
            read_code()
            total_delivery()
        except:
            print("\n\t\t\t\t   < 우선 배송정보를 입력하세요 >")
            return delivary_main()
    else:
        print("\n\t\t\t\t       < 옳은값을 입력하세요 >")

def example_total_delivary():
    delivary_example = {'result': 'Y', 'senderName': '투밀*', 'receiverName': '김선*',
                        'itemName': '2건▶심플포토케이스:(핸드폰기종=(슬림) 갤럭시 S7 엣지, '
                        '배경색=블랙)▷메세지/문구 입력:♥Since 2017.3.4~Ing♥--1개☞1EA',
                        'invoiceNo': '613771889505', 'receiverAddr': '대구광역시 중구 태평로',
                        'orderNumber': None, 'adUrl': None, 'estimate': '14∼16시', 'level': 6,
                        'complete': True, 'recipient': '김선경', 'itemImage': '',
                        'trackingDetails': [{'time': 1517404152000, 'timeString': '2018-01-31 22:09:12',
                        'code': None, 'where': '시흥대리점', 'kind': '집화처리', 'telno':
                        '070-7532-1909', 'telno2': '', 'remark': None, 'level': 2,
                        'manName': '', 'manPic': ''}, {'time': 1517404152000, 'timeString': '2018-01-31 22:09:12',
                        'code': None, 'where': '시흥', 'kind': '행낭포장',
                        'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '',
                        'manPic': ''}, {'time': 1517404345000, 'timeString': '2018-01-31 22:12:25', 'code': None,
                        'where': '시흥', 'kind': '간선상차', 'telno': '', 'telno2': '', 'remark': None,
                        'level': 3, 'manName': '', 'manPic': ''}, {'time': 1517494587000, ''
                        'timeString': '2018-02-01 23:16:27', 'code': None, 'where': '대전HUB', 'kind': '간선하차', 'telno': '',
                        'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, {'time': 1517494999000, 'timeString': '2018-02-01 23:23:19',
                        'code': None, 'where': '대전HUB', 'kind': '간선하차', 'telno': '', 'telno2': '', 'remark': None, 'level': 3,
                        'manName': '', 'manPic': ''}, {'time': 1517495087000, 'timeString': '2018-02-01 23:24:47', 'code': None,
                        'where': '대전HUB', 'kind': '행낭포장', 'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''},
                        {'time': 1517497406000, 'timeString': '2018-02-02 00:03:26', 'code': None, 'where': '대전HUB', 'kind': '간선하차', 'telno': '',
                        'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, {'time': 1517497549000, 'timeString': '2018-02-02 00:05:49',
                        'code': None, 'where': '대전HUB', 'kind': '간선상차', 'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''},
                        {'time': 1517533115000, 'timeString': '2018-02-02 09:58:35', 'code': None, 'where': '대구중Sub', 'kind': '간선하차',
                        'telno': '053-211-3858', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''},
                        {'time': 1517533379000, 'timeString': '2018-02-02 10:02:59', 'code': None, 'where': '대구중Sub', 'kind': '간선하차',
                         'telno': '053-211-3858', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, {'time': 1517537409000,
                        'timeString': '2018-02-02 11:10:09', 'code': None, 'where': '대구대신', 'kind': '배달출발',
                        'telno': '053-424-3312', 'telno2': '01035023679', 'remark': None, 'level': 5, 'manName': '조철희', 'manPic': ''},
                        {'time': 1517558807000, 'timeString': '2018-02-02 17:06:47', 'code': None, 'where': '대구대신', 'kind': '배달완료',
                         'telno': '053-424-3312', 'telno2': '01035023679', 'remark': None, 'level': 6, 'manName': '조철희', 'manPic': ''}],
                        'productInfo': None, 'zipCode': None, 'lastStateDetail': {'time': 1517558807000, 'timeString': '2018-02-02 17:06:47', 'code': None,
                        'where': '대구대신', 'kind': '배달완료', 'telno': '053-424-3312', 'telno2': '01035023679', 'remark': None, 'level': 6,
                        'manName': '조철희', 'manPic': ''}, 'firstDetail': {'time': 1517404152000, 'timeString': '2018-01-31 22:09:12', 'code': None,
                        'where': '시흥대리점', 'kind': '집화처리', 'telno': '070-7532-1909', 'telno2': '', 'remark': None, 'level': 2, 'manName': '',
                        'manPic': ''}, 'completeYN': 'Y', 'lastDetail': {'time': 1517558807000, 'timeString': '2018-02-02 17:06:47', 'code': None,
                        'where': '대구대신', 'kind': '배달완료', 'telno': '053-424-3312', 'telno2': '01035023679', 'remark': None, 'level': 6,
                        'manName': '조철희', 'manPic': ''}}

    delivary_result = delivary_example
    print('\n\t\t\t\t현재까지 진행된 배송상황을 알려드립니다')
    print('\n\t\t\t\t      발송자 : ' + delivary_result['senderName'])
    print('\t\t\t\t      수령인 : ' + delivary_result['receiverName'])

    for i in delivary_result['trackingDetails']:
        print()
        print('\t\t\t\t      시간 : ' + i['timeString'])
        print('\t\t\t\t      위치 : ' + i['where'])
        print('\t\t\t\t      상태 : ' + i['kind'])

if __name__ == "__main__":
    # delivary_main()

    speaker("안녕하세요. 전민하입니다. 스마트홈네트워크를 구동시키겠습니다. 오늘의 뉴스를 알려드리겠습니다. 홍준표 대표는 류여해의원의 성추행 고소관련하여 말도 안된다며 MBN뉴스와 싸우고 있습니다. 재미있어요? 그럼 안녕!")