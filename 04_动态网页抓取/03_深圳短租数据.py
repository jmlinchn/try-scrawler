# 本项目需要获取前20页短租房源的名称、价格、评价数量、房屋类型、床数量和房客数量。

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

driver = webdriver.Firefox(executable_path=r'D:\DevSoft\selenium-drivers\firefox-driver.exe')
driver.implicitly_wait(5)
driver.get("https://www.airbnb.cn/s/Shenzhen--China?%20page=1")
time.sleep(8)

houses = driver.find_elements_by_css_selector("div._v72lrv")
for each_house in houses:
    # 公寓类型
    house_type = each_house.find_element_by_css_selector("span._faldii7").text
    # 房间价格
    price = each_house.find_element_by_css_selector("span._1d8yint7").find_elements_by_tag_name("span")[2].text
    # 房间描述
    desc = each_house.find_element_by_css_selector("div._qrfr9x5").text
    if house_type == "":
        continue
    print("类型：%s，价格：%s，描述：%s" % (house_type, price, desc))
