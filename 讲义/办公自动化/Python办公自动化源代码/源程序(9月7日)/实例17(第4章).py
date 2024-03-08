import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel('d:\\abc\\例题锦集.xlsx',sheet_name="班级成绩")
df=df.set_index('科目')         #设置行索引

def plot_ldb(data,feature):     #自定义函数
    plt.rcParams['font.sans-serif']=['SimHei']     #设置默认字体
    plt.rcParams['axes.unicode_minus']=False    #解决坐标轴值为负数时无法正常显示负号的问题
    cols=['语文','数学','外语','物理','化学']        #指定各个班级要显示的各科的名称
    colors=['green','blue','red']                  #为每个班级设置图表中的显示颜色
    angles=np.linspace(0.1*np.pi,2.1*np.pi,len(cols),endpoint=False)  #根据要显示的科目个数对圆形进行等分
    angles=np.concatenate((angles,[angles[0]]))  #连接刻度线数据
    fig=plt.figure(figsize=(8,8))                   #设置显示图表的窗口大小
    ax=fig.add_subplot(111,polar=True)  #设置图表在窗口中的显示位置，并设置坐标轴为极坐标体系
    for i,c in enumerate(feature):
        stats=data.loc[c]                              #获取班级对应的科目数据
        stats=np.concatenate((stats,[stats[0]]))   #连接班级的指标数据
        ax.plot(angles,stats,'-',linewidth=6,c=colors[i],label='%s'%(c))  #制作雷达图
        ax.fill(angles,stats,color=colors[i],alpha=0.25)  #为雷达图填充颜色
    ax.legend()                                         #为雷达图添加图例
    ax.set_yticklabels([])                           #隐藏坐标轴数据
    plt.show()                                          #显示制作的雷达图
    return fig
fig=plot_ldb(df,['甲班','乙班','丙班'])   #调用自定义函数制作雷达图




























