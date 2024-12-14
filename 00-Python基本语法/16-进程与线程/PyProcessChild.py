#-*-coding:gbk-*-
import os
import time
from multiprocessing import Process
'''
ʹ�ü̳з�ʽ���н���
'''
class MyProcess(Process):
	def __init__(self,ctime,name='test'):
		super(MyProcess,self).__init__()#Process.__init__(self)
		self.ctime=ctime
		self.name=name
	def run(self):#��Ҫ�˷������ܵ���start������start�������Զ�����run����
		tbegin=time.time()
		print('�ӽ��̣�%s����ʼִ�У����ĸ������ǣ�%s��'%(os.getpid(),os.getppid()))
		time.sleep(self.ctime)#��ʱ�������룩
		tend=time.time()
		print('�����ӽ���(%s)ִ��ʱ��Ϊ%0.2f��'%(os.getpid(),tend-tbegin))

	
def main():
	print('�����̿�ʼ��%s'%os.name)
	p=MyProcess(ctime=1,name='test1')
	p1=MyProcess(ctime=2)
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

if __name__=='__main__':
	main()