"""
    运算符
"""
# 除和整除  /   //
print(10 / 3)
print(10 // 3)

# 取模/余  %
print(10 % 3)

# 赋值运算 +=、-=、*=、/=、//=、%=
a = 10
# b = a + 10
a += 10
a *= 10
print(a)


# 比较运算 <、>、<=、>=、!=  == 得到的结果是布尔类型
print(10 > 5)

# is / is not
print(a is a)


# 布尔运算符 and-所有为True时才为True,or-只要有一个为True就为True,not-取反
print(10 > 5 and 10 < 5)