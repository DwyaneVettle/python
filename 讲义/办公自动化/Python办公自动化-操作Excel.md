# Python办公自动化-操作Excel

本课件参考《Python办公自动化-玩转Excel》,ISBN:9787522602714

素材下载：链接：https://pan.baidu.com/s/1Un9NPhkVwRu6RXoerU19ig?pwd=7777 
					提取码：7777

## 一、xlrd库、xlwt库和xlwings库

### 1.创建及读取Excel文件

#### 1.1.创建Excel文件

**实例01：**在D盘abc文件夹下创建一个工作簿，要求期中包含名为“职工工资”的工作表，在第一个单元格中输入“职工号”，并将工作簿以“211.xls”为名进行保存。

```python
import xlwt

newwb = xlwt.Workbook()  # 创建工作簿
worksheet = newwb.add_sheet("职工工资")  # 创建工作表
worksheet.write(0, 0, "职工号")  # 填写内容
newwb.save(r"d:\abc\211.xls")  # 保存工作簿
```

![image-20240307094149177](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403071357848.png)

​	说明，在工作表中，第一个单元格的位置为`0,0`，在进行保存时，代码中的小写字母`r`的含义为转义：首先需要在D盘建立一个名字为abc的文件夹，用来存放所创建的文件并完成响应的第三方库的安装；`xlrd`是Python语言中用于读取Excel表格内容的外部库，可以实现指定工作表、指定单元格的读取；`xlrd`支持`.xls`文件的读取，对`.xlsx`文件无效。

#### 1.2.读取Excel文件

**实例02：**打开工作簿“饮料销售情况.xls”并输出期中内容：

```python
import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")  # 获取工作簿
she = excelbook.sheet_by_index(0)  # 获取工作表
for i in range(she.nrows):
    print(she.row(i))  # 输出工作表内容
```

![image-20240307101344801](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403071357849.png)



#### 1.3.读取Excel工作表（以工作表名称打开）

**实例03：**以工作表名称打开工作表：

```python
import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")  # 获取工作簿
she = excelbook.sheet_by_name("sheet1")  # 以名字获取工作表
for i in range(she.nrows):
    print(she.row(i))  # 输出工作表内容
```

​	说明：一个Excel文件就是一个Excel工作簿，Excel工作簿由一个或多个工作表组成；打开Excel文件之后还需要打开具体的工作表；用Python读取Excel工作表的方法有两种，分别以工作表名称打开和以工作表序号打开。

#### 1.4.读取Excel工作表（以工作表序号打开）

**实例04：**以工作表序号的方式打开工作表：

```python
import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")  # 获取工作簿
she = excelbook.sheets()[0]
for i in range(she.nrows):
    print(she.row(i))
```

​	`sheets()`函数代表所有的工作表，0表示其为第一个。

### 2.写入数据及计算数据

#### 2.1.写入数据

**实例05：**建立工作簿，并在其中建立工作表“销售情况”，在该工作表的第1行第1列输入内容“品名”、第1行第2列输入“编号”，并以“221.xls”为名保存工作簿：

```python
import xlwt

wb = xlwt.Workbook()  # 创建新的工作簿
she = wb.add_sheet("销售情况")  # 创建新的工作表
she.write(0, 0, "品名")  # 写入数据
she.write(0, 1, "编号")  # 写入数据
wb.save(r"d:\abc\221.xls")  # 保存工作簿
```

​	说明：`xlwt`库用于将内容写入Excel文件，可以实现指定表单、指定单元格写入。

#### 2.2.获取工作表总行数（nrows)

**实例06：**打开工作簿“饮料销售情况.xls”，输出其中工作表中的数据总行数：

```python
import xlrd

excelbook = xlrd.open_workbook(r'd:\abc\饮料销售情况.xls')  # 获取工作簿
she = excelbook.sheets()[0]  # 获取工作表
print(she.nrows)  # 输出工作表中的数据总行数
```

​	说明：对于工作表中包含数据的行数，在工作表中数据量小的情况下可以直接看出；在工作表中数据量大的情况下，可以通过程序进行计算。

#### 2.3.获取工作表总列数（ncols)

**实例07：**打开工作簿“饮料销售情况.xls”，输出其中工作表中的数据：

```python
import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")  # 获取工作簿
she = excelbook.sheets()[0]  # 获取工作表
print(she.ncols)  # 获取总列数
```

#### 2.4.row（索引）获取对应的行

**实例08：**打开工作簿“饮料销售情况.xls”，并输出其中工作表中第3行（农夫山泉）的数据：

```python
import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")  # 获取工作簿
she = excelbook.sheets()[0]  # 获取工作表
print(she.row(2))  # 输出工作表中第3行的数据
```

#### 2.5.col（索引）获取对应的列

**实例09：**打开工作簿“饮料销售情况.xls”，并输出其中工作表中第4列（总量）的数据：

```python
import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
she = excelbook.sheets()[0]
print(she.col(3))  # 获取工作表中第4列数据
```

#### 2.6.使用字典向工作表中写入数据

