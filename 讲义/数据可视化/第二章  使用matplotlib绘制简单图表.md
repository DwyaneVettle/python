# 第二章  使用matplotlib绘制简单图表

## 1.绘制折线图

### 1.1.使用plot()绘制折线图

​	使用pyplot的`plot()`函数可以快速绘制折线图。`plot()`函数的语法格式如下：

```python
plot（x, y, fmt, scalex=True, scaley=True, data=None, label=None, *args, **kwargs）
```

- **x**：表示x轴的数据，默认值为range(len(y))。

- **y：**表示y轴的数据。

- **fmt：**表示快速设置线条样式的格式字符串。

- **label：**表示应用于图例的标签文本。

  `plot()`函数会返回一个包含<font color="red">**Line2D**</font>类对象（代表线条）的列表。

  使用pyplot的plot()函数还可以绘制具有多个线条的折线图，通过以下任意一种方式均可以完成。

1. 多次调用`plot()`函数来绘制具有多个线条的折线图：

   ```python
   plt.plot(x1, y1)
   plt.plot(x2, y2)
   ```

2. 调用`plot()`函数时传入一个二维数组来绘制具有多个线条的折线图，例如将二维数组arr的第一行数据作为x轴数据，其他行数据全部作为y轴数据：

   ```python
   arr = np.array([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9],
                            [10, 11, 12]])
   plt.plot(arr[0], arr[1:]) 
   ```

3. 调用`plot()`函数时传入多组数据来绘制具有多个线条的折线图：

   ```python
   plt.plot(x1, y1, x2, y2)
   ```

   
   
   **示例：**要求根据下表的数据，将日期列的数据作为x轴数据，将最高气温和最低气温两列的数据作为y轴数据，使用`plot()`函数绘制下图所示的折线图。

<img src="C:/Users/HP/AppData/Roaming/Typora/typora-user-images/image-20230830165856158.png" alt="image-20230830165856158" style="zoom:50%;" />

​	根据图示我们可以得知：将“日期”这一列作为x轴数据，将“最高气温”和“最低气温”两列的数据作为y轴数据，代码实现如下：

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4, 19)
y_max = np.array([32, 33, 34, 34, 33, 31, 30, 29, 30,
                  29, 26, 23, 21, 25, 31])
y_min = np.array([19, 19, 20, 22, 22, 21, 22, 16, 18,
                  18, 17, 14, 15, 16, 16])
# 绘制折线图
plt.plot(x, y_max)
plt.plot(x, y_min)
plt.show()
```

​	运行结果如下：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302048711.png" alt="image-20230830172913886" style="zoom:50%;" />

## 2.绘制柱形图或堆积柱形图

### 2.1.使用bar()绘制柱形图或堆积柱形图

​	使用pyplot的`bar()`函数可以快速地绘制柱形图或堆积柱形图 。`bar()`函数的语法格式如下：

```python
bar(x, height, width=0.8, bottom=None, align=‘center’, tick_label=None, xerr=None, yerr=None, **kwargs)
```

- **x:**表示柱形的<font color="red">x坐标值</font>。
- **height:**表示柱形的<font color="red">高度</font>。
- **width:**表示柱形的<font color="red">宽度</font>，默认为0.8。
- **bottom:**表示柱形底部的<font color="red">y值</font>，默认为0。
- **tick_label**：表示柱形对应的刻度标签。
- **xerr，yerr :**若未设为None，则需要为柱形图添加<font color="red">水平/垂直误差棒</font>。



​	`bar()`函数会返回一个`BarContainer`类的对象。`BarContainer`类的对象是一个包含柱形或误差棒的容器，它亦可以视为一个元组，可以遍历获取每个柱形或误差棒。此外，`BarContainer`类的对象也可以访问`patches`或`errorbar`属性分别获取图表中所有的柱形或误差棒。

​	例如，绘制以下柱形图：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302057687.png" alt="image-20230830205717615" style="zoom:33%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y1 = np.array([10, 8, 7, 11, 13])
# 柱形的宽度
bar_width = 0.3
# 绘制柱形图
plt.bar(x, y1, tick_label=['a', 'b', 'c', 'd', 'e'], width=bar_width)
plt.show()
```

