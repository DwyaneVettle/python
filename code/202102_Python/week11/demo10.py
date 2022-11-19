# author by Michealzou@126.com
# 2022/11/15 11:48
"""
    递归求当前电脑中指定目录及子目录
"""
import os
#通过递归调用一层层获取
def getAllSub2(path, dirlist=[], filelist=[]):
    flist = os.listdir(path)
    for filename in flist:
        subpath = os.path.join(path, filename)
        if os.path.isdir(subpath):
            dirlist.append(subpath)		# 如果是文件夹，添加到文件夹列表中
            getAllSub2(subpath, dirlist, filelist)	# 向子文件内递归
        if os.path.isfile(subpath):
            filelist.append(subpath)	# 如果是文件，添加到文件列表中
    return dirlist, filelist


if __name__ == "__main__":
    path = r'D:\笔记\Python'
    Dirlist, Filelist = getAllSub2(path)
    print(Dirlist)
    print(Filelist)