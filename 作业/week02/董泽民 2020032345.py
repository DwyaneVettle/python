# author by Michealzou@126.com
# 2022/2/21 17.24
# 作业：1.熟悉python安装环境；2.画四个正方形



import turtle
# 第一个正方形
turtle.color("red")
turtle.width(2)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# 第二个正方形
turtle.penup()
turtle.goto(150,0)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# 第三个正方形
turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# 第四个正方形
turtle.penup()
turtle.goto(150,-150)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)