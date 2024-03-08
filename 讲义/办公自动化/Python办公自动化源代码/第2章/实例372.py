import xlwings as xw
import datetime as dt
app=xw.App(visible=True,add_book=False)
wobo=app.books.add()                	#创建新的工作簿

day=dt.datetime.now().day             	#创建时间的日期
month=dt.datetime.now().month        	#创建时间的月份
timestr=str(month)+"月"+str(day)+"日"

wobo.sheets.add(timestr)             	#创建新的工作表 
wobo.save(r"d:\abc\242.xls")          	#保存文件
wobo.close()                       	#关闭工作簿
app.quit()                          	#退出工作簿
