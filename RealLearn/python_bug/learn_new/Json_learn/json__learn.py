import json

a = {'1':'aaa', '2':'bbb'}
print(a)
print(type(a))

b = json.dumps(a) # dic转str
print(b)
print(type(b))

c = json.loads(b) # str转dic
print(c)
print(type(c))


