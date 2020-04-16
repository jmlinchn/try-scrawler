import re
import time

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# 循环获取10页数据
for i in range(0, 10):
    link = 'https://beijing.anjuke.com/sale/p' + str(i)
    r = requests.get(link, headers=headers)
    print("现在爬取的是第", i + 1, "页")

    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('li', class_="list-item")

    for index, house in enumerate(house_list):
        # 使用content获取子元素
        name = house.find('div', class_='house-title').a.text.strip()
        area = house.find("div", class_="details-item").find_all("span")[1].text
        address = house.find("span", class_="comm-address").text.strip()
        address = re.sub(r"\s+", " ", address)
        price = house.find('span', class_='price-det').text.strip()
        price_area = house.find('span', class_='unit-price').text.strip()

        # 解析房屋详情页，只爬取房屋编码作为样例
        href = house.find('div', class_='house-title').a.attrs["href"]
        r = requests.get(href, headers=headers)
        soup_detail = BeautifulSoup(r.text, 'lxml')
        house_code = soup_detail.find('span', id="houseCode").text.strip()
        house_code = re.sub(r"\s+", " ", house_code)

        print(i * 60 + index + 1, name)
        print("\t", house_code, address, area, price, price_area)
        time.sleep(5)

    # 注意不能请求太过频繁，不然容易被网站禁用ip，或者要求人工验证
    time.sleep(10)
