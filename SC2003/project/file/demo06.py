# author by Michealzou@126.com
# 2022/5/12 17:57
# 删除目录
import os
import shutil
# 判断目录是否存在
# print(os.path.exists("重命名"))
# shutil.rmtree("重命名")
# 确认目录是否删除
# print(os.path.exists("重命名"))

# 获取文件夹列表
current_path = r"D:\Software"
print(os.listdir(current_path))