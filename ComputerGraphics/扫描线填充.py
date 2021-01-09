"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.14 16:23
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 扫描线填充
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""

import cv2 as cv
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.filedialog as fd


def setpixel(image, x, y, newvalue):
    image[x][y] = newvalue


def scanlineseedfill(image, x, y, boundaryvalue, newvalue):
    x0, x1, xr, y0, xid = 0, 0, 0, 0, 0
    s = [[x, y]]
    while len(s) != 0:
        xx, yy = s.pop()
        setpixel(image, xx, yy, newvalue)
        x0 = xx + 1
        while (not cmp(image[x0, yy], boundaryvalue)) and (not cmp(image[x0, yy], newvalue)):
            setpixel(image, x0, yy, newvalue)
            x0 += 1
        xr = x0 - 1

        x0 = xx - 1
        while (not cmp(image[x0, yy], boundaryvalue)) and (not cmp(image[x0, yy], newvalue)):
            setpixel(image, x0, yy, newvalue)
            x0 -= 1
        xl = x0 + 1
        y0 = yy

        for i in range(-1, 2, 2):
            x0 = xr
            yy = y0 + i
            while x0 >= xl:
                flag = False
                while (not cmp(image[x0, yy], boundaryvalue)) and (not cmp(image[x0, yy], newvalue)) and x0 >= xl:
                    if not flag:
                        flag = True
                        xid = x0
                    x0 -= 1
                if flag:
                    s.append([xid, yy])
                    flag = False
                while cmp(image[x0, yy], boundaryvalue) or cmp(image[x0, yy], newvalue):
                    x0 -= 1


def cmp(color1, color2):
    if color1[0] == color2[0] and color1[1] == color2[1] and color1[2] == color2[2]:
        return True
    else:
        return False


if __name__ == '__main__':
    img = cv.imread("test.jpg")
    boundary = [0, 0, 0]
    newcolor = [255, 0, 0]
    plt.imshow(img)
    tmpy, tmpx = list(map(int, plt.ginput(1)[0]))
    scanlineseedfill(img, tmpx, tmpy, boundary, newcolor)
    # cv.imshow('b',img)
    # cv.waitKey()
    plt.clf()
    plt.imshow(img)
    plt.show()
