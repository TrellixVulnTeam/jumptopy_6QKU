#공원 입장료 계산 프로그램 Ver_1.0
#
# while 1 :
#     print("Welcome to the best and biggest amusement park in the world~!\n\
# (If you wanna shut this program, input one number lower than 0)")
#     Age = int(input("Before you enter the park, tell me how old you are.\n"))
#
#     if Age > -1 :
#        if Age <= 65 and Age >= 19 :
#            print("It is \ 5,000. Thank you.\n")
#        elif Age <= 18 and Age >=14 :
#             print("It is \ 3,000. Thank you.\n")
#        elif Age <= 13 and Age >= 4 :
#             print("It is \ 2,000. Thank you.\n")
#        else :
#            print("You don't need to pay for ticket.\n")
#     else :
#         print("Program is being terminated now.")
#         break

#공원 입장료 계산 프로그램 Ver_5.0
Money_Table = { "유아" : 0, "어린이" : 2000, "청소년" : 3000, "성인" : 5000, "노인" : 0 }
customer_counting = 0
promotion = [5, 3]
while 1 :
    print("Welcome to the best and biggest amusement park in the world~!\n\
(If you wanna shut this program, input one number lower than 0)")
    Age = int(input("Before you enter the park, tell me how old you are.\n"))

    class_type = ""
    if Age >= 66 :
        print("You are in old-man class and you don't need to pay for ticket. Thank you.\n")
        class_type = "노인"
    elif Age <= 65 and Age >= 19 :
          print("You are in adult class. It is \ 5,000. Thank you.\n")
          class_type = "성인"
    elif Age <= 18 and Age >=14 :
            print("You are in It is \ 3,000. Thank you.\n")
            class_type = "청소년"
    elif Age <= 13 and Age >= 4 :
            print("It is \ 2,000. Thank you.\n")
            class_type = "어린이"
    elif Age <= 3 and Age >= 0 :
        print("You don't need to pay for ticket.\n")
        class_type = "유아"
    else :
        print("Error")
        continue

    while Age >= 4 and Age <= 65 :
        Pay_method = int(input("How would you like to pay for ticket?\n\
    (Press 1 : Cash, Press 2 : Credit card\n"))
        if Pay_method == 1 :
            Income_Money = int(input("Give me money.\n"))
            if Income_Money == Money_Table[class_type] :
                print("Thank you. Here is ticket.\n")
                customer_counting += 1
                break
            elif Income_Money > Money_Table[class_type] :
                print("Thank you. Here are ticket and change %d." %(Income_Money - Money_Table[class_type]))
                customer_counting += 1
                break
            elif Income_Money < Money_Table[class_type] :
                print("Sorry. You should give me \\%d more. Return your money back. Here is \\%d.\n\
" %((Money_Table[class_type] - Income_Money), Income_Money))
                break
        elif Pay_method == 2 :
            if Age >= 60 and Age <= 65 :
                print("\\%d was paid. Here is your ticket.\n" %int(((Money_Table[class_type] * 0.9)) * 0.95))
                customer_counting += 1
                break
            else :
                print("\\%d was paid. Here is your ticket.\n" %int(Money_Table[class_type]*0.9))
                customer_counting += 1
            break
        else :
            print("Press 1 or 2")
            continue
    if customer_counting > 0 and customer_counting % 4 == 0  and promotion[0] > 0 :
        print("congratulation~! You got a chance to buy a yearly membership ticket. Here you are yearly discount ticket.")
        promotion[0] -= 1
        print("%d ticket left\n." %promotion[0])
    elif customer_counting > 0 and customer_counting % 7 == 0 and promotion[1] > 0 :
        print("congratulation~! You won an annual event. Here is a free ticket.\n")
        promotion[1] -= 1
        print("%d ticket left\n." %promotion[1])
