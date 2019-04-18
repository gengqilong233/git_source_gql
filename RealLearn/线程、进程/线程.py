import time
import threading

# ----------------------------------------------------------------------------------------------------------------------
# 【线程初步认识】
# def music(music, count):
#     for i in range (count):
#         print('我在听%s %s' %(music, time.strftime('%Y-%m-%d %H:%M:%S')))
#         time.sleep(2)
#
#
# def movie(movie, count):
#     for i in range(count):
#         print('我在看%s %s' %( movie, time.strftime('%Y-%m-%d %H:%M:%S')))
#         time.sleep(2)
#
#
# threads = [] # 创建线程组
# t1 = threading.Thread(target=music, args=('<敦煌>',2)) # 创建线程t1
# threads.append(t1) # 添加t1到线程组
# t2 = threading.Thread(target=movie, args=('<绝地求生>', 2)) # 创建线程t2
# threads.append(t2) # 添加t2到线程组
#
#
# if __name__ == '__main__':
#     # 启动线程
#     for t in threads:
#         t.start()
#
#     # 守护线程
#     for t in threads:
#         t.join()
#
#     print('结束了 %s' %time.strftime('%Y-%m-%d %H:%M:%S'))
#     print('-' * 60)

# ----------------------------------------------------------------------------------------------------------------------

# 下列代码是多个线程通过迭代的方式放入进程组的演示
# def test(done, count):
#     for i in range(count):
#         print(done, time.strftime('%Y-%m-%d %H:%M:%S'))
#         time.sleep(2)
#
# thred = []
# dic = {'听音乐':2, '玩游戏':3}
# for a, b in dic.items():
#     t = threading.Thread(target=test, args=(a,b))
#     thred.append(t)
#
# if __name__ == '__main__':
#     for t in thred:
#         t.start()
#     for t in thred:
#         t.join()
#     print('end %s' %time.strftime('%Y-%m-%d %H:%M:%S'))

# ----------------------------------------------------------------------------------------------------------------------

# 【创建线程类】
class myThread(threading.Thread):
    def __init__(self, func, count, name):
        threading.Thread.__init__(self) # 用于继承threading.Thread类
        self.func = func
        self.count = count
        self.name = name

    def run(self):
        self.func(*self.count)


def lesson(done, count):
    for i in range(count):
        print("I'm doing %s, and it's %s time" %(done,i+1))
        time.sleep(2)

threads = []
do_dict = {'看书':2, '玩':3}
for key, value in do_dict.items():
    sa = myThread(lesson,(key, value), lesson.__name__)
    threads.append(sa)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()



