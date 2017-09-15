import turtle
radius = turtle.numinput('','Enter a number for your circle\'s radius: ')

#Defining a function to make a circle
def olympicRings(arg):
    turtle.pensize(12)

    turtle.pu()
    turtle.goto(-300, 100)
    turtle.pd()
    turtle.color('blue')
    turtle.circle(int(arg))

    turtle.pu()
    turtle.goto(-200, 100)
    turtle.pd()
    turtle.color('black')
    turtle.circle(int(arg))

    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.color('red')
    turtle.circle(int(arg))

    turtle.pu()
    turtle.goto(-150, 20)
    turtle.pd()
    turtle.color('green')
    turtle.circle(int(arg))

    turtle.pu()
    turtle.goto(-250, 20)
    turtle.pd()
    turtle.color('yellow')
    turtle.circle(int(arg))

#Call the function on input radius to make all olympic rings
olympicRings(radius)
