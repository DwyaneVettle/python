# author by Michealzou@126.com
# 2022/5/9 15:12
# 匿名函数：只能完成一个功能的函数
# lambda [arg01,arg02...] : expression
def sum(num01,num02):
    return num01 + num02

print(sum(3,5))

sum = lambda num03,num04 : num03 + num04
print(sum(3,5))