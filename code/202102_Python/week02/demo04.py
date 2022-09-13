# author by Michealzou@126.com
# 2022/9/13 11:01
"""
   标识符的命名规则
   1.区分大小写
   2.标识符采用驼峰命名法命名
   3.不能以数字开头，可以使用_,字母等开头
   4.不能使用关键字来命名标识符
   5.构造函数,析构函数是以__开始，__结束
"""


def helloWorld():
    print(1 + 1)


def HELLO():
    print(2 + 2)


helloWorld()
HELLO()