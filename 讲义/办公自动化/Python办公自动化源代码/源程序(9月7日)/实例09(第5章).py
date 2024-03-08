import xlwt
import datetime
workbook=xlwt.Workbook()                   #创建工作簿
worksheet=workbook.add_sheet('第5章')   #创建工作表
style=xlwt.XFStyle()                       #初始化样式
style.num_format_str = 'M/D/YY'          #设置时间格式

worksheet.write(0,0,datetime.datetime.now(),style) #填加数据

workbook.save(r'd:\abc\523.xls')          #保存文件

