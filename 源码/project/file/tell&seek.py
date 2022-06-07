# author by Michealzou@126.com
# 2022/4/26 9:21
# 文件的打开
file = open('a.txt', 'r', encoding='utf-8')
print(file.read(5))  # 读取5个字节
print(file.tell())  # 15 输入文件读取的位置(汉字为3个字节)

file = open('a.txt', 'w', encoding='utf-8')
file.seek(3,0)
print(file.write("你好！！"))
file.close()