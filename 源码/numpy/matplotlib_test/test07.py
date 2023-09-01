import numpy as np
import matplotlib.pyplot as plt

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.array([0.959, 0.951, 0.935, 0.924, 0.893,
              0.892, 0.865, 0.863, 0.860, 0.856,
              0.854, 0.835, 0.826, 0.816, 0.798,
              0.765, 0.763, 0.670])
y = np.arange(1, 19)
labels = ["家政、家教、保姆等生活服务", "飞机票、火车票", "家具",
          "手机、手机配件", "计算机及其配套产品", "汽车用品", "通信充值、游戏充值",
          "个人护理用品", "书报杂志及音像制品", "餐饮、旅游、住宿", "家用电器",
          "食品、饮料、烟酒、保健品", "家庭日杂用品", "保险、演出票务",
          "服装、鞋帽、家用纺织品", "数码产品", "其他商品和服务", "工艺品、收藏品"]
# 绘制条形图
plt.barh(y, x, tick_label=labels, align="center", height=0.6)
plt.show()
