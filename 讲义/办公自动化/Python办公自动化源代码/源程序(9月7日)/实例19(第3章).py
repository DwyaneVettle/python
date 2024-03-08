import pandas as pd
                          
df=pd.read_excel('d:/abc/例题锦集.xlsx','饮料全表') 

kk=df.groupby(['单位','容量']).sum()     #按“单位”分组

kk.to_excel('d:/abc/327.xlsx')  






