#-*-coding:gbk-*-
import sys
import os
'''
ѭ���ṹ��
for�ṹ
	for value in range(squeen):
		CodeSegment
'''
def baseFor():
	'''
	�������forѭ��
	������ʾ�����0-9������
	ʵ���������range(10)�൱��range(0,10)������һ������ҿ�����
	��C�����е�(i=0;i<10;i++)һ��
	'''
	for i in range(10):
		print(i)

def ForStep():
	'''
	����step��forѭ��
	������ʾ�����0-10�е�ż��
	ʵ���������range(0,10,2)�൱��
	range(start=0,stop=10,step=2)
	(����ò�Ʋ���ô֧������д��)������һ������ҿ�����
	��C�����е�(i=0;i<10;i+=2)һ��
	'''
	for i in range(0,10,2):
		print(i)
		
def ForEnumerate():
	'''
	ʹ��enumerate�ؼ������forѭ��
	ʵ�ֻ�ȡԪ�ص��±�
	����������ʽ��Ϊ��0=h 1=e 2=l 3=l 4=o
	
	���������len()ʹ��
	for i in len(str):
	'''
	str="hello"
	for index,value in enumerate(str):
		print(index,value,sep="=")
	
def Table99():
	'''
	Ƕ��ѭ��
	ʵ������˷���
	'''
	for i in range(1,10):
		for j in range(1,i+1):
			print("%d*%d=%d"%(i,j,i*j),end="\t")
		print("")

def RegTrangle():
	'''
	�����������
	������С10row*20col
	'''
	for i in range(10):
		for k in range(10-i):
			print(' ',end='')
		for j in range(i*2-1):
			print('*',end='')
		print()
def TragleYangHui():
	'''
	����������
	��ĸ������
	'''
	for i in range(27):
		for j in range(27-i):
			print(" ",end='')
		for j in range(i):
			print(chr(j+ord('A')),end='')
		for j in range(i-1):
			print(chr(i-1-j+ord('A')-1),end='')
		print()
	
def main():
	print('forSegment')
	baseFor()
	ForStep()
	ForEnumerate()
	Table99()
	RegTrangle()
	TragleYangHui()

if __name__=='__main__':
	main()
