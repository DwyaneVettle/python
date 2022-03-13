#date：2022/2/27
import turtle

for i in range(4):
    turtle.forward(60)
    turtle.left(90)

turtle.penup()
turtle.goto(100,0)
turtle.pendown()
for i in range(4):
    turtle.forward(60)
    turtle.left(90)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
for i in range(4):
    turtle.forward(60)
    turtle.left(90)

turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
for i in range(4):
    turtle.forward(60)
    turtle.left(90)