#-*-coding:gbk-*-
import sys
import os
'''
�����쳣���඼��Exception
������exceptionsģ����
'''
'''
�����쳣
δ�����ı�����NameError
����Ϊ0��ZeroDivisionError
�﷨����SyntaxError
��������IndexError
������KeyError
�ļ��Ҳ�����FileNotFoundError
'''
def baseCatchExcept():
	'''
	�����ṹ
		try:
			�������д����
		except �쳣���� as ����:
			�쳣�������飬����ͨ�������õ��쳣
		except �����쳣
			�����쳣����
		else:
			û�з����쳣ʱ���еĴ����
			������һ�� if except ... else ... 
		finally:
			�����Ƿ�����쳣�����ն����еĴ����
		
	�������Ҫ����ָ�����쳣
		try:
			...
		except:
			...
		
	���߲���Ҫ����
		try:
			...
		except �쳣��:
			...
	
	����쳣�ļ�д
		try:
			...
		except (�쳣��1���쳣��2...) as err:
			...
	'''
	fp=None
	try:
		fp=open('aaa.txt','r')
		print(fp.read())
	except (FileNotFoundError,IOError) as err:
		print(str(err))
	except Exception as err:
		print(str(err))
	else:
		print('not found any error')
	finally:
		if fp!=None:
			fp.close()
		# ʹ��locals()���ص�ǰ�������еı�������
		# �����������ж�Ҳ����,���ֵĺô��ǲ�����try֮ǰ��������
		# if 'fp' in locals(): 
			# fp.close()
			
def ZeroDivErrTest():
	'''
	����Ϊ0�Ĵ���
	'''
	try:
		num1=eval(input('�������һ������'))
		num2=eval(input('������ڶ�������'))
		div=num1/num2
		print('%d/%d=%d'%(num1,num2,div))
	except Exception as err:
		print('�쳣������',str(err))
	else:
		print('û�з����쳣')
	finally:
		print('���մ����')

def main():
	print('myexcept')
	baseCatchExcept()
	ZeroDivErrTest()

if __name__=='__main__':
	main()
