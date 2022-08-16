# author by Michealzou@126.com
# 2022/8/8 11:33
#  1.高级可变参数 **params 会将参数封装到字典中
def show3(**params):
    print(params)

# 判断参数中是否有hobbys，如果有就用-拼接hobbys的内容
    if 'hobbys' in params:
        hobbys = params.get('hobbys')
        result = "-".join(hobbys)
        print(result)

show3(name="Jack", age=28, salary=8000.0, hobbys=['basketball', 'football'])
