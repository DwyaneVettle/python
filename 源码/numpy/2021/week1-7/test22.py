# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 准备数据
# x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# y1, y2 = np.sin(x), np.cos(x)
#
# # 绘制图形
# lines = plt.plot(x, y1, x, y2)
# # 绘制图例
# plt.legend(lines, ['上海', '北京'], shadow=True, fancybox=True)
# # 绘制辅助图形-x/y轴的标签 xlabel(xlabel, fontdict, labelpad) ylabel()
# plt.xlabel("年份")
# plt.ylabel("雨量")
#
# # 绘制刻度范围和刻度标签 xlim() xticks()
# plt.xlim(x.min() + 1.7, x.max() + 1.7)
# plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
#            [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi / 2$', r'$\pi$'])
#
# # 添加网格-grid(which='major', axis='both', lw)
# plt.grid(which='major', axis='both')
#
# # 添加参考线 axhline()水平参考线  axvline()垂直参考线
# plt.axhline(y=2, linestyle='dashed')
# plt.axvline(x=1, linestyle='-')
#
# # 添加参考区域 axhspan()水平参考区域 axvspan()垂直参考区域
# plt.axhspan(ymin=0.5, ymax=1.0, alpha=0.3)
# plt.axvspan(xmin=0.5, xmax=1.0, alpha=0.3)
#
# # 指向型注释文本的添加：annotate()
# """
#     参数说明：
#         s：注释文本的内容
#         xy:被注释的点的坐标位置，接收元组
#         xytext:表示注释文本的坐标位置，接收元组
#         arrowprops：指向箭头的属性字典
#         bbox：表示注释文本的边框
# """
# plt.annotate('最小值', (-np.pi / 2, -1.0), xytext=(-(np.pi / 2), -0.5),
#              arrowprops=dict(arrowstyle='->'))
#
# """
#     添加无指向型的注释文本：text()
#         参数：
#             x,y：表示注释文本的位置
#             s：注释的文本，
#             bbox：注释文本的盒子
# """
# plt.text(3.10, 0.10, "y=sin(x)", bbox=dict(alpha=0.3))
#
# """
#     添加表格辅助阅读
#         tabel():
#         参数：
#             cellText:表示表格单元格中的数据，可以是一个二维列表
#             cellColour:表示单元格的背景颜色
#             colWidth：表示每列的宽度
#             rowLoc:行标题对其的方式
#             rowLables:表示行标题的文本
#             colLabels：表示列标题的文本
#             loc:表示绘图区域的位置
# """
# plt.table(cellText=[[6, 6, 6], [8, 8, 8]], rowLabels=['第1行', '第2行'],
#           colLabels=['第1列', '第2列', '第3列'], loc='lower right',
#           colWidths=[0.1] * 3)
# # 展示图形
# plt.show()

import matplotlib
a = matplotlib.rc_params()
print(a)
