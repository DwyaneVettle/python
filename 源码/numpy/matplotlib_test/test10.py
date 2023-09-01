import numpy as np
import matplotlib.pyplot as plt
# 10000个随机数
random_state = np.random.RandomState(19680801)
radom_x = random_state.randn(10000)
# 绘制包含25个矩形条的直方图
plt.hist(radom_x, bins=25)
plt.show()
