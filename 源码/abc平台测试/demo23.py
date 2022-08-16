# author by Michealzou@126.com
# 2022/8/7 21:35
# 8.5
# 字符串的切片（重点）
# 切片语法：  str[start:end:step]  区间【start，end） step表示切片步长

num = "123456789"
# 起始索引start默认是0，结束索引end 默认是-1
print(num[0:-1])  # -1表示最后一个索引
print(num[-3:-1])  # 78
print(num[-1:-3:-1])  # 98
print(num[::3]) # 147

# ********** End *********