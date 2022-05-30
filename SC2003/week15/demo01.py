# author by Michealzou@126.com
# 2022/5/30 14:13
# __all__定义可以导出的模板，只针对from ... import...
__all__ = ['fun01', 'fun02', "Student"]
def fun01():
    print("这是demo01的fun01方法")


def fun02():
    print("这是demo01的fun02方法")


class Student:
    name = "john"
    def fun03(self):
        print("这时student类中的方法")


if __name__ == '__main__':
    fun01()