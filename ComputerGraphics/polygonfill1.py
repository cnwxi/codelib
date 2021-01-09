"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.13 22:04
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : polygonfill1
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

array = np.ndarray((660, 660, 3), np.uint8)
color = (20, 20, 20)


def init():
    global array
    array[:, :] = (255, 255, 255)


def creat_Net(point, row, y_min, y_max):
    Net = [([] * y_max) for i in range(y_max)]
    point_count = point.shape[0]
    for j in range(0, point_count):
        x = np.zeros(10)
        first = int(min(point[(j + 1) % point_count][1], point[j][1]))
        a = point[(j + 1) % point_count][0] - point[j][0]
        b = point[(j + 1) % point_count][1] - point[j][1]
        if a == 0:
            x[1] = 0
        elif b == 0:
            x[1] = float('Inf')
        else:
            x[1] = a / b
            x[2] = max(point[(j + 1) % point_count][1], point[j][1])
        if (point[(j + 1) % point_count][1] < point[j][1]):
            x[0] = point[(j + 1) % point_count][0]
        else:
            x[0] = point[j][0]
        Net[first].append(x)
    return Net


def draw_line(i, x, y):
    # for j in range(int(x), int(y) + 1):
    #     if ((i-j) % 5) == 0:
    #         array[i,j] = color
    array[i, int(x):int(y) + 1] = color


def polygon_fill(point):
    y_min = np.min(point[:, 1])
    y_max = np.max(point[:, 1])
    net = creat_Net(point, y_max - y_min + 1, y_min, y_max)
    x_sort = [] * 3
    for i in range(y_min, y_max):
        x = net[i]
        if (len(x) != 0):
            for k in x:
                x_sort.append(k)
        x_image = [] * 3
        for cell in x_sort:
            x_image.append(cell[0])
        x_image.sort()
        if (len(x_image) >= 3 and x_image[0] == x_image[1] and x_image[2] > x_image[1]):
            x_image[1] = x_image[2]
        draw_line(i, x_image[0], x_image[1])

        linshi = [] * 3
        for cell in x_sort:
            if cell[2] > i:
                cell[0] += cell[1]
                linshi.append(cell)
        x_sort = linshi[:]

        x_image = [] * 3
        for cell in x_sort:
            x_image.append(cell[0])
        x_image.sort()
        draw_line(i, x_image[0], x_image[1])


if __name__ == "__main__":
    image = Image.fromarray(array)
    plt.imshow(image)
    point = []
    init()
    image = Image.fromarray(array)
    plt.imshow(image)
    while True:
        pos = list(map(int, plt.ginput(1)[0]))
        # print(type(pos), pos)
        point.append(pos)
        print(len(point))
        pointlist = np.array(point)
        if (len(point) > 1):
            init()
            plt.clf()
            polygon_fill(pointlist)
            image = Image.fromarray(array)
            plt.imshow(image)
            # plt.clf()
