import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
  
miss=page1.loc[page1['姓名'].str[0:1]=='李']   #筛选数据

page1.drop(index=miss.index,inplace=True)     #有条件删除
students=page1.reset_index(drop=True)         #重新设置索引

students.to_excel('d:/abc/349.xlsx')















