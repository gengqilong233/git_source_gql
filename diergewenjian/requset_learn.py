import requests
import bs4

url = 'https://music.163.com/'
r = requests.request('get', url)
data = r.text
# print(data)

soup = bs4.BeautifulSoup(data, 'lxml')

p = soup.find('p')
print('获取第一个标签p: %s' % p)
print('获取其中的字符串: %s' % p.string)
print('获取标签名: ', p.name)
print('获取类属性：', p['class'])
print('-'*60)


# find_all( name , attrs , recursive , string , **kwargs )
# name 参数：可以查找所有名字为 name 的tag。
# attr 参数：就是tag里的属性。
# string 参数：搜索文档中字符串的内容。
# recursive 参数： 调用tag的 find_all() 方法时，Beautiful Soup会检索当前tag的所有子孙节点。如果只想搜索tag的直接子节点，可以使用参数 recursive=False 。
p_all = soup.find_all(name='p', attrs='s-fc3') # 标签p和class查
print('通过标签p和class查: ', p_all)
print('-'*60)

p_all = soup.find_all(name='p', string='很抱歉，服务器开小差了，请稍后再试') # 标签p和字符串查
print('通过标签p和字符串查：', p_all)
print('-'*60)

p_all = soup.find_all('p')
for a in p_all:
    print(a)
print('-'*60)



