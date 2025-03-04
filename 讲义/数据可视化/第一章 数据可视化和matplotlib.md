# Python数据可视化

# 第一章 数据可视化和matplotlib

## 1.数据可视化概述

### 1.1.什么是数据可视化

​	数据可视化旨在借助**图形化**的手段，将一组数据**以图形的形式表示**，并利用**数据分析和开发工具**发现其中未知信息的处理过程。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301015885.png" alt="image-20230830101526611" style="zoom:50%;" />

​	                                                                            数据可视化发展历史

​	可视化其实是一个抽象的过程，它可以简单地理解为将一个不易描述的事物形成一个可感知画面的过程，也就是从数据空间到图形空间的映射。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301017785.png" alt="image-20230830101704710" style="zoom:50%;" />

​	无论原始数据被映射为哪种图形数据，最终要达到的目的只有一个，便是准确地、高效地、全面地传递信息，进而建立起数据间的关系，使人们发现数据间的规律和特征，并挖掘出有价值的信息，提高数据沟通的效率。

​	假设某公司员工在整理全年KPI报告时准备了表格和图形这两种形式的数据。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301023445.png" alt="image-20230830102340374" style="zoom:50%;" />

​	                                                                            表格

​	表格可以帮助公司领导快速地知道各季度的具体数值，但无法快速地了解各季度之间的比较情况。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301024674.png" alt="image-20230830102411608" style="zoom:50%;" />

​	                                                                             图形

​	图形可以帮助公司高层准确地了解各季度之间的比较情况，方便对公司下一年的工作做出有效地决策。

​	**总结：**综上所述，数据可视化是数据分析工作中重要的一环，对数据潜在价值的挖掘有着深远的影响。随着数据可视化**平台的拓展、表现形式的变化**，以及**实时动态效果、用户交互使用**等功能的增加，数据可视化的内涵正在不断扩大，相信数据可视化的应用领域会越来越广泛。



### 1.2.常见的数据可视化方式

- **折线图：**折线图是将数据标注成<font color="red">**点**</font>，并通过<font color="red">**直线**</font>将这些点按某种顺序连接而成的图表，它以折线的倾斜程度来形象地反映事物沿某一维度的变化趋势，能够清晰地展示数据增减的<font color="red">**趋势、速率、规律及峰值**</font>等特征。 

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301029672.png" alt="image-20230830102905542" style="zoom:50%;" />

​                                               成都市4月23-29日的最高气温和最低气温的变化情况

- **柱状图：**柱形图是由一系列宽度相等的<font color="red">**纵向矩形条**</font>组成的图表，它使用矩形条的<font color="red">**高度表示数值**</font>，以此反映不同分类数据之间的差异。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301032463.png" alt="image-20230830103251381" style="zoom:50%;" />

​                                                                    2015-1018年阿里巴巴公司营收情况

- **条形图：**条形图是横置的柱形图，由一系列高度相等、长短不一的<font color="red">**纵向矩形条**</font>横向矩形条组成。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301041469.png" alt="image-20230830104114355" style="zoom:50%;" />

​                                                        2022年上半年快手用户对各类商品广告的关注率

- **堆积图：**堆积图可分为**堆积面积图、堆积柱形图和堆积条形图**。其中堆积面积图是由若干条折线与折线或水平坐标轴之间的填充区域组成的图表，用于强调每个部分变化的趋势；堆积柱形图和堆积条形图是由若干个以颜色或线条填充、高度不一的纵向矩形条或横向矩形条堆叠而成的图表，主要用于反映各构成部分在总体中的比重。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301043962.png" alt="image-20230830104328749" style="zoom:50%;" />

- **直方图：**直方图又称质量分布图，是由一系列高低不等的<font color="red">**纵向矩形条或线段**</font>组成的图表，用于反映数据的分布和波动情况。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301044575.png" style="zoom:50%;" />

​                                                             某厂商对 100 个抽样产品的质量级别评定情况

**柱形图与直方图的区别**包括以下两点：

1. 柱形图用于展示离散型数据的分布，而直方图用于展示连续型数据的分布
2. 柱形图的各矩形条之间具有固定的间隙，而直方图的各矩形条之间没有任何间隙。

