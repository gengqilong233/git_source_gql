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


# 小说大类
# url = 'https://www.sbiquge.com/'
# r = requests.request('get', url)
# result = r.text
# # print(result)
#
# soup = bs4.BeautifulSoup(result, 'lxml')
# soup_catalog = soup.find_all('div', attrs='nav')
#
# for i in soup_catalog[0].ul.children:
#     c = i.find('a')
#     if 'href' in str(c):
#         print(c.text, url + str(c['href'].split('/')[1]))
#     else:
#         pass

# 汉字转拼音
# import xpinyin
# pin = xpinyin.Pinyin()
#
# test1 = pin.get_pinyin('大江东去浪淘尽', '')
# print(test1)

# 数据结构
# a = [
#     {
#         'type': '玄幻',
#         'type_url': 'url',
#         'story_list':
#             {
#                 'story0': {
#                     'story_name': '遮天',
#                     'story_url': 'url',
#                     'list': {
#                         '第 一章 xx': 'url'
#                     }
#                 },
#                 'story1': {
#                     'story_name': '完美世界',
#                     'story_url': 'url',
#                     'list': {'第一章': 'url'}
#                 }
#             }
#     },
#     # {
#     #     'type': '修真',
#     #     'type_url': 'url',
#     # }
# ]
# for i in a:
#     sotry_type = i['type']
#     sotry_type_url = i['type_url']
#     story_lilst = i['story_list']
#     print('小说类型:', sotry_type)
#     print('小说类型url:', sotry_type_url)
#
#     for key, value in story_lilst.items():
#         story_info = value
#         story_name = story_info['story_name']
#         story_url = story_info['story_url']
#         list = story_info['list']
#         print('小说名:', story_name)
#         print('小说url:', story_url)
#
#         for key, value in list.items():
#             story_chapter = key
#             story_chapter_url = value
#             print('小说章节名:', story_chapter)
#             print('小说章节url:', story_chapter_url)

# # 小说列表
# url = 'https://www.sbiquge.com/xuanhuanxiaoshuo'
# result = requests.request('get', url).text
# # print(result)
#
# soup = bs4.BeautifulSoup(result, 'lxml')
# list = soup.find('div', attrs='r bd')
# for i in list.ul.children:
#     c = i.find('a')
#     # print(c)
#     if 'href' in str(c):
#         print(c.text, 'https://www.sbiquge.com' + str(c['href']))
#     else:
#         pass

# a = [1, 10, 9, 6, 5, 7, 4, 2, 3, 8]
#
# count = len(a)
# for i in range(0, count):
#     for j in range(i+1, count):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)



a = {'list': {'事件①：风波！夜晚的惨叫声！': 'https://www.sbiquge.com/33_33805/19177075.html',
          '事件②：风波！深夜的撕裂者！': 'https://www.sbiquge.com/33_33805/19177076.html',
          '事件③：风波！夜晚的四个人！': 'https://www.sbiquge.com/33_33805/19177077.html',
          '事件④：风波！深夜的医院内！': 'https://www.sbiquge.com/33_33805/19177078.html',
          '事件⑤：风波！夜晚的音子熙！': 'https://www.sbiquge.com/33_33805/19177079.html',
          '十一章：开篇，五菱演武选拔赛。': 'https://www.sbiquge.com/33_33805/19177073.html',
          '十一话：贪婪野心,神之诅咒': 'https://www.sbiquge.com/33_33805/19177029.html',
          '十三话：战斗之后,各自觉悟': 'https://www.sbiquge.com/33_33805/19177031.html',
          '十二章：开篇，预备赛前的风波。': 'https://www.sbiquge.com/33_33805/19177074.html',
          '十二话：承载思念,冰莲玄雷': 'https://www.sbiquge.com/33_33805/19177030.html',
          '新版本：第一章节,往事随风': 'https://www.sbiquge.com/33_33805/19177032.html',
          '新版本：第二章节,接上二卷': 'https://www.sbiquge.com/33_33805/19177033.html',
          '番外①：承诺！我与你的约定！': 'https://www.sbiquge.com/33_33805/19177080.html',
          '第一章：开篇，幻想神域的由来。': 'https://www.sbiquge.com/33_33805/19177063.html',
          '第一话：往事难忘,噩梦惊醒': 'https://www.sbiquge.com/33_33805/19177019.html',
          '第一集：世界和平,苍穹破军': 'https://www.sbiquge.com/33_33805/19177034.html',
          '第七话：夜幕淫笑,战斗再开': 'https://www.sbiquge.com/33_33805/19177025.html',
          '第七集：开篇，止戈若曦再相遇。': 'https://www.sbiquge.com/33_33805/19177069.html',
          '第七集：端木若曦,东方止戈': 'https://www.sbiquge.com/33_33805/19177040.html',
          '第三章：开篇，七星演武的由来。': 'https://www.sbiquge.com/33_33805/19177065.html',
          '第三话：闺蜜神乐,欲斩止戈': 'https://www.sbiquge.com/33_33805/19177021.html',
          '第三集：雷鸣紫电,东方止戈': 'https://www.sbiquge.com/33_33805/19177036.html',
          '第九章：开篇，突如其来的选拔。': 'https://www.sbiquge.com/33_33805/19177071.html',
          '第九话：神乐止戈,战斗再开': 'https://www.sbiquge.com/33_33805/19177027.html',
          '第二章：开篇，等级制度的由来。': 'https://www.sbiquge.com/33_33805/19177064.html',
          '第二话：锥心之痛,铭记于心': 'https://www.sbiquge.com/33_33805/19177020.html',
          '第二集：通天之塔,蓝雷刹那': 'https://www.sbiquge.com/33_33805/19177035.html',
          '第五章：开篇，东方家族战止戈。': 'https://www.sbiquge.com/33_33805/19177067.html',
          '第五话：交错乱入,黑化止戈': 'https://www.sbiquge.com/33_33805/19177023.html',
          '第五集：超能觉醒,阴雷黑鸦': 'https://www.sbiquge.com/33_33805/19177038.html',
          '第八话：爆走梦歌,超能反转': 'https://www.sbiquge.com/33_33805/19177026.html',
          '第八集：幻想神域,正式开篇': 'https://www.sbiquge.com/33_33805/19177041.html',
          '第八集：开篇，突然传来的广播。': 'https://www.sbiquge.com/33_33805/19177070.html',
          '第六章：开篇，止戈与战的目标。': 'https://www.sbiquge.com/33_33805/19177068.html',
          '第六话：三重封印,审问开始': 'https://www.sbiquge.com/33_33805/19177024.html',
          '第六集：通天之塔,设定解析': 'https://www.sbiquge.com/33_33805/19177039.html',
          '第十章：开篇，乱斗选拔秒结束。': 'https://www.sbiquge.com/33_33805/19177072.html',
          '第十话：科学疯子,讲述真相': 'https://www.sbiquge.com/33_33805/19177028.html',
          '第四章：开篇，东方战假意偷袭。': 'https://www.sbiquge.com/33_33805/19177066.html',
          '第四话：交错思念,黑化瞬间': 'https://www.sbiquge.com/33_33805/19177022.html',
          '第四集：超能觉醒,镜花水月': 'https://www.sbiquge.com/33_33805/19177037.html'},
 'story_name': '幻想神域Testament',
 'story_url': 'https://www.sbiquge.com/33_33805/'}




a = {'1':[1,2,3]}
print(a)