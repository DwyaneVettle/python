"""
    函数的返回值
    def 函数名():
        return 返回值
    注意：return后面的语句不再有任何的作用
        return后面没有数据，相当于None
        函数体没有return，也相当于是None
"""


def fun01():
    print("fun01执行咯！！！")
    # return 

re = fun01()
print(re)  # None
