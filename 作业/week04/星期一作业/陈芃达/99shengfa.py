# 2022/3/20 20:06
# 99乘法表
for a in range(1, 10):
    for b in range(1, a+1):
        print(a, 'x', b, '=', (a*b), end='\t')
    print()