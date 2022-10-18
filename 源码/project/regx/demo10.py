# author by Michealzou@126.com
# 2022/6/7 10:39
# 贪婪匹配
import re
words = "Life is short, use python"
result = re.search(r"use\s.*",words)
print(result.group())  # use python
result_two = re.search(r"use\s.*?",words)
print(result_two.group())  # use
# 贪婪匹配
print(re.search(r"use\s.+",words))  # <regx.Match object; span=(15, 25), match='use python'>
# 非贪婪匹配
print(re.search(r"use\s.+?",words))  # <regx.Match object; span=(15, 20), match='use p'>
