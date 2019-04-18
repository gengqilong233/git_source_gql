# map() # 接收2参数，1：函数，2：一个list

def f(x):
    return x * x

l = [1,2,3,4]
c = map(f, l)
d = list(c)
print(d)

a = list(map(str,l)) # 用str方法将list变为字符串的list
print(a)

