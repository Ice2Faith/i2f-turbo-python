#-*-coding:gbk-*-
import sys
import os

def getUserName():
	filename='rem.data'
	try:
		with open(filename,'r') as fp:
			username=fp.read()
	except FileNotFoundError:
		return None
	else:
		return username

def putUserName():
	uname=input('�������û���:')
	filename='rem.data'
	with open(filename,'w') as fp:
		fp.write(uname)
	return uname

def userLogin():
	uname=getUserName()
	if uname==None:
		uname=putUserName()
	print('��ӭ %s ��½'%uname)

def main():
	print('mylogin')
	userLogin()

if __name__=='__main__':
	main()
