"""
    变量：具有可改变值的对象
    命名： 变量名 = 变量值
    变量可以手动删除：del 变量名
"""
name = "张三"
sex = "男"
name = "李四"
del name # 删除变量
# print(name)  # NameError: name 'name' is not defined

# 链式肤质-快速定义多个变量
# a = 10
# b = 10
a = b = 10
print(a, b)

# 系列解包赋值
a, b, c = 10, 20, 30
print(a, b, c)



