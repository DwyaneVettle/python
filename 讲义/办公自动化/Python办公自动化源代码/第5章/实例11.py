import xlwt
workbook=xlwt.Workbook()             	#创建工作簿
worksheet=workbook.add_sheet('第5章')  	#创建工作表
worksheet.write(0,0,xlwt.Formula('HYPERLINK("http://www.baidu.com";"baidu")')) #添加超链接

workbook.save(r'd:\abc\525.xls')          #保存文件
