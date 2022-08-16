# author by Michealzou@126.com
# 2022/8/5 11:47
# 6.4
# 计算0！+1！+4！+7！+…+13!(while)
jie_0 = 1
i = 1
sum = 0

# ********** Begin *********

while i <= 13:
    # 对每一次循环后的i求阶乘
    ji = 1
    j = 13
    while j > 0:
       ji *= j
       j -= 1
    sum += ji
    i += 3

# ********** End *********

print("0！+1！+4！+7！+…+13!={}".format(sum+jie_0))