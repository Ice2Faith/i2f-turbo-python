# -- coding: gbk --
#�ֵ�
#����ɾ�������
#key:context(key����Ψһ)
dict={'qq':'30017862154','ID':'511401178712110100'}
print(dict)
dict.clear()
print(dict)
del dict
dict={}
del dict
dict=dict()
del dict
#ͨ��ӳ�亯��zip���б�Ԫ�鴴���ֵ�
tuple=(101,102,103,104,105)
list=['jack','mellen','alice','keyle','daivel']
dict=dict(zip(tuple,list))
print(dict)
del dict
del list
del tuple
#����ӳ�佨��
dict=dict(槼�='��ʦ','�ݼ�'='����')
print(dict)
del dict
#������ֵ�ֵ�
list=['槼�','���Ѿ�','��ɪ','����']
dict=dict.fromkeys(list)
# ����һ������Ĭ��ֵ���ֵ�
dict={}.fromkeys(list,'aaa')
print(dict)
del dict
del list
#��һ��Ԫ����Ϊ����һ���б���Ϊֵ
tuple=(101,102,103,104,105)
list=['jack','mellen','alice','keyle','daivel']
dict={tuple:list}
print(dict)
del dict
del list
del tuple
#�ֵ�ķ���
dict=dict(槼�='��ʦ','�ݼ�'='����')
print('槼��ǣ�',dict['槼�'] if '槼�' in dict else '槼�û�ҵ�')
print('�����ǣ�',dict.get('����','�Ҳ���')) #�Ҽ���ֵ���Ҳ������ø�����Ĭ�ϲ���
#����
for key in dict.keys(): #��������������sorted(dict.keys())��������֮�����
	print(dict[key])
for value in dict.values(): #����ֵ
	print(value)
for item in dict.items(): #������
	print(item)
for key,value in dict.items(): #��������ֿ���ֵ
	print('Key=',key,'Value=',value)
#��ɾ��
dict['����']='����' #�����ڼ������
print(dict)
dict['����']='��ʦ' #���ڼ��޸�
print(dict)
if '����' in dict: #�жϼ��Ƿ���� ����ʹ��not in dict.values()�ж�ֵ�Ƿ����
	del dict['����'] #ɾ��һ����ֵ
	dict.pop('����') #ɾ��һ����ֵ���᷵��ɾ���ļ���Ӧ��ֵ
	dict.popitem() #���ɾ��һ��Ԫ�أ�ͬʱ���ؼ���ֵ
	dict.clear() #����ֵ�
	print(dict)
else:
	print("����ɾ����Ч�������ڣ�")
dict.update({'٤��':'����'}) #�����ֵ䣬��������ھ��޸ģ������ھ���ӽ�ȥ
del dict #ɾ�������ֵ�
#�ֵ��Ƶ�ʽ
name=['槼�','���Ѿ�','��ɪ','����']
job=['��ʦ','��ʦ','սʿ','����']
dict={n:j+'��' for n,j in zip(name,job)}
print(dict)
del dict
del name
del job