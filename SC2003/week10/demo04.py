# author by Michealzou@126.com
# 2022/4/25 14:58
# return后没有数据相当于None，函数体没有return，相当于None
def fun01(account):
    print("fun01执行了。。。。")
    return account

re = fun01(10)
print(re)