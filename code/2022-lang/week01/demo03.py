import turtle

# 调整画笔的宽度
turtle.width(10)

# 第一个圆
turtle.color("blue")
turtle.circle(50)

# 第二个圆
turtle.color("black")
turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.circle(50)

# 第三个圆
turtle.color("red")
turtle.penup()
turtle.goto(240, 0)
turtle.pendown()
turtle.circle(50)

# 第四个圆
turtle.color("yellow")
turtle.penup()
turtle.goto(60, -50)
turtle.down()
turtle.circle(50)

# 第五个圆
turtle.color("green")
turtle.penup()
turtle.goto(180, -50)
turtle.pendown()
turtle.circle(50)

# 画布不关闭
turtle.done()
