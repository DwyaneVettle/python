import xlwings as xw
import datetime as dt
app=xw.App(visible=True,add_book=False)
wobo=app.books.add()               	#创建新的工作簿

day=dt.datetime.now().day             	#创建时间的日期
month=dt.datetime.now().month        	#创建时间的月份
ts=str(month)+"月"+str(day)+"日"

she=wobo.sheets.add(ts)              	#创建新的工作表 

##############

def Style():                         	#设定工作表的格式
    fw1=she.range("A1:D1")         	#设定范围
    fw1.api.Merge()                 	#合并第一行单元格 
    fw1.value="超市营销记录"
    fw1.api.Font.Size=25
    fw1.api.HorizontalAlignment=-4108 	#设置居中
    fw1.row_height=38.25

    fw2=she.range("A2:D2")
    fw2.value=["品名","单价","数量","总价"]
    fw2.api.HorizontalAlignment=-4108
    fw2.api.Font.Bold=True

    fw3=she.range("A2:D100")       	#设置边界线
    fw3.api.Borders(11).LineStyle=1   	#设置内部边框(垂直)
    fw3.api.Borders(11).Weight=2
    fw3.api.Borders(12).LineStyle=1   	#设置内部边框(水平)
    fw3.api.Borders(12).Weight=2

Style()

########
def inputdata(m):                     	#接收键盘数据写入工作表
    for i in range(3,100):
        str1="A"+str(i)
        str2="D"+str(i)
        if she.range(str1).value==None:
            she.range(str1).value=strlist  	#写入数据
            she.range(str2).value=float(strlist[1])*int(strlist[2])
            she.range(str1+":"+str2).api.HorizontalAlignment=-4108
            break
        else:
            continue
###########
flag=True
print(""*20,'===================')
print(""*20,"请输入产品信息")           	#提示信息
print(""*20,"例如：怡宝 1.6 100")
print(""*20,"结束时输入ok并按Enter键")
while flag:                           	#死循环
    str3=input(""*21+"请输入数据：")
    if str3=="ok":
        wobo.save(r"d:\abc\244.xls")    	#保存文件
        wobo.close()                	#关闭工作簿
        app.quit()                  	#退出工作簿
        flag=False
    else:
        strlist=str3.split("")   	#以空格为间隔，转换为列表
        inputdata(strlist)     	#调用自定义函数，将列表数据输入
        print(""*20,'===================')
