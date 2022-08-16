# author by Michealzou@126.com
# 2022/8/5 10:39
# 6.2
"""
计算100内的奇数与偶数和（while）
"""
j = 1  # 初始化变量
even_sum = 0  # 偶数求和变量
odd_sum = 0   # 奇数求和变量

# ********** Begin *********

while j <= 100:
    if j % 2 == 0:
        even_sum += j
    else:
        odd_sum += j
    j += 1

# ********** End *********

print("奇数和：%d,偶数和：%d" %(odd_sum, even_sum))
