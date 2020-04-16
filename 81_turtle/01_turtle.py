import turtle as t  # 引入海龟模块

t.screensize(500, 500, "white")  # 设置窗口大小，颜色
t.reset()  # 复位
t.penup()  # 抬笔
t.goto(-200, 200)  # 移动笔到坐标点，（0，0）在中心
t.pendown()  # 下笔
for i in range(0, 4):
    t.forward(40)  # 画一段
    t.right(90)  # 右转

t.hideturtle()  # 把海龟藏起来
