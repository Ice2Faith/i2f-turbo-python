#-*-coding:gbk-*-
import os
import time
from multiprocessing import Process
from multiprocessing import Queue

'''
����֮���Queue��ʽͨ��
empty:�ж��Ƿ�Ϊ��
get([block[,timeout]]):��ȡ��Ϣ���е�һ����Ϣ��Ȼ���Ƴ���Ϣ��blockĬ��ΪTrue
get_nowait():�൱��get(Flase)
put(item[,block[,timeout]]):item��ʶ�������Ϣ
put_nowait(item):�൱��put(item,Flase)
full���Ƿ�����
qsize:������Ϣ����
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
	print('�����̿�ʼ��%s'%os.getpid())
	#QueueBegin()
	q=Queue()
	pw=Process(target=writetask,args=(q,))
	pr=Process(target=readtask,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.join()
	print('�����̽���')

if __name__=='__main__':
	main()