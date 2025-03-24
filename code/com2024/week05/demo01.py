"""
    回顾字符串索引和切片
    1. 索引
        字符串[索引]
        - 正向索引：从0开始，从左到右
        - 反向索引：从-1开始，从右到左
    2. 切片
        字符串[start:stop:step]
        - start:起始索引
        - stop:结束索引
        - step:步长
        无论是正向还是反向切片都应该遵从从左到右的顺序
"""
# str01 = "hello python"
# # 通过索引获取p
# print(str01[6])
#
# print(str01[-6])
# # 切片o p
# print(str01[4:7:1])
# print("==============")
# print(str01[-8:-5:1])



"""
    input函数：用于获取用户在控制台中的输入，并可以保存到变量中
    变量的类型？字符串
"""
# num01 = int(input("输入数字1："))
# num02 = int(input("输入数字2："))
# print(num01 + num02)

print(1 != 1)
print(1 == 1)


print(1 > 0 and 1 < 2)  # and只有两边同时为True才为True，其余为False
print(1 > 0 or 1 < 2)  # or只要有一边为True为True，其余为False
print(not 1 < 2)  # or只要有一边为True为True，其余为False


"""
    位运算符:
        位与&：对应数位都是1结果位数才是1，否则为0
        位或\|:对应数位都是0结果位数才是0，否则为1
        >> 右移：除以2
        >> 左移：乘以2
"""
print(4 & 8)
print(4 | 8)
print(4 >> 1)
print(4 << 1)

print(5 & 7)
print(5 | 7)