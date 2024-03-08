import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')

page1.drop(index=range(2,6),inplace=True)    #删除

page1.to_excel('d:/abc/347.xlsx')  













