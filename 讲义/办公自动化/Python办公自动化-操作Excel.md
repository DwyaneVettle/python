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

```python
import xlwings as xw
app = xw.App(visible=True, add_book=False)  # 启动程序
wobo = app.books.open(r"d:\abc\饮料销售情况.xls")
sht = wobo.sheets['sheet1']
wobo.sheets.add('销售情况')  # 增加工作表

wobo.save(r"d:\abc\2210.xls")  # 保存工作簿
wobo.close()    # 关闭工作簿
app.quit()      # 退出excel程序
```



#### 2.11.复制工作表

**实例15：**通过复制D盘abc文件夹下的“饮料销售情况.xls”工作簿，生成一个名为“2211.xls”的工作波并将其保存：

```python
import xlrd
import xlwt
from xlutils.copy import copy

wosh = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
new = copy(wosh)              	#复制工作簿

new.save(r"d:\abc\2211.xls")    	#保存工作簿
```

#### 2.12.激活活动表格

**实例16：**将工作簿“饮料销售情况.xls”中的工作表Sheet2激活为活动表格，并将工作簿以“2212.xls”为名进行保存。

```python
import xlwings as xw
app = xw.App(visible=True,add_book=False)   #启动Excel程序
wobo = app.books.open(r"d:\abc\饮料销售情况.xls")
she = wobo.sheets["Sheet2"]
she.activate()                	#设置活动表格

wobo.save(r"d:\abc\2212.xls")  	#保存工作簿
wobo.close()               	#关闭工作簿
app.quit()                  	#退出Excel程序
```

说明：在操作Excel工作簿时，显示在当前屏幕上并可以操作的工作表成为活动表格。

#### 2.13.获取工作表中有效范围的有效数据

**实例17：**打开工作簿“饮料销售情况.xls”及其中的工作表sheet1，将其中内容全部显示。

```python
import xlwings as xw
app = xw.App(visible=True, add_book=False)       	#启动Excel程序
wobo = app.books.open(r"d:\abc\饮料销售情况.xls") 	#获取工作簿
she = wobo.sheets[0]                           	#获取工作表
fw = she.range("A1:F10")                       	#设置范围
for i in fw.current_region.value:
    print(i)
wobo.close()                                 	#关闭工作簿
app.quit()                                    	#退出Excel程序
```

![image-20240509161407254](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202405091614575.png)

说明：工作表中需要进行操作的一定范围内的数据称为有效数据。

- 有效数据：有内容的才是有效数据
- 有效范围：一个工作表中所有有效数据所圈定的一个长方形区域（范围）。



### 3.格式控制

#### 3.1.设置工作表的行高和列宽

**实例18：**打开工作簿“饮料销售情况.xls”及其中的工作表“职工工资”，设置第1列的列宽为20，设置第一行的行高为40，并将工作簿以“231.xls”为名进行保存：

```python
import xlrd
import xlwt
from xlutils.copy import copy
exbo = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
nexbo = copy(exbo)                  	#复制工作簿
nsht = nexbo.get_sheet(0)              	#打开新的工作表
nsht.col(0).width = 256*20             	#设置列宽，256为一个衡量单位
nsht.row(0).height_mismatch=True     	#行高初始化
nsht.row(0).height = 20*40             	#设置行高，20为一个衡量单位

nexbo.save(r"d:\abc\231.xls")          	#保存工作簿
```

说明：修改Excel文件时，需要通过xlutils将原来的工作簿复制生成另一个工作簿（可以保留工作簿原有的格式）

- col().width函数用来设置列宽，1个衡量单位为256
- row().height用来设置行高，1个衡量单位为20

#### 3.2.设置工作表文字格式

**实例19：**打开工作簿“饮料销售情况.xls”及其中的工作表sheet1，在单元格B13中以黑体、不加粗、字号20写入“文字格式”字样，并将工作簿以“232.xls”为名进行保存：

```python
import xlrd
import xlwt
from xlutils.copy import copy

exbo = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
nexbo = copy(exbo)  # 复制工作簿
nsht = nexbo.get_sheet(0)  # 打开新的工作表

style = xlwt.XFStyle()  # 初始化样式（第1步）
font = xlwt.Font()  # 创建属性对象（第2步）

font.name = "黑体"  # 设置字体名称（第3步）
font.blod = False  # 是否加粗（不加粗）
font.height = 400  # 设置字号，值为字号*20

style.font = font  # 将设置好的属性赋值给style对应的属性（第4步）
nsht.write(12, 1, "文字格式", style)  # 写入数据时使用style对象（第5步）

nexbo.save(r"d:\abc\232.xls")  # 保存工作簿
```

![image-20240509162537169](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202405091625178.png)

说明：工作表中文字格式的设置是使工作表更加美观的方式之一。文字格式的设置主要包括以下5个步骤：

1. 初始化样式
2. 创建属性对象
3. 设置字体名称，设置文字是否加粗，设置字号
4. 将设置好的属性赋值给style对象的属性
5. 写入数据时使用style对象



#### 3.3.设置字体属性(Font)

**实例20：**打开工作表“饮料销售情况.xls”及其中的工作表sheet1，在单元格B13中以微软雅黑为字体、加粗、字号30、斜体、颜色为12写入“文字格式”字样，并以“233.xls”为名进行保存：

```python
import xlrd
import xlwt
from xlutils.copy import copy

exbo = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")

nexbo = copy(exbo)  # 复制工作簿
nsht = nexbo.get_sheet(0)  # 打开新的工作表

style = xlwt.XFStyle()  # 初始化样式（第1步）

font = xlwt.Font()  # 创建字体属性对象（第2步）

font.name = "Microsoft JhengHei Light"  # 字体名称（第3步）
font.blod = True  # 是否加粗（加粗）
font.height = 30 * 20  # 字号*30
font.italic = True  # 斜体
font.colour_index = 12  # 颜色

style.font = font  # 将设置好的属性对象赋值给style对应的属性（第4步）
nsht.write(12, 1, "文字格式", style)  # 写入数据时使用style对象（第5步）

nexbo.save(r"d:\abc\233.xls")  # 保存工作簿
```

说明：字体的属性包括字体、字号、斜体、颜色等。字体属性的各种具体数据及说明如下表：

| 字体属性                                  | 说明                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| font.name=""                              | 字体名称，可设置任意字体                                     |
| font.blod=False                           | 是否加粗，默认为False不加粗                                  |
| font.underline=True                       | 是否提娜佳下划线，True为添加，False不添加                    |
| font.italic=True                          | 是否为斜体                                                   |
| font.escapement=xlwt.Font.ESCAPEMENT_NONE | 字体效果。ESCAPEMENT_SUPERSCRIPT字体悬空位于上方；ESCAPEMENT_SUBSCRIPT字体悬空位于下方；ESCAPEMENT_NONE字体不悬空 |
| font.colour_index=33                      | 参考颜色值                                                   |

