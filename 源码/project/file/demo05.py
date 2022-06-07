# author by Michealzou@126.com
# 2022/5/12 15:34
# 创建目录
import os
dir_path = input("请输入要创建目录：")
# 判断目录是否存在
y_or_n = os.path.exists(dir_path)
if y_or_n is False:
    os.mkdir(dir_path)
    new_file=open(os.getcwd()+"\\"+dir_path+"\\"+"dir_demo.txt","w",encoding="utf-8")
    new_file.write("life is short, use Python.")
    print("写入成功")
else:
    print("该目录已经存在！")
