count=0
while count<100:
    count+=1
    if int(count/5)!=count/5:
        continue     #满足条件重新判断
    print(count, end =" ")
