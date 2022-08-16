# author by Michealzou@126.com
# 2022/8/8 14:10
# 点(x,y)  圆(圆心，半径) ，请使用面向对象的思想完成编程
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

class Circle:
    def __init__(self, center, r):
        # 圆心center本质就是一个点
        if isinstance(center, Point):
            self.center = center
        else:
            self.center = Point(0.0, 0.0)  # 当点不正确时，默认圆心就是坐标原点
        if isinstance(r, int) or isinstance(r, float):
            self.r = r
        else:
            r = 0

    def __str__(self):
        return "center of a circle is ({},{}),radius {}".format(self.center.x, self.center.y, self.r)

# 在(3.0, 0.0)创建圆点，并根据圆点创建圆

p = Point(3.0, 0.0)
yuan = Circle(p, 3)
print(yuan)