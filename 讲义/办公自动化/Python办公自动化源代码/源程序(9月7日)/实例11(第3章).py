import pandas as pd
books=pd.read_excel("d:/abc/例题锦集.xlsx",sheet_name='期末成绩')

temp=books[['语文','数学','英语']]              #提取数据
row_sum=temp.sum(axis=1)                        #计算行的总分
books['总分']=row_sum                            #写入总分到列

books.to_excel('d:/abc/3111.xlsx')             #保存位置



