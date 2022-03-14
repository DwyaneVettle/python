# @Time : 2022/3/13 21:51
score = float(input('请输入金额：'))
if 1 < score < 100:
    c = score * 1
    print('折后金额为', c)
elif 100 <= score <= 1001:
    c = score*0.95
    print('折后金额为', c)
elif 1001 <= score <= 3000:
    c = score*0.9
    print('折后金额为', c)
elif 3001 <= score <= 5000:
    c = score*0.8
    print('折后金额为', c)
elif 5001 <= score:
    c = score*0.8
    print('折后金额为', c)
else:
    print('请输入正确的金额')