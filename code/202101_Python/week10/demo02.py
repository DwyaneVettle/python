# author by Michealzou@126.com
# 2022/11/9 9:05
set01 = {1, 2, 3, 4}
set02 = {2, 3, 4, 5, 6}
# 1.交集 &
print(set01 & set02)  # {2, 3, 4}
# 2.并集 |
print(set01 | set02)  # {1, 2, 3, 4, 5, 6}
# 3.补集 -
print(set01 - set02)  # {1}
# 4.补集 ^
print(set01 ^ set02)  # {1, 5, 6}
# 5.子集 <
print(set01 < set02)  # False
# 6.超集 >
print(set01 > set02)  # False
# 7.是与不是 == !=
print(set01 == set02)  # False


