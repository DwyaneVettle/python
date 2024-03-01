# 第一章 Python入门



2016年3月，AlphaGo Lee与围棋世界冠军、职业九段棋手李世石进行围棋人机大战，以4比1的总比分获胜；

2017年5月，AlphaGo Master在中国乌镇围棋峰会上，与世界排名第一的围棋冠军柯洁对战，以3比0的比分获胜。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700367.png" alt="image-20220905164958661" style="zoom:50%;" />

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700369.png" alt="image-20220905171242574" style="zoom:50%;" />

## 1.什么是Python

​	**人生苦短，快学Python。**

​	Python由荷兰数学和计算机科学研究学会的[吉多·范罗苏姆](https://baike.baidu.com/item/吉多·范罗苏姆/328361) 于1990 年代初设计，作为一门叫做[ABC语言](https://baike.baidu.com/item/ABC语言/334996)的替代品。  Python提供了高效的高级[数据结构](https://baike.baidu.com/item/数据结构/1450)，还能简单有效地[面向对象](https://baike.baidu.com/item/面向对象/2262089)编程。Python语法和动态类型，以及[解释型语言](https://baike.baidu.com/item/解释型语言/8888952)的本质，使它成为多数平台上写[脚本](https://baike.baidu.com/item/脚本/1697005)和快速开发应用的编程语言，  随着版本的不断更新和语言新功能的添加，逐渐被用于独立的、[大型项目](https://baike.baidu.com/item/大型项目/3986637)的开发。官网：www.python.org 

![image-20220108201723449](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700371.png)

​	Python 单词是“大蟒蛇”的意思。但是龟叔不是喜欢蟒蛇才起这个名字，而是正在追 剧：英国电视喜剧片《蒙提·派森的飞行马戏团》(Monty Python and the Flying Circus)。

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700372.jpg)

​	Python和Java一样，需要安装一定的环境才能运行程序。不过我们可以通过官网提供的脚本interactive shell 来入门 Python。

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700373.png)

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700374.png)



## 2.Python的特点

​	Python的主要特点有以下几个：

- **可读性强：**可读性远比听上去重要的多得多。一个程序会被反复的修改，可读性强意味着让你  可以在更短时间内学习和记忆，直接提高生产率。

- **简洁，简洁，简洁：**研究证明，程序员每天可编写的有效代码数是有限的。完成同样功能只用一半的代 码，其实就是提高了一倍的生产率。Python 是由 C 语言开发，但是不再有 C 语言中指针等复杂数据类型，Python 的 简洁性让开发难度和代码幅度大幅降低，开发任务大大简化。程序员再也不需要关注复 杂的语法，而是关注任务本身。

  

- **免费、开源：**Python是FLOSS（自由/开放源码软件）之一。使用者可以自由地发布这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。FLOSS是基于一个团体分享知识的概念。

- **跨平台性：**由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE、PocketPC、Symbian以及Google基于linux开发的android平台

- **可扩展性、可扩充性**：如果需要一段关键代码运行得更快或者希望某些算法不公开，可以部分程序用C或C++编写，然后在Python程序中使用它们。

- **做科学计算优点多：**Python拥有丰富的扩展库，可以轻易完成各种高级任务，开发者可以用Python实现完整的应用程序所需的各种功能。

- **丰富的库：**Python标准库确实很庞大。它可以帮助处理各种工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV文件、密码系统、GUI（图形用户界面）、Tk和其他与系统有关的操作。

- **性能较低：**Python是解释型语言，性能较低。如果对于性能方面有要求，可以使用Java，C，Go等语言。但随着不断的发展，Python的解释器会越来越快。



## 3.Python的应用领域

​	Python作为一种解释型脚本语言，可以应用的领域有很多，可以概括为以下几个：

