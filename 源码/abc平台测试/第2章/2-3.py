# author by Michealzou@126.com
# 2022/8/8 12:44
# 函数式编程
def add(x, y):
    return x+y

def mult(x, y):
    return x*y


def my_function(a, b, func_name):
# 根据函数的调用，返回恰当的值

    return func_name(a, b)

print(my_function(3, 6, add))
print(my_function(3, 6, mult))