# author by Michealzou@126.com
# 2022/3/7 16:47
# 流程控制-判断if
money = 1000
jine = int(input('请输入取款金额：'))
if jine <= 1000:
    money = money - jine
    print(f'取款成功，取款金额为{jine},余额位为{money}')
else:
    print(f'取款失败，{jine}大于银行卡的余额')
