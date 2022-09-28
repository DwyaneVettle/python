# author by Michealzou@126.com
# 2022/9/28 11:36
"""
    2.已知：加速度、初速度、时间
    求：距离
    加速度=(距离-初速度*时间)*2 / 时间平方
    距离=加速度*时间平方 *0.5  + 初速度*时间
"""
plus_speed = int(input("请输入加速度："))
init_speed = int(input("请输入初速度："))
time = int(input(input("请输入时间：")))
# 做运算是数值在做
distance = plus_speed * time**2 * 0.5 + init_speed * time
print(f"距离为{distance}")
