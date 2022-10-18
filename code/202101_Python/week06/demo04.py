# author by Michealzou@126.com
# 2022/10/12 10:21
"""
    输出50以内5的倍数的数
    continue 跳出当前代码，执行下一个段代码
"""
for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)
