import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y1, y2 = np.sin(x), np.cos(x)
plt.plot(x, y1, x, y2)
# 设置x轴和y轴的标签
plt.xlabel("x轴")
plt.ylabel("y轴")
# 添加标题
plt.title("正弦曲线和余弦曲线")
# 添加图例
lines = plt.plot(x, y1, x, y2)
plt.legend(lines, ['正弦', '余弦'], shadow=True, fancybox=True)
# 添加网格
plt.grid(axis='y', linewidth=0.3)
# 添加参考线
plt.axvline(x=0, linestyle='--')
plt.axhline(y=0, linestyle='--')
# 添加参考区域
plt.axvspan(xmin=0.5, xmax=2.0, alpha=0.3)
plt.axhspan(ymin=0.5, ymax=1.0, alpha=0.3)

# 添加指向型注释文本
plt.annotate('最小值', xy=(-np.pi / 2, -1.0), xytext=(-(np.pi / 2), -0.5), arrowprops=dict(arrowstyle="->"))

# 添加无指向型注释文本
plt.text(3.10, 0.10, "y=sin(x)", bbox=dict(alpha=0.2))

# 添加表格
plt.table(cellText=[[6, 6, 6], [8, 8, 8]], colWidths=[0.1] * 3, rowLabels=['第1行', '第2行'], colLabels=['第1列', '第2列', '第3列'], loc='lower right')


# 设置x轴的刻度范围和刻度标签
plt.xlim(x.min() * 1.5, x.max() * 1.5)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2,
                 np.pi],  [r'$-\pi$', r'$-\pi/2$',
                 r'$0$', r'$\pi/2$', r'$\pi$'])

plt.show()
