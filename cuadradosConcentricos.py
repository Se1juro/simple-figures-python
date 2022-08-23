from ctypes.wintypes import POINT
from graphics import *


def drawLine(x1, y1, x2, y2, color):
    ln = Line(Point(x1, y1), Point(x2, y2))
    ln.setOutline(color)
    ln.setWidth(3)

    return ln


def main():
    win = GraphWin("Window", 700, 750)
    win.setBackground(color_rgb(0, 0, 0))

    variar = 0
    center = 380

    for x in range(1, 31):
        ln = drawLine(center-variar, center-variar, center -
                      variar+variar*2, center-variar, "blue")
        ln.draw(win)
        ln = drawLine(center-variar, center-variar, center -
                      variar, center-variar+variar*2,  "red")
        ln.draw(win)
        ln = drawLine(center-variar+variar*2, center-variar, center -
                      variar+variar*2, center-variar+variar*2,  "green")
        ln.draw(win)
        ln = drawLine(center-variar, center-variar+variar*2, center -
                      variar+variar*2, center-variar+variar*2,  "yellow")
        ln.draw(win)
        variar += 10

    win.getMouse()
    win.close()


main()
