# -- coding: gbk --
#���ϣ�ע�⣬��Ȼ�����Ի����ű�ʶ������Ҫע��
ll={} #�⽫�õ�һ�����ֵ�
ll=set() #����ܵõ�һ���ռ���
#�����������ɾ��
set={0,1,2,5,4,2,6}
print(set)
set.clear()
del set
#�ռ��Ϻʹ���
set=set()
del set
set=set(['Ů�','�缧','������'])
print(set)
#��ɾԪ��
set.add('����')
if 'С��' in set:
	set.remove('С��')
	print('�Ƴ��ɹ�-','С��')
else:
	print('û���ҵ�')
#��|��&��-����ͶԳƲ^
set2={'�ݼ�','���Ѿ�','������'}
print('������',set|set2)
print('������',set&set2)
print('���',set-set2)
print('�ԳƲ��',set^set2)
