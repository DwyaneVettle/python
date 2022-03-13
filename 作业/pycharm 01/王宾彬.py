import turtle

turtle.width(1)
turtle.color("red")
arr = [[0, 0], [70, 0], [0, -70], [70, -70]]

for i in range(len(arr)):
    # 定位
    index = arr[i]
    turtle.penup()
    turtle.goto(index[0], index[1])

    # 画正方形
    turtle.pendown()
    for j in range(4):
        turtle.forward(50)
        turtle.right(90)
