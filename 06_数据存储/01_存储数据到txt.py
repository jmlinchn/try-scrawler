title = "This is a test sentense"

# 在文件路径前面添加 r(raw string) 代表将内容当做纯粹的字符串处理
output = '\t'.join(['name', 'title', 'age', 'gender'])
with open(r"../temp/txt_output.txt", "w+", encoding='UTF-8') as f:
    f.write(output)
    f.close()
