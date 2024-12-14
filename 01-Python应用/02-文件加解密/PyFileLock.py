#-*-coding:utf-8-*-
helpinfo='''-----------------------
	PyFileLock
	Copyright@Ice2Faith-2019
this model is a simple file lock tool
you need give it working mode,sourcename,directname,password
mode: lock/unlock
other:
	you can pull a file to PyFileLock.py icon to boot
	or,cmd:PyFileLock.py [mode] [sourcename] [newname] [password]
-----------------------'''
import sys
import struct

def PyMain():
	if(len(sys.argv)==1):
		print(helpinfo)
		sourcename=str(input('please input source name:'))
		mode=str(input('Please input mode:'))
		newname=str(input('please input new name:'))
		password=str(input('please input your password:'))
		if(0==FileLock(mode,sourcename,newname,password)):
			print('Success!!Run End!!')
		else:
			print('Some Error raise!')
	elif(len(sys.argv)<1+4):
		print('Load File:',sys.argv[1])
		mode=str(input('Please input mode:'))
		newname=str(input('please input new name:'))
		password=str(input('please input your password:'))
		if(0==FileLock(mode,sys.argv[1],newname,password)):
			print('Success!!Run End!!')
		else:
			print('Some Error raise!')
	else:
		if(0==FileLock(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])):
			print('Success!!Run End!!')
		else:
			print('Some Error raise!')
	
	
def InLock(bytearray,len):
	pindex=0
	while(pindex<len):
		bytearray[pindex]=bytearray[pindex]^(0x51+pindex)
		pindex=pindex+1
	return bytearray
	
def FileLock(mode,filename,newfilename,password):
	#File Flag
	FFlag='I2FFL_2019'
	FFlagbytes=bytearray(FFlag.encode('utf-8'))
	FFlaglen=len(FFlagbytes)
	FFlagbytes=InLock(FFlagbytes,FFlaglen)
	#File Password
	password=password+'_I2FL_2019'
	passbytes=bytearray(password.encode('utf-8'))
	passlen=len(passbytes)
	passbytes=InLock(passbytes,passlen)
	if(mode.upper()=='LOCK'):
		#read File Context
		fin=open(filename,'rb')
		filecontext=fin.read()
		filesize=fin.tell()
		fin.close()
		filecontextbytes=bytearray(filecontext)
		#Lock File Context
		index=0
		passindex=0
		while(index<filesize):
			filecontextbytes[index]=filecontextbytes[index]^passbytes[passindex]
			index=index+1
			passindex=(passindex+1)%passlen
		#build save file
		fout=open(newfilename,'wb',)
		#Save Flag
		fout.write(FFlagbytes)
		#Save Passlen
		fout.write(struct.pack('i',passlen))
		#Save password
		fout.write(passbytes)
		#Save Locked Context
		fout.write(filecontextbytes)
		fout.close()
		return 0
	elif(mode.upper()=='UNLOCK'):
		#read File Context
		fin=open(filename,'rb')
		pfflag=fin.read(FFlaglen)
		if(pfflag==FFlagbytes):
			ppasslen=struct.unpack('i', fin.read(4))[0]
			ppassword=fin.read(ppasslen)
			if(ppassword==passbytes):
				filebegin=fin.tell()
				filecontext=fin.read()
				filesize=fin.tell()-filebegin
				fin.close()
				filecontextbytes=bytearray(filecontext)
				#Lock File Context
				index=0
				passindex=0
				while(index<filesize):
					filecontextbytes[index]=filecontextbytes[index]^passbytes[passindex]
					index=index+1
					passindex=(passindex+1)%passlen
				#build save file
				fout=open(newfilename,'wb',)
				#Save Locked Context
				fout.write(filecontextbytes)
				fout.close()
				return 0
			else:
				print('ERROR!!Your unlock password is not true')
				return -1
		else:
			print('ERROR!!This file not be locked')
			return -2
	else:
		print('ERROR!!Please set true mode')
		return -3
	
	
PyMain()