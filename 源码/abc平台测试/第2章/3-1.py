# author by Michealzou@126.com
# 2022/8/8 12:49
# 设计递归必须要有结束条件
# 6! = 6*5*4*3*2*1*jie_cheng(0)
def jie_cheng(num):
# 判断参数的数值，并处理阶乘业务逻辑


    if isinstance(num, str) or isinstance(num, float):
        return "计算阶乘需要输入整数"
    if num < 0:
        return "负数没有阶乘"
    if num == 0:
        return 1  # 阶乘的结束条件
    return num*jie_cheng(num-1)  # 递归

print(jie_cheng(6))