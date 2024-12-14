#-*-coding:gbk-*-
import os
import time
from multiprocessing import Process
'''
使用继承方式运行进程
'''
class MyProcess(Process):
	def __init__(self,ctime,name='test'):
		super(MyProcess,self).__init__()#Process.__init__(self)
		self.ctime=ctime
		self.name=name
	def run(self):#需要此方法才能调用start方法，start方法会自动运行run方法
		tbegin=time.time()
		print('子进程（%s）开始执行，他的父进程是（%s）'%(os.getpid(),os.getppid()))
		time.sleep(self.ctime)#延时函数（秒）
		tend=time.time()
		print('我是子进程(%s)执行时间为%0.2f秒'%(os.getpid(),tend-tbegin))

	
def main():
	print('主进程开始：%s'%os.name)
	p=MyProcess(ctime=1,name='test1')
	p1=MyProcess(ctime=2)
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

if __name__=='__main__':
	main()