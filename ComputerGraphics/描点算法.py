"""

_|          _|  _|      _|  _|      _|  @Time : 2020.10.29 8:23
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 描点算法.py
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import win32gui as gui
import win32api as api
import numpy as np

dc = gui.GetDC(0)
color = api.RGB(255, 255, 255)

gui.SetViewportOrgEx(dc, 50, 50)


# for i in range(1000):
#     gui.SetPixel(dc, i, i, color)
def DDALIne(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    e = [abs(dx), abs(dy)][abs(dx) > abs(dy)]
    dx /= e
    dy /= e
    x = x1
    y = y1
    for i in range(e + 1):
        gui.SetPixel(dc, int(x + 0.5), int(y + 0.5), color)
        x += dy
        y += dy


def MidpointLine(x0, y0, x1, y1):
    a = y0 - y1
    b = x1 - x0
    d = 2 * a + b
    delta1 = 2 * a
    delta2 = 2 * (a + b)
    x = x0
    y = y0
    gui.SetPixel(dc, x, y, color)
    while x < x1:
        if d < 0:
            x += 1
            y += 1
            d += delta2
        else:
            x += 1
            d += delta1
        gui.SetPixel(dc, x, y, color)


def BresenhamLine(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx
    for i in range(x, x2 + 1):
        gui.SetPixel(dc, i, y, color)
        if p > 0:
            y += 1
            p += 2 * (dy - dx)
        else:
            p += 2 * dy


def MidpointCircle(R):
    x, y, d = 0, R, 1.25 - R
    gui.SetPixel(dc, x, y, color)
    while x < y:
        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2 * (x - y) + 5
            x += 1
            y -= 1
        gui.SetPixel(dc, x, y, color)


def MidpointCircle1(R):
    x, y, d = 0, R, 1 - R
    gui.SetPixel(dc, x, y, color)
    while x < y:
        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2 * (x - y) + 5
            x += 1
            y -= 1
        gui.SetPixel(dc, x, y, color)


def MidpointCircle2(R):
    x, y, d = 0, R, 1 - R
    delta1 = 3
    delta2 = 5 - 2 * R
    gui.SetPixel(dc, x, y, color)
    while x < y:
        if d < 0:
            d += delta1
            delta1 += 2
            delta2 += 2
            x += 1
        else:
            d += delta2
            delta1 += 2
            delta2 += 4
            x += 1
            y -= 1
        gui.SetPixel(dc, x, y, color)


def BresenhamCircle(R):
    x, y, p = 0, R, 3 - 2 * R
    while x <= y:
        gui.SetPixel(dc, x, y, color)
        if p > 0:
            p += 4 * (x - y) + 10
            y -= 1
        else:
            p += 4 * x + 6
        x += 1


def MidpointElliose(a, b):
    x, y = 0, b
    d1 = b * b + a * a * (-b + 0.25)
    gui.SetPixel(dc, x, y, color)
    while b * b * (x + 1) < a * a * (y - 0.5):
        if d1 < 0:
            d1 += b * b * (2 * x + 3)
            x += 1
        else:
            d1 += (b * b * (2 * x + 3) + a * a * (-2 * y + 2))
            x += 1
            y -= 1
        gui.SetPixel(dc, x, y, color)
    d2 = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
    while y > 0:
        if d2 < 0:
            d2 += b * b * (2 * x + 2) + a * a * (-2 * y + 3)
            x += 1
            y -= 1
        else:
            d2 += a * a * (-2 * y + 3)
            y -= 1
        gui.SetPixel(dc, x, y, color)


def BresenhamElliose(a, b):
    aa, bb, x, y = a * a, b * b, 0, b
    d = 2 * bb - 2 * b * aa + aa
    gui.SetPixel(dc,x, y, color)
    p_x = int(aa / np.sqrt(aa + bb))
    while x <= p_x:
        if d < 0:
            d += 2 * bb * (2 * x + 3)
        else:
            d += 2 * bb * (2 * x + 3) - 4 * aa * (y - 1)
            y -= 1
        x += 1
        gui.SetPixel(dc,x, y, color)
    d = bb * (x * x + x) + aa * (y * y - y) - aa * bb
    while y >= 0:
        gui.SetPixel(dc,x, y, color)
        y -= 1
        if d < 0:
            x += 1
            d = d - 2 * aa * y - aa + 2 * bb * x + 2 * bb
        else:
            d = d - 2 * aa * y - aa