import urllib.request
client_id = "CJsADWzyJq8m29Qm7l11"           # <= 변경
client_secret = "cv55RE05hD" # <= 변경
default_str="""안녕하세요. 전민하입니다. 스마트홈네트워크를 구동시키겠습니다. 
오늘의 뉴스를 알려드리겠습니다. 
홍준표 대표는 류여해의원의 성추행 고소관련하여 말도 안된다며 
MBN뉴스와 싸우고 있습니다. 뉴스 재미있어요? 그럼 안녕!"""
emotion_str="안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"
# encText = urllib.parse.quote(emotion_str)
encText = urllib.parse.quote(default_str)
data = "speaker=jinho&speed=0&text=" + encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('11112.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)