​	运行结果如下：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302128219.png" alt="image-20230830212828144" style="zoom:33%;" />

​	使用pyplot的`bar()`函数还可以绘制具有多组柱形的柱形图，如下图：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302134149.png" alt="image-20230830213408066" style="zoom: 33%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y1 = np.array([10, 8, 7, 11, 13])
y2 = np.array([19, 6, 5, 10, 12])
# 柱形的宽度
bar_width = 0.3
# 根据多组数据绘制柱形图
plt.bar(x, y1, tick_label=['1月', '2月', '3月', '4月', '5月'],
        width=bar_width)
plt.bar(x+bar_width, y2, width=bar_width)
plt.show()
```

- **可以使用`bottom`参数传值的方式控制柱形的y值，使后悔之的柱形图位于先绘制的柱形的上方**：

```python
plt.bar(x, y1, tick_label=['1月', '2月', '3月', '4月', '5月'],
        width=bar_width)
# plt.bar(x+bar_width, y2, width=bar_width)
plt.bar(x, y2, bottom=y1, width=bar_width)
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302137099.png" style="zoom:50%;" />

- **可以通过给xerr、yerr参数传值的方式为柱形添加误差棒：**

```python
error = [2, 1, 2.5, 2, 1.5]
# 根据多组数据绘制柱形图
plt.bar(x, y1, tick_label=['1月', '2月', '3月', '4月', '5月'],
        width=bar_width)
plt.bar(x, y2, bottom=y1, width=bar_width, yerr=error)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302141816.png" alt="image-20230830214154713" style="zoom:33%;" />

### 2.2.实例：2013-2019财年某电商平台的GMV

​	本实例要求根据下表的数据，将财年列的数据作为x轴数据，将GMV（一定时间内的成交总额）列的数据作为y轴数据，使用bar()函数绘制下图所示的柱形图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302143746.png" alt="image-20230830214348652" style="zoom:50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308302143956.png" alt="image-20230830214359861" style="zoom:33%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 8)
y = np.array([10770, 16780, 24440, 30920, 37670, 48200, 57270])
# 绘制柱形图
plt.bar(x, y, tick_label=['FY2013', 'FY2014', 'FY2015', 'FY2016',
                          'FY2017', 'FY2018', 'FY2019'], width=0.5)
plt.show()
```



## 3.绘制条形图或堆积条形图

### 3.1.使用barh()绘制条形图或堆积条形图

​	使用pyplot的`barh(`)函数可以快速地绘制条形图或堆积条形图 ，语法格式如下：

```shell
barh(y, width, height=0.8, left=None, align='center', *, **kwargs)
```

- **y**：表示条形的<font color="red">y值</font>>。
- **width：**表示条形的<font color="red">宽度</font>。
- **height：**表示条形的<font color="red">高度</font>，默认值为0.8。
- **left：**条形左侧的<font color="red">x坐标值</font>，默认值为0。
- **align**：表示条形的<font color="red">对齐方式</font>，默认值为“center”,即条形与刻度线居中对齐。
- **tick_label：**表示条形对应的<font color="red">刻度标签</font>。
- **xerr，yerr：**若未设为None，则需要为条形图添加<font color="red">水平/垂直误差棒</font>。



​	例如，绘制如下图形：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311530982.png" alt="image-20230831153032805" style="zoom:33%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
# 条形的高度
bar_height = 0.3
# 绘制条形图
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'],
         height=bar_height)
plt.show()
```

- **使用`barh()`函数还可以绘制具有多组条形的条形图：**

```python
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
x2 = np.array([9, 6, 5, 10, 12])
bar_height = 0.3
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
plt.barh(y+bar_height, x2, height=bar_height)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311534901.png" alt="image-20230831153421807" style="zoom:33%;" />

- **使用`barh()`函数还可以通过给left参数传值的方式控制条形的x值，使后绘制的条形位于先绘制的条形的右方：**

