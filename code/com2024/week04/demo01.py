"""
    字符串格式化方式
    方式：占位符%，format()方法，f-strings三种方式

    {}.format(参数)
    f-{strings}三种方式
"""
name = "micheal"
age = 20
# 1.%占位符
print("大家好，我是%s，我今年%d" % (name, age))

# 2.format()方法
print("大家好，我是{}, 我今年{}".format(name, age))

# 3.f-{strings}
print(f"大家好，我是{name}, 今年{age}")