import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1.准备数据
kind = ['购物', '人情往来', '餐饮美食', '通信物流', '生活日用',
        '交通出行', '休闲娱乐', '其他']
money = [800/3000, 100/3000, 1000/3000, 200/3000, 300/3000,
         200/3000, 200/3000, 200/3000]
postion = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# 2.绘制饼图
plt.pie(money, labels=kind, autopct='%3.1f%%',
        shadow=True, explode=postion, startangle=90)
# 3.显示图表
plt.show()
