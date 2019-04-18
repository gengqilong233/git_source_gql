# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get('http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3')
#
#
#
# page_info = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[2]/a[4]')
# print(page_info)
# pages = page_info.text
# print(pages)


import requests
import threading
import time
# http://offline-lms-api.hfjy.com
def aa():  # test-lms-api.hfjy.com
    r = r'D:\接受文件\roster-template-v3.01.xlsx'
    r1 = r'D:\接受文件\roster-template-v3.0111111111.xlsx'
    url = 'https://lms-api.hfjy.top/ixb/lms/student/import'
    head = {'Authorization':'Bearer c50e8ae4-bfcd-4b1c-a4a8-8a5c38c242041553053460589'}
    files = {'file': open(r, "rb")}
    data = {'file':'',
        'pool':'KF_PUB',
        'userId':'1100871',
    }




    r = requests.post(url, data,  files=files, headers=head)
    r.encoding='unicode'
    print(str(time.strftime('%Y-%m-%d %H:%M:%S')))
    print(r.json())



if __name__ == '__main__':
    thread = []
    for i in range(1):
        t = threading.Thread(target=aa)
        thread.append(t)

    for t in thread:
        t.start()
    for t in thread:
        t.join()