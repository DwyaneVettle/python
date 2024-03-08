flag=True
print(""*20,'===================')
print(""*20,"请输入产品信息")            	#提示信息
print(""*20,"例如：怡宝 1.6 100")
print(""*20,"结束时输入ok并按Enter键")
while flag:                              	#死循环
    str=input(""*21+"请输入数据：")
    if str=="ok":
        wobo.save(r"d:\abc\241.xls")       	#保存文件
        wobo.close()                    	#关闭工作簿
        app.quit()                       	#退出工作簿
        flag=False
    else:
        strlist=str.split("")    				#以空格为间隔，转换为列表
        print(strlist)                  		#输出列表
        print(""*20,'===================')
