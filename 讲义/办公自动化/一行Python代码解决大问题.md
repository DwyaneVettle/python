# 一行Python代码解决大问题



## 1.免费测网速

Python本地测试的方法：

- 安装第三方库：

```python
pip install wftools
```

- 实现代码：

```python
import wftools
wftools.net_speed_test()
```

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171716844.png)



## 2.解析二维码

即使手上没有手机，也可以用Python解析。

- 安装第三方库

```python
pip install poiamge
```

- 代码实现

```python
import poimage
poimage.decode_qrcode(qrcode_path=r"D:\qrcode.jpg")
```

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171716845.png)



## 3.pdf转word文档

- 安装第三方库

```python
pip install popdf
```

- 代码实现

```python
import popdf
popdf.pdf2docx(file_path="HTML.pdf")
```

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171716846.png)



## 4.给图片添加水印

- 安装第三方库

```python
pip install poimage
```

- 代码实现

```python
import poimage
poimage.add_watermark(file="qrcode.jpg", mark="你的水印")
```

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171716847.png)





## 5.多个表格关联查询

- 安装第三方库

```python
pip install poexcel
```

- 代码实现

```python
import poexcel

poexcel.find_excel_data(search_key='你要搜索的内容', target_dir='存放excel的文件夹位置')
```



## 6.建议爬虫下载图片

- 安装第三方库

```python
pip install poimage
```

- 代码实现

```python
import poimage

poimage.down4img(
    url='https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/2-free-group.jpg',
    output_name='Michealzou',
    type='jpg')
```

![](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171716848.png)



## 7.简单翻译

- 安装第三方库

```python
pip install wftools
```

- 代码实现

```python
import wftools  
  
# to_lang，是翻译的结果使用哪种语言，支持全球100多个语言；content，是你想翻译的文本内容
wftools.transtools(to_lang='Chinese', content='Life is short, you need Python')
```





## 8.根据内容查找文件

- 安装第三方库

```python
pip install search4file
```

- 实现代码

```python
import search4file  
  
search4file.search_by_content(search_path=r'D:\笔记\你要查找的文件夹',search_content='你要查找的内容')
```



## 9.批量重命名目录/文件

- 安装第三方库

```python
pip install pofile
```

- 代码实现

```python
import pofile  
  
pofile.replace4filename(path=r'D:\你要替换的目录位置',del_content='文件名里需要删除的内容',replace_content='文件名里需要替换的内容')
```



## 10.查询天气

- 安装第三方库

```python
pip install wftools
```

- 代码实现

```python
import wftools  
  
wftools.weather()
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171716849.png" alt="image-20221204110532265" style="zoom:50%;" />

来源：www.python-office.com