n=input("请输入学生成绩：")
if int(n)>=90:
    print("成绩"+n+"：优秀")
elif 60<=int(n)<90:
    print("成绩"+n+"：通过")
else:
    print("成绩"+n+"：末通过")
