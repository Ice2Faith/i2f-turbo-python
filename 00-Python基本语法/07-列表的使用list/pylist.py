#-*-coding:gbk-*-
import sys
import os
'''
list �б�����

'''

def baseList():
	'''
	list�Ļ����÷�
	'''
	a=[] #�õ�һ�����б�
	a=[1,2.5,'hello',[1,1,2],(3,4,5)] #�õ�һ����ͨ�б��б���Դ���������ͣ�������Ƕ��
	print(a)
	a=a[0:len(a):2] #ȡ���б��е�ż����γ�һ���µ��б�
	print(a)
	print(a[2]) #ȡ��һ���±�Ԫ��
	b=a+[10,10,10] #�����б����γ�һ���µ��б���
	print(b)
	b=a*2 #�ظ��б��൱�ڸ��Ƽ���������ȥ�����γ�һ���µ��б���
	print(b)
	a=[11,12]
	a.append([13,14]) #���б������һ����Ԫ�أ�����ʲôֻ����һ��Ԫ�ؼӽ�ȥ
	print(a)
	a.extend([13,14]) #��һ���б�׷�ӵ�ԭ�б��У������һ���б������ӳ��б�
	print(a)
	a.insert(2,'hello') #����ָ��λ��һ��Ԫ�أ�ָ��ֵ����֮����±�������ԭ���ĺ���
	print(a)
	# ��ȡԪ���±�index()��������Ԫ��[����ʼ�±�[�������±�]]
	print(a.index('hello')) #��ȡָ��Ԫ�صĵ�һ���±�
	print(a.index('hello',2)) #��ȡ���±�2��ʼ�ĵ�һ�������ֵ��±�
	print(a.index('hello',2,4)) #��ȡָ��Ԫ����ĳ���±�������±�
	# ͳ��Ԫ�س��ֵĴ���
	print(a.count(13)) # ע�⣬����ͳ�����б���Ϊ���б��൱��һ��Ԫ��
	# �ж�Ԫ���Ƿ�������
	print(14 in a)
	#�б��ɾ��
	del a[2] #ɾ���±�Ԫ��
	a.remove(13) #ɾ����һ�γ��ֵ�Ԫ�أ���������ڻᱨ��
	a.pop() #ȡ�����һ��Ԫ��
	print(a)
	# �޸�Ԫ��ֵ
	a[0]='hello'
	print(a)
	del a #ɾ�������б�
	del b

def usualFunc():
	'''
	list���ú���
	'''
	a=[11,12]
	b=[12,13]
	# print(cmp(a,b)) #py2��ʹ�÷�ʽ����������ֵ��ʶ��С
	print(a>b) #py3�ıȽϷ�ʽ���ַ��������ַ�����Ƚ�
	print(len(a)) #��ȡ�б�ĳ��ȣ�ʵ�������б�����ú��������ñ���__len__,�����������»��߱�ʶ�ģ�private���ɷ���
	print(max(a)) # ��ȡԪ�ص����ֵ�����ǣ��б�Ԫ��������Ҫһ�£�����ʧ��
	print(sum(a)) #�б���ͣ����ǲ��������ַ�����sum(a,12),�⽫���ټ���һ��12
	print(sorted(a)) #����һ���б�ֻ����ͬһ���ͣ�Ĭ���������򣬲��ı�Դ�б�˳��ʹ�ò�����reverse=True�ı�Ϊ��������
	a.sort() #���õ����򷽷����Ḳ��ԭ�б�ͬ��Ҳ��reverse����
	a.reverse() #��ת�б�Ԫ��
	# ��ת����
	matrix=[[1,2,3,4],[5,6,7,8],[3,10,11,12]]
	tmatrix=[]
	for j in range(4):
		tmatrix.append([row[j] for row in matrix])
	print(tmatrix)


import random
def test():
	'''
	8��ѧ�����������������
	'''
	stus=['stu'+str(i) for i in range(8)]
	clas=[[] for i in range(3)]
	for i in stus:
		clas[random.randint(0,2)].extend([i])
	print(clas)
	

def test2():
	'''
	��6��ѧ��ƽ�����䵽�����༶
	'''
	stus=['stu'+str(i) for i in range(6)]
	avgclas=[[] for i in range(3)]
	for i in stus:
		ri=random.randint(0,2)
		while len(avgclas[ri])>=2:
			ri=random.randint(0,2)
		avgclas[ri].append(i)
	print(avgclas)
	
def proveList():
	'''
	list���б��Ƶ�ʽ
	'''
	a=[i**2 for i in range(100)] #�б��Ƶ�ʽ�����磺�Ƶ��� ѭ������
	print(a)
	
import time
def IDParse(id):
	list_id=['350100','������','350101','��Ͻ��',
        '350102','��¥��',
        '350103','̨����',
        '350104', '��ɽ��',
        '350105', '��β��',
        '350111', '������',
        '350121', '������',
        '350122', '������',
        '350123', '��Դ��',
        '350124', '������',
        '350125', '��̩��',
        '350128', 'ƽ̶��',
        '350181', '������',
        '350182', '������']
	city=id[0:6]
	index=list_id.index(city)
	if index<0:
		print('�ó�����δ֧��')
	else:
		print(list_id[index+1])
		tm=time.localtime(time.time())
		print('%d����'%(tm.tm_year-int(id[6:10])))
		print('��������:%s-%s-%s'%(id[6:10],id[10:12],id[12:14]))
		
def main():
	test()
	test2()
	print('list�б��ʹ��')
	baseList()
	usualFunc()
	proveList()
	IDParse(input('���������֤�ţ�'))

if __name__=='__main__':
	main()
