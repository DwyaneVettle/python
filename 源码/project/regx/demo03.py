# author by Michealzou@126.com
# 2022/6/7 9:07
# match()函数
import re
data_one = "Today is June 7, 2022"
data_two = "7 June, 2022"
print(re.match(r"\d",data_one))  # None
print(re.match(r"\d",data_two))  # <regx.Match object; span=(0, 1), match='7'>