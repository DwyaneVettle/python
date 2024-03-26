"""
    for 初始化变量 in 可迭代的对象
        代码块
"""
# for i in 'python':
#     print(i)
#
# print("=======")
# for item in range(0, 100, 2):
#     print(item)
print("=======")
even_sum = 0
odd_sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print("偶数之和是：" + str(even_sum))
print("奇数之和是：" + str(odd_sum))
