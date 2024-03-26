"""
    运算符：
        算术运算符：+ - * / ...
        比较运算符：> < is(not)
        赋值运算符：= += -=...
        位运算符：<< >>...
        布尔运算符：and or not
            and：只有两个都为True时，结果才为True
            or:只要有一个为True，结果就为True
            not:True-结果False，False-结果True
"""
# is(not)比较两个对象的id是否相同
a = b = c = 10
print(a is not b)  # False
# ==比较对象的值是否相等
print(a == b and b == c)
print(a != b and b == c)
print(a != b or b == c)
print(not a != b)

