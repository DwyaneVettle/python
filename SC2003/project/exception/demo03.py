# author by Michealzou@126.com
# 2022/5/24 10:53
# finally子句
try:
    file = open("异常.txt",'r')
    file.write("人生苦短，快用python")
except Exception as e:
    print("写入文件失败",e)
finally:
    file.close()
    print("文件已关闭")
