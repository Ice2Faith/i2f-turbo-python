#-*-coding:gbk-*-
from multiprocessing import Process 
import time
import os
'''
ֱ��ʹ�÷�ʽʹ�ý���
'''
def test(stime):
	tbegin=time.time()
	print('�ӽ��̣�%s����ʼִ�У����ĸ������ǣ�%s��'%(os.getpid(),os.getppid()))
	time.sleep(stime)#��ʱ�������룩
	tend=time.time()
	print('�����ӽ���(%s)ִ��ʱ��Ϊ%0.2f��'%(os.getpid(),tend-tbegin))

def test1(stime):
	tbegin=time.time()
	print('�ӽ��̣�%s����ʼִ�У����ĸ������ǣ�%s��'%(os.getpid(),os.getppid()))
	time.sleep(stime)#��ʱ�������룩
	tend=time.time()
	print('�����ӽ���(%s)ִ��ʱ��Ϊ%0.2f��'%(os.getpid(),tend-tbegin))

def main():
	print('�����̿�ʼ��%s'%os.name)
	p=Process(target=test,args=(1,))#����Ϊtest������Ĳ���ΪԪ��1
	p1=Process(target=test1,name='test1',args=(2,))
	p.start()
	p1.start()
	print('p is_alive:',p.is_alive())
	print('p1 is_alive:',p1.is_alive())
	print('p name:',p.name)
	print('p1 name:',p1.name)
	print('p pid:',p.pid)
	print('p1 pid:',p1.pid)
	p.join()
	p1.join()#�������߳�
	print('�����̽���')
	#�Ƿ������� p.is_alive()
	#�ȴ����н��� p.join()
	#û��target����ʱ���ö����run���� p.run()
	#ǿ����ֹ���� p.terminate()
	#name���� p.name
	#pid���� p.pid

if __name__=='__main__':
	main()