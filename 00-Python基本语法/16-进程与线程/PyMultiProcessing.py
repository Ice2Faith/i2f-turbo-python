#-*-coding:gbk-*-
from multiprocessing import Process 
import time
import os
'''
直接使用方式使用进程
'''
def test(stime):
	tbegin=time.time()
	print('子进程（%s）开始执行，他的父进程是（%s）'%(os.getpid(),os.getppid()))
	time.sleep(stime)#延时函数（秒）
	tend=time.time()
	print('我是子进程(%s)执行时间为%0.2f秒'%(os.getpid(),tend-tbegin))

def test1(stime):
	tbegin=time.time()
	print('子进程（%s）开始执行，他的父进程是（%s）'%(os.getpid(),os.getppid()))
	time.sleep(stime)#延时函数（秒）
	tend=time.time()
	print('我是子进程(%s)执行时间为%0.2f秒'%(os.getpid(),tend-tbegin))

def main():
	print('主进程开始：%s'%os.name)
	p=Process(target=test,args=(1,))#任务为test，任务的参数为元组1
	p1=Process(target=test1,name='test1',args=(2,))
	p.start()
	p1.start()
	print('p is_alive:',p.is_alive())
	print('p1 is_alive:',p1.is_alive())
	print('p name:',p.name)
	print('p1 name:',p1.name)
	print('p pid:',p.pid)
	print('p1 pid:',p1.pid)
	p.join()
	p1.join()#加入主线程
	print('主进程结束')
	#是否还在运行 p.is_alive()
	#等待运行结束 p.join()
	#没有target参数时调用对象的run方法 p.run()
	#强制终止进程 p.terminate()
	#name属性 p.name
	#pid属性 p.pid

if __name__=='__main__':
	main()