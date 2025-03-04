"""
    箱型图：
        boxplot()
        x:绘制箱型图的数据
        sym:异常值垂直摆放
        vert:是否将箱型图垂直摆放
        meanline:箱型图的中位线
        widths:箱型图的宽度，默认是0.5
        patch_artist:是否填充箱型图的颜色
        showfliers:是否显示异常值
"""
import matplotlib.pyplot as plt
import numpy as np

# 生成一组随机数据
data = np.random.randn(100)
plt.boxplot(data, meanline=True, widths=0.3, patch_artist=True,
            showfliers=False)
plt.show()

