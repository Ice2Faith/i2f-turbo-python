#-*-coding:gbk-*-
import os
import time
from multiprocessing import Process

'''
����֮�䲢���ܹ��ù�����Ϣ������֮���໥����
����֮��ͨ����Ҫ���к͹ܵ����и���
'''
gnum=100#ȫ�ֱ���

def plus():
	print('�ӽ���1��ʼ')
	global gnum#ȫ�ֱ�������
	gnum+=50
	print('gnum is %d'%gnum)
	print('�ӽ���1����')

def minus():
	print('�ӽ���2��ʼ')
	global gnum
	gnum-=50
	print('gnum is %d'%gnum)
	print('�ӽ���2����')

def main():
	print('�����̿�ʼ��%s'%os.getpid())
	p1=Process(target=plus)
	p2=Process(target=minus)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print('�����̽���')

if __name__=='__main__':
	main()