1. Web和Internet开发：如豆瓣、知乎、YouTube等；
2. 爬虫：模仿人去网站获取海量数据；
3. 科学计算和统计：使用数据分析，从数据中获取有用信息；
4. 人工智能；
5. 桌面界面开发；
6. 软件后端开发；
7. 游戏开发；
8. 机器学习；
9. 自动化测试和运维；
10. 办公自动化；

。。。。。



## 4.Python的主要发布版本

| 发布版本 | 发布日期  | GPL兼容 |
| -------- | --------- | ------- |
| 0.9-1.2  | 1991-1995 | 是      |
| 1.6      | 2000      | 否      |
| 2.0      | 2000      | 否      |
| 3.0      | 2008      | 否      |



## 5.Python的解释器

​	Python程序的执行依赖于解释器，常用的Python解释器有以下几种：

- CPython: 使用 C语言实现的解释器，最常用的解释器。通常说的解释器指的就是它;
- Jython:使用 java 语言实现的解释器。Jython 可以直接调用 java 类库，适合在 java 平台上开 发;
- IronPython:.NET 平台上使用的解释器。可直接调用.NET 平台的类，适合.NET 平台上开发;
- PyPy:使用 Python 语言实现的解释器。



## 6.Python开发入门

### 	6.1.Python下载安装和配置

​	我们需要进入官网（www.python.org/downloads/）下载Python解释器，并配置环境变量。在安装解释器时勾选"Add Python to enviroment variable"，这样就会将Python自动添加到环境变量Path中，我们可以在Windows环境下运行Python解释器。

![image-20240227092846196](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202402270928477.png)



### 	6.2.Python环境检测

​	安装了Python的解释器后，我们可以在当前系统中Windows+R键输入cmd，再输入命令python，当看到当前Python安装版本后，就表示已经安装成功。

![image-20240226211510929](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202402262115989.png)



### 	6.3.Python的开发环境

​		开发环境IDE（Integrated Development Environment 集成开发环境）本质上是对Python解释器中python.exe的封装，核心都一样。IDE相当于是解释器的一个外挂，目的是让程序员较少出错率，增加开发效率。常用的开发环境有：

1. IDLE
2. Pycharm
3. wingIDE
4. IDEA
5. IPython



### 	6.4.IDLE开发环境入门

#### 		6.4.1.IDLE介绍

​	IDLE 是 Python 的官方标准开发环境，Python 解释器安装完后同时就安装了 IDLE。IDLE 已经具备了 Python 开发几乎所有功能（语法智能提示、不同颜色显示不同类型等等），也不需要其他配置，非常适合初学者使用，它是 Python 标准发行版内置的一个简单小巧的 IDE，包括了交互式命令行、编辑器、调试器等基本组件，足以应付大多数简单应用。

​	IDLE 是用纯 Python 基于 Tkinter 编写，最初的作者正是 Python 之父 Guido van Rossum。

#### 		6.4.2.IDLE实操

​	在开始菜单栏中搜索IDLE就可以打开该程序进行使用：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700380.png" alt="image-20220109214026550" style="zoom:50%;" />

​	**打开IDLE后就可以点击File-->New File创建Python源文件，创建前我们需要将文件保存为.py文件在本地才能运行，创建我们的第一个Python文件：**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700381.png" alt="image-20220109220526740" style="zoom:50%;" />

```py
print("Hello World")
print("Hello Python")
```

​	**写好代码后，就可以在IDLE中点击Run-->Run Model运行此Python文件了：**

![image-20220109221006743](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700382.png)

​	**运行结果显示在IDLE的命令行模式中可以看到**

![image-20220109221053256](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700383.png)

​	**尝试以下创建以下代码，查看运行结果：**

```py
import turtle
t = turtle.Pen()

for x in range(360):
    t.forward(x)
    t.left(59)
```

### 	6.5.Python代码的基本格式和规范

