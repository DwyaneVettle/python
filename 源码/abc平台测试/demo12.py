# author by Michealzou@126.com
# 2022/8/5 10:45
# 6.3
"""
# 计算6的阶乘  (6*5*3*4*2*1)
"""

ji = 1
num = 6

# ********** Begin *********

while num > 0:
    ji *= num
    num -= 1

# ********** End *********

print("6!={}".format(ji))  #"".format()  字符串的第二种格式化方法