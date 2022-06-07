# author by Michealzou@126.com
# 2022/6/7 9:19
# search()函数
import re
info_one = "I was born in 2000"
info_two = "20000607"
print(re.search(r"\d",info_one))  # <re.Match object; span=(14, 15), match='2'>
print(re.search(r"\D",info_two))  # <re.Match object; span=(0, 1), match='2'>