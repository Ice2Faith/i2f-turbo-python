#-*-coding:gbk-*-
import os
import time
from multiprocessing import Process
from multiprocessing import Queue

'''
进程之间的Queue方式通信
empty:判断是否为空
get([block[,timeout]]):获取消息队列的一条消息，然后移除消息，block默认为True
get_nowait():相当于get(Flase)
put(item[,block[,timeout]]):item标识放入的消息
put_nowait(item):相当于put(item,Flase)
full：是否已满
qsize:返回消息数量
'''
def QueueBegin():
	q=Queue(3)
	q.put('Msg1')
	q.put('Msg2')
	print('Is full:%s'%q.full())
	q.put('Msg3')
	print('Is full:%s'%q.full())
	try:
		q.put('Msg4',True,2)
	except:
		print('Msg is full %s',q.qsize())
	if not q.empty():
		print('Get mes:')
		for i in range(q.qsize()):
			print(q.get_nowait())
	if not q.full():
		q.put('Msg4')
		
def writetask(q):
	if not q.full():
		for i in range(5):
			q.put('Msg'+str(i))
			print('WMsg:'+'Msg'+str(i))
			
def readtask(q):
	time.sleep(1)
	while not q.empty():
		print('RMsg:',q.get(True,2))
def main():
	print('主进程开始：%s'%os.getpid())
	#QueueBegin()
	q=Queue()
	pw=Process(target=writetask,args=(q,))
	pr=Process(target=readtask,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.join()
	print('主进程结束')

if __name__=='__main__':
	main()