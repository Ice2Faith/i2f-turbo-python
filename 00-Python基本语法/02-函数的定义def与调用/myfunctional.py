# -- coding: gbk --
import os

'''
�����Ķ�����ʽ��
def ������([�����б�=Ĭ��ֵ]):
	������
	[return ����ֵ�б�]
����������Կ�����֧�ֶ�������������������
����ֵҲ�����ж���������ǿ���û�з���ֵ��
����Ҳ�ǿ�����Ĭ��ֵ�ģ�����Ĭ��ֵӦ���б����
��ѡ������ֵ����Ϊ���ַ���
����Ҳ�����ǿɱ䳤�Ĳ���*�ſ�ͷ������ȥ��Ϊ�б���ڣ�����ʱ��12,13,14
����*�ŵĲ�������ʶ��һ���䳤���ֵ䣬����ʱ��a=12,b=15
def func():
	a=12
def func(a,b,c):
	return a+b+c,(a+b+c)/3
def func(a,b,c=12):
	pass
def func(a,b,c=''):
	pass
def func(a,b,*args):
	for it in args:
		print(it)
'''
'''
�����ĵ��ã�
���԰��պ�����������Ĳ���λ�ý��е���
Ҳ����ͨ��������ָ���ļ�ֵʹ��
func(1,2,3)
func(a=1,c=3,b=2)
'''

def Command(mind):
	'''
	����ϵͳcmd������
	'''
	os.system(mind)

def getListMaxMin(ls):
	'''
	��ȡ�б�����ֵ����Сֵ
	'''
	if len(ls)==0:
		return None,None
	min=max=ls[0]
	for item in ls:
		if item>max:
			max=item
		if item<min:
			min=item
	return max,min
	
def getSumAvg(a,b):
	return a+b,(a+b)/2

def swap(a,b): #����ֵ����ʵPY��û��Ҫ����ʹ�ã�ֱ��a,b=b,a��������
	return b,a #���һ��ʹ�ü��ϵķ�ʽ�����������壬���ϴ��������ô���
	
def getUserInfo(map):
	while True:
		name=input('please input name(input q quit):')
		if name=='q':
			break
		age=int(input('please input %s\'s age:'%name))
		map[name]=age
'''
�����ĵݹ�
����������������Լ�
���ǣ�д�ݹ����Ҫ�г�������
'''
def MultiplySuper(number):
	'''
	�ݹ���׳�
	'''
	if number<=1 :
		return 1
	return number*MultiplySuper(number-1)
'''
����������
�����������ʹ����ȫ�ֱ�������ôҪ��ʹ��֮ǰ������ʹ����ȫ�ֱ���
�Ͼ�PY�ǲ���Ҫ��������ģ������������ֱ��ʹ�ã���ô�ͻ�ʹ�þֲ�����
x=10
def func():
	global x # ����ȫ�ֱ���
	x=20 # ����ͽ�ȫ�ֱ�����Ϊ20

def func():
	x=20 # �������һ���ֲ��������޸Ĳ���Ӱ��ȫ�ֱ���
'''
	
def main():
	#���ú���
	map={}
	getUserInfo(map)
	print(map)
	
	Command('color f1')
	Command('Pause')
	
	print(getListMaxMin((1,2,5,4,9,-2)))
	print(getSumAvg(b=3,a=5))
	
if __name__=='__main__':
	main()