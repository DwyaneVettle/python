"""
    python函数的返回值：
        方法定义者告诉调用者的结果
        return 需要返回的值
    return的下面的所有语句没有任何作用，不再执行
    return后没有数据返回相当于None，如果函数体没有return，相当于None
"""
def fun01():
    print("fun01执行了！！")
    return


re = fun01()
print(re)
