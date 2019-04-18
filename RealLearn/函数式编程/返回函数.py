# # 可变参数
# def dsad(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
# # print(dsad(*(1,2,3)))
#
# # 返回函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax +n
#         return ax
#     return sum
#
#
# f1 = lazy_sum(1,3,5,7,9) # 得到的结果是求和公式
# print('f:', f1)
# F = f1() # 调用f1时，才是真正的结果
# print('f1求和结果：',F) #
#
# f2 = lazy_sum(1,3,5,7,9) # 即使传入相同的参数，都会得到一个新的函数，且不相等
# print('f2:',f2)
# print('f1判断f2相等：',f1 == f2)

map = {'1':'wqe', '2':'aaa'}
print(map)


del  map['1']
print(map)
