"""
    采用10000个随机数绘制人脸识别的
    直方图
    hist()
    random
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成10000个随机数
random_state = np.random.RandomState(196846430)
x = random_state.randn(10000)

# 绘制直方图
plt.hist(x, bins=30)
plt.show()