```shell
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
# plt.barh(y+bar_height, x2, height=bar_height)
plt.barh(y, x2, left=x1, height=bar_height)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311539240.png" alt="image-20230831153933135" style="zoom:50%;" />

- **在使用barh()函数绘制图表时，可以通过给xerr、yerr参数传值的方式为条形添加误差棒：**

```python
error = [2, 1, 2.5, 2, 1.5]
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
# plt.barh(y+bar_height, x2, height=bar_height)
plt.barh(y, x2, left=x1, height=bar_height, xerr=error)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311542693.png" alt="image-20230831154238597" style="zoom:33%;" />

### 3.2.实例：各商品种类的网购代替率

​	网络购物已经成为人们日常生活的一部分，它在创造新的消费方式的同时，也在改变着人们的消费模式和习惯，成为拉动居民消费的重要渠道。国家统计局抽取了771个样本，并根据这些样本测算用户网购替代率（网购用户线上消费对线下消费的替代比率）的情况。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311543573.png" alt="image-20230831154343494" style="zoom: 80%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311548621.png" alt="image-20230831154823523" style="zoom:50%;" />

​	根据图示可以得知，将“商品种类”一列的数据作为y轴的刻度标签，将“替代率”一列的数据作为x轴的数据，具体代码如下：

```python
import numpy as np
import matplotlib.pyplot as plt

# 显示中文
# 运行配置参数中的字体（font）为黑体（SimHei）
plt.rcParams['font.sans-serif'] = ['SimHei']
#运行配置参数总的轴（axes）正常显示正负号（minus）
plt.rcParams['axes.unicode_minus'] = False
x = np.array([0.959, 0.951, 0.935, 0.924, 0.893,
              0.892, 0.865, 0.863, 0.860, 0.856,
              0.854, 0.835, 0.826, 0.816, 0.798,
              0.765, 0.763, 0.670])
y = np.arange(1, 19)
labels = ["家政、家教、保姆等生活服务", "飞机票、火车票", "家具",
          "手机、手机配件", "计算机及其配套产品", "汽车用品", "通信充值、游戏充值",
          "个人护理用品", "书报杂志及音像制品", "餐饮、旅游、住宿", "家用电器",
          "食品、饮料、烟酒、保健品", "家庭日杂用品", "保险、演出票务",
          "服装、鞋帽、家用纺织品", "数码产品", "其他商品和服务", "工艺品、收藏品"]
# 绘制条形图
plt.barh(y, x, tick_label=labels, align="center", height=0.6)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311601430.png" alt="image-20230831160148239" style="zoom:50%;" />

## 4.绘制堆积面积图

### 4.1.使用stackplot()绘制堆积面积图

​	使用pyplot的stackplot()函数可以快速地绘制堆积面积图 ，语法格式为：

```python
stackplot(x, y,labels=(), baseline='zero', data=None, *args, **kwargs)
```

- **x：**表示<font color="red">x轴的数据</font>，可以是一维数组。

- **y：**表示<font color="red">y轴的数据</font>，可以是二维数组或一维数组序列。

- **labels：**表示每个填充区域的标签。

- **baseline：**表示<font color="red">计算基线的方法</font>，包括zero、sym、wiggle和weighted_wiggle。其中zero表示**恒定零基线**，即简单的叠加图；sym表示**对称于零基线**；wiggle表示**最小化平方斜率之和**；weighted_wiggle表示**执行相同的操作**，但权重用于说明每层的大小。

  绘制如下图示：

  <img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311607511.png" alt="image-20230831160751380" style="zoom:33%;" />

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
y1 = np.array([1, 4, 3, 5, 6, 7])
y2 = np.array([1, 3, 4, 2, 7, 6])
y3 = np.array([3, 4, 3, 6, 5, 5])
# 绘制堆积面积图
plt.stackplot(x, y1, y2, y3)
plt.show()
```

### 4.2.实例：物流公司物流费用统计

