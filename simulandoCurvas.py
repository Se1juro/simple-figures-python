from ctypes.wintypes import POINT
from graphics import *


def drawLine(x1, y1, x2, y2, color):
    ln = Line(Point(x1, y1), Point(x2, y2))
    ln.setOutline(color)
    ln.setWidth(3)

    return ln


def main():
    win = GraphWin("Window", 400, 450)
    win.setBackground(color_rgb(0, 0, 0))

    for x in range(0, 200, 10):
        ln = drawLine(200, x, x+200, 200, "blue")
        ln2 = drawLine(200, x, 200-x, 200, "blue")
        ln2.draw(win)
        ln.draw(win)
    for j in range(400, 200, -10):
        ln = drawLine(200, j, 600-j, 200, "blue")
        ln2 = drawLine(200, j, j-200, 200, "blue")
        ln2.draw(win)
        ln.draw(win)

    win.getMouse()
    win.close()


main()
