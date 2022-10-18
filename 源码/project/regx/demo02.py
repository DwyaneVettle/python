# author by Michealzou@126.com
# 2022/6/7 8:57
# 预编译
import re
# 通过匹配模式\d预编译为正则对象regex_obj
regex_obj = re.compile(r'\d') # \d表示匹配数字
words = "Today is June 7, 2022"
print(regex_obj.findall(words))  # ['7', '2', '0', '2', '2']

# 匹配所有的英文字母可通过flags参数忽略大小写
regex_one = re.compile(r"[a-z]+",re.I)
print(regex_one.findall(words))  # ['Today', 'is', 'June']