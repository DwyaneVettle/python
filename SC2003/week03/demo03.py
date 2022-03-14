# author by Michealzou@126.com
# 2022/3/7 14:53
# 字符串的索引和切片
# Python可以采用的索引方式有正向索引和逆向索引
# 正向索引从第一个字符开始下标位0，每增加一个字符索引值+1
# 逆向索引从最后一个字符开始下标为-1，逆向增加一个字符索引值-1
str1 ='Python'
print(str1[2])
print(str1[-4])
# 索引不能越界
# print(str1[6]) IndexError: string index out of range
# 切片-[起始值:末尾值:步长]-步长默认为1，为默认值的时候可以不写
# 左闭右开
print(str1[2:4:1])
print(str1[1:5:3])
# 1.只要ello；2.  只要o--用逆向索引的方式切片
str2 = 'HelloWorld'
print(str2[1:5])
print(str2[4:7:2])
print("================")
print(str2[-9:-5:1])
print(str2[-6:-3:2])


