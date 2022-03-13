import turtle
turtle.width(7)
turtle.color("black")
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(150,0)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(150,-150)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.hideturtle()
turtle.done()