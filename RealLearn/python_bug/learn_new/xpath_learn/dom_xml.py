from xml.dom import minidom

doc = minidom.parse(r'D:\pycharm\PythonImport\RealLearn\python_bug\learn_new\xpath\book')
root = doc.documentElement
print(type(root))
# print(dir(root))
print(root.nodeName)
books = root.getElementsByTagName('book')
print(books)
for book in books:
    titles = root.getElementsByTagName('title')[0].childNodes[0].nodeValue
    prices = root.getElementsByTagName('price')[0].childNodes[0].nodeValue
    print(titles)
    print(prices)

