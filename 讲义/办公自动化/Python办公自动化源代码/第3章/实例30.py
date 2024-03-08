import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')

page1.drop(index=[2,3,4,5],inplace=True)    #删除

page1.to_excel('d:/abc/346.xlsx')
