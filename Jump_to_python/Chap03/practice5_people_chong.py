people=0
annualticket=5
freeticket=3
while True:
    age=int(input("나이를 입력하세요:"))
    if age <= 3:
         print("귀하는 %s등급이며, 요금은 %s입니다." %('유아','무료'))
         print("감사합니다. 티켓을 발행합니다.")
    elif age >=4 and age <=13:
         print("귀하는 %s등급이며, 요금은 %s입니다." %('어린이','2000원'))
         select = int(input("1: 현금, 2: 공원전용 신용카드:"))
         if select==2:
             print("%s원 결제되었습니다. 티켓을 발행합니다." %(2000*0.9))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         elif select==1:
          charge = int(input("요금을 입력하세요:"))
          if charge <=1999:
             print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." %(2000-charge,charge))
          elif charge ==2000:
             print("감사합니다. 티켓을 발행합니다.")
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
          else:
             print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." %(charge-2000))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         else: continue
    elif age >=14 and age <=18:
         print("귀하는 %s등급이며, 요금은 %s입니다." %('청소년','3000원'))
         select = int(input("1: 현금, 2: 공원전용 신용카드:"))
         if select==2:
             print("%s원 결제되었습니다. 티켓을 발행합니다." %(3000*0.9))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         elif select==1:
          charge = int(input("요금을 입력하세요:"))
          if charge <=2999:
             print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." %(3000-charge,charge))
          elif charge ==3000:
             print("감사합니다. 티켓을 발행합니다.")
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
          else:
             print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." %(charge-3000))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         else: continue
    elif age >=19 and age <=59:
         print("귀하는 %s등급이며, 요금은 %s입니다." %('성인','5000원'))
         select = int(input("1: 현금, 2: 공원전용 신용카드:"))
         if select==2:
             print("%s원 결제되었습니다. 티켓을 발행합니다." %(5000*0.9))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         elif select==1:
          charge = int(input("요금을 입력하세요:"))
          if charge <4999:
             print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." %(5000-charge,charge))
          elif charge ==5000:
             print("감사합니다. 티켓을 발행합니다.")
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
          else:
             print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." %(charge-5000))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         else: continue
    elif age >=60 and age <=65:
         print("귀하는 %s등급이며, 요금은 %s입니다." %('성인','5000원'))
         select = int(input("1. 현금, 2: 공원전용 신용카드:"))
         if select==2:
             print("%s원 결제되었습니다. 티켓을 발행합니다." %(5000*0.90*0.95))
             people+=1
             if people % 4 == 0:
                 if annualticket >= 1:
                     print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                     annualticket -= 1
                     if annualticket == 0: continue
             elif people % 7 == 0:
                 if freeticket >= 1:
                     print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                     freeticket -= 1
                     if freeticket == 0: continue
         elif select==1:
            charge = int(input("요금을 입력하세요:"))
            if charge < 4999:
                  print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." % (5000 - charge, charge))
            elif charge == 5000:
                  print("감사합니다. 티켓을 발행합니다.")
                  people+=1
                  if people % 4 == 0:
                      if annualticket >= 1:
                          print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                          annualticket -= 1
                          if annualticket == 0: continue
                  elif people % 7 == 0:
                      if freeticket >= 1:
                          print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                          freeticket -= 1
                          if freeticket == 0: continue
            else:
                  print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (charge - 5000))
                  people+=1
                  if people % 4 == 0:
                      if annualticket >= 1:
                          print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket - 1))
                          annualticket -= 1
                          if annualticket == 0: continue
                  elif people % 7 == 0:
                      if freeticket >= 1:
                          print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료 티켓 %s장" % (freeticket - 1))
                          freeticket -= 1
                          if freeticket == 0: continue
         else: continue
    else:
          print("귀하는 %s등급이며, 요금은 %s입니다." %('노인','무료'))
          print("감사합니다. 티켓을 발행합니다.")