import re

line = "Fat cats are smarter then dogs, is it right?"
m = re.match(r'(.*) are (.*?) dogs', line)
print('匹配的整句话', m.group(0))
print('匹配的第一个结果', m.group(1))
print('匹配的第二个结果', m.group(2))
print('匹配的结果列表', m.groups())
