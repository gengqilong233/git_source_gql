import threading
import time

def hello(word):
    print('hello fc '+ word + ' ' + str(time.strftime('%Y-%m-%d %H:%M:%S')))



thread = []
for i in range(3):
    t = threading.Thread(target=hello, args=('aaa',))
    thread.append(t)

if __name__ == '__main__':
    for i in thread:
        i.start()
    for i in thread:
        i.join()






