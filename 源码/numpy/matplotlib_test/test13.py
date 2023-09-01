import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 饼状图外侧文字说明
kinds = ['购物', '人情往来', '餐饮美食', '通信物流', '生活日用',
         '交通通行', '休闲娱乐', '其他']
# 饼状图数据
money_scale = [800/3000, 100/3000, 1000/3000, 200/3000,
               300/3000, 200/3000, 200/3000, 200/3000]
dev_position = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# 饼图绘制
plt.pie(money_scale, labels=kinds, autopct='%3.1f%%', shadow=True,
        explode=dev_position, startangle=90)
plt.show()
