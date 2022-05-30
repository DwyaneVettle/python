# author by Michealzou@126.com
# 2022/5/30 15:56
# 文件的读写
# 打开文件 open(),返回的是一个stream流
txt =open("abc",mode="r",encoding="utf-8")
print(txt)
# read()表示读取文件的内容，可以传入多少个字节
buff = txt.read(2)
print(buff)
# readline()读取某一行
print(txt.readline())
# readlines()表示读取所有内容
print(txt.readlines())
# 关闭stream
txt.close()