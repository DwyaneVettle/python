# author by Michealzou@126.com
# 2022/8/5 10:26
# 5.2
has_ticket = True  # 默认有票
knife_length = 25.5  # 刀的长度
if has_ticket:

# ********** Begin *********

    # 首次检票通过，继续进行下一个安检
    if knife_length > 20:
        print('您的刀长为%.1fcm，超过20cm，不允许上车' %(knife_length))
    else:
        print('恭喜，安检通过')
else:
        print('您没有车票，不允许进门')