- **分号：**不要在行尾加分号，也不要用分号将两条命令放在同一行。
- **缩进：**用4个空格进行缩进，不要用tab键或tab键混搭空格进行缩进，因为Python和Java不一样，Python使用缩进来表示程序块而不是{}。
- **空行：**顶级定义之间(类与第一个方法之间)空2行，方法定义之间空一行。
- **大小写：**Python区分大小写。
- **注释：**
  - **行注释：**每行注释前加#，当解释器看到#，就会忽略#后面的内容；
  - **段注释：**使用三个连续双引号'''，看到'''则会扫描到下一个'''，然后忽略它们之间的内容。
  - **编码注释：**Python默认的编码是utf-8，但可以通过"#coding:编码" 的方式设置其他编码，这个编码方式需写道文件最前面
- **行连接符：**一行程序的长度是不限制的，但是为了可读性强，我们可以使用\行连接符，Python解释器就会把\前后的代码解释为同一行。

**Python 官方推荐的 PEP-8 代码风格详细说明：https://www.python.org/dev/peps/pep-0008/**

## 7.练习图形化界面

​	Python为我们提供了一个海龟(turtle)画图的图形化库，为了让大家对Python进一步理解，提高大家的兴趣，我们可以演示以下两端代码：

```py
import turtle #导入 turtle 模块 

turtle.showturtle() #显示箭头 
turtle.write("你好") #写字符串 
turtle.forward(300) #前进 300 像素 
turtle.color("red") #画笔颜色改为 red 
turtle.left(90) #箭头左转 90 度 
turtle.forward(300) 
turtle.goto(0,50) #去坐标（0,50） 
turtle.goto(0,0) 
turtle.penup() #抬笔。这样，路径就不会画出来 
turtle.goto(0,300) 
turtle.pendown() #下笔。这样，路径就会画出来 
turtle.circle(100) #画圆
```

- 海归绘图画奥运五环

![image-20220110115421235](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700384.png)

```py
import turtle 

turtle.width(10) 

turtle.color("blue") 
turtle.circle(50)

turtle.color("black") 
turtle.penup() 
turtle.goto(120,0) 
turtle.pendown() 
turtle.circle(50)

turtle.color("red") 
turtle.penup() 
turtle.goto(240,0)
turtle.pendown() 
turtle.circle(50)

turtle.color("yellow") 
turtle.penup() 
turtle.goto(60,-50) 
turtle.pendown() 
turtle.circle(50)

turtle.color("green") 
turtle.penup() 
turtle.goto(180,-50) 
turtle.pendown() 
turtle.circle(50)
```



**绘制多角星：**

```python
import turtle as t
t.color('black', 'red')   # 设置画笔颜色，以及填充颜色
t.setup(450, 400)           # 设置主窗口的大小为450*400
t.begin_fill()              # 在绘制要填充的形状之前调用
while True:
    t.forward(150)          # 向当前画笔移动150个像素
    t.left(150)             # 逆时针移动150
    if abs(t.pos()) < 1:    # 如果当位置绝对值小于跳出循环
        break
t.end_fill()                # 结束填充位置
t.done()                    # 停止画笔绘制，窗体不关闭
```



## 8.pycharm安装及使用

​	pycharm是jetbrains公司提供的一款专门开发Python项目的开发软件，是目前最流行的Python程序开发工具。

​	下载地址：https://www.jetbrains.com/pycharm/download

​	**安装步骤：**

- 选择安装路径：



- 选择以下几个选项：

  

- Install安装



## 9.Python程序执行过程分析

Python虽然是解释型语言，但为了提高运行效率，使用了一种编译的方法，编译之后得到pyc文件，存储了字节码（特定的Python表现形式，不是机器码）。





**本章作业：**

1.构建Python开发环境，编写第一个Python程序；

2.自己再次完成奥运五环绘图程序；

3.使用海归绘图，画出4个正方形：

![image-20220110115852662](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171700388.png)



## Python学习方法

- 弱语法，重规则
- 重思想，重设计
- 是技术，更艺术
- 项目化，实战化
- what-->why-->-->where-->how

