import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备数据
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y1, y2 = np.sin(x), np.cos(x)

# 绘制图形
lines = plt.plot(x, y1, x, y2)
# 绘制图例
plt.legend(lines, ['上海', '北京'], shadow=True, fancybox=True)
# 绘制辅助图形-x/y轴的标签 xlabel(xlabel, fontdict, labelpad) ylabel()
plt.xlabel("年份")
plt.ylabel("雨量")

# 绘制刻度范围和刻度标签 xlim() xticks()
plt.xlim(x.min() + 1.7, x.max() + 1.7)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi / 2$', r'$\pi$'])

# 添加网格-grid(which='major', axis='both', lw)
plt.grid(which='major', axis='both')

# 添加参考线 axhline()水平参考线  axvline()垂直参考线
plt.axhline(y=2, linestyle='dashed')
plt.axvline(x=1, linestyle='-')

# 添加参考区域 axhspan()水平参考区域 axvspan()垂直参考区域
plt.axhspan(ymin=0.5, ymax=1.0, alpha=0.3)
plt.axvspan(xmin=0.5, xmax=1.0, alpha=0.3)
# 展示图形
plt.show()

