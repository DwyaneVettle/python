import pandas as pd
import tushare as ts                                  #调用财经数据接口包
import matplotlib.pyplot as plt

frame=ts.get_k_data('300111',start='2009-01-01') #查询“向日葵”股票信息 
frame=frame.set_index('date')                       #为日期设置索引
frame.index=pd.to_datetime(frame.index)           #获取指定的日期
plt.plot(frame['close'])                             #绘制基础走势图 

plt.show()































