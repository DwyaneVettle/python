# author by Michealzou@126.com
# 2022/6/7 9:38
# Match对象相关方法
import re
word = "Hello Python"
match_result = re.search(r"\wth\w",word)
print(match_result)  # <re.Match object; span=(7, 11), match='ytho'>
print(match_result.group())  # 匹配对象
print(match_result.start())  # 起始位置
print(match_result.end())  # 结束位置
print(match_result.span())  # （起始位置，结束位置）

words = re.search("(o)(n)","python bron in 1995")
print(words.group(1))  # 获取第一个子组的匹配结果 o
print(words.groups())  # ('o', 'n')
