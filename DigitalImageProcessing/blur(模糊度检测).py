"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.19 21:31
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : blur
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
# 基于dct的模糊度检测
# 论文链接
# https://www.researchgate.net/publication/3835246_Blur_determination_in_the_compressed_domain_using_DCT_information
# 相关链接
# https://yinguobing.com/dct-blur-image/
import cv2
import numpy as np
import tkinter as tk
import tkinter.filedialog as fdl


def check_image_size(image, block_size=8):
    # 检查图片大小，保证图片的宽和高能被8整除
    result = True
    height, width = image.shape[:2]
    _y = height % block_size
    _x = width % block_size

    pad_x = pad_y = 0

    if _y != 0:
        pad_y = block_size - _y
        result = False
    if _x != 0:
        pad_x = block_size - _x
        result = False

    image = cv2.copyMakeBorder(
        image, 0, pad_y, 0, pad_x, cv2.BORDER_REPLICATE)

    return result, image


class BlurDetector(object):

    def __init__(self):
        # 初始化模糊检测器
        self.dct_threshold = 8.0
        self.max_hist = 0.1
        self.hist_weight = np.array([8, 7, 6, 5, 4, 3, 2, 1,
                                     7, 8, 7, 6, 5, 4, 3, 2,
                                     6, 7, 8, 7, 6, 5, 4, 3,
                                     5, 6, 7, 8, 7, 6, 5, 4,
                                     4, 5, 6, 7, 8, 7, 6, 5,
                                     3, 4, 5, 6, 7, 8, 7, 6,
                                     2, 3, 4, 5, 6, 7, 8, 7,
                                     1, 2, 3, 4, 5, 6, 7, 8
                                     ]).reshape(8, 8)
        self.weight_total = 344.0

    def get_blurness(self, image, block_size=8):
        # 计算图像的模糊度
        hist = np.zeros((block_size, block_size), dtype=int)
        if len(image.shape) > 2:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('result', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        height, width = image.shape
        round_v = int(height / block_size)
        round_h = int(width / block_size)
        for v in range(round_v):
            for h in range(round_h):
                v_start = v * block_size
                v_end = v_start + block_size
                h_start = h * block_size
                h_end = h_start + block_size

                image_patch = image[v_start:v_end, h_start:h_end]
                image_patch = np.float32(image_patch)
                patch_spectrum = cv2.dct(image_patch)
                patch_none_zero = np.abs(patch_spectrum) > self.dct_threshold
                hist += patch_none_zero.astype(int)

        _blur = hist < self.max_hist * hist[0, 0]
        _blur = (np.multiply(_blur.astype(int), self.hist_weight)).sum()
        return _blur / self.weight_total


if __name__ == "__main__":
    bd = BlurDetector()
    root = tk.Tk()
    root.withdraw()
    file = fdl.askopenfilename()
    img = cv2.imread(file)
    if img is None:
        print('error')
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res, img = check_image_size(gray)
        blur = bd.get_blurness(img)
        print("模糊度: {:.4f}".format(blur))
