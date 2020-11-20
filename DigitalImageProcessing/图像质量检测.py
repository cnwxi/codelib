"""

_|          _|  _|      _|  _|      _|  @Time : 2020.11.18 17:11
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 图像质量检测
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog
import fft


# 清晰度
def clarity(img):
    # 转换为灰度图像
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.namedWindow('img', cv.WINDOW_NORMAL)
    # cv.imshow('img', img_gray)
    # 高斯模糊降噪
    img_gray = cv.GaussianBlur(img_gray, (7, 7), 0)
    # cv.imshow('l',img_gray)
    # v1 = cv.Canny(img_gray, 50, 150)
    # de0 = v1.var()
    v2 = cv.Scharr(img_gray, cv.CV_32F, 1, 0)
    v3 = cv.Scharr(img_gray, cv.CV_32F, 0, 1)
    v2 = cv.convertScaleAbs(v2)
    v3 = cv.convertScaleAbs(v3)
    grad = cv.addWeighted(v2, 0.5, v3, 0.5, 0)

    # grad = cv.addWeighted(v2 ** 2, 0.5, v3 ** 2, 0.5, 0)
    # grad += (v2 + v3)
    # print(img_gray.size)
    de1 = np.sum(grad) / img_gray.size
    return de1
    # cv.imshow('test', v1)
    # cv.namedWindow('tidu', cv.WINDOW_NORMAL)
    # cv.imshow('tidu', grad)
    # cv.waitKey()
    # cv.destroyAllWindows()


# 亮度
def brightness(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    n = img_gray.size
    hist = cv.calcHist([img_gray], [0], None, [256], [0, 255])
    da = np.sum([(i - 128) * hist[i][0] for i in range(256)]) / n
    d = abs(da)
    ma = np.sum([abs(i - 128 - da) * hist[i][0] for i in range(256)]) / n
    m = abs(ma)
    if m != 0:
        k = d / m
    else:
        k = 1
    if k >= 1:
        if da > 0:
            return 1
        else:
            return -1
    else:
        return 0


# 对比度
def contrast(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    raw, col = img_gray.shape
    b = 0.0
    for i in range(1, raw - 1):
        for j in range(1, col - 1):
            b += ((int(img_gray[i, j]) - int(img_gray[i, j + 1])) ** 2 +
                  (int(img_gray[i, j]) - int(img_gray[i, j - 1])) ** 2 +
                  (int(img_gray[i, j]) - int(img_gray[i + 1, j])) ** 2 +
                  (int(img_gray[i, j]) - int(img_gray[i - 1, j])) ** 2)
    cg = b / (4 * (raw - 2) * (col - 2))
    return int(cg)


if __name__ == '__main__':
    # imagepath = sys.argv[1]
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    image = cv.imread(file_path)
    print("相对梯度：%.2f" % (clarity(image)))
    tmp = brightness(image)
    print("亮度：", end='')
    if tmp == -1:
        print('暗')
    elif tmp == 0:
        print('正常')
    else:
        print('亮')
    print("对比度：%d" % (contrast(image)))
    print("可能的噪声占比？%f%%" % (fft.run(image) * 100))