- **箱形图：**箱形图又称盒须图、箱线图，是一种利用数据中的<font color="red">**5个统计量**</font>——最小值、下四分位数、中位数、上四分位数和最大值­——**描述数据**的图表，主要用于反映一组或多组数据的对称性、分布程度等信息，因形状如箱子而得名 。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301047422.png" alt="image-20230830104757343" style="zoom:50%;" />

​                                                                      不同厂家所产地毯的耐用性

​	箱形图中每个图形的结构是相同的，包括**一个矩形箱体、上下两条竖线、上下两条横线**。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301049334.png" alt="image-20230830104941226" style="zoom:50%;" />

- **饼图：**饼图是由若干个面积大小不一、颜色不同的<font color="red">**扇形**</font>组成的圆形图表，它使用圆表示数据的总量，组成圆的每个扇形表示数据中各项占总量的比例大小，主要用于显示数据中<font color="red">**各项大小与各项总和的比例**</font>。   

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301051528.png" alt="image-20230830105109403" style="zoom:50%;" />

​                                                                2022年全国居民的人均消费支出情况 

- **散点图：**散点图又称X-Y图，是由若干个数据点组成的图表，主要用于<font color="red">**判断两变量之间是否存在某种关联**</font>，或者总结数据点的分布模式。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301052128.png" alt="image-20230830105218047" style="zoom:50%;" />

​                                                             股票回报率与基金回报率 的投资分析情况

​	散点图中数据点的分布情况可以体现变量之间的相关性。

- 若所有的数据点在一条直线附近呈波动趋势，说明变量之间是线性相关的。
- 若数据点在曲线附近呈波动趋势，说明变量之间是非线性相关的。
- 若数据点没有显示任何关系，说明变量之间是不相关的。	



- **气泡图：**气泡图是散点图的变形，它是一种能够展示<font color="red">**多变量关系**</font>的图表。气泡图一般使用两个变量标注气泡在坐标系中的位置，使用第3个变量标注气泡的面积，适用于分类数据**对比**、多变量相关性等情况。 

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301055175.png" alt="image-20230830105511080" style="zoom:50%;" />

​                                                  第 1 梯队和第 2 梯队主流 App 用户量与上线时间的分布情况

- **误差棒图：**误差棒图是使用<font color="red">**误差棒**</font>注明被测量数据的不确定度大小的图表，用于表示测量数据中客观存在的<font color="red">**测量偏差**</font>。误差棒是在表示测量值大小的方向上的一条线段，它以被测量数据的平均值为中点，线段长度的一半为不确定度。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301056341.png" alt="image-20230830105618253" style="zoom:50%;" />

​                                                                              成都上半年的降雨量

- **雷达图：**雷达图又称蜘蛛网图、星状图、极区图，由一组坐标轴和多个等距<font color="red">**同心圆或多边形**</font>组成，是一种表现<font color="red">**多维（4维以上）数据**</font>的图表。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301058461.png" alt="image-20230830105830307" style="zoom:50%;" />

​                                                                某人通过霍兰德职业兴趣测试的结果

- **统计地图：**统计地图是一种以<font color="red">**地图**</font>为背景，使用各种<font color="red">**线纹、色彩、几何图形或实物形象**</font>标注指标数值的大小及其在不同地理位置的分布状况的图表。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301059176.png" alt="image-20230830105954074" style="zoom:50%;" />

​                                                        2021年2月1日中国新型冠状病毒肺炎疫情地图

- **3D图表：**3D图表是一类在<font color="red">**三维坐标系**</font>中呈现数据的图表，常用的图表包括3D散点图、3D折线图、3D曲面图、3D直方图、3D柱形图等。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301101553.png" alt="image-20230830110142405" style="zoom:50%;" />

​																				豆粕期权隐含波动率

### 1.3.选择正确的数据可视化图标

​	数据可视化的图标类型十分丰富，好的图表可以有效、清晰地呈现数据地信息。对于用户而言，选择正确地图表是十分关键地，不仅可以达到“一图胜千言”地效果，而且会直接影响分析的结果。

​	用户选择正确的数据可视化图表，需要明确数据的逻辑关系。数据的逻辑关系可分为4种：<font color="red">**比较、分布、构成和联系**</font>。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301149970.png" alt="image-20230830114717452" style="zoom:50%;" />

- **基于比较关系可选择的图表：**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301150016.png" alt="image-20230830115052877" style="zoom:50%;" />

