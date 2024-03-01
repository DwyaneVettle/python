"""
    python一切皆为对象
    每一个对象都由标识、类型、值组成
        标识：唯一标识对象  -- id()
        类型：对象的表示形式、数据类型  --type()
        值：数据信息  --value()
"""
a = 100
b = "hello"
c = True
# 获取对象的标识
print(id(a))  # 2167966928208
print(id(b))  # 2167968234608
print(id(c))  # 140708632456040

# 获取对象的类型
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'bool'>

# 获取对象的值
print(a)  # 100
print(b)
print(c)
