#-*-coding:gbk-*-
import os
import time
import random
from threading import Thread
from queue import Queue
'''
线程之间通过Queue通信
生产者消费者解决方案
'''
class Producer(Thread):
	def __init__(self,name,queue):
		Thread.__init__(self,name=name)
		self.data=queue
	def run(self):
		for i in range(5):
			print('Producer %s product %d into queue'%(self.getName(),i))
			self.data.put(i)
			time.sleep(random.random())
		print('Product End!')
class Consumer(Thread):
	def __init__(self,name,queue):
		Thread.__init__(self,name=name)
		self.data=queue
	def run(self):
		for i in range(5):
			val=self.data.get()
			print('Consumer %s consume %d from queue'%(self.getName(),val))
			time.sleep(random.random())
	print('Consume End!')
def main():
	print('主线程开始：%s'%os.getpid())
	queue=Queue()
	producer=Producer('Producer',queue)
	consumer=Consumer('Consumer',queue)
	producer.start()
	consumer.start()
	producer.join()
	consumer.join()
	print('主线程结束')

if __name__=='__main__':
	main()