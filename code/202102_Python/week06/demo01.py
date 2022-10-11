# author by Michealzou@126.com
# 2022/10/11 8:48
"""
    求100以内单双数的和
"""
# while
# 1.定义初始化值
i = 1
even_sum = 0 # 偶数求和的初始化变量
odd_sum = 0  # 奇数求和的初始化变量
# 2.条件判断
while i <= 100:
    # 3.判断i是奇数还是偶数
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    # 4.初始值变化
    i = i + 1
print("偶数的和为"+str(even_sum))
print("奇数的和为"+str(odd_sum))


even_sum = 0 # 偶数求和的初始化变量
odd_sum = 0  # 奇数求和的初始化变量
for i in range(1, 101):
    # 3.判断i是奇数还是偶数
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print("偶数的和为" + str(even_sum))
print("奇数的和为" + str(odd_sum))