"""
    字符串的索引 -[index]
    正序：下标从0开始，依次递增
    倒序：下标从-1开始，依次递减
    下标不能超过最大范围，否则报越界异常
"""
str01 = "Python"
print(str01[2])  # 正序t
print(str01[-4])  # 倒叙 t

"""
    切片-[start:end:step]
    start表示切片开始的下标-包含此下标
    end表示切片结束的下标-不包含此下标
    step表示切片的步长-隔几个元素进行切片，默认值为1，可以不传递,步长也要包含一个元素
    切片无论是正序还是倒序都是从左至右进行的
"""
str01 = "Python"
str02 = str01[2:4:1]
print(str02)  # th

str03 = "PythonAndJava"
# dJ
print(str03[8:10])  # dJ
# Ph
print(str03[0:4:3])
# oda
print(str03[4:13:4])
print(str03[-9:0:4])
