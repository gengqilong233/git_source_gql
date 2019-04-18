import threading
import time
from selenium import webdriver

# ----------------------------------------------------------------------------------------------------------------------
# 1【多线程执行百度查询】
# def search_baidu(browser, text):
#     driver = ''
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     else:
#         print('暂时还没有其他浏览器驱动')
#         exit(1)
#
#     driver.get('https://www.baidu.com/')
#     bai_text = driver.find_element_by_class_name('s_ipt')
#     bai_text.send_keys(text)
#     bai_text.submit()
#     print(time.strftime('%Y-%m-%d %H:%M:%S'))
#     print('查询%s链接:%s' %(text, driver.current_url))
#
#
#
# if __name__ == '__main__':
#     threads = []
#     do_dic = {'python':'chrome', 'java':'chrome'}
#
#     for key,value in do_dic.items():
#         t = threading.Thread(target=search_baidu, args=(value,key))
#         threads.append(t)
#
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()

# ----------------------------------------------------------------------------------------------------------------------
# 2【定义一个类执行多线程】

class baidu_test(threading.Thread):
    def __init__(self, do, count):
        threading.Thread.__init__(self)
        self.do = do
        self.count = count
        self.driver = webdriver.Chrome()

    def func(self):
        for i in range(self.count):
            # self.driver = webdriver.Chrome()
            self.driver.get(self.do)
            now = time.strftime('%Y-%m-%d %H:%M:%S')
            print('当前链接：%s,第%s次' % (self.driver.current_url, i+1), now)
            time.sleep(2)

if __name__ == '__main__':
    # d = baidu_test('https://www.baidu.com/', 2)
    # d.func()

    threads = []
    do_dict = {'https://www.baidu.com/':2,
               'http://i.hfjy.com/resource/index.html#!/':1}

    for key, value in do_dict.items():
        t = threading.Thread(target=baidu_test(key,value).func, args='')
        threads.append(t)

    for i in threads:
        i.start()
    for i in threads:
        i.join()


