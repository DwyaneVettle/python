import turtle
turtle.pen()
turtle.color("black")
turtle.width(10)
for j in range(4):
    x=0
    y=0
    if j==1:
        x=240
    elif j==2:
        y=240
    elif j==3:
        x=240
        y=240
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
