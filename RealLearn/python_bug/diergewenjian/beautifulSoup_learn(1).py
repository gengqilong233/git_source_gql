from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml') # 声明BeautifulSoup对象
find = soup.find('p') # 查找标签，还可用find_all查到所有标签遍历查找下列内容
print('标签返回类型: %s'%type(find))
print('第一个标签: %s' % find)
print('获取标签名: %s' % find.name)
print('获取标签class属性: %s' % find['class'])
print('获取标签文本: %s' % find.string)

print(soup.parent)



# # 判断注释
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'lxml')
# comment = soup.b.string # 获取注释
# print(type(comment))
# print(comment)
#
# if type(comment) == bs4.element.Comment:
#     print('该字符是注释')
# else:
#     print('该字符不是注释')


# # 父子标签学习
# a = '''<div id="content-innerText">
#   <p>
#     <img src="http://222.186.150.182/wp-content/uploads/2016/02/2016-10-30_22-28-51.jpg" title="" alt="" width="801" height="1200">
#     <img src="http://222.186.150.182/wp-content/uploads/2016/02/2016-10-30_22-28-52.jpg" title="" alt="" width="1080" height="1616">
#     <img src="http://222.186.150.182/wp-content/uploads/2016/02/2016-10-30_22-28-48.jpg" title="" alt="" width="682" height="1024">
#     <img src="http://222.186.150.182/wp-content/uploads/2016/02/2016-10-30_22-28-49.jpg" title="" alt="" width="682" height="1024">
#     <img src="http://222.186.150.182/wp-content/uploads/2016/02/2016-10-30_22-28-491.jpg" title="" alt="" width="682" height="1024">
#     <img src="http://222.186.150.182/wp-content/uploads/2016/02/2016-10-30_22-28-50.jpg" title="" alt="" width="682" height="1024">
#   </p>
# </div>'''
#
# b = bs4.BeautifulSoup(a, 'lxml')
# # c = b.find_all('div')
# #
# # for i in c[0].p.children:
# #     print(i.src)
# #     print(type(i))
#
#
# elem = b.find_all("div", {"id": "content-innerText"})
# for i in elem[0].p.children:
#     if 'img' in str(i):
#         print('哈哈： ' + str(i['src']))
#     else:
#         pass
#     # print(type(i))