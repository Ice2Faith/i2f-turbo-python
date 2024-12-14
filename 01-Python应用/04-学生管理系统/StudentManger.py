#-*-coding:gbk-*-
import os
def StudentManger():
	uname=userLogin()
	if uname==None:
		return
	studb=[]
	loadFileInfo(studb)
	while True:
		sel=Menu()
		if sel==0:
			writeFileInfo(studb)
			return
		elif sel==1:
			displayAllStudent(studb)
		elif sel==2:
			addStudent(studb)
		elif sel==3:
			modifyStudentInfo(studb)
		elif sel==4:
			deleteStudent(studb)
			
	
def Menu():
	print('<<<< StudentManger >>>>')
	print('-'*20)
	print('1.查看已有学生')
	print('2.增加学生')
	print('3.修改信息')
	print('4.删除学生')
	print('0.退出程序')
	print('-'*20)
	sel=-1
	while sel<0 or sel>4 :
		sel=int(input('请选择：'))
	return sel

def getUserInfo():
	filename='rem.data'
	try:
		with open(filename,'r') as fp:
			username=fp.read()
	except FileNotFoundError:
		return None
	else:
		return username

def putUserInfo():
	uname=input('请输入用户名:')
	upass=input('请输入密码：')
	uinfo=uname+'\t'+upass
	filename='rem.data'
	with open(filename,'w') as fp:
		fp.write(uinfo)
	return uinfo

def userLogin():
	uinfo=getUserInfo()
	if uinfo==None:
		uinfo=putUserInfo()
	ui=uinfo.split('\t')
	print('欢迎 %s 登陆'%ui[0])
	iup=input('请输入登陆密码：')
	if ui[1] != iup:
		return None
	return ui[0]
	
	
def loadFileInfo(studb):
	fp=None
	try:
		fp=open('studb.db','r')
		filelines=fp.read().splitlines()
		for line in filelines:
			fomatline=line.split('\t')
			stu={}
			stu['name']=fomatline[0]
			stu['age']=int(fomatline[1])
			stu['sex']=fomatline[2]
			stu['tel']=fomatline[3]
			studb.append(stu)
	except FileNotFoundError:
		pass
	finally:
		if fp:
			fp.close()
	
def writeFileInfo(studb):
	fp=open('studb.db','w')
	for stu in studb:
		fp.write('%s\t%d\t%s\t%s\n'%(stu['name'],stu['age'],stu['sex'],stu['tel']))
	fp.close()
	
def displayAllStudent(studb):
	print('-'*5,'All Students','-'*5)
	print('NO\t\tName\t\tAge\t\tSex\t\tTel')
	for index,stu in enumerate(studb):
		showStudentofIndex(stu,index)

def showStudentofIndex(stu,index):
	print('%d\t\t%s\t\t%d\t\t%s\t\t%s'%(index,stu['name'],stu['age'],stu['sex'],stu['tel']))
			
	
def addStudent(studb):
	stu={}
	sname=input('请输入姓名：')
	sage=int(input('请输入年龄：'))
	sexTable=['男','女']
	isex=''
	while isex not in [0,1]:
		isex=int(input('请选择性别：0：男 1：女：'))
	ssex=sexTable[isex]
	stel=input('请输入联系电话：')
	stu['name']=sname
	stu['age']=sage
	stu['sex']=ssex
	stu['tel']=stel
	studb.append(stu)
	
def modifyStudentInfo(studb):
	index=-1
	while index <0 or index>=len(studb):
		index=int(input('请输入修改信息的学生序号：'))
	showStudentofIndex(studb[index],index)
	
	sname=input('请输入新姓名：')
	sage=int(input('请输入新年龄：'))
	sexTable=['男','女']
	isex=''
	while isex not in [0,1]:
		isex=int(input('请选择新性别：0：男 1：女：'))
	ssex=sexTable[isex]
	stel=input('请输入联系电话：')
	
	sel=input('输入1确认修改，否则撤销')
	if sel=='1':
		studb[index]['name']=sname
		studb[index]['age']=sage
		studb[index]['sex']=ssex
		studb[index]['tel']=stel
		print('学生信息已修改')
	else:
		print('信息修改已撤销')
	
def deleteStudent(studb):
	index=-1
	while index <0 or index>=len(studb):
		index=int(input('请输入删除信息的学生序号：'))
	print('即将删除学生：')
	showStudentofIndex(studb[index],index)
	sel=input('输入1确认删除，否则撤销')
	if sel=='1':
		del studb[index]
		print('学生已删除')
	else:
		print('删除已撤销')

def main():
	StudentManger()

if __name__=='__main__':
	main()
