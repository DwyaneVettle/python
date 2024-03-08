import xlrd
import xlwt
wb=xlwt.Workbook()                   #创建新的工作簿
she=wb.add_sheet("销售情况")         #创建新的工作表

xsqk={"品名":["单位","单价","容量","数量","总价"],
"怡宝":["瓶",1.6,"350ml",50],
"农夫山泉":["瓶",1.6,"380ml",50],
"屈臣氏":["瓶",2.5,"400ml",50],
"加多宝":["瓶",5.5,"500ml",30],
"可口可乐":["瓶",2.8,"330ml",40],
"椰树椰汁":["听",4.6,"245ml",60],
"美汁源":["瓶",4,"330ml",60],
"雪碧":["听",2.9,"330ml",60],
"红牛饮料":["听",6.9,"250ml",30]}
      
i=0
for key,value in xsqk.items():
    she.write(i,0,key)               #将字典中的健放在第0列
    for j in range(len(value)):
        she.write(i,j+1,value[j])   #写入数据
    i+=1
wb.save(r"d:\abc\226.xls")          #保存工作簿
