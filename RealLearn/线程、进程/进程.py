import threading
import multiprocessing
from time import ctime, sleep

def super_play(file_, time):
    for i in range(2):
        print('开始播放：%s! %s' %(file_, ctime()))
        sleep(time)

list = {'《敦煌》':3, '《Refrain》':3, '《骑马与砍杀》':5, '《权利的游戏》':4}

thread = []
# files = range(len(list))

for file, time in list.items():
    # t = threading.Thread(target=super_play, args=(file, time))  # 线程
    t = multiprocessing.Process(target=super_play, args=(file, time))  # 进程
    thread.append(t)


if __name__ == '__main__':
    for t in range(len(list)):
        thread[t].start()

    for t in range(len(list)):
        thread[t].join()
    print('结束 %s' %ctime())
