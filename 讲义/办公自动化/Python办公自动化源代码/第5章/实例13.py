import xlwt
workbook=xlwt.Workbook()              	#创建工作簿
worksheet=workbook.add_sheet('第5章')  	#创建工作表
alignment=xlwt.Alignment()                   	#创建对齐属性
alignment.horz=xlwt.Alignment.HORZ_CENTER 	#设置水平居中
alignment.vert=xlwt.Alignment.VERT_CENTER  	#设置垂直居中
style=xlwt.XFStyle()                        	#初始化样式
style.alignment=alignment        	#将设置好的属性对象赋值给style对应的属性
worksheet.write(0,0,'第1节',style)  	#输入数据并使用style对象

workbook.save(r'd:\abc\527.xls')
