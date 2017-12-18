inputs = input("두 수를 입력하세요.")
input_list = inputs.split()

try:
    num = int(input_list[0])
except:
    print("죄송합니다. 첫번째 입력이 '"+input_list[0]+"'입니다. 숫자를 입력하세요 ")
try:
    num = int(input_list[1])
except:
    print("죄송합니다. 두번째 입력이 '"+input_list[1]+"'입니다. 숫자를 입력하세요 ")

print("end")