**实例10：**将下图所示数据写入工作表“销售情况”中并以“226.xls”为工作簿名进行保存：

![image-20240307113145766](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403071357850.png)

```python
import xlrd
import xlwt

wb = xlwt.Workbook()  # 创建新的工作簿
she = wb.add_sheet("销售情况")  # 创建新的工作表

xsqk = {"品名": ["单位", "单价", "容量", "总价"],
        "怡宝": ["瓶", 1.6, "350ml", 50],
        "农夫山泉": ["瓶", 1.6, "380ml", 50],
        "屈臣氏": ["瓶", 2.5, "400ml", 50],
        "加多宝": ["瓶", 5.5, "500ml", 30],
        "可口可乐": ["瓶", 2.8, "330ml", 40],
        "椰树椰汁": ["听", 4.6, "245ml", 60],
        "美汁源": ["瓶", 4, "330ml", 60],
        "雪碧": ["听", 2.9, "330ml", 60],
        "红牛饮料": ["听", 6.9, "250ml", 30]}
i = 0
for key,value in xsqk.items():
    she.write(i, 0, key)  # 将字典中的键放在第0列
    for j in range(len(value)):
        she.write(i, j+1, value[j])  # 写入数据
    i += 1
wb.save(r"d:\abc\226,xls")  # 保存工作簿
```

​	说明：将大批量数据写入Excel文件需要借助字典工具。字典也是Python语言的重要组成部分，它由键值对组成，键值之间通过英文冒号连接，多个键值对之间用逗号连接。

#### 2.7.利用公式计算数据并进行填充

**实例11：**将实例10工作表中的“总价”写入“227.xls”文件中并进行保存：

```python
import xlrd
import xlwt

wb = xlwt.Workbook()  # 创建新的工作簿
she = wb.add_sheet("销售情况")  # 创建新的工作表

xsqk = {"品名": ["单位", "单价", "容量", "数量", "总价"],
        "怡宝": ["瓶", 1.6, "350ml", 50],
        "农夫山泉": ["瓶", 1.6, "380ml", 50],
        "屈臣氏": ["瓶", 2.5, "400ml", 50],
        "加多宝": ["瓶", 5.5, "500ml", 30],
        "可口可乐": ["瓶", 2.8, "330ml", 40],
        "椰树椰汁": ["听", 4.6, "245ml", 60],
        "美汁源": ["瓶", 4, "330ml", 60],
        "雪碧": ["听", 2.9, "330ml", 60],
        "红牛饮料": ["听", 6.9, "250ml", 30]}

i = 0
for key, value in xsqk.items():
    she.write(i, 0, key)  # 将字典中的键放在第0列
    for j in range(len(value)):
        she.write(i, j + 1, value[j])  # 写入数据
    i += 1

m = 0  # 代表行
for key, value in xsqk.items():
    if m > 0:
        she.write(m, len(value) + 1, value[1] * value[3])
    m += 1

wb.save(r"d:\abc\227.xls")  # 保存工作簿
```

​	**说明：**除了原始以外，工作表中的其他数据可以通过计算获得。本例在实例10的基础上计算出总价，其中用到的`len()`方法用来计算列的长度；`value[1]`代表单价；`value[3]`代表数量；若需要增加新的数据，可以通过在字典尾部写入实现。



#### 2.8.修改源工作表中的数据的方式（修改内容）

​	**实例12：**打开工作簿“饮料销售情况.xls”，将其sheet1工作表中第3行第1列的数据“农夫山泉”修改为“百事可乐”，并将工作簿以“228.xls”为名进行保存：

```python
import xlwings as xw

wb = xw.Book(r"d:\abc\饮料销售情况.xls")
sht = wb.sheets["sheet1"]
sht.range("A3").value = "百事可乐"  # 修改对应表格数据
wb.save(r"d:\abc\228.xls")
```

![image-20240307115229366](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403071357851.png)

​	说明：`xlwings`第三方库可以读写Excel文件，并且可以识别`.xlsx`或`.xls`文件类型（与xlrd和xlwt的区别），同时可以进行单元格格式的设置和修改。如果工作表中的数据量巨大，应该以程序的方式进行修改。

#### 2.9.修改源工作表中数据的方式（修改标题）

**实例13：**打开工作簿“饮料销售情况.xls”，将工作表sheet1中第1行第1列数据“品名”修改为“品名名称”，并将工作簿以“229.xls”为名进行保存：

```python
import xlwings as xw

wb = xw.Book(r"d:\abc\饮料销售情况.xls")
sht = wb.sheets['sheet1']
sht.range("A1").value = sht.range("A1").value + "名称"  # 修改对应表格数据
wb.save(r"d:\abc\229.xls")  # 保存工作簿
```

![image-20240307120129867](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403071357852.png)

#### 2.10.在源工作簿中增加新的工作表

**实例14：**打开工作簿“饮料销售情况.xls”，增加名称为“销售情况”的新工作表，并将工作簿以“2210.xls”为名进行保存。