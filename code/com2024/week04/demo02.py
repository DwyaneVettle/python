"""
    字符串的相关操作
"""
# 1.拼接 +
str01 = "我是"
str02 = "张三"
str03 = str01 + str02
print(str03)
# 2.字符串替换 str.replace(old, new, count)count为替换次数
# 如果替换只出现一次的字符串，可以不用传递count,默认为1，不传递也会替换所有
str04 = "我是张三"
str05 = str04.replace("张三", "李四")
print(str05)
myStr = 'hello world and Python and java and php'
myStr01 = myStr.replace("h", "H", 2)
print(myStr01)


# 3.字符串的分割str.split()
print(myStr.split("and"))
print(myStr.split())

# 4.用strip()方法来去除字符串两侧的空格
str06 = "      hello        "
print(str06.strip())

# 5.合并字符串 str.join(iterable)
list01 = ["a", "b", "c"]  # 字符串列表
print("".join(list01))
print("-".join(list01))

