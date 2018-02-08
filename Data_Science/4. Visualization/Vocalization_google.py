from gtts import gTTS

default_str="""
안녕하세요. 전민하입니다. 스마트홈네트워크를 구동시키겠습니다. 
오늘의 뉴스를 알려드리겠습니다. 
홍준표 대표는 류여해의원의 성추행 고소관련하여 말도 안된다며 
MBN뉴스와 싸우고 있습니다. 뉴스 재미있어요? 그럼 안녕!"""
emotion_str="안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("test.mp3")

    open("test.mp3")


speaker(default_str)
# speaker(emotion_str)
