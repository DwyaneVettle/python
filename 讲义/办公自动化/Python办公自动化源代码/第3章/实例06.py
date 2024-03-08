from xlwt import *
file=Workbook()               	#创建工作簿
table=file.add_sheet('data')        	#创建工作表

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

num=[]                    
for a in xsqk:                	#取出key存入列表num中 
  num.append(a)

ldata=[]
for x in num:                	#将字典中的key和value分批保存到列表中
  t=[(x)]
  for a in xsqk[x]:
      t.append(a)
  ldata.append(t)            	#将key和value存入列表ldata中

for i,p in enumerate(ldata):     	#写入文件
  for j,q in enumerate(p):
      table.write(i,j,q)

file.save('d:\\abc\\316.xlsx')    	#保存文件
