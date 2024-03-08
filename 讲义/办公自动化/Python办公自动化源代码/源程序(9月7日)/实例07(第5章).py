import xlwt
workbook = xlwt.Workbook()                   #创建工作簿
worksheet = workbook.add_sheet('第5章')   #创建工作表
worksheet.write(0, 0,'星期一')               #填加数据
workbook.save(r'd:\abc\521.xls')           #保存文件

