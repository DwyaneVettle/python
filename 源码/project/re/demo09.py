# author by Michealzou@126.com
# 2022/6/7 10:30
# sub()和subn()
import re
words = "Life is short, use python"
result_one = re.sub(r"\s","-",words)
print(result_one)  # Life-is-short,-use-python
result_two = re.subn(r"\s","-",words)
print(result_two)  # ('Life-is-short,-use-python', 4)
result = re.split(r"\s",words)
print(result)  # ['Life', 'is', 'short,', 'use', 'python']