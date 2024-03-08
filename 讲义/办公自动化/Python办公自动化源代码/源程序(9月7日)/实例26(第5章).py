import pandas as pd
import numpy as np
df=pd.DataFrame({'A':1.,'B':pd.Timestamp('20200101'),
                  'C':pd.Series(1,index=range(4),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(['test1','test2','test3','test4']),
                  'F':'foo'})
df=df.sort_index(axis=1,ascending=False)   #沿着列方向对col name进行排序

print(df)  
