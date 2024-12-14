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
	print('1.�鿴����ѧ��')
	print('2.����ѧ��')
	print('3.�޸���Ϣ')
	print('4.ɾ��ѧ��')
	print('0.�˳�����')
	print('-'*20)
	sel=-1
	while sel<0 or sel>4 :
		sel=int(input('��ѡ��'))
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
	uname=input('�������û���:')
	upass=input('���������룺')
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
	print('��ӭ %s ��½'%ui[0])
	iup=input('�������½���룺')
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
	sname=input('������������')
	sage=int(input('���������䣺'))
	sexTable=['��','Ů']
	isex=''
	while isex not in [0,1]:
		isex=int(input('��ѡ���Ա�0���� 1��Ů��'))
	ssex=sexTable[isex]
	stel=input('��������ϵ�绰��')
	stu['name']=sname
	stu['age']=sage
	stu['sex']=ssex
	stu['tel']=stel
	studb.append(stu)
	
def modifyStudentInfo(studb):
	index=-1
	while index <0 or index>=len(studb):
		index=int(input('�������޸���Ϣ��ѧ����ţ�'))
	showStudentofIndex(studb[index],index)
	
	sname=input('��������������')
	sage=int(input('�����������䣺'))
	sexTable=['��','Ů']
	isex=''
	while isex not in [0,1]:
		isex=int(input('��ѡ�����Ա�0���� 1��Ů��'))
	ssex=sexTable[isex]
	stel=input('��������ϵ�绰��')
	
	sel=input('����1ȷ���޸ģ�������')
	if sel=='1':
		studb[index]['name']=sname
		studb[index]['age']=sage
		studb[index]['sex']=ssex
		studb[index]['tel']=stel
		print('ѧ����Ϣ���޸�')
	else:
		print('��Ϣ�޸��ѳ���')
	
def deleteStudent(studb):
	index=-1
	while index <0 or index>=len(studb):
		index=int(input('������ɾ����Ϣ��ѧ����ţ�'))
	print('����ɾ��ѧ����')
	showStudentofIndex(studb[index],index)
	sel=input('����1ȷ��ɾ����������')
	if sel=='1':
		del studb[index]
		print('ѧ����ɾ��')
	else:
		print('ɾ���ѳ���')

def main():
	StudentManger()

if __name__=='__main__':
	main()
