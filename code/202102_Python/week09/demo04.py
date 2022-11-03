# author by Michealzou@126.com
# 2022/11/1 10:46
"""
    列表：可变，存放任何数据类型
            优点：切片/索引 得到列表中某一段列表，相较于字典存储孔教较少
            缺点：通过索引查找多个元素时耗时
    字典：可变，存放任何类型的k(str)-v结构的数据
            优点：以k-v结构存放，查找耗时相较于列表少
            缺点：存储空间大，以空间换时间的容器
    案例：
        在控制台中录入多个人的多个喜好,输入空字符停止
        姓名：
            喜好1:
            喜好2：
        姓名：
            喜好1：
            喜好2
        {桂嘉良:["迪丽热巴","洗脚","麻将"]}
"""
dict_hobby = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_hobby[name] = []
    while True:
        hobby = input("请输入你的爱好：")
        if hobby == "":
            break
        dict_hobby[name].append(hobby)

for name, list_hobby in dict_hobby.items():
    print(name)
    for hobby in list_hobby:
        print(hobby)
