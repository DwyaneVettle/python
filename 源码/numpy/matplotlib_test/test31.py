import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 汇率
eurcny_2017 = np.array([6.8007, 6.8007, 6.8015, 6.8060, 6.8060,
                        6.8060, 6.8036, 6.8025, 6.7877, 6.7835,
                        6.7758, 6.7700, 6.7463, 6.7519, 6.7511,
                        6.7511, 6.7539, 6.7265, 6.7265, 6.7265])
eurcny_2019 = np.array([6.8640, 6.8705, 6.8697, 6.8697, 6.8697,
                        6.8881, 6.8853, 6.8856, 6.8677, 6.8662,
                        6.8662, 6.8662, 6.8827, 6.8761, 6.8635,
                        6.8860, 6.8737, 6.8796, 6.8841, 6.8841])
data_x = np.array([3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13,
                   14, 17, 18, 19, 24, 25, 26, 31])
fig = plt.figure()
ax = fig.add_subplot(111)
# 第一条折线：湖绿色、实线、线宽2
ax.plot(data_x, eurcny_2017, color='#006370', lw=2,
        label='2017年7月美元/人民币汇率')
# 第二条折线：紫色、长虚线、线宽2
ax.plot(data_x, eurcny_2019, color='#8a2e76',ls='--', lw=2,
        label='2019年7月美元/人民币汇率')
ax.set_title('2017年7月与2019年7月美元/人民币汇率走势')
ax.set_xlabel('日期')
ax.set_ylabel('汇率')
ax.legend()
plt.show()
