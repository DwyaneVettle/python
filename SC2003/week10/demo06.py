# author by Michealzou@126.com
# 2022/4/25 15:33
# 实参
def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 1.位置传参实参和形参一一对应
fun01(1, 2, 3, 4)
# 2.关键字传参
fun01(d=2, c=4, a=6, b=8)
# 3.序列(字符串/列表/元组)传参，使用*拆分序列
list01 = [1,"abc",True,20.2]
fun01(*list01)
# tup = tuple(1,2,3,4)
# fun01(*tup)
# 4.字典传参，将形参作为key存放，只需要传入value。用**拆分
dict01 = {"a":1,"b":"abc","c":True,"d":2020}
fun01(**dict01)

