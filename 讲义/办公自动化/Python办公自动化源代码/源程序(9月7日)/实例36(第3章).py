import pandas as pd
import numpy as np

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
page1['名次']=np.arange(1,len(page1)+1)    #追加列数据

page1.to_excel('d:/abc/353.xlsx')
















