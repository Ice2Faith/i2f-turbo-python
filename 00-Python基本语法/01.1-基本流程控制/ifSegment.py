#-*-coding:gbk-*-
import sys
import os
'''
�������̿���
'''
def IfSegment():
	'''
	if ������д����
	ʹ��ð�����������
	ʹ���������Ƴ���εĹ���
	if���ж�����Ҫʹ��������
	'''
	a=12
	if a==12:
		print("a is 12")
	elif a>12 :
		print("a gather than 12")
	else:
		print("a lower than 12")
	print("if-elsesegment quit")

def CharToUpper(a):
	'''
	ʵ���ַ�ת��д
	ord():ת����
	chr():ת�ַ�
	'''
	print(chr(ord(a)&~32))

def sort3Number(x,y,z):
	'''
	ʵ���������ֵıȽϴ�С��˳���������С����
	'''
	if x>y :
		x,y=y,x
	if x>z :
		x,z=z,x
	if y>z :
		y,z=z,y
	print(x,y,z,sep='<')
def symmetryNumber(num):
	'''
	�������ж�
	'''
	num=str(num)
	res=True
	for i in range(len(num)//2) : #for in Ҳ����foreach,���е�range����ȡ0-����һ�������ķ�Χ
		if num[i] != num[len(num)-1-i] : #��ȡ�ַ����ĵ�i��
			res=False
			break
	print(res)
def gradePrint(score):
	'''
	�ȼ��ж�
	'''
	grade='E'
	score//=10
	if score==9 or score==10 :
		grade='A'
	elif score==8:
		grade='B'
	elif score==7:
		grade='C'
	elif score==6:
		grade='D'
	print('grade is:',grade)
	
def main():
	print('baseProcessRoute')
	IfSegment()
	CharToUpper('a')
	x,y,z=eval(input('please input 3 number:'))# ע�⣬��������뷽ʽ�ö��ŷָ�
	sort3Number(x,y,z)
	symmetryNumber(12121)
	gradePrint(89)

if __name__=='__main__':
	main()
