import xlwings as xw

app=xw.App(visible=True, add_book=False)
wb=app.books.add()
sht=wb.sheets.active
sht.range(2,4).value="中国"

fw=sht.range('B2:E3')

"""设置单元格大小"""
sht.autofit()                  	#自动调整单元格大小
sht.range(1,4).column_width=20 	#设置第4列列宽，(1,4)表示第1行第4列的单元格
sht.range(2,4).row_height=60   	#设置第2行行高

"""设置单元格字体格式"""
fw.color=255,200,255        	#设置单元格的填充颜色
fw.api.Font.ColorIndex=3     	#设置字体的颜色
fw.api.Font.Size=24          	#设置字体的大小
fw.api.Font.Bold=True         	#设置字体为粗体
fw.api.HorizontalAlignment=-4108	#-4108表示水平居中
fw.api.VerticalAlignment=-4108   	#-4108表示垂直居中
fw.api.NumberFormat="0.00"      	#设置单元格内数字的格式

"""设置边框"""
fw=sht.range('B5')
fw.api.Borders(9).LineStyle=1   	#Borders(9)表示底部边框，LineStyle=1表示实线
fw.api.Borders(9).Weight=3    	#设置边框粗细

fw=sht.range('D5')
fw.api.Borders(7).LineStyle=2  	#Borders(7)表示左边框，LineStyle=2表示虚线
fw.api.Borders(7).Weight=3

fw=sht.range('C5')
fw.api.Borders(8).LineStyle=5  	#Borders(8)表示顶部框，LineStyle=5表示双点划线
fw.api.Borders(8).Weight=3

fw=sht.range('E5')
fw.api.Borders(10).LineStyle=4 	#Borders(10)表示右边框，LineStyle=4表示点划线
fw.api.Borders(10).Weight=3

fw=sht.range('B7:C10')
fw.api.Borders(5).LineStyle = 1 	#Borders(5)表示从单元格左上角到右下角
fw.api.Borders(5).Weight = 3

fw=sht.range('D7:E10')
fw.api.Borders(6).LineStyle=1 	#Borders(6)表示从单元格左下角到右上角
fw.api.Borders(6).Weight=3

fw=sht.range('B12:D15')
fw.api.Borders(11).LineStyle=1	#Borders(11)表示内部垂直中线
fw.api.Borders(11).Weight=3

fw=sht.range('E12:G15')
fw.api.Borders(12).LineStyle=1	#Borders(12)表示内部水平中线
fw.api.Borders(12).Weight=3

"""合并、拆分单元格"""
sht.range('G5:H6').api.Merge()    	#合并单元格
sht.range('G7:H8').api.Merge()   
sht.range('G7:H8').api.UnMerge()  	#拆分单元格

"""插入、读取公式"""
sht.range('F1').formula='=sum(D1+E1)'	#插入公式
print(sht.range('F1').formula)			#读取公式

wb.save(r'd:\abc\5419.xlsx')
wb.close()
app.quit()
