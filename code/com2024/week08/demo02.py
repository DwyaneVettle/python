"""
    99乘法表
    行：9
    列：行数=列数
"""
for i in range(1, 10):  # 控制行
    for j in range(1, i + 1):
        print(i, "x", j, "=", i*j, end="\t")
    print()
i = 1
j = 1
while i <= 9:
    while j <= i:
        print(i, "x", j, "=", i*j, end="\t")
        j += 1
        print()
        i += 1
        j = 1
    print()