import re

m = re.match('www', 'www.baidu.com')

print("匹配结果是：", m)
print("匹配的起始与终点", m.span())
print("匹配的起始位置", m.start())
print("匹配的终点位置", m.end())
