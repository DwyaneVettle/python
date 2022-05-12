# author by Michealzou@126.com
# 2022/5/12 15:11
# 文件的复制
file_name = "test.txt"
source_file = open(file_name,"r",encoding="utf-8")
all_data = source_file.read()
flag = file_name.split(".")
new_file = open(flag[0] + '备份' + ".txt",'w',encoding="utf-8")
new_file.write(all_data)
source_file.close()
new_file.close()