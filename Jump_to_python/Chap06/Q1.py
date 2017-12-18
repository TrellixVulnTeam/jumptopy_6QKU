Flag=0
while True:
    dan=input('숫자를 입력하세요(-1:종료, all:구구단 전체 출력)')
    if dan == 'all':
        for i in range(2, 10):
            for j in range(1, 10):
                print('%d * %d = %d' % (i, j, i * j))
            print()
            Flag=1
    elif dan == '-1':
        break
    try:
        dan=int(dan)
    except:# 정수형으로 변환 할 수 없을때는
        if Flag==1:
            continue
        print('잘못된 입력')
        continue
    try:
        raise ValueError
    except ValueError:
        if dan < -1:
            continue

    for i in range(1,10):
        print('%d * %d = %d' % (dan, i, dan * i))
