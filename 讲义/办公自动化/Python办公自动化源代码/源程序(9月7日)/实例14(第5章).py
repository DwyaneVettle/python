import xlwt
workbook=xlwt.Workbook()                    #创建工作簿
worksheet=workbook.add_sheet('第5章')    #创建工作表
borders=xlwt.Borders()                      #创建边界属性
borders.left=xlwt.Borders.DASHED           #设置虚线
borders.right=xlwt.Borders.DASHED         #设置虚线
borders.top=xlwt.Borders.DASHED           #设置虚线
borders.bottom=xlwt.Borders.DASHED        #设置虚线
style=xlwt.XFStyle()                         #初始化样式
style.borders=borders                        #添加边框
worksheet.write(1,1,'第1节',style)        #输入数据并使用style对象

workbook.save(r'd:\abc\528.xls')
