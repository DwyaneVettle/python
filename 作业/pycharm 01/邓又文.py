"""
日期2022年02月27日--17:58
使用工具：PyCharm
"""
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(0, -120)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(120, -120)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)