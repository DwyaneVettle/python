"""
    嵌套循环语句：
        外循环控制行，内循环控制列
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "*", j, "=", i * j, end='\t')
    print()
