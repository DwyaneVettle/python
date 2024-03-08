import xlrd
import xlwt
from xlutils.copy import copy

workbook=xlrd.open_workbook(r'd:\abc\饮料销售情况.xls') 
sheet1=workbook.sheets()[0]                      #打开工作表
row1=sheet1.row_values(0)                        #取出第一行
col={str(i):row1[i] for i in range(0,len(row1))} #设置行索引
col4=sheet1.col_values(3)                        #取出第四列，
row={str(i):col4[i] for i in range(0,len(col4))} #设置列索引
print("行索引内容为：",end="")
print(list(enumerate(col)))                      #输出行索引
print("列索引内容为：",end="")
print(list(enumerate(row)))                      #输出列索引

mtitle="容量"   
mname="500ml"   
a="".join([i for i in row if row[i]==mname]) #获取"容量"所在行索引
b="".join([i for i in col if col[i]==mtitle])#获取"500ml"所在列索引
print("500ml的行索引与列索引为：",end="")
print(a,b)                                           #输出行索引和列索引
