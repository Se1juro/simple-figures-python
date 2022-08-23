from ctypes.wintypes import POINT
from graphics import *


def drawLine(x1, y1, x2, y2, color):
    ln = Line(Point(x1, y1), Point(x2, y2))
    ln.setOutline(color)
    ln.setWidth(3)

    return ln


def main():
    win = GraphWin("Window", 750, 750)
    win.setBackground(color_rgb(0, 0, 0))

    valX1 = 10
    valX2 = 70
    valY1 = 10
    valY2 = 70
    for x in range(0, 10):
        for j in range(0, 10):
            rect = Rectangle(
                Point(valX1, valY1), Point(valX2, valY2))
            rect.setOutline("red")
            rect.draw(win)
            valX2 += 70
            valX1 += 70
        valY1 += 70
        valY2 += 70
        valX1 = 10
        valX2 = 70

    win.getMouse()
    win.close()


main()
