import xlwt                              	#调用第三方库
newwb=xlwt.Workbook()                   	#创建工作簿
worksheet=newwb.add_sheet("职工工资")    	#创建工作表
worksheet.write(0,0,"职工号")             	#填写内容
newwb.save(r"d:\abc\211.xls")           		#保存工作簿
