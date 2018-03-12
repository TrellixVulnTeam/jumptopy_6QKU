#게시판 페이징
def getTotalPage(m,n):
    total=0
    if m % n == 0:
        total = int(m / n)
    elif m % n != 0:
        total = int(m / n) + 1
    print('게시물 총 건수:%d, 한 페이지에 보여줄 게시물 수 : %d, 총 페이지 수:%d'%(m,n,total))

f=open('D:\Python_workspace\jump_to_python\python_jaryo\practice\\12_15/condition.txt','r')
a=f.readlines()

for line in a:
    num_list=line.split()
    # print(num_list)
    try:
        m=int(num_list[0])
        n=int(num_list[1])

        getTotalPage(m,n)
    except:
        pass

f.close()