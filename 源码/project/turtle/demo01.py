import turtle

x = -200
y = 200
turtle.pensize(10)
turtle.pencolor("red")

for i in range(1):
    turtle.penup()
    turtle.goto(x , y)
    turtle.pendown()
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)

