"""
在控制台中循环录入字符串，输入空字符串停止，打印所有不重复的文字
"""
# 创建容器-集合
words = set()
while True:
    word = input("请输入字符串：")
    if word == "":
        break
    words.add(word)
for item in words:
    print(item)
