# author by Michealzou@126.com
# 2022/5/12 19:17
import os
path01 = "D:\Software"
path02 = "jdk-17.0.2"
# windows下默认使用/分隔
sumpath = os.path.join(path01, path02)
print(sumpath)

# 如果后面路径为空，则用\来结尾
path03 = ""
sumpath02 = os.path.join(path01, path03)
print(sumpath02)