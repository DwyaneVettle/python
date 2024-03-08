import pandas as pd                #调用库
df=pd.DataFrame({'品名':['怡宝','农夫山泉','屈臣氏'],'单位':['瓶','瓶','瓶'],\
                 '单价':[1.6,1.6,2.5]})
df.to_excel('d:/abc/312.xlsx')   #保存位置
