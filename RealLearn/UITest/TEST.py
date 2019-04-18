
# a = input('输入:')
# if a.count('aa') > 0 and a.count('bb')==0:
#     print('hahaha')
# elif a.count('bb')>0 and a.count('aa') == 0:
#     print("You're out")
# elif a.count('aa')>0 and a.count('bb') > 0:
#     print('sadadasdsdadsad')
# else:
#     print('You seem to be debt')

# a = input('输入姓名：')
# b = int(input('输入数量:'))
# c = int(input('请输入单价:'))
#
# if b >= 0 and c >= 0:
#     d = b * c
#     print('共需付%s元，感谢光临%s' % (d, a))
# else:
#     print('输入数量、单价不可为负数')

# list = ['香蕉', '苹果', '梨']
# list_need = []
# a = input('输入一个值：')
# if list.count(a) > 0:
#     list_need.append(a)
#     print('我们有%s' %a)
#     b = input('输入第二个：')
#     if list.count(b) > 0:
#         list_need.append(b)
#         print('你需要的是 %s ,稍后' %list_need)
#     else:
#         print('对不起 %s 没了,你要的是：%s' % (a, list_need))
# else:
#     print('对不起 %s 没了,我们有：%s' %(a, list))


s = input('输入验证码：')
print(s)
print(type(s))