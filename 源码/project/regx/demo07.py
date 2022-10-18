# author by Michealzou@126.com
# 2022/6/7 10:19
# findall()
import re
string = "狗的英文是:Dog,猫的英文是：Cat"
# 匹配字符串中所有的中文
reg_zhn = re.compile(r"[\u4e00-\u9fa5]+")
print(re.findall(reg_zhn,string))  # ['狗的英文是', '猫的英文是']