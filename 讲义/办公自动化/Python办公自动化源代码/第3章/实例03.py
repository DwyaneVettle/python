import pandas as pd             	#调用库
df=pd.DataFrame({'品名':['怡宝','农夫山泉','屈臣氏'],'单位':['瓶','瓶','瓶'],\
                 '单价':[1.6,1.6,2.5]})
df=df.set_index('品名')           	#将“品名”设置为索引

df.to_excel('d:/abc/313.xlsx')   		#保存位置
