# author by Michealzou@126.com
# 2022/5/9 13:35
import os
#通过递归调用一层层获取
def getAllSub2(path, dirlist=[], filelist=[]):
    # 返回指定的文件夹包含的文件或文件夹的名字的列表
    flist = os.listdir(path)
    for filename in flist:
        # 将多个路径组合后返回
        subpath = os.path.join(path, filename)
        # 判断路径是否为目录
        if os.path.isdir(subpath):
            dirlist.append(subpath)		# 如果是文件夹，添加到文件夹列表中
            getAllSub2(subpath, dirlist, filelist)	# 向子文件内递归
        # 判断路径是否为文件
        if os.path.isfile(subpath):
            filelist.append(subpath)	# 如果是文件，添加到文件列表中
    return dirlist, filelist


if __name__ == "__main__":
    path = r'D:\笔记\Python'
    Dirlist, Filelist = getAllSub2(path)
    print(Dirlist)
    print(Filelist)
