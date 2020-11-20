"""

_|          _|  _|      _|  _|      _|  @Time : 2020.11.18 18:16
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : fft
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import numpy as np
import math
import cv2 as cv

T = 50  # 阈值设定，大于T则判定偏离xy轴过多


# 复数类
class Complex:
    def __init__(self):
        self.real = 0.0
        self.image = 0.0


# 复数乘法
def mul_ee(complex0, complex1):
    complex_ret = Complex()
    complex_ret.real = complex0.real * complex1.real - complex0.image * complex1.image
    complex_ret.image = complex0.real * complex1.image + complex0.image * complex1.real
    return complex_ret


# 复数加法
def add_ee(complex0, complex1):
    complex_ret = Complex()
    complex_ret.real = complex0.real + complex1.real
    complex_ret.image = complex0.image + complex1.image
    return complex_ret


# 复数减法
def sub_ee(complex0, complex1):
    complex_ret = Complex()
    complex_ret.real = complex0.real - complex1.real
    complex_ret.image = complex0.image - complex1.image
    return complex_ret


# 对输入数据进行倒序排列
def forward_input_data(input_data, num):
    j = num // 2
    for i in range(1, num - 2):
        if i < j:
            complex_tmp = input_data[i]
            input_data[i] = input_data[j]
            input_data[j] = complex_tmp
            # print "forward x[%d] <==> x[%d]" % (i, j)
        k = num // 2
        while j >= k:
            j = j - k
            k = k // 2
        j = j + k


# 实现1D FFT
def fft_1d(in_data, num):
    forward_input_data(in_data, num)  # 倒序输入数据

    # 计算蝶形级数，也就是迭代次数
    m = 1  # num = 2^m
    tmp = num // 2
    while tmp != 1:
        m = m + 1
        tmp = tmp // 2
    # print "FFT level：%d" % m

    complex_ret = Complex()
    for L in range(1, m + 1):
        b = int(math.pow(2, L - 1))  # B为指数函数返回值，为float，需要转换integer
        for J in range(0, b):
            p = math.pow(2, m - L) * J
            for K in range(J, num, int(math.pow(2, L))):
                # print "L:%d b:%d, J:%d, K:%d, p:%f" % (L, b, J, K, p)
                complex_ret.real = math.cos((2 * np.pi / num) * p)
                complex_ret.image = -math.sin((2 * np.pi / num) * p)
                complex_mul = mul_ee(complex_ret, in_data[K + b])
                complex_add = add_ee(in_data[K], complex_mul)
                complex_sub = sub_ee(in_data[K], complex_mul)
                in_data[K] = complex_add
                in_data[K + b] = complex_sub
                # print "A[%d] real: %f, image: %f" % (K, in_data[K].real, in_data[K].image)
            # print "A[%d] real: %f, image: %f" % (K + b, in_data[K + b].real, in_data[K + b].image)


def test_fft_1d(in_data):
    # in_data = [2,3,4,5,7,9,10,11,100,12,14,11,56,12,67,12] #待测试的x点元素
    k = 1
    while 1:
        if pow(2, k) < len(in_data) <= pow(2, k + 1):  # 不足的补0
            # fftlen=pow(2,k+1)
            # in_data.extend([0 for i in range(pow(2,k+1)-len(in_data))])
            fftlen = pow(2, k)
            break
        k += 1
    # 变量data为长度为x、元素为complex类实例的list，用于存储输入数据
    data = [(Complex()) for i in range(len(in_data))]
    # 将8个测试点转换为complex类的形式，存储在变量data中
    for i in range(len(in_data)):
        data[i].real = in_data[i]
        data[i].image = 0.0

    # 输出FFT需要处理的数据
    # print("The input data:")
    # for i in range(len(in_data)):
    #    print("x[%d] real: %f, image: %f" % (i, data[i].real, data[i].image))

    fft_1d(data, fftlen)

    # 输出经过FFT处理后的结果
    # print("The output data:")
    # for i in range(len(in_data)):
    # print("X[%d] real: %f, image: %f" % (i, data[i].real, data[i].image))

    tnum = 0
    for i in range(len(in_data)):  # 虚实值都大于T的才叫偏离
        if abs(data[i].real) > T and abs(data[i].image) > T:
            tnum += 1
    return round(tnum / len(in_data), 4)


# test the 1d fft
# in_data=[2,3,4,5,7,9,10,11]
# demo = Image.open("noise_check//5.jpg")
# im = np.array(demo.convert('L'))  # 灰度化矩阵
# in_data = []
# for item in im:
#     in_data.extend(item)
# test_fft_1d(in_data)

# 统计噪声
def run(img):
    im = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    in_data = []
    for item in im:
        in_data.extend(item)
    return test_fft_1d(in_data)
