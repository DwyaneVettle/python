import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates=pd.date_range('20200101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
print(df)
