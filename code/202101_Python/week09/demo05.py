# author by Michealzou@126.com
# 2022/11/2 11:14
"""
    列表：[]
        优点：内存占用少
        缺点：查找-切片和下标，耗时长
    字典：{k:v}
        优点：通过key查找value,耗时短
        缺点：占用内存多
    练习:
        在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.
[
    {“无忌”:[赵敏,周芷若,小赵]}
]
"""
# 1.创建列表存放个人爱好
list_hobby = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict01 = {name: []}
    list_hobby.append(dict01)
    while True:
        hobby = input("请输入你的爱好：")
        if hobby == "":
            break
        dict01[name].append(hobby)
print(list_hobby)

"""
{
    “无忌”:[赵敏,周芷若,小赵]
}
"""