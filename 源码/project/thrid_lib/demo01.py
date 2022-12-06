# author by Michealzou@126.com
# 2022/11/15 14:31
# 免费测网速
# pip install wftools
import wftools
# wftools.net_speed_test()

# 扫描二维码
# pip install poimage
import poimage
#poimage.decode_qrcode(qrcode_path=r"D:\qrcode.jpg")
# pdf转word
# pip install popdf
# import popdf
# popdf.pdf2docx(file_path="Python.pdf")
import poimage
# poimage.add_watermark(file="qrcode.jpg", mark="你的水印")
import poexcel
# poexcel.find_excel_data(search_key='面试', target_dir='D:\周报文件\★2022-2023学年职发工作周月表.xlsx')
import poimage
#poimage.down4img(
#    url='https://img-blog.csdnimg.cn/c422d9c4331c4818b9c46b632814aa3d.png',
#    output_name='Michealzou',
#    type='jpg')

import wftools

# to_lang，是翻译的结果使用哪种语言，支持全球100多个语言；content，是你想翻译的文本内容
# wftools.transtools(to_lang='Chinese', content='Life is short, you need Python')

import search4file

# search4file.search_by_content(search_path=r'D:\笔记\Python', search_content='讲义')

import pofile

# pofile.replace4filename(path=r'D:\test', del_content='t', replace_content='T')
import wftools
wftools.weather()