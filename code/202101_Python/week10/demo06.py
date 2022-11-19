# author by Michealzou@126.com
# 2022/11/9 10:26
"""
    def 定义函数的关键字 define
    attrack 函数名
    增加代码的重用性，简化代码，增加程序的可拓展性
"""
def attrack():
    print("直拳")
    print("勾拳")
    print("降龙十八掌")

attrack()
attrack()
attrack()
attrack()
print("------------")

def attrack(num):
    for i in range(num):
        print("直拳")
        print("勾拳")
        print("降龙十八掌")


attrack(21)
