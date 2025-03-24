"""
    单分支：
        if 条件表达式：
            代码块
        当条件表达式返回True时就执行代码块，如果为False就不执行

java : if(条件表达式){ 代码块 }
"""
grade = int(input("请输入成绩："))
if grade >= 90:
    print("优秀")
if grade < 60:
    print("不及格")
