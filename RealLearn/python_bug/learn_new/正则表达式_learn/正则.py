    # 正则表达式
# [0-9]任意一个数字，等价 \d
# [a-z]任意小写字母
# [A-Z]


import re

# 3位数字-3到8个数字 \d{3}-\d{3,8}
mr = re.match(r'\d{3}-\d{3,8}','010-123456')
print(mr.string)

# 分组
m = re.match(r'(\d{3})-(\d{3,8})$','010-123456')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))


p = re.compile(r'\d+')
print(p.split('one1two2'))