​	由图可知，若数据**按照时间进行比较**，当数据周期少时可以选择柱形图或折线图，数据周期多时可以选择雷达图或折线图；若数据**按分类进行比较**，当每个项目中仅包含1个变量时可以选择表格、条形图或柱形图，当每个项目包含2个变量时可以选择不等宽柱形图。



- **基于分布关系可选择的图表：**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301404352.png" alt="image-20230830140459234" style="zoom:50%;" />

​	由图可知，基于分布关系的数据包括**单变量（例如文化程度）、2个变量（例如文化程度和收入期望）、3个变量（例如文化程度、收入期望和工作经验）**。若数据为单变量，可以选择直方图或正态分布图；若数据为2个变量，可以选择散点图；若数据为3个变量，可以选择曲面图。



- **基于构成关系可选择的图表：**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301409666.png" alt="image-20230830140934518" style="zoom:50%;" />

​	由图可知，基于构成关系的数据按照是否变化可分为静态数据和随时间变化的数据。若是静态数据，可以选择饼图、瀑布图或堆积柱形图；若为随时间变化的数据，则先按照周期数分为少数周期数据和多周期数据，对于少数周期数据可以选择堆积柱形图，对于多周期数据可以选择堆积面积图。



- **基于联系关系可选择的图表：**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301412690.png" alt="image-20230830141235574" style="zoom:50%;" />

​	由图可知，基于联系关系的数据，若数据中包含2个变量，可以选择散点图进行展示；若数据中包含3个变量，可以选择气泡图进行展示。



## 2.常见的数据可视化库

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301418725.png" alt="image-20230830141843622" style="zoom:50%;" />

​	Python作为数据分析的首选语言，它针对数据分析的每个环节都提供了很多库。常见的数据可视化库包括<font color="blue">**matplotlib、seaborn、ggplot、bokeh、pygal、pyecharts**</font>。

- **matplotlib：**matplotlib是众多Python数据可视化库的鼻祖，其设计风格与20 世纪 80 年代设计的商业化程序语言MATLAB十分接近，具有很多强大且复杂的可视化功能。matplotlib包含多种类型的API，可以**采用多种方式绘制图表并对图表进行定制**。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301416258.png" alt="image-20230830141602192" style="zoom:50%;" />

- **seaborn：**seaborn是基于matplotlib进行高级封装的可视化库，它支持交互式界面，使得绘制图表的功能变得愈加容易，且图表的色彩更具吸引力，可以画出丰富多样的统计图表。
- **ggplot：**ggplot是基于matplotlib并旨在以简单方式提高matplotlib可视化感染力的库，它采用叠加图层的形式绘制图形，例如先绘制坐标轴所在的图层，再绘制点所在的图层，最后绘制线所在的图层，但其并不适用于个性化定制图形。
- **bokeh：**bokeh是一个交互式的可视化库，它支持使用Web 浏览器展示，可使用快速简单的方式将大型数据集转换成高性能的、可交互的、结构简单的图表。
- **pygal：**pygal是一个可缩放矢量图表库，用于生成可在浏览器中打开的SVG格式的图表，这种图表可以在不同比例的屏幕上自动缩放，方便用户交互。
- **pyecharts：**pyecharts是一个生成Echarts Enterprise Charts，商业产品图表）图表的库，它生成的Echarts图表凭借良好的交互性、精巧的设计得到了众多开发者的认可。



​	尽管在matplotlib的基础上封装了很多更轻量的库，但万变不离其宗，掌握matplotlib可以更好的掌握底层原理，也可以更快速的学习其他可视化库。

## 3.初识matplotlib

### 3.1.matplotlib概述

​	matplotlib是一个由John D.Hunter等人员开发的、主要用于绘制2D图表的Python库。matplotlib支持**numpy、pandas的数据结构**，具有绘制丰富的图表、定制图表元素或样式的功能。 matplotlib 还可用于绘制一些3D图表 。

​	matplotlib实际上是一个面向对象的绘图库，它所绘制的图标元素均对应一个对象。matplotlib<a href="https://matplotlib.org/">官网</a>提供了3种API：<font color="red">**pyplot API(implicit API)、object-oriented API(explicit API)、pylab API** </font>。

- **pyplot API**是使用pyplot模块开发的接口，该接口封装了一系列与MATLAB命令同名的函数，使用这些函数可以像使用MATLAB命令一样快速地绘制图表。

- **object-oriented API**是面向对象的接口，该接口封装了一系列对应图表元素的类，只有创建这些类的对象并按照隶属关系组合到一起才能完成一次完整的绘图。

