# author by Michealzou@126.com
# 2022/6/13 14:51
import zxing
from MyQR import myqr

reader = zxing.BarCodeReader()
barcode = reader.decode('WWF.gif')
myqr.run(words =str(barcode.parses),
         version = 1,
         picture = 'WWF.gif',
         colorized = True,
         save_name = 'gmyq')