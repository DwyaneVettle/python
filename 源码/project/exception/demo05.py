# author by Michealzou@126.com
# 2022/5/24 11:37
# 计算正方形面积演示异常的传递
# 计算边长
def get_width():
    print("get_width()开始执行了。。。")
    num = int(input("请输入除数："))
    # 发生异常
    width_len = 10/num
    print("get_width()执行结束。。。")
    return width_len
# 计算正方形面积
def calc_area():
    print("calc_area()开始执行。。。")
    width_len = get_width()
    print("calc_area()结束执行。。。")
    return width_len * width_len
# 展示数据
def show_area():
    try:
        print("show_area()开始执行。。。")
        area_val = calc_area()
        print(f"正方形的面积是：{area_val}")
        print("show_area()结束执行。。。")
    except ZeroDivisionError as e:
        print(f"捕获异常{e}")

if __name__ == '__main__':
    show_area()
