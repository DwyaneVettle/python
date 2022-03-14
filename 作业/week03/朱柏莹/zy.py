# @Time : 2022/3/13 21:48
l = []
for i in range(100,1000,1):
    t = str(i)
    if i == (int(t[0])**3+int(t[1])**3+int(t[2])**3):
        l.append(i)
        print(l)