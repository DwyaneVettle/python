import xlwt
workbook=xlwt.Workbook()                       #创建工作簿
worksheet=workbook.add_sheet('第5章')       #创建工作表
pattern=xlwt.Pattern()                          #创建背景属性
pattern.pattern=xlwt.Pattern.SOLID_PATTERN  #设置模式
pattern.pattern_fore_colour=5                 #设置颜色
style=xlwt.XFStyle()                            #初始化样式
style.pattern=pattern                      #将设置好的属性对象赋值给style的对应的属性
worksheet.write(1,1,'第1节',style)           #输入数据并使用style对象

workbook.save(r'd:\abc\529.xls')
