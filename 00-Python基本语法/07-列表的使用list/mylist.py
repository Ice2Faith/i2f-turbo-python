# -- coding: gbk --
import random
#�б�
# ��ֵ
llist=['����',12,125.13,['aaa',12]]
# ȡֵ����Ƭ�����䡾1��3���ϣ�ÿ���Ϊ2��ֵȡ��
pl=llist[1:3:2]
del llist
#���б�
list=[]
list+=['����']
list.append(2019)
list+=[7]
list+=[17]
list.append('�б�Ĳ���')
#�����б�
for item in list:
	print(item,end='\t')
print()
#��������ʽ�����б�
for index,item in enumerate(list):
	print(str(index)+'\t'+str(item))
list2=['hello',2019,'welcome','python']
#�����б�
list.extend(list2)
print(list)
#�޸��б�Ԫ��
list[0]='�б����'
print(list)
#ɾ���б�Ԫ��
#����λ��
del list[-1]
print(list)
#����ֵ����ҪΨһ
list.remove('welcome')
print(list)
#����ָ��λ��һ��ֵ
list.insert(-1,'python')
print(list)
#ͳ�Ƴ��ִ���
print(str(list.count(2019)))
#��ѯ�״��±�
print(str(list.index(2019)))
#���
listint=[5,12,7,6,13,15,24,37,3]
print('Sum='+str(sum(listint,0)))
#����
print('ԭ�����У�',listint)
listint.sort(reverse=True)
print('�������У�',listint)
liststr=['Cat','Animal','Dog','Brid','alter']
print('ԭ�����У�',liststr)
#�����ִ�Сд����
liststr.sort(key=str.lower,reverse=False)
print('�������У�',liststr)
#���򲢴������б�
liststr2=['Cat','Animal','Dog','Brid','alter']
print('ԭ�����У�',liststr2)
listsorted=sorted(liststr2,key=str.lower,reverse=False)
print('�������У�',listsorted)
#�б��Ƶ�ʽ--���������б�
listcreate=[str('new_'+item) for item in liststr2]
print('New List:',listcreate)

randomnumber=[random.randint(0,100) for i in range(10)]
print('Random Number:',randomnumber)
#��ά�б�
arr=[]
for i in range(1,5):
	arr.append([])	#Ϊ�ڲ㴴�����б�
	for j in range(1,5):
		arr[i-1].append(i*j)
print(arr)
#�б��ɾ��
del list
del list2
del listcreate
del listint
del listsorted
del liststr
del liststr2