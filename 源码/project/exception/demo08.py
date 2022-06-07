# author by Michealzou@126.com
# 2022/5/31 8:43
class FileTypeError(Exception):

    def __init__(self,err = "仅支持jpg/png/gif格式的图片"):
        super().__init__(err)

flie_name = input("请上传图片：")
try:
    if flie_name.split(".")[1] in ["jpg","png","gif"]:
        print("上传成功")
    else:
        raise  FileTypeError()
except FileTypeError as e:
    print(e)