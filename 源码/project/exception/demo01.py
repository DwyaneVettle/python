# author by Michealzou@126.com
# 2022/5/24 10:05
# try...except语句
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"异常原因:{e}")

try:
    print(name)
    list01 = ["python", "java", "C", "C++"]
    print(list01[5])
except NameError as e:
    print(f"异常原因{e}")
except IndexError as e:
    print(f"异常原因{e}")


try:
    print(name)
    list01 = ["python", "java", "C", "C++"]
    print(list01[5])
except Exception as e:
    print(f"异常原因{e}")