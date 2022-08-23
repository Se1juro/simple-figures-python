import turtle


def drawCircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius -= 4


def drawFlower():
    for i in range(10):
        drawCircle(150)
        turtle.right(36)


def main():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.pensize(2)
    turtle.pencolor("blue")
    drawFlower()
    turtle.done()


main()
