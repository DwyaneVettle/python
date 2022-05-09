# author by Michealzou@126.com
# 2022/5/9 14:25
# 递归函数：在函数内部调用自己，使复杂的问题简单化，减少代码量
# 求100以内的阶乘
def jiecheng(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # print(100*99*98。。。。*1)
        return num * jiecheng(num - 1)

num = int(input("请输入您想得到的阶乘数："))
print(jiecheng(num))
