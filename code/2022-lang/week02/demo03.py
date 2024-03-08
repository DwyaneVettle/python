"""
    字符串的格式化：
        1.%占位符：在使用字符串变量的地方通过%占位，指定类型
        2.format()：通过字符串{}.format()，对应变量放到{}
        3.f-strings: {}
"""
# 1.%占位符
name = "四川城市职业学院"
addr = "成都龙泉驿"
age = 18
print("我的学校是：%s, 它的地址在：%s ,它的年龄是%d" % (name, addr, age))

# 2.format()
print("我的学校是：{},它的地址在：{},它的年龄是{}".format(name, addr, age))

# 3.f-strings
print(f"我的学校是:{name},它的地址在：{addr},它的年龄是{age}")


"""
    字符串操作的相关方法
"""
# replace(old, new, count) count替换的次数
str01 = "人生苦短，我学python，我还学php"
str02 = str01.replace('h', 'k', 1)
print(str02)
str03 = str01.replace("我", "你")
print(str03)

# split() 截取
str01 = "人生苦短，我学python，我还学php"
print(str01.split())  # 不传递参数/其他参数，以列表返回
print(str01.split("我"))  # 当传递的参数为该字符串的字符时，会用逗号替换该字符

# strip() 去除字符串两端的空格
str04 = "    pyt    hon   "
print(str04.strip())


# join() 合并字符串
str05 = "python"
str06 = "java"
str07 = str05.join(str06)
print(str07)
list01 = ["python", "java"]
print("".join(list01))

