# author by Michealzou@126.com
# 2022/5/12 19:13
# 判断路径是否存在
import  os
current_path = "D:\Software"
current_path_file = "D:\Software\jdk-17.0.2"
print(os.path.exists(current_path))
print(os.path.exists(current_path_file))