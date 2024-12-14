#-*-coding:gbk-*-
import os
import time
from threading import Thread,Lock
'''
加锁-互斥锁
threading.Lock():互斥锁
mutex=threading.Lock():创建锁
mutex.acquire([blocking]):锁定
mutex.release():释放锁
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
	print('主线程开始：%s'%os.getpid())
	global mutex
	mutex=Lock()
	tlist=[]
	for i in range(10):
		t=Thread(target=task)
		tlist.append(t)
		t.start()
	for t in tlist:
		t.join()
	print('主线程结束')

if __name__=='__main__':
	main()