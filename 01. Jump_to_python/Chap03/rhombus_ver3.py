output_msg="홀수를 입력하세요(0 <- 종료): "
blank=" "
star="*"
horizontal_line="-"
vertical_line="|"
print("마름모 출력 프로그램 ver3.0")
print("")

while True:
  print(output_msg,end='')
  customer_input = int (input())
  if customer_input == 0:
       print("")
       print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
       break
  elif customer_input % 2 == 0:
      print("짝수를 입력하셨습니다. 재입력 부탁드립니다.")
      continue
  else:
      star_count = 1
      blank_count = int((customer_input - star_count)/2)
      print(blank,end='')
      print(horizontal_line*customer_input,end='')
      print(blank)
      while True:
            print(vertical_line,end='')
            print(blank*blank_count,end='')
            print(star*star_count,end='')
            print(blank*blank_count,end='')
            print(vertical_line)
            if star_count == customer_input:
                break
            star_count += 2
            blank_count -= 1
      while True:
          if star_count == 1:
              break
          star_count -= 2
          blank_count += 1
          print(vertical_line,end='')
          print(blank*blank_count,end='')
          print(star*star_count,end='')
          print(blank*blank_count,end='')
          print(vertical_line)

      print(blank,end='')
      print(horizontal_line*customer_input,end='')
      print(blank)
