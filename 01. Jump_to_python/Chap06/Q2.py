list_num=input('범위, 첫번째 수, 두번째 수를 입력하세요.(종료: 프로그램 종료)').split()
#print(list)
list_num[0]=int(list_num[0])
list_num[1]=int(list_num[1])
list_num[2]=int(list_num[2])
A=[]
B=[]
for i in range(1,list_num[0]+1):
    if i%(list_num[1])==0:
        A.append(i)
    if i%(list_num[2])==0:
        B.append(i)
A=set(A)
B=set(B)
total=A|B
result=0
total=list(total)#총합은 순서 상관없으니 집합형으로 뒀다가 리스트로 그냥 바꾸는건 문제없다

A=list(A)
B=list(B)
A.sort()
B.sort()
total.sort()

for j in range(len(total)):
    result=result+total[j]

print('0부터 %d 까지의 범위를 선택하셨습니다. 이 중에서'%list_num[0])
print('%d의 배수는 %s입니다.'%(list_num[1],A))
print('%d의 배수는 %s입니다.'%(list_num[2],B))
print('%d과(와) %d의 배수는 %s입니다.'%(list_num[1],list_num[2],total))
print('따라서 0부터 %d 이하의 범위내에서 %d와 %d의 배수의 총합은 %d입니다.'%(list_num[0],list_num[1],list_num[2],result))
