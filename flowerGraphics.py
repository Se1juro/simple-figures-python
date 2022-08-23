from ctypes.wintypes import POINT
from graphics import *


def drawLine(x1, y1, x2, y2, color):
    ln = Line(Point(x1, y1), Point(x2, y2))
    ln.setOutline(color)
    ln.setWidth(3)

    return ln


def drawCircle(win, positionPoint, radius):
    for i in range(10):
        point = Point(positionPoint, positionPoint)
        cir = Circle(point, radius)
        cir.setOutline("blue")
        cir.setWidth(2)
        cir.draw(win)
        positionPoint -= 5
        radius -= 3


def main():
    win = GraphWin("Window", 750, 750)
    win.setBackground(color_rgb(0, 0, 0))

    positionPoint = 300
    radius = 100
    point = Point(positionPoint, positionPoint)
    cir = Circle(point, radius)
    cir.setOutline("blue")
    cir.setWidth(2)
    cir.draw(win)
    positionPoint -= 5
    radius -= 3
    cir2 = Circle(point, radius)
    cir2.setOutline("red")
    cir2.setWidth(2)
    cir2.draw(win)
    """ for i in range(10):
        #drawCircle(win, positionPoint, radius)
        positionPoint -= 50 """

    win.getMouse()
    win.close()


main()
