#-*-coding:gbk-*-
import os
import time
#from multiprocessing import Process
from multiprocessing import Pool
'''
Pool�ࣺ
apply_async(func[,args[,kwds]]):ʹ�÷�������ʽ������ִ�У�����func����
apply(func[,args[,kwds]]):ʹ��������ʽ����
close():�ر�Pool���ڽ����½���
terminate():����ֹ
join():�������������ȴ��ӽ��̽�����������close��terminate֮�����
'''
def task(i):
	print('�ӽ���(%s)ִ������(%s)'%(os.getpid(),i))
	time.sleep(1)

def main():
	print('�����̿�ʼ��%s'%os.getpid())
	p=Pool(3)
	for i in range(10):
		p.apply_async(task,args=(i,))
	p.close()
	p.join()
	print('�����̽���')

if __name__=='__main__':
	main()