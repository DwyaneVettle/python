import xlwt
workbook = xlwt.Workbook()                  #创建工作簿
worksheet = workbook.add_sheet('第5章')  #创建工作表
worksheet.write(0, 0,'星期一')              #填加数据

worksheet.col(0).width = 3333              #设置单元格宽度

workbook.save(r'd:\abc\522.xls')           #保存文件
