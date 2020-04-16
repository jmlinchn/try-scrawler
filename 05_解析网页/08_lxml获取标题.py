import requests
from lxml import etree

link = 'http://www.santostang.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

r = requests.get(link, headers=headers)
html = etree.HTML(r.text)
# //h1 在文档中的任何位置选取<h1>元素
# @class="post-title" 选取<h1>元素中class为post-title的元素
# /a 选取<h1>元素中的<a>元素
# /text() 提取<a>元素中的所有文本
title_list = html.xpath('//h1[@class="post-title"]/a/text()')
print(title_list)
