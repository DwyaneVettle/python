import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')

page1.drop(index=page1[2:6].index,inplace=True)    #按切片进行删除

page1.to_excel('d:/abc/348.xlsx')  
