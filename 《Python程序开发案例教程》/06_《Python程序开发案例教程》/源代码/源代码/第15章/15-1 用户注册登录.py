"""
1.创建表
create table py_users(
id int unsigned auto_increment not null primary key,
uname varchar(20) not null,
upwd char(40) not null,
is_delete bit not null default 0
);
"""
import pymysql
# 用户注册
def mysql_registered(conn,cur):
	# 1.获取有效用户名
	sql_select = 'select * from py_users where uname=%s'
	uname = input('用户名：')
	while True:
		# 执行sql语句
		params = [uname]
		result = cur.execute(sql_select,params)
		if result == 1:
			print('用户名已存在，请重新输入')
			uname = input('用户名：')
		else:
			break
	# 3.获取密码
	upwd = input('密  码：')
	# 4.插入数据库
	sql_insert = 'insert into py_users(uname,upwd) values(%s,%s)'
	params = [uname,upwd]
	result = cur.execute(sql_insert,params)
	conn.commit()
	# 5.插入结果判断
	if result == 1:
		print('注册成功')
	else:
		print('注册失败')
# 用户登录
def mysql_login(conn,cur):
	result = 0
	while not result:			
		uname = input('用户名：')
		sql = 'select upwd from py_users where uname=%s'
		params = [uname]
		result = cur.execute(sql,params)
		if result==1:			# 如果找到了用户
			mysql_upwd = cur.fetchone()
			while True:
				upwd = input('密码：')
				if upwd == mysql_upwd[0]:
					print('登录成功')
					break
				else:
					print('密码错误，请重新输入')
		else:
			print('用户名不存在')
# 打印菜单
def menu():
	print("----功能选择----")
	print("1.注册")
	print("2.登录")
# 主函数
def main():
	# 1.打印菜单
	menu()	
	# 2.连接数据库
	conn = pymysql.connect(host='localhost',port=3306,database='python',
		user='root',password='chan1121',charset='utf8')
	cur=conn.cursor()
	# 3.功能选择
	sel = input("注册（1）o登录（2）？")
	# 选择功能
	if sel == '1':
		mysql_registered(conn,cur)
	elif sel == '2':
		mysql_login(conn,cur)
	# 4.关闭数据库
	cur.close()
if __name__ == '__main__':
	main()