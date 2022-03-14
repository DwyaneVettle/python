# -*- coding: utf-8 -*-
# @Time : 2022/3/13 20:59
# @Email :1830037686@qq.com
# @File : job.py
score = float(input('请输入金额：'))
c = 0.1
for n in range(100, 1000):
    i = n // 100
    j = (n - 1 * 100) // 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)
# 根据金额打折
score = float(input('请输入金额：'))
c = 0.1
if 1 <= score <= 100:
    c = score * 1
    print('请支付', c ,'圆')
elif 100 < score <= 300:
    c = score * 0.9
    print('请支付', c ,'圆')
elif 300 < score <= 500:
    c = score * 0.8
    print('请支付', c ,'圆')
elif 500 < score <= 800:
    c = score * 0.7
    print('请支付', c ,'圆')
elif 800 < score:
    c = score * 0.6
    print('请支付', c ,'圆')
else:
    print('请输入正确的金额')