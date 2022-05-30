# author by Michealzou@126.com
# 2022/5/30 16:13
# 文件的读写
# write()写入字符串,writelines()写入序列
txt = open("a",mode="w",encoding="utf-8")
txt.write("人生苦短，快用python")
print(txt.write("\n"+"Hello World"))
lst = ["\n"+"Hello World","\n"+"人生苦短，快用python"]
txt.writelines(lst)
# 文件定位读取,tell()获取文件读写位置，seek()设置当前文件读写位置
print(txt.tell())
txt.seek(41,0)
txt.write("abc")
