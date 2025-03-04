"""
    雷达图：
    polar()
        theta:表示每个数据点的夹角
        r:表示每个维度距离圆心的位置
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dim_num = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])
angles = np.linspace(0, 2 * np.pi, dim_num, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
data = np.concatenate((data, [data[0]]))
# 维度标签
radar_labels = ['研究型(I)', '艺术性(A)', '社会性(S)',
                '企业型(E)', '传统型(C)', '现实性(R)']
radar_labels = np.concatenate((radar_labels, [radar_labels[0]]))
radar_labels = np.concatenate((radar_labels, [radar_labels[0]]))
# 绘制雷达图
plt.polar(angles, data)
plt.show()
