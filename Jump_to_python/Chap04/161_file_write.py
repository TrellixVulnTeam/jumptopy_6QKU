f=open("D:/Temp/myfile/newfile.txt",'w')

for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()