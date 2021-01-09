"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.21 14:38
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 栅栏填充
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def addpoint(tmpx, tmpy):
    global points
    if tmpy in points:
        if tmpx not in points[tmpy]:
            points[tmpy].append(tmpx)
    else:
        points[tmpy] = [tmpx]


def bresenhamline(x0, y0, x1, y1):
    global points
    points.clear()
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0
    dx = x1 - x0
    dy = y1 - y0
    p = 0
    if 0 <= dy <= dx:  # 斜率大于0小于1
        y = y0
        for x in range(x0, x1 + 1):
            addpoint(x, y)
            if 2 * p + 2 * dy - dx < 0:
                p += dy
            else:
                y += 1
                p += (dy - dx)
    elif dy >= 0 and dy > dx:
        x = x0
        for y in range(y0, y1 + 1):
            addpoint(x, y)
            if 2 * p - 2 * dx + dy > 0:
                p -= dx
            else:
                p += (-dx + dy)
                x += 1
    elif dy <= 0 and -dy <= dx:
        y = y0
        for x in range(x0, x1 + 1):
            addpoint(x, y)
            if 2 * p + 2 * dy + dx > 0:
                p += dy
            else:
                p += (dy + dx)
                y -= 1
    elif dy <= 0 and -dy > dx:
        x = x1
        for y in range(y1, y0 + 1):
            addpoint(x, y)
            if 2 * p + 2 * dx + dy < 0:
                p += dx
            else:
                p += (dy + dx)
                x -= 1


# def simpleline(x0, y0, x1, y1):
#     global points
#     points.clear()
#     if y1 - y0 == 0:
#         addpoint(x0, y0)
#         addpoint(x1, y1)
#         return
#     deltax = (x1 - x0) / (y1 - y0)
#     if y0 > y1:
#         x0, x1, y0, y1 = x1, x0, y1, y0
#     for i in range(y0, y1 + 1):
#         addpoint(int(x0 + deltax), i)


# def getpoints():
#     global d
#     points.clear()
#     maxd = len(d) - 1
#     for i in range(maxd):
#         bresenhamline(d[i][0], d[i][1], d[i + 1][0], d[i + 1][1])
#     bresenhamline(d[maxd][0], d[maxd][1], d[0][0], d[0][1])


def findfence():
    global d
    tmpmin = np.min(d, axis=0)
    tmpmax = np.max(d, axis=0)
    # dx = maxx - minx
    # dy = maxy - miny
    tmpmid = (tmpmin[0] + tmpmax[0]) // 2
    fence = 0
    inf = 99999
    tmpx = []
    for i in range(len(d)):
        tmpx.append(d[i][0])
        tmp = abs(tmpmid - d[i][0])
        if tmp < inf:
            fence = d[i][0]
            inf = tmp
    return fence, tmpmin[1], tmpmax[1]


def change(minx, maxx, tmpy):
    global array, d
    for i in range(minx, maxx + 1):
        if [i, tmpy] not in d:
            array[i][tmpy] = 255 - array[i][tmpy]
        else:
            print([i, tmpy])


def fencefill():
    global array, d, points
    array = np.zeros((900, 900))
    fencex, min_y, max_y = findfence()
    tmpl = len(d)
    if tmpl <= 2:
        return
    for i in range(len(d)):
        lasti = (i - 1) % tmpl if i - 1 >= 0 else tmpl - 1
        nexti = (i + 1) % tmpl
        bresenhamline(d[i][0], d[i][1], d[nexti][0], d[nexti][1])
        # simpleline(d[i][0], d[i][1], d[nexti][0], d[nexti][1])
        if d[i][1] < d[nexti][1]:
            down = d[i][1]
            up = d[nexti][1]
            if d[lasti][1] < d[i][1]:
                points.pop(d[i][1])
                # print(d[i], '中间')
                down += 1
        else:
            down = d[nexti][1]
            up = d[i][1]
            if d[lasti][1] > d[i][1]:
                points.pop(d[i][1])
                # print(d[i], '中间')
                up -= 1
        for j in range(down, up + 1):
            beforex = -999
            length = len(points[j])
            for k in range(length):
                tmpx = points[j][k]
                if abs(tmpx - beforex) != 1:
                    tmpxismin = 1 if tmpx < fencex else 0
                    min_x = tmpxismin * tmpx + (1 - tmpxismin) * fencex
                    max_x = (1 - tmpxismin) * tmpx + tmpxismin * fencex
                    change(min_x, max_x, j)
                beforex = tmpx
    for i in range(900):
        array[fencex][i] = 255


if __name__ == '__main__':
    array = np.zeros((300, 300))
    img = Image.fromarray(array)
    plt.imshow(img)
    d = []
    points = {}
    while True:
        tmpy, tmpx = list(map(int, plt.ginput(1)[0]))
        d.append([tmpx, tmpy])
        print(d[len(d) - 1])
        fencefill()
        img = Image.fromarray(array)
        plt.imshow(img)
