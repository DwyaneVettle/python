# author by Michealzou@126.com
# 2022/5/23 16:46
# sys模块，系统模块
import sys
# 获取程序绝对路径
print(sys.argv)
# 获取python解释器的版本
print(sys.version)

import random
# 生成一个0-1之间的随机数
print(random.random())
# 随机生成整数
print(random.randint(0,100))
# 随机生成浮点数
print(random.uniform(1.0,100.0))
# 从序列中随机选择
name = ["李刚", "李渊", "李世民", "李隆基", "李自成"]
print(random.choice(name))
print(random.choices(name))