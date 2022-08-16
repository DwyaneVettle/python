# author by Michealzou@126.com
# 2022/8/7 21:25
# 8.4
# 2.字符串大小写转换，首字母大写
str = "shangHai"

# ********** Begin *********

print(str.upper())  # 全部转大写
print(str.lower())  # 全部转小写
print(str.capitalize())  # 首字母大写

# ********** End *********


# 3.去掉两端的空格(开发中经常使用)
uname = "  admin  "

# ********** Begin *********

uname2 = uname.strip()
print(len(uname2))

# ********** End *********

