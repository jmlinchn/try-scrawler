import requests

from bs4 import BeautifulSoup

link = 'http://www.santostang.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
# 此处 class_ 有下划线！
first_title = soup.find("h1", class_="post-title").a.text.strip()
print("第一篇文章的标题是：", first_title)

title_list = soup.find_all("h1", class_="post-title")
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print("第%s篇文章的标题是：%s" % (i + 1, title))

# 美化代码
# print(soup.prettify())
