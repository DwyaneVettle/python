"""
    练习海龟画图
"""
# 导入库
import turtle

turtle.showturtle()  # 展示画笔
turtle.write("你好")  # 写你好
turtle.forward(300)  # 往前300像素
turtle.color("red")  # 让画笔变成红色
turtle.left(90)  # 往左转90°
turtle.forward(200)
turtle.goto(0, 50)  # 让画笔移动到(0,50)坐标
turtle.forward(30)
turtle.penup()  # 抬笔
turtle.forward(30)
turtle.pendown()  # 落笔
turtle.circle(100)  # 画圆，参数为半径
turtle.width(10)  # 设置画笔的宽度，单位毫米
turtle.done()  # 结束，让幕布不关闭
