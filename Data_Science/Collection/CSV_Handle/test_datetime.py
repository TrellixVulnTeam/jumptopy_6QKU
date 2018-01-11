import datetime
post='Sat, 16 Dec 2017 16:24:00 +0900'
pDate = datetime.datetime.strptime(post,'%a, %d %b %Y %H:%M:%S +0900')
pDate = pDate.strptime('%Y-%m-%d %H:%M:%S')
print(pDate)