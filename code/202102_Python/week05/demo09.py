# author by Michealzou@126.com
# 2022/10/4 10:47
# 计算100内的奇数与偶数和(while)
i = 1
even_sum = 0  # 偶数求和的变量
odd_sum = 0  # 奇数求和的变量
# print(sum(range(1, 101, 2)))
# print(sum(range(2, 101, 2)))
while i <= 100:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i += 1
print("偶数和为：" + str(even_sum))
print("奇数和为：" + str(odd_sum))
