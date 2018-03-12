def search_visitor(f,input_name):
    guests = f.read().split()
    guest_list = list(guests)
    if input_name in guest_list:
        print("%s 님 방문해 주셔서 감사합니다. 즐거운 시간 되세요" %input_name)
    else:
        f.close()
        f = open("D:\\Python_workspace\\jumptopy\\Excerise\\Function\\guests.txt", 'a')
        input_birthday = input("생년월일을 입력하세요(예:801212):")
        print("%s 님 방문해 주셔서 감사합니다. 즐거운 시간 되세요" %input_name)
        new_visitor = input_name+" "+input_birthday
        f.write(input_name+" "+input_birthday+"\n")

f = open("D:\\Python_workspace\\jumptopy\\Excerise\\Function\\guests.txt", 'r')

while True:
    input_name = input("이름을 입력하세요: ")
    search_visitor(f,input_name)
    break

f.close()