​	近些年我国物流行业蓬勃房展，目前已经有近几千家物流公司，其中部分物流公司大打价格战，以更低的价格吸引更多的客户，从而抢占市场份额。 本实例要求根据下表的数据，将月份列的数据作为x轴的刻度标签，将A公司、B公司、C公司这三列数据作为y轴的数据，使用stackplot()函数绘制下图所示的堆积面积图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311609187.png" alt="image-20230831160910086" style="zoom:50%;" />![image-20230831160917986](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311609081.png)

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311609114.png" alt="image-20230831160951004" style="zoom:50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y_a = np.array([198, 215, 245, 222, 200, 236, 201, 253, 236, 200, 266, 290])
y_b = np.array([203, 236, 200, 236, 269, 216, 298, 333, 301, 349, 360, 368])
y_c = np.array([185, 205, 226, 199, 238, 200, 250, 209, 246, 219, 253, 288])
# 绘制堆积面积图
plt.stackplot(x, y_a, y_b, y_c)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311619454.png" alt="image-20230831161901361" style="zoom:50%;" />

## 5.绘制直方图

### 5.1.使用hist绘制直方图

​	使用pyplot的hist()函数可以快速地绘制直方图 ，语法格式如下：

```python
hist(x, bins=None, range=None, density=None, weights=None, 
       bottom=None,  **kwargs) 
```

- **x：**表示x轴的数据。

- **bins：**表示<font color="red">矩形条的个数</font>，默认为10。

- **range：**表示数据的范围，若未设置范围，默认数据范围为(x.min(), x.max())。

- **cumulative：**表示是否计算累计频数或频率。

- **histtype：**表示<font color="red">直方图的类型</font>，支持'bar'、'barstacked'、'step'、'stepfilled‘四种取值，其中'bar'为默认值，代表传统的直方图；'barstacked'代表堆积直方图；'step'代表未填充的线条直方图；'stepfilled'代表填充的线条直方图。

  绘制如下直方图：

  <img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311623501.png" alt="image-20230831162333401" style="zoom:50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
# 准备50个随机测试数据
scores = np.random.randint(0,100,50)
# 绘制直方图
plt.hist(scores, bins=8, histtype='stepfilled')
plt.show()
```

### 5.2.实例：人脸识别的灰度直方图

​	人脸识别技术是一种生物特征识别技术，它通过从装有摄像头的终端设备拍摄的人脸图像中抽取人的个性化特征，以此来识别人的身份。灰度直方图是实现人脸识别的方法之一，它将数字图像的所有像素按照灰度值的大小统计其出现的频率。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311624479.png" alt="image-20230831162424376" style="zoom:50%;" />

​	本实例要求使用一组10000个随机数作为人脸图像的灰度值，使用hist()函数绘制下图所示的灰度直方图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202308311625060.png" alt="image-20230831162511943" style="zoom:50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
# 10000个随机数
random_state = np.random.RandomState(19680801)
radom_x = random_state.randn(10000)
# 绘制包含25个矩形条的直方图
plt.hist(radom_x, bins=25)
plt.show()
```



## 6.绘制饼图或圆环图

### 6.1.使用pie()绘制饼图或圆环图

​	使用pyplot的`pie()`函数可以快速地绘制饼图或圆环图 ，语法格式如下：

```python
pie(x, explode=None, labels=None, autopct=None, pctdistance=0.6, 
      startangle=None, *, data=None) 
```

- **x：**表示扇形或楔形的数据。
- **explode：**表示扇形或楔形<font color="red">离开圆心的距离</font>。
- **labels：**表示扇形或楔形对应的标签文本。
- **autopct：**表示控制扇形或楔形的数值显示的字符串，可通过格式字符串<font color="red">指定小数点后的位数</font>。
- **pctdistance：**表示扇形或楔形对应的数值标签距离圆心的比例，默认为0.6。
- **shadow：**表示是否<font color="red">显示阴影</font>。
- **labeldistance：**表示标签文本的绘制位置（相对于半径的比例），默认为1.1。

```python
pie(x, explode=None, labels=None, autopct=None, pctdistance=0.6, 
      startangle=None, *, data=None) 
```

- **startangle：**表示<font color="red">起始绘制角度</font>，默认从x轴的正方向逆时针绘制。
- **radius：**表示扇形或楔形围成的<font color="red">圆形半径</font>。
- **wedgeprops：**表示控制扇形或楔形属性的字典。例如，通过wedgeprops = {'width': 0.7} 将楔形的宽度设为0.7。
- **textprops：**表示控制图表中文本属性的字典。
- **center**：表示图表的中心点位置，默认为（0,0）。
- **frame：**表示是否显示图框。



