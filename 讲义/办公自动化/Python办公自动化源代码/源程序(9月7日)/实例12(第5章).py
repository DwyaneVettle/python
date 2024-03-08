import xlwt
workbook=xlwt.Workbook()                         #创建工作簿
worksheet=workbook.add_sheet('第5章')         #创建工作表
worksheet.write_merge(0,0,0,3,'第1节')        #合并单元格
worksheet.write_merge(2,4,2,4,'第2节')        #合并单元格
workbook.save(r'd:\abc\526.xls')


