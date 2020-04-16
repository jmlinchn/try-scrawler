import re

# match 只能从起始位置匹配
m_match = re.match('com', 'www.baidu.com')
# search 可以扫描整个字符串，并返回第一个成功的匹配
m_search = re.search('com', 'www.baidu.com')

print(m_match)
print(m_search)
