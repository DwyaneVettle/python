import xlwings as xw
import datetime as dt
app=xw.App(visible=True,add_book=False)
wobo=app.books.add()                      #创建新的工作簿
  
day=dt.datetime.now().day                #创建时间日期
month=dt.datetime.now().month            #创建时间月份
ts=str(month)+"月"+str(day)+"日"

she=wobo.sheets.add(ts)                  #创建新的工作表 

#def style():                              #设定工作表的格式
fw1=she.range("A1:D1")                   #设定范围
fw1.api.Merge()                            #合并第一行单元格 
fw1.value="商品营销记录"
fw1.api.Font.Size=25
fw1.api.HorizontalAlignment=-4108      #设置居中
fw1.row_height=38.25

fw2=she.range("A2:D2")
fw2.value=["品名","单价","数量","总价"]
fw2.api.HorizontalAlignment=-4108
fw2.api.Font.Bold=True

fw3=she.range("A2:D100")                 #设置边界线
fw3.api.Borders(11).LineStyle=1        #设置内部边框(垂直)
fw3.api.Borders(11).Weight=2
fw3.api.Borders(12).LineStyle=1        #设置内部边框(水平)
fw3.api.Borders(12).Weight=2

wobo.save(r"d:\abc\243.xlsx")          #保存文件
wobo.close()                               #关闭工作簿
app.quit()                                 #退出工作簿
