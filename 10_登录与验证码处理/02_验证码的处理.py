# 使用命令 "pip install pytesseract" 安装 pytesseract

from PIL import Image
import pytesseract

im = Image.open('captcha.jpg')

# 步骤01：将彩色图片转为灰度图片
gray = im.convert('L')
# gray.show()

# 步骤02：二值化处理，将大于某个临界灰度值的灰度像素设置为灰度最大值
# 主要是为了降噪，去掉不需要的背景和干扰线
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
# out.show()
out.save('captcha_threshold.jpg')

# 步骤03：使用 Tesseract 进行图片识别
th = Image.open('captcha_threshold.jpg')
print(pytesseract.image_to_string(th))
