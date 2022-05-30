# author by Michealzou@126.com
# 2022/5/30 14:51
# 定义方法和类供demo04导入
# all变量表示只允许此模块中可以被导出的方法
__all__ = ['fun01', '__fun02', 'MyClass']
def fun01():
    print("这是demo03的fun01方法")


def __fun02():
    print("这是demo03的fun02方法")


class MyClass:
    def fun03(self):
        print("MyClass中的fun03")