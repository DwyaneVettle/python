# author by Michealzou@126.com
# 2022/4/19 11:40
# 文件的打开
file = open('a.txt', 'w', encoding='utf-8')
# 文件的写入,若文件不存在，会创建，若文件存在，不执行write()写入内容，会清空内容
# \n 表示换行，如果没有不会换行
file.write("hello world\n")
file.write("人生苦短，快用Python")
# 关闭
file.close()
