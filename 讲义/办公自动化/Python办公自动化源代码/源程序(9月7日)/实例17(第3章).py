import xlrd                           
data=xlrd.open_workbook('d:/abc/饮料销售情况.xls') 
table=data.sheet_by_name('sheet1')             
name=[]                                  #设置初值(空值)
data=[]                                  #设置初值(空值)
dict_data={}                            #设置初值(空值)
nr=table.nrows                          #计算工作表总行数据
nc=table.ncols                          #计算工作表总列数据
for i in range(nr):                    #读取工作表数据到列表
    name.append(table.row_values(i)[0])
    data.append(table.row_values(i)[1:nc])
print(name)
print(data)
print('=====================')
dict_data=dict(zip(name,data))         #合并列表到字典
print(dict_data)






