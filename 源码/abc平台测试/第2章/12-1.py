# author by Michealzou@126.com
# 2022/8/8 14:23
import math


def distance(x1, y1, x2, y2):
    """
       计算两点之间的距离
       :param x1: x1坐标
       :param y1: y1坐标
       :param x2: x2坐标
       :param y2: y2坐标
       :return: 两点之间的长度
       """
    print(math.sqrt((x1-x2)**2+(y1-y2)**2))

distance(0,0,3,4)
