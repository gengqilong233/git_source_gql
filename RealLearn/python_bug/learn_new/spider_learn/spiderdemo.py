import requests
import json
import xml.etree.ElementTree as EF
from xml.parsers.expat import ParserCreate

class DefailtSaxHandler(object):
    def __init__(self, province):
        self.province = province

    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.province.append([name,number])

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

class GetProvices(object):
    def __init__(self, url):
        self.url = url
        self.provice = []

    def get_province(self, content):
        handle = DefailtSaxHandler(self.provice)
        parser = ParserCreate()
        parser.StartElementHandler = handle.start_element
        parser.EndElementHandler = handle.end_element
        parser.CharacterDataHandler = handle.char_data
        parser.Parse(content)
        return self.provice


    def get_accur_provice(self):
        for i in self.provice:
            url = self.url.replace('/post/', '') + i[1]
            r = requests.request('get', url)
            r.encoding = 'gbk'
            data = r.text
            print(data)
            start = data.find('<table cellpadding="0" cellspacing="1" align="center" width="960"  style="line-height: 30px;background: #cccccc;" class="t12">')
            end = data.find('<div align="center">')
            content = data[start:end + len('<div align="center">')]
            print(content)


    def run(self):
        content = requests.get(self.url) # .content.decode('gb2321')
        content.encoding = 'gbk'
        data = content.text
        # print(data)
        start = data.find('<map name="map_86" id="map_86">')
        end = data.find('</map>')
        content = data[start:end + len('</map>')].strip()
        print(content)

        print(self.get_province(content))
        # self.get_accur_provice()


if __name__ == '__main__':
    url = 'http://www.ip138.com/post/'
    GetProvices(url).run()




# provice = get_provice_entry('http://www.ip138.com/post/')  # ('http://www.ip138.com/post/')  'http://news.baidu.com/'
# print(provice)



