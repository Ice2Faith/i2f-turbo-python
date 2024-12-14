#-*-coding:gbk-*-
import os
import time
#from multiprocessing import Process
from multiprocessing import Pool
'''
Pool类：
apply_async(func[,args[,kwds]]):使用非阻塞方式（并行执行）调用func函数
apply(func[,args[,kwds]]):使用阻塞方式调用
close():关闭Pool不在接受新进程
terminate():立终止
join():主进程阻塞，等待子进程结束，必须在close或terminate之后调用
'''
def task(i):
	print('子进程(%s)执行任务(%s)'%(os.getpid(),i))
	time.sleep(1)

def main():
	print('主进程开始：%s'%os.getpid())
	p=Pool(3)
	for i in range(10):
		p.apply_async(task,args=(i,))
	p.close()
	p.join()
	print('主进程结束')

if __name__=='__main__':
	main()