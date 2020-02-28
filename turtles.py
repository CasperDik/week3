import turtle

#sides = float(input("how many equal sides does the shape need to have: "))

screen = turtle.Screen()
casper = turtle.Turtle()

sides = 3
forward = 10
angle = 360 / sides

x = sides**5

for i in range(x):
    casper.speed(x**i)
    if i % sides == 0:
        casper.forward(i/sides)
    else:
        casper.pendown()
        casper.forward(forward + (5*forward/sides))
        casper.right(angle)
        casper.penup()


screen.exitonclick()