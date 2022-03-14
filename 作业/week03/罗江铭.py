# author by Michealzou@126.com
# 2022/3/14 9:26
money = float(input('请输入你的金额:'))
if 1 < money < 100 :
    print('不打折，付款金额为:',money*1)
elif  100 <= money <=1000:
    print('打九折，付款金额为:',money*0.9)
elif   1001 <= money <=3000 :
    print('打七五折，付款金额为',money*0.75)
elif 3001 <= money <= 5000:
    print('打六折，付款金额为', money * 0.6)
elif 5001 <= money :
    print('打三折，付款金额为', money * 0.3)
else :
    print('请输入正确的金额')

