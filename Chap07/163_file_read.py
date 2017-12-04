f = open("D:\Temp\myfile\\newfile.txt")
while True:
    line = f.readline()
    if not line: break
    print(line,end='')
f.close()