# author by Michealzou@126.com
# 2022/9/27 8:50
"""
    字符串的相关操作
    替换：字符串.replace(old,new,count)
    count表示替换的次数，默认是全部替换
    当count数值超过了实际要替换的次数，默认替换所有
    分割：字符串.split("要分隔的字符",count)
    count表示分割的次数
    返回的是一个列表
"""
myStr = 'hello world and Python and java and php'
newStr = myStr.replace('and', 'he')
print(newStr)
newStr02 = myStr.replace('and', 'he', 4)
print(newStr02)

newStr03 = myStr.split("and")
print(newStr03)  # ['hello world ', ' Python ', ' java ', ' php']
newStr04 = myStr.split("and", 1)
print(newStr04)  # ['hello world ', ' Python and java and php']
print("----------------")
"""
    字符串的拼接:要拼接的字符串.join(字符串)
    在每一个具有下标的字符后都会拼接一次
"""
myList = ['aa', 'bb', 'cc']
newStr = "and".join(myList)
print(newStr)  # aaandbbandcc
myList02 = "我的年龄是20岁"
newStr02 = "我的姓名是刘德华".join(myList02)
print(newStr02)
myStr03 = "我的姓名是刘德华"
print(myStr03 + myList02)
