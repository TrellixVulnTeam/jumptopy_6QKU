import datetime
import time

post_created_time = '2017-02-02T14:00:00+0000'
ymd = post_created_time.split('T')
tms = str(ymd[1]).split('+')
post_created_time = str(ymd[0])+' '+str(tms[0])
post_mct = datetime.datetime.strptime(post_created_time,'%Y-%m-%d %H:%M:%S')
print(type(post_mct))
print(post_mct)
post_mct = post_mct + datetime.timedelta(hours=+9)
print(type(post_mct))
print(post_mct)

year,month,day = ymd[0].split('-')
my_date = datetime.datetime(int(year),int(month),int(day),0,0,0)
print('Custom date')
print(my_date)

# import datetime
#
# myDatetimeStr = '2015-04-15 12:23:38'
# myDatetime = datetime.datetime.strptime(myDatetimeStr, '%Y-%m-%d %H:%M:%S')
# print(type(myDatetime))  # [class 'datetime.datetime']
# print(myDatetime)  # 2015-04-15 12:23:38
