#-*-coding:gbk-*-
import os
import time
from threading import Thread
'''
�߳�֮���ͨ��
�߳�֮�����ֱ�ӽ���ͨ�ţ����ݹ���
�����Ҫ���м���
threading.Lock():������
'''
gnum=100
def plus():
	print('���߳�1��ʼ')
	global gnum#ȫ�ֱ�������
	gnum+=50
	print('gnum is %d'%gnum)
	print('���߳�1����')

def minus():
	print('���߳�2��ʼ')
	global gnum
	gnum-=50
	print('gnum is %d'%gnum)
	print('���߳�2����')

def Commu():
	p1=Thread(target=plus)
	p2=Thread(target=minus)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	
def main():
	print('���߳̿�ʼ��%s'%os.getpid())
	#Commu()
	print('���߳̽���')

if __name__=='__main__':
	main()