from ctypes.wintypes import POINT
from graphics import *


def drawCircle(win, posX, posY, radius, color="blue"):
    point = Point(posX, posY)
    cir = Circle(point, radius)
    cir.setOutline(color)
    cir.setWidth(2)
    cir.draw(win)


def main():
    win = GraphWin("Window", 1800, 700)
    win.setBackground(color_rgb(0, 0, 0))

    colors = ["red", "green", "yellow", "purple", "magenta",
              "blue", "white", "orange", "pink", "olive"]

    # Top side
    initialX = 900
    initialY = 200
    radius = 120
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialY += 4
        radius -= 4

    # Top Left side
    initialX = 813
    initialY = 240
    radius = 120
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialY += 2
        initialX += 3.5
        radius -= 4

    # Top right side
    initialX = 978
    initialY = 230
    radius = 120
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialY += 3.5
        initialX -= 2
        radius -= 4

    # Right side
    radius = 120
    initialX = 1020
    initialY = 320
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialX -= 4
        radius -= 4

    # Bottom Right side
    radius = 120
    initialX = 982
    initialY = 410
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialY -= 3
        initialX -= 3
        radius -= 4

    # Left side
    radius = 120
    initialX = 780
    initialY = 320
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialX += 4
        radius -= 4

    # Bottom side
    radius = 120
    initialX = 900
    initialY = 440
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialY -= 4
        radius -= 4

    # Bottom Left side
    radius = 120
    initialX = 810
    initialY = 400
    for color in colors:
        drawCircle(win, initialX, initialY, radius, color)
        initialY -= 2
        initialX += 4
        radius -= 4

    win.getMouse()
    win.close()


main()
