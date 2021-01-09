"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.7 16:53
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : polygonfill
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import graphics

pointlist = []


# parallel = []

def findm():
    global pointlist
    minx, miny = 999, 999
    maxx, maxy = 0, 0
    for i in pointlist:
        # minx = i[0] if i[0] < minx else minx
        # maxx = i[0] if i[0] > maxx else maxx
        miny = i[1] if i[1] < miny else miny
        maxy = i[1] if i[1] > maxy else maxy
    return miny, maxy


# def et():
#     global pointlist
#     tmpet = {}
#     time = len(pointlist)
#     for i in range(time):
#         point1 = pointlist[i]
#         if i == time - 1:
#             point2 = pointlist[0]
#         else:
#             point2 = pointlist[i + 1]
#         if point1[1] >= point2[1]:
#             ymax = point1[1]
#             ymin = point2[1]
#         else:
#             ymax = point2[1]
#             ymin = point1[1]
#         # ymax = point1[1] if point1[1] > point2[1] else point2[1]
#         xmin = point1[0] if point1[0] < point2[0] else point2[0]
#         if point1[0] == point2[0]:
#             k = 0
#         elif point1[1] == point2[1]:
#             parallel.append([point1, point2])
#         else:
#             k = (point1[0] - point2[0]) / (point1[1] - point2[1])
#         if ymin in tmpet:
#             if [ymax, xmin, k] in tmpet[ymin]:
#                 continue
#             else:
#                 tmpet[ymin].append([ymax, xmin, k])
#         else:
#             tmpet[ymin] = [[ymax, xmin, k]]
#     return tmpet

def polygonfill():
    global pointlist
    tmpet = {}
    minY, maxY = findm()
    time = len(pointlist)
    for i in range(minY, maxY + 1):
        for j in range(time):
            if pointlist[j][1] == i:
                if pointlist[(j - 1 + time) // time][1] > pointlist[j][1]:
                    xmin = pointlist[j][0]
                    ymax = pointlist[(j - 1 + time) // time][1]
                    dx = (pointlist[(j - 1 + time) // time][0] - xmin) / (ymax - pointlist[j][1])
                    if i in tmpet:
                        tmpet[i].append([xmin, ymax, dx])
                    else:
                        tmpet[i] = [[xmin, ymax, dx]]
                if pointlist[(j + 1 + time) // time][1] > pointlist[j][1]:
                    xmin = pointlist[j][0]
                    ymax = pointlist[(j + 1 + time) // time][1]
                    dx = (pointlist[(j + 1 + time) // time][0] - xmin) / (ymax - pointlist[j][1])
                    if i in tmpet:
                        tmpet[i].append([xmin, ymax, dx])
                    else:
                        tmpet[i] = [[xmin, ymax, dx]]
    aet = {minY:[]}
    for i in range(minY, maxY + 1):
        # 更新aet
        if len(aet) != 0:
            for j in aet[i]:
                j[0] += j[2]

        # 删除ymax==i的结点
        if len(aet) != 0:
            tmpset = []
            for j in range(len(aet[i])):
                if aet[i][j][1] == i:
                    tmpset.append(j)
            for j in range(len(tmpset)):
                del aet[i][tmpset[j] - j]
        # 将et中的新点加入aet
        if len(aet[i]) != 0:
            for j in tmpet[i]:
                if j in aet[i]:
                    continue
                else:
                    aet[i].append(j)
        else:
            for j in tmpet[i]:
                aet[i].append(j)
        # 按xmin增序排列
        aet[i].sort()
        length = len(aet[i])
        if length != 0:
            for j in range(0, length, 2):
                for k in range(aet[i][j][0], aet[i][j + 1][0] + 1):
                    win.plot(k, i)


if __name__ == '__main__':
    height = 600
    width = 600
    print("请输入顶点数：", end='')
    num = int(input())
    if num < 1:
        print("error")
    win = graphics.GraphWin("test", width, height)
    for i in range(num):
        tmp = win.getMouse()
        x, y = int(tmp.getX()), int(tmp.getY())
        win.plot(x, y)
        pointlist.append([x, y])
        print(x, y)
    polygonfill()
    win.getMouse()
