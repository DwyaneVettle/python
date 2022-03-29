# author by MiWuXianLi
# 2022/3/20 15:20
# for循环打印99乘法表
for a in range(1, 10):
    for b in range(1, a+1):
        print(a, '*', b, '=', (a*b), end='\t')
    print()