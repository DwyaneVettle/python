import numpy as np
import matplotlib.pyplot as plt


def kock_snowflake(order, scale=10):
    def _koch_snowflake_compex(order):
        if order == 0:
            # 初始三角形
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) + np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3
            # 起点
            p1 = _koch_snowflake_compex(order - 1)
            # 终点
            p2 = np.roll(p1, shift=-1)
            # 向量连接
            dp = p2 - p1
            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_compex(order)
    x, y = points.real, points.imag
    return x, y


x, y = kock_snowflake(order=2)
fig = plt.figure()
ax = fig.add_subplot(111)
# 填充多边形使用fill()
ax.fill(x, y, facecolor='orange', edgecolor='red', lw=3)
plt.title('彩色的雪花')
plt.show()
