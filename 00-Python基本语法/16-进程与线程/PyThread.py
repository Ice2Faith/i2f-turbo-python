#-*-coding:gbk-*-
import os
import time
import threading
'''
�߳�
Thread(group[,target[,name[,args[,kargs]]]])
'''
def thread():
	for i in range(3):
		time.sleep(1)
		print('Thread Name:%s'%threading.current_thread().name)

def main():
	print('Main Thread Begin')
	threads=[threading.Thread(target=thread) for i in range(4)]#�б�����ʽ
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	print('Main Thread Begin')

if __name__=='__main__':
	main()