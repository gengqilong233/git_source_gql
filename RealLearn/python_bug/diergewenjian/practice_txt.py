import requests
import bs4
import time
import os
import operator
from pprint import pprint


class get_story(object):
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def request_txt(self, url):
        flag = True

        while flag:
            try:
                print('开始请求网页数据...')
                head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.3'}
                r = requests.request('get', url, headers=head, timeout=5)
                flag = False
                return r.text
            except Exception as e:
                print('request_txt方法将重新请求，失败原因：%s' % e)
                flag = True

    def get_story_type(self, url):
        try:
            print('获取小说大类中...')
            type_list = []
            data = self.request_txt(url)

            soup = bs4.BeautifulSoup(data, 'lxml')
            soup_catalog = soup.find_all('div', attrs='nav')

            for i in soup_catalog[0].ul.children:
                c = i.find('a')

                if 'href' in str(c):
                    if '首页' in str(c) or '临时书架' in str(c):
                        pass
                    else:
                        story_type = c.text
                        story_type_url = url + str(c['href'].split('/')[1])
                        # print(story_type, story_type_url)

                        if story_type in str(type_list):
                            pass
                        else:
                            type_list.append({'type': story_type,
                                              'type_url': story_type_url,
                                              'story_list': {}})
                else:
                    pass
            return type_list
        except Exception as e:
            print('get_stroy_type方法失败： %s' % e)

    def get_story_list(self, dict):
        try:
            a = 0
            url = dict['type_url']
            type = dict['type']
            print('开始获取 %s 类小说列表...' % type)
            time.sleep(1)

            data = self.request_txt(url)

            soup = bs4.BeautifulSoup(data, 'lxml')
            list = soup.find('div', attrs='r bd')
            for i in list.ul.children:
                c = i.find('a')

                if 'href' in str(c):
                    story_name = c.text
                    story_url = 'https://www.sbiquge.com' + str(c['href'])
                    # print(story_name, story_url)

                    dict['story_list']['story' + str(a)] = {'story_name': story_name,
                                                            'story_url': story_url,
                                                            'list': {}}

                    a += 1
                else:
                    pass
            return dict
        except Exception as e:
            print('get_story_list方法失败：%s' % e)

    def get_message(self, dict):
        try:
            url = dict['story_url']
            story_name = dict['story_name']
            print('获取 %s 目录中...' % story_name)
            time.sleep(1)

            data = self.request_txt(url)

            soup = bs4.BeautifulSoup(data, 'lxml')
            soup_all = soup.find_all('div', attrs='listmain')

            for i in soup_all[0].dl.children:
                i = i.find('a')

                if 'href' in str(i):
                    soup_title = i.text
                    soup_url = url + str(i['href'].split('/')[2])
                    # print(soup_title, soup_url)

                    if soup_title in dict['list'].keys():
                        del dict['list'][soup_title]
                        dict['list'][soup_title] = soup_url
                    else:
                        dict['list'][soup_title] = soup_url
                else:
                    pass

            return dict
        except Exception as e:
            print('get_message方法失败： %s' % e)

    def get_txt(self, chapter_name, chapter_url):
        try:
            print('开始记录 %s 内容...' % chapter_name)
            msg = self.request_txt(chapter_url)
            time.sleep(1)

            soup = bs4.BeautifulSoup(msg, 'lxml')
            soup_txt = soup.find('div', attrs='showtxt').text
            return soup_txt
        except Exception as e:
            print('get_txt方法失败：%s' % e)

    def make_dir(self, name):
        try:
            path = self.path + name
            isExists = os.path.exists(path)

            if not isExists:
                print('开始创建 %s 文件夹...' % name)
                os.makedirs(path)
                # os.chdir(path)
                print('创建 %s 文件夹成功！！！' % name)
            else:
                print('%s 文件夹已存在，可直接使用!!!' % name)
        except Exception as e:
            print('make_dir方法失败：%s' % e)

    def save_txt(self, msg, name):
        path = self.path + name + '.txt'
        with open(path, 'a+', encoding='utf8') as f:
            f.write('\n' + '\n' + str(msg) + '\n' + '\n')

    def run(self):

        type_list = self.get_story_type(self.url)
        self.save_txt(type_list, '小说大类type_list')
        # pprint(type_list)

        for type in type_list:
            type_dir_path = type['type']
            self.make_dir(type_dir_path)

            type_dict = self.get_story_list(type)
        # pprint(type_list)

            for story_no, story_detail in type_dict['story_list'].items():
                story_name = story_detail['story_name']

                story_dir_path = type_dir_path + '/' + story_name
                self.make_dir(story_dir_path)

                path = type_dir_path + '/' + "小说列表type['story_list']"
                self.save_txt(type['story_list'], path)

                story_dict = self.get_message(story_detail)

                a = 1
                for chapter_name, chapter_url in story_dict['list'].items():

                    chapter_dir_path = story_dir_path + '/' + str(a) +chapter_name

                    story_txt = self.get_txt(chapter_name, chapter_url)
                    self.save_txt(story_txt, chapter_dir_path)
                    a += 1
                exit(1)



        # catalog = self.get_message(request_result, self.url)
        # self.get_txt(catalog, self.path)





url = 'https://www.sbiquge.com/'
url2 = 'https://www.sbiquge.com/'
path = '/Users/gengqilong/Desktop/pythonProgram/RealLearn/python_bug/diergewenjian/spiderr_txt/'

a = get_story(url2, path)
a.run()


