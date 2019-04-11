import requests
import bs4
import os


# 图片
# url = 'https://unsplash.com/'
# r = requests.request('get', url)
# data = r.text
# # print(data)
#
# soup = bs4.BeautifulSoup(data, 'lxml')
# a_all = soup.find_all('img', '_2zEKz')
# z = []
# for a in a_all:
#     # print(a)
#     a_http = a.get('src')
#     if a_http:
#         if a_http in z:
#             pass
#         else:
#             z.append(a_http)
#             print(a_http)
#             print(a)


# 遮天小说
# url = 'https://www.sbiquge.com/0_466/'
# r = requests.request('get', url)
# r_result = r.text
# # print(r_result)
#
# result = bs4.BeautifulSoup(r_result, 'lxml')
#
# z = result.find('div', attrs='listmain')
# # print(z)
#
# list = []
# for i in z.dl.children:
#     c = i.find('a')
#     if 'href' in str(c):
#         print(c)
#         list.append(c)
#
# for i in list[6:-1]:
#     print(i.text)
#     print(i['href'])




head = {'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cache-Control': 'max-age=0'
        }
url = 'https://www.sbiquge.com/0_466/253493.html'
r = requests.request('get', url, headers=head)
# r.encoding = 'gbk'
c = r.text

soup = bs4.BeautifulSoup(c, 'lxml')
b = soup.find('div', attrs='showtxt')


def save_txt(path, msg):
    with open(path, 'a+', encoding='utf8') as f:
        f.write(msg + '\n')

save_txt('/Users/gengqilong/Desktop/pythonProgram/RealLearn/python_bug/diergewenjian/spiderr_txt/1', b.text)



