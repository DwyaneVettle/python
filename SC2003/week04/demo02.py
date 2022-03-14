# author by Michealzou@126.com
# 2022/3/14 14:59
"""
range()函数：左开右闭
range(stop):表示从0开始取值，一直到stop结束
range(start, stop): 表示从start开始，到stop结束
range(start, stop, step):表示从start开始，到stop结束，步长为step
"""
# for i in range(100):
#     print(f"循环{i}次")
# for i in range(50, 100):
#     print(f"循环了{i}次")
for i in range(50, 100, 2):
    print(f"循环了{i}次")
print(5 in range(1, 100))
