# author by Michealzou@126.com
# 2022/6/7 10:24
# finditer()
import re
string = "狗的英文是:Dog,猫的英文是：Cat"
reg_eng = re.compile(r"[a-zA-Z]+")
result_info = re.finditer(reg_eng,string)
print(result_info)  # <callable_iterator object at 0x000001DA89BB7C40>
print(type(result_info))  # <class 'callable_iterator'>
print(result_info.__next__())  # <regx.Match object; span=(6, 9), match='Dog'>