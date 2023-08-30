# 第二章  使用matplotlib绘制简单图表

## 1.绘制折线图

### 2.1.使用plot()绘制折线图

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

<img src="C:/Users/HP/AppData/Roaming/Typora/typora-user-images/image-20230830172913886.png" alt="image-20230830172913886" style="zoom:50%;" />