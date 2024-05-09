"""
    函数：是对一个功能的封装
    作用：能提高代码的复用性和可维护性
    def 函数名():
        函数体
    1.定义函数；2.创建函数体的功能；3.调用函数-函数名()
    注意：函数名和变量的命名规则相同，见名知义
    参数：
        形式参数：形参-定义参数的时候等待用户传递的值，由程序员编写功能时创建
        实际参数：实参-用户调用函数时传递过来的真实的值
"""
def weather(today, temp, air):
    print(f"日期：{today}")
    print(f"温度：{temp}")
    print(f"空间质量：{air}")

weather("4.20", '24', '优')
weather("3.20", '15', '优')

"""
    练习：模拟拳击动作-用直拳，勾拳，肘击三个动作实现三次攻击 attack
"""
def attack(count):
    for i in range(count):
        print("直拳")
        print("勾拳")
        print("肘击")

attack(5)

