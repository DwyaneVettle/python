import pandas as pd
import numpy as np
df=pd.DataFrame({'A':1.,'B':pd.Timestamp('20200101'),
                  'C':pd.Series(3,index=range(4)),
                  'D':np.array([3]*4),
                  'E':pd.Categorical(['test1','test2','test3','test4']),
                  'F':'foo'})
print(df.head(2))         	#显示前2行信息
print(df.tail(2))          	#显示后2行信息
print("行索引：",end=" ")
print(df.index)          	#显示行索引
print("列索引：",end=" ")
print(df.columns)       	#显示列索引
print("各列数据类型：")
print(df.dtypes)         	#显示各个列的数据类型
print(df.values)         	#显示DataFrame的值
