# author by Michealzou@126.com
# 2022/8/4 16:02
# 3.4
a = "123"
b = 123
e = 123.0
c = '123'
# 输出b和e是否相等，b是不是e，a和b是否相等，a是不是c
# ********** Begin *********

print(b == e)
print(b is e)
print(a == b)  # 既比较地址，又比较值
print(a is c)  # is比较的是id

# ********** End *********