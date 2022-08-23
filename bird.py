from ctypes.wintypes import POINT
from graphics import *


def line(x1, y1, x2, y2):
    return Line(Point(x1, y1), Point(x2, y2))


def main():
    win = GraphWin("Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    """ pt1 = Point(250, 250)
    pt2 = Point(250, 350) """

    """ pt1.setOutline(color_rgb(255, 255, 0))
    pt1.draw(win) """

    ln = line(250, 100, 250, 350)
    ln.setOutline(color_rgb(0, 255, 255))
    ln.setWidth(3)
    ln.draw(win)

    rect = Rectangle(Point(250, 250), Point(350, 350))
    rect.setOutline(color_rgb(0, 255, 255))
    rect.setFill(color_rgb(255, 100, 50))
    rect.draw(win)

    cir = Circle(Point(250, 250), 100)
    cir.setOutline(color_rgb(0, 255, 255))
    cir.setFill(color_rgb(100, 255, 50))
    cir.setWidth(5)
    cir.draw(win)

    poly = Polygon(Point(240, 350), Point(250, 450), Point(100, 450),)
    poly.setFill(color_rgb(255, 0, 255))
    poly.setOutline(color_rgb(0, 255, 255))
    poly.setWidth(5)
    poly.draw(win)

    win.getMouse()
    win.close()


main()
