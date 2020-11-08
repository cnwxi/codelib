"""

_|          _|  _|      _|  _|      _|  @Time : 2020.11.6 19:53
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 计算机图形学p44T7.py
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import win32gui as gui
import win32api as api

dc = gui.GetDC(0)
color = api.RGB(255, 255, 255)
gui.SetViewportOrgEx(dc, 960, 540)


def BresenhamCircle(R):
    x, y, p = 0, R, 3 - 2 * R
    while x <= y:
        gui.SetPixel(dc, x, y, color)
        if p > 0:
            p += 4 * (x - y) + 10
            y -= 1
        else:
            p += 4 * x + 6
        x += 1


def drawcircle(r):
    e, u, v = 1 - r, 1, 1 - 2 * r
    x, y = 0, r
    while x <= y:
        gui.SetPixel(dc, x, y, color)
        if x == y:
            break
        x += 1
        u += 2
        if e < 0:
            v += 2
            e += u
        else:
            v += 4
            e += v
            y -= 1


drawcircle(10)
BresenhamCircle(10)

# 验证关系p=2*e+1
"""
假设p=2*e+1
∴p'=p+Δp=2*e'+1=2*(e+Δe)+1=2*e+1+2*Δe
则有Δp=2Δe关系成立

从算法1中可以提取以下关系式
Δp1=4*(x-y)+10 p>0
Δp2=4*x+6       p<=0

从算法2中可以提取以下关系式
Δe1=v           e>=0
Δe2=u           e<0

算法2中v、u的变化如下：
x = x + 1
u += 2
if e < 0:
    v += 2
    e += u
else:
    v += 4
    e += v
    y -= 1
部分代码可以观察出u、v的变化与x、y有关，且算法1与算法2的x+=1的先后不一致
u的初始值为1，v的初始值为1-2*r
//e<0 v+=2,e>=0 v+=4 → v+=2 e>=0,v+=2
Δe1=v
    =1-2*r+2*x+2*(r-y)//此时的x相对于算法1是算法1中x自加后的结果。
    =1+2*((x+1)-y)  //令x=x+1，统一算法1、2中的x
    =2*(x-y)+3
//∀e,u+=2
Δe2=u
    =1+2*x
    =1+2*(x+1)      //令x=x+1，统一算法1、2中的x
    =2*x+3
此时刚好满足Δp=2Δe的条件
于是假设成立。
"""
# 解释算法2的可行性
"""
个人感觉是基于Bresenham算法的优化，
在Bresenham算法中
Δp1=4*(x-y)+10 p>0
Δp2=4*x+6       p<=0
其中x无论p的正负都会自加1，y当满足p>0自减1。y的初值为r。
所以变换一下式子。
Δp1=4*(x-y)+10=4*x+4*(r-y)+10
Δp2=4*x+6
可以发现无论p的正负，ΔΔp中都有4这个常数（因为x+=1永远要执行）
当p为正时，ΔΔp中多出一个4（因为只有p>0，才执行y-=1，Δp1中第二项就会有Δ=4）
于是考虑将计算x、y关系转换为计算累计值。
"""
