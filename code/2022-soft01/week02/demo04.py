"""
    字符串的常见方法
"""
# replace(old, new, count)-字符串的替换
name = "我学的课程叫python"
str01 = name.replace("python", "java")
print(str01)

str02 = "我我我"
str03 = str02.replace("我", "你", 2)
print(str03)

# 字符串的分割split()-默认不加参数（,），返回列表,添加参数，用逗号替换该参数分割
str04 = "人生苦短，快用python"
print(str04.split('苦'))

# 去除字符串两端的空格strip()
name = "   python       "
print(name)
print(name.strip())

# 合并字符串join()
str05 = "aa"
str06 = "bb"
print(str05.join(str06))  # baab
myList = ['aa', 'bb']
newList = "".join(myList)
print(newList)   # aabb


print("========")
"""
    字符串的索引有两种：
        1.正向索引：从第一个字符开始，下标为0，依次递增，n-1结束
        2.反向索引：从最后一个字符开始，下标为-1，依次递减，-n结束
        通过索引找到对应字符的方式是：字符串[index]
"""
str07 = "python"
print(str07[3])
print(str07[-3])
# print(str07[-7])  # IndexError 下标越界

print("========")
"""
    字符串切片：找到指定的字符
        切片的格式：字符串[start:end:step]
                    start:切片开始的下标
                    end:切片结束的下标
                    step:步长-间隔几个字符进行切片,步长默认为1，可以不用写
        注意：切片动作包含start,不包含end
"""
str08 = "python"
print(str08[2:4:1])  # 正向切片
print(str08[-4:-2:1])  # 反向切片
print(str08[-4:-2])  # 反向切片
# 练习：
str09 = "人生苦短，快学python"  # 正向0-12 反向-1--13
# 苦,
print(str09[2:5:2])
print(str09[-11:-8:2])
# 快 p
print(str09[5:8:2])
print(str09[-8:-5:2])
# 生 短 快
print(str09[1:6:2])
print(str09[-12:-7:2])


"""
    编码的转换：ord()-将字符转为数字
              chr()-将数字转为字符
    安装ASCII码表转换
"""
print(ord('A'))  # 65
print(ord('a'))  # 97
print(chr(98))  # b
