from datetime import datetime, date
input_date='1/20/14'
input_date=input_date.split('/')
# input_date[0] = int(input_date[2])
# input_date[1] = int(input_date[0])
# input_date[2] = int(input_date[1])
# input_date.append(0)
# input_date.append(0)
# input_date.append(0)
temp_date = [int(input_date[2]),int(input_date[0]),int(input_date[1]),0,0,0]
temp_date = tuple(temp_date)

# input_date = int(input_date)
# input_date=tuple(int(input_date[2]),int(input_date[0]),int(input_date[1]),0,0,0)
# convert_date = date(int(input_date[2]),int(input_date[0]),int(input_date[1]))
# date.strptime(indate,'%m/%d/%Y')
# convert_date = datetime.date(convert_date, '%m/%d/%Y')
# print(convert_date)
converted_date = date(*temp_date[0:3]).strftime('%m/%d/%Y')
print(converted_date)
print("End")