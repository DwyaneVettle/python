import xlwings as xw
app=xw.App(visible=True,add_book=False)
wobo=app.books.open(r"d:\abc\人员名单.xlsx")
shtlist=wobo.sheets                  	#获取所有工作表
gds=wobo.sheets.add("广东省")        	#新增工作表
vlist=[]                            	#建立新列表

def readr(ex):        				#将符合条件的记录添加到新列表中
    for i in range(2,100):
        str1="E"+str(i)
        str2="A"+str(i)+":"+"E"+str(i) 	#一整行
        str3=ex.range(str1).value
        if str3=="广东省":
            strrow=ex.range(str2).value
            vlist.append(strrow)      	#追加到空列表中

for ex in shtlist:
    readr(ex)

gds.range("A1:E1").value=["姓名","级别","学历","薪资","地区"]

flag=1
for i in vlist:
    flag+=1
    str_sheet1="A"+str(flag)+":"+"E"+str(flag)
    gds.range(str_sheet1).value=i


wobo.save(r"d:\abc\245.xls")          	#保存文件
wobo.close()                       	#关闭工作簿
app.quit()                          	#退出工作簿
