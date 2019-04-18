import requests
import bs4
import os
import time


class BeautifulPicture(object):
    def __init__(self, url, picture_path):
        self.url = url
        self.picture_path = picture_path

    def requests(self, url):
        try:
            r = requests.request('get', url)
            data = r.text
            return data
        except Exception as e:
            print(e)

    def make_dir(self, picture_path):
        isExists = os.path.exists(picture_path)
        if not isExists:
            print('【开始创建图片文件夹...】')
            os.makedirs(picture_path)
            os.chdir(picture_path)
            print('创建成功')
        else:
            print('改文件夹已存在，可直接使用...')
            os.chdir(picture_path)
            pass
            # print(picture_path, '文件夹路径已存在,请更换路径')
            # exit(0)

    def save_img(self, img_url):
        name = img_url.split('/')[3].split('?')[0]
        file_name = str(name) + '.jpg'
        img = requests.request('get', img_url)
        time.sleep(5)
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def get_picture(self):
        print('开始请求网页数据...')
        data = self.requests(self.url)

        all_http = []
        soup = bs4.BeautifulSoup(data, 'lxml')
        img_all = soup.find_all('img', '_2zEKz')

        for img in img_all:
            img_http = img.get('src')
            print(img)
            print(type(img))
            if img_http:
                if img_http in all_http:
                    pass
                else:
                    all_http.append(img_http)


        print(all_http)

        # self.make_dir(self.picture_path)
        #
        # for picture_http in all_http:
        #     print(picture_http)
        #     self.save_img(picture_http)



url = 'https://unsplash.com/'
path = '/Users/gengqilong/Desktop/pythonProgram/RealLearn/python_bug/diergewenjian/spider_img'

a = BeautifulPicture(url, path)
a.get_picture()







