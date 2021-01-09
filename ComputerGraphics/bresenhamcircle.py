"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.7 16:26
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : bresenhamcircle
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""

import graphics


def draw(p, offset):
    for i in range(2):
        for j in range(2):
            win.plot((-1) ** i * p[0] + offset[0], p[1] * (-1) ** j + offset[1])
    for i in range(2):
        for j in range(2):
            win.plot((-1) ** i * p[1] + offset[0], p[0] * (-1) ** j + offset[1])
    # win.plot(p[0] + offset[0], p[1] + offset[1])
    # win.plot(p[0] + offset[0], -p[1] + offset[1])
    # win.plot(-p[0] + offset[0], p[1] + offset[1])
    # win.plot(-p[0] + offset[0], -p[1] + offset[1])


def bresenhamcircle(radius):
    x, y, p = 0, radius, 3 - 2 * radius
    point = []
    while x <= y:
        point.append([x, y])
        if p >= 0:
            p += 4 * (x - y) + 10
            y -= 1
        else:
            p += 4 * x + 6
        x += 1
    return point


def drawcircle(pointlist, offset):
    for i in pointlist:
        draw(i, offset)


if __name__ == "__main__":
    height = 600
    width = 600
    win = graphics.GraphWin("test", width, height)
    while True:
        tmp1 = win.getMouse()
        tmpx1, tmpy1 = int(tmp1.getX()), int(tmp1.getY())
        # graphics.Point(tmpx1, tmpy1).draw(win)
        print('圆心：(%d,%d)' % (tmpx1, tmpy1), end='\t')
        tmp2 = win.getMouse()
        tmpx2, tmpy2 = int(tmp2.getX()), int(tmp2.getY())
        o = (tmpx1, tmpy1)
        r = int(((tmpx1 - tmpx2) ** 2 + (tmpy1 - tmpy2) ** 2) ** 0.5)
        print('半径：%d' % (r))
        list = bresenhamcircle(r)
        print("finished\ndrawing")
        drawcircle(list, o)
