def check_number():
    if(number<0):
        raise ValueError

try:
    number = int(input("양수를 입력하세요"))
    check_number()
        # print("양수를 입력하세요.")
    # f=open("나없는파일",'r')
    # 4/0
    print("Hello World")
except FileNotFoundError as e:
    print("없는 파일을 열었습니다.")
    print("시스템 에러 메세지: "+str(e))
    print(e)
except ZeroDivisionError:
    # print("에러가 발생했습니다.")
    print("0으로 나누었습니다.")
except ValueError as e:
    print("잘못된 값을 입력하셨습니다.")
    print("시스템 에러 메세지: "+str(e))
else:
    print("Thank You!!")
finally:
    print("See ya later")
print("프로그램 정상 종료")