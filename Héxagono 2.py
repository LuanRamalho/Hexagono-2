import turtle
turtle.speed(0)
def triângulo(posx, posy,lado):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()

    for i in range(6):
        turtle.forward(lado)
        turtle.left(60)
        turtle.hideturtle()
    turtle.end_fill()

turtle.color('black', 'blue')
turtle.begin_fill()
triângulo(-625,150,100)

turtle.color('gray', 'yellow')
turtle.begin_fill()
triângulo(-400,150,100)

turtle.color('darkgreen', 'cyan')
turtle.begin_fill()
triângulo(-175,150,100)

turtle.color('red', 'orange')
turtle.begin_fill()
triângulo(50,150,100)

turtle.color('black', 'violet')
turtle.begin_fill()
triângulo(275,150,100)

turtle.color('orange', 'lightblue')
turtle.begin_fill()
triângulo(500,150,100)

turtle.color('green', 'pink')
turtle.begin_fill()
triângulo(-625,-75,100)

turtle.color('cyan', 'magenta')
turtle.begin_fill()
triângulo(-400,-75,100)

turtle.color('yellow', 'darkblue')
turtle.begin_fill()
triângulo(-175,-75,100)

turtle.color('black', 'green')
turtle.begin_fill()
triângulo(50,-75,100)

turtle.color('gray', 'purple')
turtle.begin_fill()
triângulo(275,-75,100)

turtle.color('yellow', 'darkcyan')
turtle.begin_fill()
triângulo(500,-75,100)

turtle.color('violet', 'lightgreen')
turtle.begin_fill()
triângulo(-625,-300,100)

turtle.color('blue', 'darkorange')
turtle.begin_fill()
triângulo(-400,-300,100)

turtle.color('darkred', 'darkred')
turtle.begin_fill()
triângulo(-175,-300,100)

turtle.color('violet', 'darkgray')
turtle.begin_fill()
triângulo(50,-300,100)

turtle.color('blue', 'brown')
turtle.begin_fill()
triângulo(275,-300,100)

turtle.color('pink', 'gray')
turtle.begin_fill()
triângulo(500,-300,100)

turtle.done()