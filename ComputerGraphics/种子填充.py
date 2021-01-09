"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.14 14:45
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 种子填充
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image


def floodfill4(image, x, y, oldcolor, newcolor):
    if 100 > x >= 0 and 100 > y >= 0 and image[x, y] == oldcolor:
        image[x, y] = newcolor
        floodfill4(image, x, y - 1, oldcolor, newcolor)
        floodfill4(image, x, y + 1, oldcolor, newcolor)
        floodfill4(image, x - 1, y, oldcolor, newcolor)
        floodfill4(image, x + 1, y, oldcolor, newcolor)


if __name__ == "__main__":
    sys.setrecursionlimit(99999999)
    array = np.zeros((100, 100))

    for i in range(0, 100, 1):
        array[i, 10] = 255
        array[i, 90] = 255
    for i in range(0, 100, 1):
        array[10, i] = 255
        array[90, i] = 255
    # img = cv.imread('test.jpg')
    img = Image.fromarray(array)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.imshow(img)
    plt.title('种子填充')
    pos = list(map(int, plt.ginput(1)[0]))
    print(pos)
    temx, temy = pos
    old = array[pos[0], pos[1]]
    print(old)
    # pos = list(map(int, plt.ginput(1)[0]))
    # print(pos)
    # new = img[pos[0]][pos[1]]
    new = 255
    floodfill4(array, temy, temx, old, new)
    plt.clf()
    img = Image.fromarray(array)
    plt.imshow(img, 'gray')
    plt.show()
