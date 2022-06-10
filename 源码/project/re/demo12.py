# author by Michealzou@126.com
# 2022/6/7 11:23
import re
# 或
print(re.findall("ab|cd","abcdefg"))  # ['ab', 'cd']
# 匹配任意一个字符
print(re.findall("张.","张三"))  # ['张三']
# 字符集[]，取反^
print(re.findall("[^张].","张三李四"))  # ['张三']
print(re.findall("[^aeiou]","Hello World"))  # ['H', 'l', 'l', ' ', 'W', 'r', 'l', 'd']
# ^匹配目标字符串开始位置
print(re.findall("^James","James,Hello"))  # ['James']
# $匹配目标字符串结尾位置
print(re.findall("James$","Hello,James"))  # ['James']
# ^和$必须出现在字符串开头和结尾位置
# * 匹配前面的字符0次或多次
print(re.findall("wo*","wooooo~~w!"))  # ['wooooo', 'w']
# 匹配所有以大写字母开头的单词
print(re.findall("[A-Z][a-z]*","How are you? Fine,Tankyou"))  # ['How', 'Fine', 'Tankyou']
# + 匹配前面的字符出现1次或多次
print(re.findall("[A-Z][a-z]+","How are you? Fine,Tankyou"))  # ['How', 'Fine', 'Tankyou']
# 如果是单个单词，+不能匹配
print(re.findall("[A-Z][a-z]+","A Boy"))  # ['Boy']
# ？ 匹配前面的字符出现0次或1次
print(re.findall("ab?","abbbbb,abcde"))  # ['ab', 'ab']
print(re.findall("-?[0-9]+","22 -23 24 -25"))  # 匹配所有正数负数
print(re.findall("[^ ]+","Port-9 Error #404# %@STD"))  # 匹配所有