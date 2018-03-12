while True:
    choice= int(input("메뉴를 선택하세요: "))
    print("1. 덧셈")
    print("2. 종료")

    if(choice==2):
        break

    a=int(input("첫번째 값을 입력하세요: "))
    b=int(input("두번째 값을 입력하세요: "))
    result = a+b
    result = int(input("첫번째 값을 입력하세요: "))+int(input("두번째 값을 입력하세요: "))
    print("result: ", result)

