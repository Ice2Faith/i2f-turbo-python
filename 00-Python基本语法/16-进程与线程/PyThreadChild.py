#-*-coding:gbk-*-
import os
import time
from threading import Thread
'''
�߳����࣬�߳�֮������˳���޹�
��дrun����
'''
class MyThread(Thread):
	def run(self):
		for i in range(3):
			time.sleep(1)
			msg='ChildThread'+self.name+'Process,i='+str(i)
			print(msg)
	
def main():
	print('Main Thread Begin')
	t1=MyThread()
	t2=MyThread()
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('Main Thread Begin')

if __name__=='__main__':
	main()