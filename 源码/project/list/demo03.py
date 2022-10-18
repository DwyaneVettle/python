# author by Michealzou@126.com
# 2022/10/17 22:36
list01 = [9, 25, 12, 8]
# for item in list01:
#     if item > 10:
#         list01.remove(item)

#3 2  1 0
#-1 -2 -3 -4
for i in range(len(list01)-1,-1,-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)