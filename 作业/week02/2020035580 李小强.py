# 作业: 1.熟悉python安装环境: 2.画4个正方形
import turtle
t = turtle.Pen()

for x in range(4):
    t.width(4)
    t.forward(90)
    t.left(90)

t.penup()
t.goto(200,0)
for x in range(4):
    t.left(90)
    t.pendown()
    t.forward(90)

t.penup()
t.goto(200, 100)
for x in range(4):
    t.left(90)
    t.pendown()
    t.forward(90)

t.penup()
t.goto(90,100)
for x in range(4):
    t.left(90)
    t.pendown()
    t.forward(90)


