#-*-coding:gbk-*-
import os
import time
from threading import Thread,Lock
'''
����-������
threading.Lock():������
mutex=threading.Lock():������
mutex.acquire([blocking]):����
mutex.release():�ͷ���
'''
n=100
mutex=None
def task():
	global n
	mutex.acquire()
	time.sleep(0.1)
	n-=1
	print('Shop Success,stay %d tickets'%n)
	mutex.release()


def main():
	print('���߳̿�ʼ��%s'%os.getpid())
	global mutex
	mutex=Lock()
	tlist=[]
	for i in range(10):
		t=Thread(target=task)
		tlist.append(t)
		t.start()
	for t in tlist:
		t.join()
	print('���߳̽���')

if __name__=='__main__':
	main()