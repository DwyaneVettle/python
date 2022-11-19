# author by Michealzou@126.com
# 2022/11/8 8:51
"""
    在控制台中循环录入字符串，
    输入空字符串停止，打印所有不重复的文字

    列表：任何数据类型，可重复
    元组：任何数据类型，不可重复，按需分配
    字典：k-v
    集合：不重复不可变
"""
# 1.定义集合
set01 = set()
# 2.循环录入字符串
while True:
    str01 = input("请输入字符串：")
    # 3.录入空字符串停止
    if str01 == "":
        break
    # 4.往集合添加字符串
    set01.add(str01)
for i in set01:
    print(i)
