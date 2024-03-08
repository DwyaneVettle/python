"""
    python的基础数据类型：整型int、浮点型float、布尔型bool、字符串类型str

    1.整型：计算机10进制
            二进制：0b
            八进制：0o
            十六进制：0x
    2.浮点类型：小数
            浮点类型的数据不能用于计算，丢失精度，小数运算使用Decimal

    3.布尔类型：True、False
                转换成整型：True-1、False-0

    4.字符串类型：
            表现形式：''、“”、变量=”“”换行“”“
"""
# 整型
num01 = 0b0001
num02 = 0o34567
num03 = 0xFFFFBB
print(num01, num02, num03)
num04, num05, num06 = 100, -100, 0

# 浮点类型
print(1.1 + 2.2)

from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))

# 布尔类型
b01 = True
b02 = False
print(type(b01), type(b02))  # <class 'bool'> <class 'bool'>
print(b01 + 1)  # 2
print(b02 + 1)  # 1

# 字符串
str01 = 'python'
str02 = "python"
print(str01, str02, id(str01), id(str02))
str03 = """
    人生苦短，
    快用python
"""
print(str03)

name = "四川城市职业学院"
addr = "成都龙泉驿"
print("我的学校是：" + name + ",它的地址在：" + addr)