绘制饼图：

```python
import numpy as np
import matplotlib.pyplot as plt
data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# 绘制饼图：半径为0.5，数值保留1位小数
plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011144482.png" alt="image-20230901114434245" style="zoom: 33%;" />

绘制圆环图：

```python
import numpy as np
import matplotlib.pyplot as plt
data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# 绘制圆环图
plt.pie(data, radius=1.5, wedgeprops={'width': 0.7}, 
           labels=pie_labels, autopct='%3.1f%%',      
           pctdistance=0.75) 
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011146445.png" alt="image-20230901114656330" style="zoom:33%;" />

### 6.2.实例：支付宝月账单报告

​	近年来随着支付App的出现，人们的生活发生了翻天覆地的变化，无论是到超市选购商品，还是跟朋友聚餐，或是来一场说走就走的旅行，都可以使用移动支付App轻松完成支付，非常便捷。支付宝是人们使用较多的支付方式，它拥有自动记录每月账单的功能，可以方便用户了解每月资金的流动情况。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011147064.png" alt="image-20230901114749972" style="zoom:33%;" />

​	本实例要求根据下表的数据，将分类列的数据作为饼图的标签，将各分类对应的金额与总支出金额的比例作为饼图的数据，使用pie()函数绘制下图所示的饼图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011148370.png" alt="image-20230901114823288" style="zoom:50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011149044.png" alt="image-20230901114902930" style="zoom:50%;" />

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 饼状图外侧文字说明
kinds = ['购物', '人情往来', '餐饮美食', '通信物流', '生活日用',
         '交通通行', '休闲娱乐', '其他']
# 饼状图数据
money_scale = [800/3000, 100/3000, 1000/3000, 200/3000,
               300/3000, 200/3000, 200/3000, 200/3000]
dev_position = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# 饼图绘制
plt.pie(money_scale, labels=kinds, autopct='%3.1f%%', shadow=True,
        explode=dev_position, startangle=90)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011159057.png" alt="image-20230901115912918" style="zoom:50%;" />

## 7.绘制散点图或气泡图

### 7.1.使用scatter()绘制散点图或气泡图

​	使用pyplot的`scatter()`函数可以快速地绘制散点图或气泡图，语法格式如下：

```python
scatter(x, y, s=None, c=None, marker=None, cmap=None, linewidths=None, edgecolors=None, *, **kwargs) 
```

- **x，y：**表示<font color="red">数据点的位置</font>。
- **s：**表示<font color="red">数据点的大小</font>。
- **c：**表示数据点的<font color="red">颜色</font>。
- **marker：**表示数据点的样式，默认为圆形。
- **alpha：**表示透明度，可以取值为0~1。
- **linewidths：**表示<font color="red">数据点的描边宽度</font>。
- **edgecolors：**表示<font color="red">数据点的描边颜色</font>。



绘制散点图：

```python
import numpy as np
import matplotlib.pyplot as plt
num = 50
x = np.random.rand(num)
y = np.random.rand(num)
plt.scatter(x, y)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011203164.png" alt="image-20230901120355056" style="zoom: 33%;" />

绘制气泡图：

```python
import numpy as np
import matplotlib.pyplot as plt
num = 50
x = np.random.rand(num)
y = np.random.rand(num)
area = (30 * np.random.rand(num))**2
plt.scatter(x, y, s=area)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011204263.png" alt="image-20230901120450130" style="zoom: 33%;" />

### 7.2.汽车速度与制动距离的关系

​	汽车的制动距离主要取决于汽车的车速。若车速增加1倍，则汽车的制动距离将增大至近4倍。某汽车生产公司对一批丰田汽车进行抽样测试，并分别记录了不同的车速对应的制动距离。

​	本实例要求根据下表的数据，将车速(km/h)列的数据作为x轴的数据，将制动距离(m)列的数据作为y轴的数据，使用scatter()函数绘制下图所示的散点图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011206428.png" alt="image-20230901120616339" style="zoom: 50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011207120.png" alt="image-20230901120701033" style="zoom:50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备x轴和y轴数据
x_speed = np.arange(10, 210, 10)
y_distance = np.array([0.5, 2.0, 4.4, 7.9, 12.3, 17.7,
                       24.1, 31.5, 39.9, 49.2, 59.5, 70.8,
                       83.1, 96.4, 110.7, 126.0, 142.2,
                       159.4, 177.6, 196.8])
