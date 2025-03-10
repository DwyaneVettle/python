"""
    每一个字符串的每一个字符都有一个索引
    规则：
    1.从左边第一个字符开始索引为0，向右每增加一个字符
    索引加1，直至最后一个字符索引为n-1
    2.从右边开始的第一个字符索引为-1,直到最左边的-n结束
    通过索引获取对应字符的方法  字符串[索引]

    切片：获取字符串中对应的一个或多个字符
    语法：字符串[开始下标:结束下标:步长]
    开始下标表示要截取字符串开始的位置
    结束下标表示要截取字符串结束的位置
    注意：左开右闭：包含开始，不包含结束
    步长：间隔几个字符截取，默认为1
    切片无论是正索引还是负索引都是从左往右
"""
name = "python"
# 正索引获取t
print(name[2])  # 正索引
# 倒索引获取t
print(name[-4])
# 切片 th
print(name[2:4:1])
print(name[-4:-2:1])
# print(name[-3:-5:1])
# 索引和切片不能超过索引值
# print(name[6])  # IndexError
# 改变步长切片
print(name[1:4:2])
# python -> pn
print(name[0:6:5])
print(name[-6:0:5])
print("================")
myStr = 'hello world and Python and java and php'
# 1.获取第一个l
print(myStr[2])
print(myStr[-37])
# 2.获取最后一个h
print(myStr[-2])
# 3.获取三个a
print(myStr[-11])

