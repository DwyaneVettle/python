# author by Michealzou@126.com
# 2022/8/8 11:29
# 全局变量(函数外)与局部变量
a = 10
g_b = 20  # 资源的共享

# 定义show()和show2()，在show()中定义变量a=5,全局变量g_b=15，并分别在两个函# 数中输出变量a和g_b

def show():  # 局部变量
    a = 5  # 局部变量
    global g_b  # 再方法内使用全部变量时需要先声明再赋值
    g_b = 15
    print(a, g_b)


def show2():
    print(a, g_b)


show()
show2()