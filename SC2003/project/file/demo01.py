# author by Michealzou@126.com
# 2022/4/12 9:05
# 文件的打开
"""
file：文件名
mode:文件打开的方式,r-只读打开，w-只写打开，a-追加打开
encoding:字文件的编码格式，常见gbk和utf-8
返回值是一个文件对象
"""
txt = open("test.txt", mode='r', encoding="utf-8")
print(txt)
# 文件的读取
buff = txt.read()
print(buff)
# 文件的关闭
txt.close()
