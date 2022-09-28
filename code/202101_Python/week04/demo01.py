# author by Michealzou@126.com
# 2022/9/28 8:49
"""
    1.将字符串str01 = "人生苦短，快用Python"按切片截取如下数据
        人生
        短快
        th
        用o
        生P
        str[start:end:step]
        start:表示切片的开始，包含其中
        end:表示切片的结束，不包含，最好切片后退一位
        step:表示的切片的步长，表示隔几个进行切片，end-1-start
        切片无论是正序还是倒叙都是从左至右的
"""
str01 = "人生苦短，快用Python"
print(str01[0:2:1])  # 人生
print(str01[-13:-11:])
print(str01[3:6:2])
print(str01[-10:-7:2])
print(str01[11:13:2])
