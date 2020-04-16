import re

m_match = re.match('[0-9]+', '12345 is the first number, 23456 is the second')
m_search = re.search('[0-9]+', 'The first number is 12345, 23456 is the second')
# 找到所有的匹配，返回数组
m_findall = re.findall('[0-9]+', '12345 is the first number, 23456 is the second')

print(m_match.group())
print(m_search.group())
print(m_findall)
