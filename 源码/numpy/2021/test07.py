import numpy as np
import matplotlib.pyplot as plt
# 显示中文，需要进行配置,将字体配置成黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 配置参数总的轴axes，正常显示正负号
plt.rcParams['axes.unicode_minus'] = False
# barh() - 条形图

labels = ['家政、家教、保姆等生活服务', '飞机票、火车票', '手机、手机配件',
          '计算机及其配套产品', '汽车用品', '通信充值、游戏充值', '个人护理用品',
          '书报杂志及音响制品', '餐饮、旅游、住宿', '家用电器', '食品、饮料、烟酒、保健品',
          '家庭日杂用品', '保险、演出服务', '服装、鞋帽、家庭纺织品', '数码产品',
          '其他商品和服务', '工艺品、收藏品']
x = np.array([0.959, 0.951, 0.935, 0.924, 0.876,
              0.983, 0.999, 0.789, 0.899, 0.678,
              0.566, 0.788, 0.999, 0.678, 0.567,
              0.986, 0.955])
y = np.arange(1, 18)
# 绘制
plt.barh(y, x, tick_label=labels, height=0.5)
plt.show()

