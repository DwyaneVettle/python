"""
    用while循环计算0-10之间的和
"""
# sum = 0  # 定义的求和初始化变量
# i = 0  # 定义的开始变量
# while i <= 10:
#     sum = sum + i
#     i += 1
# print("0-10之间的和为：" + str(sum))

"""
    练习：计算100以内奇数和偶数之和
"""
i = 1
even_sum = 0  # 偶数求和的初始化变量
odd_sum = 0  # 奇数求和的初始化变量
while i <= 100:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i + 1
print("偶数和为：" + str(even_sum))
print("奇数和为：" + str(odd_sum))

print(sum(range(1, 101, 2)))
print(sum(range(2, 101, 2)))
