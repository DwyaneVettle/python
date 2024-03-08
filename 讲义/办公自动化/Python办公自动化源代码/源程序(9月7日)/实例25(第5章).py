import pandas as pd
import numpy as np
df=pd.DataFrame({'A':1.,'B':pd.Timestamp('20200101'),
                  'C':pd.Series(1,index=range(4),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(['test1','test2','test3','test4']),
                  'F':'foo'})
print(df.head())            #显示前5行信息
print(df.tail())            #显示后5行信息
print("行标签：",end="")
print(df.index)             #显示行标签
print("列标签：",end="")
print(df.columns)           #显示列标签
print("各列数据类型：")
print(df.dtypes)            #显示各个列的数据类型
print(df.values)            #显示DataFrame的值
