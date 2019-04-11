import requests
import bs4
import time


class get_story(object):
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def request_txt(self, url):
        try:
            print('开始请求网页数据...')
            head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.3'}
            r = requests.request('get', url, headers=head)
            return r.text

        except Exception as e:
            print('request请求失败：%s' % e)
            exit(1)

    def get_message(self, data, url):
        try:
            print('获取目录中...')
            message_dict = {}
            soup = bs4.BeautifulSoup(data, 'lxml')
            soup_all = soup.find_all('div', attrs='listmain')

            for i in soup_all[0].dl.children:
                i = i.find('a')

                if 'href' in str(i):
                    soup_title = i.text
                    soup_url = url + str(i['href'].split('/')[2])
                    print(soup_title, soup_url)

                    if soup_title in message_dict.keys():
                        del message_dict[soup_title]
                        message_dict[soup_title] = soup_url
                    else:
                        message_dict[soup_title] = soup_url
                else:
                    pass
            return message_dict
        except Exception as e:
            print('获取章节、url失败： %s' % e)

    def get_txt(self, dic, path):
        for key, value in dic.items():
            print('开始记录 %s 内容...' %key)
            msg = self.request_txt(value)
            time.sleep(2)

            soup = bs4.BeautifulSoup(msg, 'lxml')
            soup_txt = soup.find('div', attrs='showtxt').text
            self.save_txt(soup_txt, path)

    def save_txt(self, msg, path):
        with open(path, 'a+', encoding='utf8') as f:
            f.write(msg + '\n' + '\n')

    def run(self):
        request_result = self.request_txt(self.url)
        catalog = self.get_message(request_result, self.url)
        self.get_txt(catalog, self.path)





url = 'https://www.sbiquge.com/0_466/'
path = '/Users/gengqilong/Desktop/pythonProgram/RealLearn/python_bug/diergewenjian/spiderr_txt/遮天.txt'

a = get_story(url, path)
a.run()


