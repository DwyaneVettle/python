# author by Michealzou@126.com
# 2022/8/8 11:23
# 两数相加
def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    else:
        print("数据格式错误")

# 两数相减
def sub(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x-y
    else:
        return "数据不是int类型"

print(add(10, 20))
print(sub(20, 10))