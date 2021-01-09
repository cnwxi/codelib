"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.19 13:18
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 平面
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math


def bresenhamline(x0, y0, x1, y1):
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0
    dx = x1 - x0
    dy = y1 - y0
    p = 0
    if 0 <= dy <= dx:  # 斜率大于0小于1
        y = y0
        for x in range(x0, x1 + 1):
            points.append([x, y])
            if 2 * p + 2 * dy - dx < 0:
                p += dy
            else:
                y += 1
                p += (dy - dx)
    elif dy >= 0 and dy > dx:
        x = x0
        for y in range(y0, y1 + 1):
            points.append([x, y])
            if 2 * p - 2 * dx + dy > 0:
                p -= dx
            else:
                p += (-dx + dy)
                x += 1
    elif dy <= 0 and -dy <= dx:
        y = y0
        for x in range(x0, x1 + 1):
            points.append([x, y])
            if 2 * p + 2 * dy + dx > 0:
                p += dy
            else:
                p += (dy + dx)
                y -= 1
    elif dy <= 0 and -dy > dx:
        x = x1
        for y in range(y1, y0 + 1):
            points.append([x, y])
            if 2 * p + 2 * dx + dy < 0:
                p += dx
            else:
                p += (dy + dx)
                x -= 1


def four(x, y):
    global length, d
    half = int(length / 2)
    d.append([x - half, y + half])
    d.append([x + half, y + half])
    d.append([x + half, y - half])
    d.append([x - half, y - half])


# 外点
# x=Rcos(72°*k)  y=Rsin(72°*k)   k=0,1,2,3,4
# 内点
# r=Rsin18°/sin36°
# x=rcos(72°*k+36°)  y=rsin(72°*k+36°)   k=0,1,2,3,4

def five(x, y):
    global length, d
    r = length * math.sin(math.pi / 20) / math.sin(math.pi / 10)
    for i in range(5):
        a = int(length * math.cos(math.pi * 2 / 5 * i))
        b = int(length * math.sin(math.pi * 2 / 5 * i))
        d.append([x - b, y - a])
        a = int(r * math.cos(math.pi * 2 / 5 * i + math.pi / 5))
        b = int(r * math.sin(math.pi * 2 / 5 * i + math.pi / 5))
        d.append([x - b, y - a])


def six(x, y):
    global length, d
    d.append([x - length, y])
    d.append([int(x - length / 2), int(y + length * math.sin(math.pi / 3))])
    d.append([int(x + length / 2), int(y + length * math.sin(math.pi / 3))])
    d.append([x + length, y])
    d.append([int(x + length / 2), int(y - length * math.sin(math.pi / 3))])
    d.append([int(x - length / 2), int(y - length * math.sin(math.pi / 3))])


def getpoints(p):
    points.clear()
    maxd = len(p) - 1
    for i in range(maxd):
        bresenhamline(p[i][0], p[i][1], p[i + 1][0], p[i + 1][1])
    bresenhamline(p[maxd][0], p[maxd][1], p[0][0], p[0][1])


def changeimage():
    global points, origin
    global draw
    draw = Image.fromarray(image)
    draw.putpixel(origin, 255)
    for i in points:
        draw.putpixel(i, 255)


def tr():
    global t, d
    maxlen = len(d)
    for i in range(maxlen):
        a = d[i]
        a = np.array([a[0], a[1], 1])
        tmpp = np.dot(a, t)[:2]
        d[i] = tmpp.astype('int32')
    # maxlen = len(points)
    # for i in range(maxlen):
    #     a = points[i]
    #     a = [a[0], a[1], 1]
    #     a = np.dot(a, t).astype('int32')[:2]
    #     points[i] = a
    getpoints(d)
    changeimage()


def getkey(event):
    key = True
    global t, origin
    # 平移
    if event.key == 'A':
        t = np.array([[1, 0, 0], [0, 1, 0], [-10, 0, 1]])
    elif event.key == 'D':
        t = np.array([[1, 0, 0], [0, 1, 0], [10, 0, 1]])
    elif event.key == 'S':
        t = np.array([[1, 0, 0], [0, 1, 0], [0, 10, 1]])
    elif event.key == 'W':
        t = np.array([[1, 0, 0], [0, 1, 0], [0, -10, 1]])
    # 缩放
    elif event.key == 'I':
        sx = 1
        sy = 2
        t = np.array([[sx, 0, 0], [0, sy, 0], [origin[0] * (1 - sx), origin[1] * (1 - sy), 1]])
    elif event.key == 'K':
        sx = 1
        sy = 0.5
        t = np.array([[sx, 0, 0], [0, sy, 0], [origin[0] * (1 - sx), origin[1] * (1 - sy), 1]])
    elif event.key == 'J':
        sx = 0.5
        sy = 1
        t = np.array([[sx, 0, 0], [0, sy, 0], [origin[0] * (1 - sx), origin[1] * (1 - sy), 1]])
    elif event.key == 'L':
        sx = 2
        sy = 1
        t = np.array([[sx, 0, 0], [0, sy, 0], [origin[0] * (1 - sx), origin[1] * (1 - sy), 1]])
    # 旋转
    elif event.key == 'Q':
        x0, y0 = origin
        cos = math.cos(xita * math.pi / 180)
        sin = math.sin(xita * math.pi / 180)
        t = np.array([[cos, sin, 0],
                      [-sin, cos, 0],
                      [x0 * (1 - cos) + y0 * sin, y0 * (1 - cos) - x0 * sin, 1]])
    elif event.key == 'E':
        x0, y0 = origin
        cos = math.cos(-xita * math.pi / 180)
        sin = math.sin(-xita * math.pi / 180)
        t = np.array([[cos, sin, 0],
                      [-sin, cos, 0],
                      [x0 * (1 - cos) + y0 * sin, y0 * (1 - cos) - x0 * sin, 1]])
    # 错切
    elif event.key == 'Z':
        t = np.array([[1, 0, 0], [1, 1, 0], [0, 0, 1]])
    elif event.key == 'X':
        t = np.array([[1, 0, 0], [-1, 1, 0], [0, 0, 1]])
    elif event.key == 'C':
        t = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    elif event.key == 'V':
        t = np.array([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
    else:
        key = False
    if key:
        tr()
        plt.clf()
        plt.imshow(draw)
        plt.show()


def getmouse(event):
    global origin
    origin = [int(event.xdata), int(event.ydata)]
    print(origin)


if __name__ == '__main__':
    # origin = [0, 0]
    d = []
    points = []
    xita = 6
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('key_press_event', getkey)
    fig.canvas.mpl_connect('button_press_event', getmouse)
    t = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    image = np.zeros((1000, 900))
    length = 50
    draw = Image.fromarray(image)
    plt.imshow(draw)
    xx, yy = list(map(int, plt.ginput(1)[0]))
    origin = [0, 0]
    five(xx, yy)
    getpoints(d)
    changeimage()
    plt.clf()
    plt.imshow(draw)
    plt.show()
