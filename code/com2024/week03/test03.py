"""
    变量：可变化的数据
        命名规则：由字母、数字、下划线组成，不能以数字开头，不能用关键字
    常量：不可变化的数据,一旦定义，值不可改变
        命名规则：由字母、数字、下划线组成，不能以数字开头，不能用关键字
                名字通常是大写
        python中一般不存在常量，通过约定俗成来定义
        变量、常量的定义尽量做到见名知义
"""
firstName = "张"
MAX_SCORE = 100
MIN_SCORE = 0
print(MAX_SCORE, MIN_SCORE)
MAX_SCORE = 0
print(MAX_SCORE)


lastName = "三"
PRICE = 10000