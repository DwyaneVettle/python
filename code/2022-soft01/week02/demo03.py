"""
    字符串的格式化：占位符%，format()方法，f-strings
"""
# 字符串的拼接方式
name = '龟叔'
age = 60
print("python的创始人" + name + "他的年龄是：" + str(age))

# 占位符%
name = "python"
print("我们上的课程叫%s" % name)
age = 18
print("我的年龄是%d" % age)
print("python的创始人%s,他的年龄是%d" % (name, age))  # 元组传递


# format()-在字符串所在出用{}占位，字符串.format()
name = "micheal"
sex = "男"
print("姓名是{}，性别是{}".format(name, sex))
# 如果参数顺序打乱，可按照下标传递到大括号，下标从0开始
print("姓名是{1}，性别是{0}".format(sex, name))

# f-strings-所有字符串的前面加字母f，把参数传递到{}
# f-strings效率更高，开发中常用
name = '四川城市职业学院'
addr = '成都龙泉'
print(f"我们的学校是{name},地点在{addr}")
