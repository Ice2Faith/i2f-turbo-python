# -- coding: gbk --
#�ַ���
#���������
string='���ѽ��python'
print(string)
stringcode=string.encode(encoding='utf-8',errors='replace')
print(stringcode)
stringret=stringcode.decode('utf-8')
print(stringret)
#�ַ�������+
#�󳤶�len(string)��Ĭ���ַ�����Ϊ���ȣ�����Ҫ�����encode��������
print(len(string))
print(len(string.encode('gbk')))
#�ַ�����ȡ��ʹ����Ƭ
print(string[2:-1:1])
#��ȡ�����쳣
try:
	print(string[15:20])
except IndexError:
	print("ָ������������")
#�ָ���ϲ�
#�ָ�󱣴浽�б���split(�ָ��ǣ����ָ����=Ĭ�ϲ�����)
list=string.split('��')
print(list)
#�ɵ�������ƴ��Ϊ�ַ��������ӷ�.join(��������)
newstring=' && '.join(list)
print(newstring)
#����
newstring.index('py') #�����Ӵ��Ŀ�ʼλ��
newstring.find('py') #�����Ӵ�λ�ã���indexһ����ֻ��index����Ҳ����ᱨ�쳣
newstring.count('py') #�����Ӵ�����

#����
print('-'*20)
str1='this is a string test'
str1.replace('is','was') #ע��this�е�isҲ�ᱻ�滻�������Ҫ�Ļ�����Ҫ��ǰ�ÿո�����
#str1.replace(' is',' was')
print(str1)
strg=str1.split(' ') #�����ַ���������ָ���ķ�����ţ��õ�һ���б�
print(strg)
str1=','.join(strg) #ƴ���ַ������б����շָ�����кϲ�������ķָ��ֱ��ʹ����','
print(str1) #�﷨Ϊ��str=sep.join(list)

#�жϵ����Ƿ�Ԫ����ĸ��ͷ
aeo='aeiouAEIOU'
alist=[input('������һ������:') for i in range(5)]
for word in alist:
	if word[0] in aeo:
		print('Ԫ����',word)