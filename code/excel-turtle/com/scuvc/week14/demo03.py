"""
    支付宝月度消费账单饼图
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as ml
# 对中文字体的设置
ml.rcParams['font.sans-serif'] = ['SimHei']
ml.rcParams['axes.unicode_minus'] = False
# 数据
# 外部刻度标签
kinds = ['购物', '人情往来', '餐饮美食', '通信物流', '生活日用',
         '交通出行', ' 娱乐休闲', '其他']
# 饼图中央的数据占比
money = [800/3000, 100/3000, 1000/3000, 200/3000,
               300/3000, 200/3000, 200/3000, 200/3000]
position = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# 绘制饼图
plt.pie(money, labels=kinds, autopct='%3.1f%%',
        shadow=True, startangle=90, explode=position)
# 显示饼图：
plt.show()
