"""
    python中的关键字是不能被用来命名标识符
        help(keyword)
"""
print(help("keywords"))

# 变量命名：变量名=value
a = 123
print(a)
# 回收变量：del--手动回收
del a
# print(a)
"""
    如果变量没有并引用（引用指数器=1），被内存自动 回收
    
    python中变量的命名还可以支持级联赋值和系列解包赋值
    a = b = 100
    a,b,c = 100, 200, 300
    级联赋值变量id相同，不同变量指向同一个堆内存
"""
a = b = 100  # 级联赋值,id相同
print(id(a))
print(id(b))

# 系列解包赋值的值和变量应该一一对应
x, y, z = 10, 20, 30
print(id(x), id(y), id(z))
"""
    x, y, z = 10, 20
    print(x, y)
"""
# 常量的命名方式：常量名=值   常量名通常所有字母都大写
MAX_SCORE = 100
MIN_SCORE = 0
print(MAX_SCORE, MIN_SCORE)
