# author by Michealzou@126.com
# 2022/8/8 12:56
# 需要求任意数的平方（参数只能是int,若不是int就抛出异常）
def pow(num):
    if not isinstance(num, int):
# 抛出异常
        raise TypeError('参数只能是int类型')  # 异常处理机制1：抛出异常
    return num**2
# 异常处理机制2：捕获异常
try:
    num = 6
    result = pow(num)
    print("{}的平方为:{}".format(num,result))


except TypeError as e:  # 捕获到异常的对象
    print(e)
