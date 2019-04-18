import time
import calendar
#
# NowTime = time.time() # 当前时间戳
# print('当前时间戳为： %s' % NowTime)

#
# LocalTime = time.localtime(time.time()) # 获取本地时间
# print('本地时间为： ', LocalTime)
#
# LocalTime = time.asctime(time.localtime(time.time())) # 本地时间格式化 Fri Apr 13 11:50:19 2018 格式
# print('获取格式化  本地时间：', LocalTime)
#
LocalTime1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # 转化成 2018-04-13 11:50:19 格式
print('格式化日期后的  本地时间：', LocalTime1)
#
# LocalTime = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()) # 转化成：Fri Apr 13 14: 08: 07 2018
# print('格式化日期后的 本地时间： ', LocalTime)
#
# a = 'Fri Apr 13 14:08:07 2018'
# print(time.mktime(time.strptime(LocalTime, '%a %b %d %H:%M:%S %Y')))
#
# print(time.mktime(time.strptime(LocalTime1, '%Y-%m-%d %H:%M:%S')))
#
#
# cal = calendar.month(2018, 4) # 打开2016年1月的日历
# print('2016年1月的日历:')
# print(cal)

# event_time = (2018, 6, 14, 17, 1, 38)
# etime = str(event_time).split('.')[0]
# print(etime)
# timeArray = time.strptime(etime, '%Y-%m-%d %H:%M:%S')
# print(timeArray)

# nowtime = time.time()
# print(nowtime)
# print(str(nowtime))
#
# ntime = str(nowtime).split('.')[0]
# print(ntime)