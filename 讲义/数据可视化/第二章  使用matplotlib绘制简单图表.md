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

