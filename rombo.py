from ctypes.wintypes import POINT
from graphics import *


def drawLine(x1, y1, x2, y2, color):
    ln = Line(Point(x1, y1), Point(x2, y2))
    ln.setOutline(color)
    ln.setWidth(3)

    return ln


def main():
    win = GraphWin("Window", 600, 600)
    win.setBackground(color_rgb(0, 0, 0))

    xValue = 10
    yValue = 5

    while yValue < 300:
        ln1 = drawLine(xValue, 300-yValue, xValue, 300+yValue, "blue")
        ln1.draw(win)

        xValue += 5
        yValue += 5

    while yValue > 0:
        ln1 = drawLine(xValue, 300-yValue, xValue, 300+yValue, "red")
        ln1.draw(win)

        xValue += 5
        yValue -= 5

    win.getMouse()
    win.close()


main()
