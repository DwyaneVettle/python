# author by Michealzou@126.com
# 2022/3/7 14:30
# 字符串的常用操作
# 1.字符串的拼接-+
str1 = '人生苦短,'
str2 = '快用Python。'
print(str1 + str2)  # 人生苦短,快用Python。
# 2.字符串的替换-replace(old, new)
str3 = '我是李刚'
str4 = str3.replace('我', '你')
print(str4)
# 用repalce()方法如果没有找到替换对象，那么会输出原字符串
print(str3.replace('你', '他'))
# 3.字符串的截取-split()
str5 = "人生苦短,快用Python。"
print(str5.split('苦'))
str6 = '1 2 3'
print(str6.split())
# 4.去除空格或特殊字符-strip()
str7 = '%%Python%%'
print(str7.strip("%"))


