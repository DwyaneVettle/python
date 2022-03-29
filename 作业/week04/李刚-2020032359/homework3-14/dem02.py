# 2022/3/14 17:42
# 嵌套for循环打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d\t" % (j,i,j*i),end=" ")
    print()
