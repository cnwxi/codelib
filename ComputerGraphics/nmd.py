"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.14 15:39
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : nmd
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import numpy as np
import sys
from PIL import Image
import matplotlib.pyplot as plt

length=100
sys.setrecursionlimit(99999999)
a = np.zeros((length, length))



def one(a, x, y):
    if x < length-10 and x >= 10 and y < length-10 and y >= 10 and a[x, y] == 0:
        a[x, y] = 255
        one(a, x - 1, y)
        one(a, x + 1, y)
        one(a, x, y - 1)
        one(a, x, y + 1)


one(a, 50, 50)
img = Image.fromarray(a)
plt.imshow(img)
plt.show()
