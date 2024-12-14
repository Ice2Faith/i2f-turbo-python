# -- coding: gbk --
import struct,pickle
'''
���������򵥵�ʾ��
'''
def ReadTextFile(filename):
	'''
	��ȡһ���ı��ļ�������ʾ����Ļ��
	'''
	fp=open(filename,'r')
	string='\0'
	while(True):
		string=fp.read()
		print(string)
		if string=='':
			break
	fp.close()
	

def SaveTextToFile(filename):
	'''
	�½�һ����Ϊ��filename���ļ�
	���ڲ������ַ�����֪������#�ſ�ʼ���ַ�����������
	'''
	fp=open(filename,'a+')
	string='0'
	while(True):
		string=input('������(#�Ž���)>> ')
		if string[0]=='#':
			break
		print(string,file=fp)
	fp.close()

'''
#�ļ��������
filename=input('��������Ҫ������ļ�����:')
SaveTextToFile(filename)
'''

'''
#��ȡ�ļ�����
ReadTextFile('01.txt')
'''

'''
�ļ��Ĵ򿪣���Ҫ�ļ��Ѵ��ڣ�������׳�����FileNotFoundError,
����ʹ��try: ... except FileNotFoundError: ...�����쳣���� 
���ļ���д�룬����Ҫ�����Ƿ���ڣ������ڻ��Զ�����
'''
def ReadFile():
	try:
		# �ļ��Ĵ򿪷�ʽ������C�ķ�ʽ�����򿪵�ģʽ��C������һ����������ָ�������ʽ
		fp=open('aaa.txt','r',encoding='utf-8')
		str=fp.read() #�����������ļ���ȡ���
		# ���ʹ��read(20),�����Ϳ��Զ�ȡָ���ַ����Ĵ�
		
		print(str)
		pos=fp.tell() # ��ȡ��ǰ�ļ�ָ��λ��
		print(pos)

		fp.seek(0,0) #�����ļ�ָ�룬������ƫ�ƣ����ֵ��0���ļ�ͷ��1����ǰ��2���ļ�β��
		# ����������ļ�ָ��ָ���ļ���ͷ���ֿ��Զ�ȡ��
		# ��Ҫע�⣬�����ʱ����Ҫ�ö����Ʒ�ʽ�򿪲���
		
		#�ļ�����֮������Ҫ�رյ�
		fp.close()
	except FileNotFoundError:
		print('�ļ�������')
	
def WriteFile():
	#����ʹ�����һ�����ļ�
	fp=open('aaa.txt','w',encoding='utf-8')
	#д��һ���ı������ҷ���д��ĸ���
	fp.write('hello,����Python���ļ�д����Ϣ\n')
	# Ҳ����ʹ��writelines()д��һ���б��Զ�ʵ�ֻ���
	fp.close()

'''
ʹ��with��ʽ�����ļ���д
'''
def withOpenFile():
	#ʹ��with��ʽ���ļ��Ĺر����Զ��رյģ�����Ҫ�ֶ��ر�
	#��Ҳ������Ϊ����with����������ʱ���Զ��ر�
	#���ǣ�����Ҫע���ļ��������쳣
	with open('aaa.txt','w') as fp:
		fp.write('hello,����Python��with�ļ�д����Ϣ\n')
	with open('aaa.txt','r') as fp:
		print(fp.read())
'''
ȫ����ȡ�ļ������зָ�
'''
def readAllLineSplit():
	# �����ȫ����ȡ���������зָread().splitlines()�������õ��ľ���һ���ָ�õ��ַ����б�
	# �����ַ����б��ǲ��������з�\n��
	fp=open('aaa.txt','r')
	lines=fp.read().splitlines()
	for line in lines:
		print(line)
	fp.close()

'''
���ж�ȡ
'''
def readSingleLine():
	# �����һ��һ�еĶ�ȡ�Ļ�������ʹ��readline()�������������һ�У��ǰ������з��ģ�����ʹ��strip()����ȥ������
	# ������ļ��������ͷ��ؿմ�
	fp=open('aaa.txt','r')
	line=fp.readline()
	while line!='':
		print(line)
		line=fp.readline()
	fp.close()
	'''
	# ������д�ĸ����
	fp=open('aaa.txt','r')
	for line in fp:
		print(line)
	fp.close()
	'''
	
'''
��ʽ����ȡ
'''
def readFormat():
	fp=open('aaa.txt','r')
	# ͨ�����ж�ȡ֮���չ���ָ��ַ�������
	line=fp.readline().strip()
	valus=line.split()
	#�����ͷָ��������
	fp.close()

'''
�����ƵĶ�д��import struct
����pack��unpack���д���ͽ��

Ҳ��ʹ��import pickle�����������ַ�ʽΪ����ʹ��struct��ʽ�ľ�������
����dump��load���д���ͽ��
'''
def binaryIOFile():
	fp=open('bbb.bin','wb')
	pickle.dump(12,fp)
	pickle.dump(True,fp)
	pickle.dump(12.125,fp)
	fp.close()
	
	fp=open('bbb.bin','rb')
	a=pickle.load(fp) #���ص����ַ����������Ҫ������ǿת
	b=pickle.load(fp)
	c=pickle.load(fp)
	print(a,b,c)
	fp.close()
	
def fileSystemOperation():
	os.rename('source.txt','target.txt') #������
	os.remove('delete.txt')	#ɾ���ļ�
	os.mkdir('floder')	#�����ļ���
	os.rmdir('delete dir') #ɾ���ļ���
	fileNamelist=os.listdir('./') #����ļ����µ��ļ��б�������Ǿ���·��

def main():
	WriteFile()
	ReadFile()
	withOpenFile()
	binaryIOFile()

if __name__=='__main__':
	main()