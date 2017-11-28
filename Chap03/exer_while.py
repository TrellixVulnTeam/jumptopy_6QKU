customer_input="홀수를 입력하세요(0 <- 종료): "
blank=" "
print("마름모 출력 프로그램 ver1.0")
print("")

while True:
  print(customer_input,end='')
  choice = int (input())
  if choice == 0:
       print("")
       print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
       break
  elif choice % 2 == 0:
      print("")
      print("홀수를 입력해 주세요")
      continue
  else:
      index = 0
      while True:
            index = index+1
            blank_count = choice - index
            if index > choice:
                break
            if index%2==0:
                continue
            else:
                blank_count = int(blank_count/2)

            print(blank*blank_count,end='')
            print("*"*index)
            print(blank*blank_count)

