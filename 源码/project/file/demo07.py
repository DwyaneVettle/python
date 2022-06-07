# author by Michealzou@126.com
# 2022/5/12 19:06
# 路径操作
import os
print(os.path.isabs("test01.txt"))
print(os.path.isabs("D:\Software"))
print(os.path.abspath("test01.txt"))

current_path = os.getcwd()
print(current_path)