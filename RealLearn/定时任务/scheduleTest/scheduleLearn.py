import schedule
import time
import threading


def job():
    print('测试定时任务')
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


def haha(params, data):
    print('haha的参数：%s%s' %(params,data))

def run():
    # schedule.every(1).seconds.do(job)
    # # schedule.every().second.do(job) # 与上边区别在于，second默认每1秒，seconds需要填参数(minutes,hours,days)
    # schedule.every(1).minutes.do(job)
    # schedule.every(1).hours.do(job)
    schedule.every(1).days.at('11:20').do(job) # 每天在几点执行
    # # 每月的话可能需要自己实现一下
    # schedule.every().monday.at('14:13').do(job) # 每周一几点执行，也可以是其他周一至周天

    # schedule.every().second.do(haha, params=1, data='测试') # 如果要调用函数有参数，可以这么写(单个多个都可以)，也可以去掉参数名(parms、data)

    # schedule.every(1).to(10).second.do(job)

    while True: # 一直运行不应该是一个死循环，这样...(看下边)
    # a = 0
    # while a<10: # 可以这样限制一下(当然这个是我自己写的)
        schedule.run_pending() # 这个是保证schedule一直运行，去查询上边的任务
        time.sleep(1)
        # a+= 1

    # 这里面job不应当是死循环类型的，也就是说，这个线程应该有一个执行完毕的出口。一是因为线程万一僵死，会是非常棘手的问题；
    # 二是下一次定时任务还会开启一个新的线程，执行次数多了就会演变成灾难。如果schedule的时间间隔设置得比job执行的时间短，
    # 一样会线程堆积形成灾难，所以，还是需要注意一下的

run()
# ----------------------------------------------------------------------------------------------------------------------
# 利用多线程的方法同时执行多个任务
# def threadJob1():
#     t = threading.Thread(target=job)
#     t.start()
#     t.join()
#
#
# def threadJob2():
#     t = threading.Thread(target=job)
#     t.start()
#     t.join()
#
#
# schedule.every(1).second.do(threadJob1)
# schedule.every(1).second.do(threadJob2)
#
# while True:
#     schedule.run_pending()
