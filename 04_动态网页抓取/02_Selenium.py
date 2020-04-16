import time

from selenium import webdriver

# 设置禁用css/图片/js的加载
# fp = webdriver.FirefoxProfile()
# fp.set_preference("permissions.default.stylesheet", 2)
# fp.set_preference("permissions.default.image", 2)
# fp.set_preference("javascript.enabled", False)

# executable_path 属性修改为电脑中相应 driver.exe 程序的地址
driver = webdriver.Firefox(executable_path=r'D:\DevSoft\selenium-drivers\firefox-driver.exe')

# driver = webdriver.Chrome(executable_path=r'D:\DevSoft\selenium-drivers\chrome-driver.exe')

# driver = webdriver.Edge(executable_path=r'D:\DevSoft\selenium-drivers\edge-driver.exe')

driver.implicitly_wait(20)  # 隐性等待，一找到就开始执行

driver.get("http://www.santostang.com/2018/07/04/hello-world/")

time.sleep(8)

# 下滑到页面底部
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 由于评论内容在 iframe 中，需要定位到 iframe 中进行查找
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
commentList = driver.find_elements_by_css_selector('div.reply-wrapper')
for comment in commentList:
    writer = comment.find_element_by_class_name('writer-name').find_element_by_tag_name("span").text
    content = comment.find_element_by_class_name('reply-content').find_element_by_tag_name("p").text
    print("%s 发表了 %s\n" % (writer, content))

# 其实，selenium选择元素的方法有很多，具体如下所示：
# find_element_by_id：通过元素的id选择，例如:driver.find_element_by_id(‘loginForm’)
# find_element_by_name：通过元素的name选择，driver.find_element_by_name(‘password’)
# find_element_by_xpath：通过xpath选择，driver.find_element_by_xpath(“//form[1]”)
# find_element_by_link_text：通过链接地址选择
# find_element_by_partial_link_text：通过链接的部分地址选择
# find_element_by_tag_name：通过元素的名称选择
# find_element_by_class_name：通过元素的class选择
# find_element_by_css_selector：通过css选择器选择
# 有时候，我们需要查找多个元素。在上述例子中，我们就查找了所有的评论。因此，也有对应的元素选择方法，就是在上述的element后加上s，变成elements。
# – find_elements_by_name
# – find_elements_by_xpath
# – find_elements_by_link_text
# – find_elements_by_partial_link_text
# – find_elements_by_tag_name
# – find_elements_by_class_name
# – find_elements_by_css_selector
