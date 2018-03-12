ywl = {'3':'유아','13':'어린이','18':'청소년','65':'성인','66':'노인'}
ywls = {'3':'유아','13':'어린이','18':'청소년','59':'성인','65':'장년','66':'노인'}
ywp = {'3':'무료','13':'2000','18':'3000','65':'5000','66':'무료'}
ywps = {'3':'무료','13':'1800','18':'2700','59':'4500','65':'4250','66':'무료'}

money = 0
age = 0
card = 1
ticket = 0
free = 3
event = 5

while True:

    print("요금 유형을 선택하십시요.\n(1.현금 2.공원 전용 신용 카드)")
    card = int(input(":"))
    if card == 1:
        while True:
            age = int(input("나이를 입력하세요:"))
            if age <= 3:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s] 입니다." % (ywl.get('3'),ywp.get('3')))
                print("감사합니다 티켓을 발행합니다.")
                ticket = ticket + 1
                while ticket % 7 == 0:
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(free - 1))
                    free = free - 1
                    break
                while ticket % 4 == 0:
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(event - 1))
                    event = event - 1
                    break
                break
            if 4<= age <=13:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywl.get('13'), ywp.get('13')))
                money = int(input("돈을 넣어주세요:"))
                if money == 2000:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
                elif money < 2000:
                    print("%d원이 모자랍니다" % abs(money-2000))
                    print("입력하신 %d원을 반환합니다." % money)
                    break
                elif money > 2000:
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (money - 2000))
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if 14 <= age <= 18:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywl.get('18'), ywp.get('18')))
                money = int(input("돈을 넣어주세요:"))
                if money == 3000:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
                elif money < 3000:
                    print("%d원이 모자랍니다" % abs(money - 3000))
                    print("입력하신 %d원을 반환합니다." % money)
                    break
                elif money > 3000:
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (money - 3000))
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if 19<= age <=65:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywl.get('65'), ywp.get('65')))
                money = int(input("돈을 넣어주세요:"))
                if money == 5000:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
                elif money < 5000:
                    print("%d원이 모자랍니다" % abs(money - 5000))
                    print("입력하신 %d원을 반환합니다." % money)
                    break
                elif money > 5000:
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (money - 5000))
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if age >= 66:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]입니다." % (ywl.get('66'), ywp.get('66')))
                print("감사합니다 티켓을 발행합니다.")
                ticket = ticket + 1
                while ticket % 7 == 0:
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(free - 1))
                    free = free - 1
                    break
                while ticket % 4 == 0:
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(event - 1))
                    event = event - 1
                    break
                break

    if card == 2:
        print("결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인됩니다")
        while True:
            age = int(input("나이를 입력하세요:"))
            if age <= 3:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s] 입니다." % (ywl.get('3'),ywps.get('3')))
                print("감사합니다 티켓을 발행합니다.")
                ticket = ticket + 1
                while ticket % 7 == 0:
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(free - 1))
                    free = free - 1
                    break
                while ticket % 4 == 0:
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(event - 1))
                    event = event - 1
                    break
                break
            if 4<= age <=13:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywl.get('13'), ywps.get('13')))
                card = int(input("카드를 넣어주시고 1번을 눌러주세요:"))
                if card == 1:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if 14 <= age <= 18:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywl.get('18'), ywps.get('18')))
                card = int(input("카드를 넣어주시고 1번을 눌러주세요:"))
                if card == 1:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if 19<= age <=59:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywls.get('59'), ywps.get('59')))
                card = int(input("카드를 넣어주시고 1번을 눌러주세요:"))
                if card == 1:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if 60<= age <=65:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]원 입니다." % (ywls.get('65'), ywps.get('65')))
                card = int(input("카드를 넣어주시고 1번을 눌러주세요:"))
                if card == 1:
                    print("감사합니다 티켓을 발행합니다.")
                    ticket = ticket + 1
                    while ticket % 7 == 0:
                        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(free - 1))
                        free = free - 1
                        break
                    while ticket % 4 == 0:
                        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                        print("잔여 무료 티켓[{0}]장.".format(event - 1))
                        event = event - 1
                        break
                    break
            if age >= 66:
                print("귀하의 등급은 [%s] 등급이며 요금은 [%s]입니다." % (ywl.get('66'), ywps.get('66')))
                print("감사합니다 티켓을 발행합니다.")
                ticket = ticket + 1
                while ticket % 7 == 0:
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(free - 1))
                    free = free - 1
                    break
                while ticket % 4 == 0:
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다.")
                    print("잔여 무료 티켓[{0}]장.".format(event - 1))
                    event = event - 1
                    break
                break
