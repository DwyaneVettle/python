"""
    商品网购替代率条形图
    在图形中如果有中文需要改变字符编码的设置
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
"""
import matplotlib.pyplot as plt
import numpy as np

# 显示中文
# 运行配置参数中字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 轴axes正常显示正负号
plt.rcParams['axes.unicode_minus'] = False
# 1.准备数据
# 1.1 商品替代率
x = np.array([0.959, 0.951, 0.935, 0.924, 0.893,
              0.892, 0.865, 0.863, 0.860, 0.856,
              0.854, 0.835, 0.826, 0.816, 0.798,
              0.765, 0.763, 0.670])
y = np.arange(1, 19)
# 1.2 商品替代率对应的x轴坐标
labels = ["家政、家教、保姆等生活服务", "飞机票、火车票", "家具",
          "手机、手机配件", "计算机及其配套产品", "汽车用品", "通信充值、游戏充值",
          "个人护理用品", "书报杂志及音像制品",
          "餐饮、旅游、住宿", "家用电器",
          "食品、饮料、烟酒、保健品",
          "家庭日杂用品", "保险、演出票务",
          "服装、鞋帽、家用纺织品", "数码产品",
          "其他商品和服务", "工艺品、收藏品"]
# 2.绘制图形
plt.barh(y, x, tick_label=labels, align="center", height=0.5)
plt.show()