# 绘制散点图
plt.scatter(x_speed, y_distance, s=50, alpha=0.9)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011211157.png" alt="image-20230901121159049" style="zoom:50%;" />

## 8.绘制箱型图

### 8.1.使用boxplot()绘制箱型图

​	使用pyplot的`boxplot()`函数可以快速地绘制箱形图，语法格式如下：

```python
boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, *, data=None)
```

- **x：**绘制箱形图的数据。
- **sym：**表示<font color="red">异常值对应的符号</font>，默认为空心圆圈。
- **vert：**表示<font color="red">是否将箱形图垂直摆放</font>，默认为垂直摆放。
- **whis：**表示箱形图上下须与上下四分位的距离，默认为1.5倍的四分位差。
- **positions：**表示箱体的位置。
- **widths：**表示<font color="red">箱体的宽度</font>，默认为0.5。
- **patch_artist：**表示是否填充箱体的颜色，默认不填充。
- **meanline：**是否用横跨箱体的线条<font color="red">标出中位数</font>，默认不使用。
- **showcaps：**表示是否显示箱体顶部和底部的横线，默认显示。
- **showbox：**表示<font color="red">是否显示箱形图的箱体</font>，默认显示。
- **showfliers：**表示<font color="red">是否显示异常值</font>，默认显示。
- **labels：**表示箱形图的标签。
- **boxprops：**表示控制箱体属性的字典。

