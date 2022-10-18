# author by Michealzou@126.com
# 2022/10/12 8:38
"""
    100以内单双数的和
        1.取出100以内的正整数
        2.遍历100以内的数，并判断它是单数还是双数
        3.初始化求和的变量，单数，双数
        4.累加求和
"""
# 1.使用while取出100以内的正整数
# i = 1
# # 初始化求和的变量
# even_sum = 0
# odd_sum = 0
# while i <= 100:
#     # print(i)
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum += i
#     # 改变变量值
#     i = i + 1
# print(f"偶数的和为{even_sum}")
# print(f"单数的和为{odd_sum}")

# for(i = 1; i <= 100; i++) {}
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    # print(i)
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum += i
print(f"偶数的和为{even_sum}")
print(f"单数的和为{odd_sum}")
