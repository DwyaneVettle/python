"""
    初始条件值
    while 条件表达式:
        条件执行体（循环体）
        条件变化
"""
# 需求：0-10
i = 0
while i <= 10:
    print(i)
    i += 1
print("========")
# 练习：求1-5之间所有整数的和
sum = 0
i = 1
while i <= 5:
    sum = sum + i
    i = i + 1
print(sum)

print("========")
# 练习：求100以内，所有偶数和奇数的和
even_sum = 0  # 偶数的求和初始化变量
odd_sum = 0  # 奇数的求和初始化变量
i = 1
while i <= 100:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i + 1
print("偶数的和为：" + str(even_sum))
print("奇数的和为：" + str(odd_sum))