- **pylab API**是使用pylab模块开发的接口，它最初是为了模仿MATLAB的工作方式而设计的，包括pyplot、numpy模块及一些其它附加功能，适用于Python交互环境中。

  <a href="https://matplotlib.org/stable/api/index.html">官方API参考</a>

  **注：**matplotlib官方不建议使用pylab API进行开发，并在最新的版本中弃用了pylab API。用户在使用时可以根据自身的实际情况进行选择 ，若只是需要快速地绘制图表，可以选择pyplot API进行开发；若需要自定义图表，可以选择object-oriented API进行开发。



### 3.2.安装matplotlib

​	在安装matplotlib前，需要先安装配置好Python环境，此处采用Python3.10作为环境：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301439463.png" alt="image-20230830143949376" style="zoom:50%;" />

​	安装matplotlib有多种方式，可以通过pip命令(<font color="red">pip install matplotlib</font>)直接安装，也可以使用Anaconda工具进行安装。Anaconda是一个开源的Python发行版本，包括conda、Python环境，以及诸如numpy、pandas、matplotlib、scipy等180多个科学计算包，既可以在同一台计算机上安装不同版本的软件包和依赖项，也能在不同环境之间进行切换，非常适合初学者使用。

​	<a href="https://anaconda.org.cn/">Anaconda中文网</a>可以作为安装学习参考。

- 从Anaconda<a href="https://www.anaconda.com/">官网</a>下载安装文件：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301451511.png" style="zoom:33%;" />

- 启动Anaconda3安装程序，进入欢迎界面后点击“Next”按钮进入要求用户接收许可协议的界面，点击“T Agree”进入安装界面：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302106298.png" alt="image-20230830210626183" style="zoom:33%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302106041.png" alt="image-20230830210640931" style="zoom:33%;" />

- 这里选择为谁安装，“Just me”即只为当前用户，"All Users"即为当前主机所有用户，根据用户需求选择：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302108661.png" alt="image-20230830210820578" style="zoom:33%;" />

- 选择安装路径，最好不含中文路径：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302109510.png" alt="image-20230830210905412" style="zoom:33%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302110920.png" alt="image-20230830211001837" style="zoom:33%;" />

- 在开始菜单栏种找到`Anaconda3`的“Anaconda Prompt”输入命令`conda list`即可看到`Anaconda`所集成的库：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302120733.png" alt="image-20230830212053346" style="zoom:33%;" />

- 点击“Jupter Notebook”即可在浏览器打开web界面编辑，选择"New--Python3"就可以创建文件了。

### 3.3.使用matplotlib绘制图表

​	绘制如下图表：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301558339.png" alt="image-20230830155857268" style="zoom: 50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
# 准备数据
data = np.array([1, 2, 3, 4, 5])
# 创建代表画布的Figure类的对象fig
fig = plt.figure()
# 在画布fig上添加坐标系风格的绘图区域
ax = fig.add_subplot(111)
# 绘制图表
ax.plot(data)
# 展示图表
plt.show()
```

​	下面使用pyplot的函数快速地绘制同一个图表：

```python
import numpy as np
import matplotlib.pyplot as plt
# 准备数据
data = np.array([1, 2, 3, 4, 5])
plt.plot(data)
plt.show()
```

​	plot()函数与plot()方法地参数用法是相同地，它们唯一的区别在于plot()函数缺少了`self`参数，可以直接被`pyplot`模块调用；而`plot()`方法只能被Axes类的对象调用。关于Canvas对象、Figure对象、Axes对象的结构如下图所示：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301605020.png" alt="image-20230830160533914" style="zoom:50%;" />

​		Axes对象拥有属于自己的坐标系，它可以是直角坐标系，即包含x轴和y轴的坐标系，也可以是三维坐标系（Axes的子类Axes3D对象），即包含x轴、y轴、z轴的坐标系。

​		假设大家想画一幅素描：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308301607811.png" alt="image-20230830160718670" style="zoom:33%;" />

​	使用matplotlib绘制的图形主要由三层组成：容器层、图像层和辅助显示层：

- **容器层**主要由Canvas对象、Figure对象、Axes对象组成；
- 图像层是指绘图区域内绘制的图形；
- 辅助显示层是指绘图区域内除所绘图形之外的辅助元素，包括坐标轴、标题、图例、注释文本等。