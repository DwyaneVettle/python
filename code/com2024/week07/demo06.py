"""
    for 自定义变量 in 可迭代对象:
        循环体
    执行流程：自定义变量在这个可迭代对象中，执行循环体
    可迭代对象:字符串、列表、元组、字典等
    取出可迭代对象的每一个元素
    i是自定义变量，可以自定义，但是不要和关键字冲突，也可以用_代替
    range(start, stop, step)
"""
# for i in 'python':
#     print(i)
#
# for _ in 'hello':
#     print(_)
for i in range(1, 10, 1):
    print("人生苦短，快用python！")
# 求0-100之间奇数和偶数的和
# 偶数和
# even_sum = 0
# # 奇数和
# odd_sum = 0
# # 2.遍历0-100
# for i in range(0, 101):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
# print(f"偶数的和为{even_sum}")
# print(f"奇数的和为{odd_sum}")
