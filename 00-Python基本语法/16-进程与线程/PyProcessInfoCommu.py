#-*-coding:gbk-*-
import os
import time
from multiprocessing import Process

'''
进程之间并不能共用公用信息，进程之间相互独立
进程之间通信需要队列和管道进行辅助
'''
gnum=100#全局变量

def plus():
	print('子进程1开始')
	global gnum#全局变量声明
	gnum+=50
	print('gnum is %d'%gnum)
	print('子进程1结束')

def minus():
	print('子进程2开始')
	global gnum
	gnum-=50
	print('gnum is %d'%gnum)
	print('子进程2结束')

def main():
	print('主进程开始：%s'%os.getpid())
	p1=Process(target=plus)
	p2=Process(target=minus)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print('主进程结束')

if __name__=='__main__':
	main()