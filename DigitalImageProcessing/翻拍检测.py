"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.14 9:36
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 翻拍检测
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""

import cv2 as cv
import numpy as np
import tkinter as tk
import tkinter.filedialog as fdl
from PIL import Image
root = tk.Tk()
root.withdraw()
file = fdl.askopenfilename()
img = cv.imread(file)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = np.float32(img)
img_dct = cv.dct(img)
dct=Image.fromarray(img_dct)
dct.show()