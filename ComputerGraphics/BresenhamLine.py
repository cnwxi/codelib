"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.7 14:37
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : BresenhamLine
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""

import graphics


def bresenhamline(x0, y0, x1, y1):
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0
    dx = x1 - x0
    dy = y1 - y0
    p = 0
    if 0 <= dy <= dx: #斜率大于0小于1
        y = y0
        for x in range(x0, x1 + 1):
            win.plot(x, y)
            if 2 * p + 2 * dy - dx < 0:
                p += dy
            else:
                y += 1
                p += (dy - dx)
    elif dy >= 0 and dy > dx:
        x = x0
        for y in range(y0, y1 + 1):
            win.plot(x, y)
            if 2 * p - 2 * dx + dy > 0:
                p -= dx
            else:
                p += (-dx + dy)
                x += 1
    elif dy <= 0 and -dy <= dx:
        y = y0
        for x in range(x0, x1 + 1):
            win.plot(x, y)
            if 2 * p + 2 * dy + dx > 0:
                p += dy
            else:
                p += (dy + dx)
                y -= 1
    elif dy <= 0 and -dy > dx:
        x = x1
        for y in range(y1, y0 + 1):
            win.plot(x, y)
            if 2 * p + 2 * dx + dy < 0:
                p += dx
            else:
                p += (dy + dx)
                x -= 1


if __name__ == "__main__":
    height = 600
    width = 600
    win = graphics.GraphWin("test", width, height)
    while True:
        tmp = win.getMouse()
        tmpx1, tmpy1 = int(tmp.getX()), int(tmp.getY())
        print('(%d,%d)' % (tmpx1, tmpy1), end='\t')
        tmp = win.getMouse()
        tmpx2, tmpy2 = int(tmp.getX()), int(tmp.getY())
        print("(%d,%d)" % (tmpx2, tmpy2))
        bresenhamline(tmpx1, tmpy1, tmpx2, tmpy2)
