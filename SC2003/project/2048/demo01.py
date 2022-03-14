# author by Michealzou@126.com
# 2022/3/14 22:16
import random
import time
import os
str_dt = "2022-03-01 12:59:59"
# 转换成数组
time_struct = time.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
# 转换成时间戳
timestamp = time.mktime(time_struct)
print(time_struct)
print(timestamp)