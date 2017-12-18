import sys
args=sys.argv[:]

def file_a(choice):
    try:
        f = open('D:\Python_workspace\jumptopy\Jump_to_python\Chap06\memo.txt','r')
        al=f.read()
        f.close()
    except:
        print('아래 중 선택하세요.')
        if choice !=2:
            print('1. 새로 생성하시겠습니까?')
        else:
            print('1. 종료하시겠습니까?')
        print('2. 파일 경로를 입력하겠습니다.')
        menu=int(input())
        if menu==1 and choice==2:
            sys.exit(1)
        if menu==1 and choice !=2:#새로 생성
            f = open('D:\Python_workspace\jumptopy\Jump_to_python\Chap06\memo.txt', 'a')
            if choice==0:
                f.write(args[2])
            elif choice==1:
                f.write(args[2].upper())
            f.write('\n')
            f.close()
        elif menu==2:#파일 경로 입력
            path=input('파일 경로를 입력해 주세요.:')
            f = open(path,'a')
            if choice!=1:
                f.write(args[2])
            else:
                f.write(args[2].upper())
            f.write('\n')
            f.close()
def file_au():
    pass
for i in args:
    if i=='-a':
        none=0
        file_a(none)
    elif i=='-au':#모두 대문자로 바꾼다
        upper=1
        file_a(upper)
    elif i=='-v':#memo.txt 파일이 있으면 열고 없으면 물어보자.
        exit=2
        file_a(exit)
    # else:
    #     pass
        # print(i)