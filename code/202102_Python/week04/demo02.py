# author by Michealzou@126.com
# 2022/9/27 9:12
"""
上周作业
1.将字符串str01 =  "人生苦短，快用Python"按切片截取如下数据
人生
短快
th
用o
生P
"""
str01 = "人生苦短，快用Python"
print(str01[0:2:])  # 人生
print(str01[-13:-11])
print(str01[3:6:2])
print(str01[-10:-7:2])  # 倒叙切片：短快

