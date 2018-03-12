while 1 :
    height = int(input("정마름모를 찍어드립니다. 높이를 입력해 주세요.(프로그램 종료 : 0)"))
    Star1 = 1
    Star2 = height - 2
    Space1 = int((height - 1) / 2)
    Space2 = 1
    if height == 0 : break
    if height %2 != 1 and height != type(int) :
        print("정수형 홀수를 입력해 주세요")
    else :
        while Star1 <= height :
            print(' ' * Space1 , end='')
            print('*' * Star1)
            Star1 += 2
            Space1 -= 1

        while Star2 >= 1 :
            print(' ' * Space2 , end='')
            print('*' * Star2)
            Star2 -= 2
            Space2 += 1

print("\n마름모 찍기 프로그램을 이용해 주셔서 감사합니다.")