```python
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(100)
plt.boxplot(data, meanline=True, widths=0.3, patch_artist=True,
            showfliers=False)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011216986.png" alt="image-20230901121641873" style="zoom:33%;" />

### 8.2.实例：2017年和2018年全国发电量统计

​	本实例要求根据下表的数据，将发电量(亿千瓦时)列的数据作为x轴的数据，将2017年和2018年作为y轴的刻度标签，使用boxplot()函数绘制下图所示的箱形图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011217409.png" alt="image-20230901121755313" style="zoom:50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011218030.png" alt="image-20230901121819891" style="zoom:50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data_2018 = np.array([5200, 5254.5, 5283.4, 5107.8, 5443.3,
                      5550.6, 6400.2, 6404.9, 5483.1, 5330.2, 5543, 6199.9])
data_2017 = np.array([4605.2, 4710.3, 5168.9, 4767.2, 4947,
                      5203, 6047.4, 5945.5, 5219.6, 5038.1,
                      5196.3, 5698.6])
# 绘制箱型图
plt.boxplot([data_2018, data_2017], labels=('2018年', '2017年'),
            meanline=True, widths=0.5, vert=False, patch_artist=True)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011226451.png" alt="image-20230901122658316" style="zoom:50%;" />

## 9.绘制雷达图

### 9.1.使用polar()绘制雷达图

​	使用pyplot的polar()函数可以快速地绘制雷达图，语法格式如下：

```python
polar(theta, r, **kwargs) 
```

- **theta:**表示每个数据点所在射线与极径的夹角。
- **r:**表示每个数据点到原点的距离。

### 9.2.实例：霍兰德职业兴趣测试

​	霍兰德职业兴趣测试是由美国职业指导专家霍兰德根据他本人大量的职业咨询经验及其职业类型理论编制的测评工具。

​	根据个人兴趣的不同，霍兰德将人格分为研究型（I）、艺术型（A）、社会型（S）、企业型（E）、传统型（C）和现实型（R）6个维度，将这6个维度不同程度的组合形成每个人的性格。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011229895.png" alt="image-20230901122907777" style="zoom:50%;" />

​	本实例要求根据下表的数据，将标题一行的数据作为雷达图的标签，将其余行的数据作为雷达图的数据，使用polar()函数绘制下图所示的雷达图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011229907.png" alt="image-20230901122932807" style="zoom:50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309011229239.png" alt="image-20230901122947108" style="zoom: 50%;" />

​	由图可知，用户1偏向于现实型人格；用户2偏向于研究型人格；用户3偏向于艺术型人格；用户4偏向于企业型人格；用户5偏向于社会型人格；用户6偏向于传统型人格。

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dim_num = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])
angles = np.linspace(0, 2 * np.pi, dim_num, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
data = np.concatenate((data, [data[0]]))
# 维度标签
radar_labels = ['研究型(I)', '艺术性(A)', '社会性(S)',
                '企业型(E)', '传统型(C)', '现实性(R)']
radar_labels = np.concatenate((radar_labels, [radar_labels[0]]))
# 绘制雷达图
plt.polar(angles, data)
# 设置极坐标的标签
plt.thetagrids(angles * 180/np.pi, labels=radar_labels)
# 填充多边形
plt.fill(angles, data, alpha=0.25)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309012144725.png" alt="image-20230901214438459" style="zoom:50%;" />

## 10.绘制误差棒图

### 10.1.使用errerbar()绘制误差棒

​	使用pyplot的errorbar()函数可以快速地绘制误差棒图，语法格式如下：

```python
errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None,  *, data=None, **kwargs) 
```

- **x，y：**表示<font color="red">数据点的位置</font>。
- **xerr，yerr：**表示<font color="red">数据的误差范围</font>。
- **fmt：**表示数据点的标记样式和数据点之间连接线的样式。
- **elinewidth：**表示误差棒的<font color="red">线条宽度</font>。
- **capsize：**表示误差棒边界横杆的<font color="red">大小</font>。
- **capthick：**表示误差棒边界横杆的<font color="red">厚度</font>。

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y = (25, 32, 34, 20, 25)
y_offset = (3, 5, 2, 3, 3)
plt.errorbar(x, y, yerr=y_offset, capsize=3, capthick=2)
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309012148932.png" alt="image-20230901214813768" style="zoom:50%;" />

### 10.2.实例：4个书中不同季节的细跟生物量

​	细根生物量的多少反映了根系从土壤中吸收水分和养分的能力，是植物地下部分集汇能力的重要体现。不同树种细根生物量存在差异性，各树种细根生物量在不同季节间差异较为明显。 

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309012149485.png" alt="image-20230901214942358" style="zoom:50%;" />

​	本实例要求根据下表的数据，将季节列的数据作为x轴的刻度标签，将其他列的数据作为y轴的数据，使用errorbar()函数绘制下图所示的误差棒图。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309012149263.png" alt="image-20230901214959163" style="zoom: 50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309012150766.png" alt="image-20230901215019641" style="zoom:50%;" />

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 准备 x 轴和 y 轴的数据
x = np.arange(3)
y1 = np.array([2.04, 1.57, 1.63])
y2 = np.array([1.69, 1.61, 1.64])
y3 = np.array([4.65, 4.99, 4.94])
y4 = np.array([3.39, 2.33, 4.10])
# 指定测量偏差
error1 = [0.16, 0.08, 0.10]
error2 = [0.27, 0.14, 0.14]
error3 = [0.34, 0.32, 0.29]
error4 = [0.23, 0.23, 0.39]
bar_width = 0.2
# 绘制柱形图
plt.bar(x, y1, bar_width)
plt.bar(x + bar_width, y2, bar_width, align="center",
        tick_label=["春季", "夏季", "秋季"])
plt.bar(x + 2*bar_width, y3, bar_width)
plt.bar(x + 3*bar_width, y4, bar_width)
# 绘制误差棒 : 横杆大小为 3,  线条宽度为 3,  线条颜色为黑色, 数据点标记为像素点
plt.errorbar(x, y1, yerr=error1, capsize=3, elinewidth=2, fmt=' k,')
plt.errorbar(x + bar_width, y2, yerr=error2, capsize=3, elinewidth=2, fmt='k,')
plt.errorbar(x + 2*bar_width, y3, yerr=error3, capsize=3, elinewidth=2, fmt='k,')
plt.errorbar(x + 2*bar_width, y3, yerr=error3, capsize=3, elinewidth=2, fmt='k,')
plt.show()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202309012155492.png" alt="image-20230901215530350" style="zoom:50%;" />