# author by Michealzou@126.com
# 2022/5/23 17:08
import time
# 时间模块
before = time.time()
for i in range(10000):
    print(123)
after = time.time()
print(after - before)
