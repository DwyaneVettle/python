# -*- coding: utf-8 -*-
# @Time : 2022/3/20 17:45
# @Email :1830037686@qq.com
# @File : job.py
# @Author : 邹志鹏
# @Class : 软件三班
# for循环
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum = sum + i
print(sum)
# while循环
sum1 = 0
j = 1
while j <= 100:
    if j %2 == 0:
        sum1 = sum1 + j
    j += 1
print(sum1)
# 9*9表格
for a in range(1,10):
    b=1
    while b < a + 1:
        print(f'{b}*{a}={a*b}',end='\t')
        b = b + 1
print()
