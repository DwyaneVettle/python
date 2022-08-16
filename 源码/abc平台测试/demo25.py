# author by Michealzou@126.com
# 2022/8/7 21:49
# 8.7
# 1.统计方法 max（） min（） sorted（） reversed()
num2 = "123456789"
# ASCII中 A:65 a:97  0:48
num = [1, 2, 3, 9, 5, 6, 7, 8, 4]

print(min(num))
num3 = sorted(num)  # 默认升序
num4 = sorted(num, reverse=True)  # 降序
num5 = num[::-1]  # 倒序
print(num3)
print(num4)
print(num5)

# enumerate(str)获取索引
str01 = "abcdefg"

# ********** Begin *********

for index, item in enumerate(str01):

# ********** End *********

    print(index, item)

# 2.字符串分割，以#和/为分割符
str02 = "admin#123"

# ********** Begin *********

user = str02.split('#')
print(user)

# ********** End *********
