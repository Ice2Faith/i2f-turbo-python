#-*-coding:gbk-*-
import os
import time
from threading import Thread
'''
线程之间的通信
线程之间可以直接进行通信，数据共享，
因此需要进行加锁
threading.Lock():互斥锁
'''
gnum=100
def plus():
	print('子线程1开始')
	global gnum#全局变量声明
	gnum+=50
	print('gnum is %d'%gnum)
	print('子线程1结束')

def minus():
	print('子线程2开始')
	global gnum
	gnum-=50
	print('gnum is %d'%gnum)
	print('子线程2结束')

def Commu():
	p1=Thread(target=plus)
	p2=Thread(target=minus)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	
def main():
	print('主线程开始：%s'%os.getpid())
	#Commu()
	print('主线程结束')

if __name__=='__main__':
	main()