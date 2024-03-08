import pandas as pd
import numpy as np
df=pd.DataFrame({'A':1.,'B':pd.Timestamp('20200101'),
                'C':pd.Series(1,index=range(4),dtype='float32'),
                'D':np.array([3]*4,dtype='int32'),
                'E':pd.Categorical(['test2','test4','test3','test1']),
                'F':'foo'})
print(df)               	#原始数据
df=df.sort_values(by='E')  	#根据E列数据进行排序
print(df)               	#排序后的数据
