#-*-coding:gbk-*-
import sys
import os
'''
ѭ���ṹ��
while�ṹ
	while boolExp:
		codeSegment
'''
def baseWhile(num):
	'''
	�������whileѭ��
	չʾһ��0+...+num�Ĺ���
	'''
	i=0
	sum=0
	while i<=num :
		sum+=i
		i+=1
	return sum

def WhileElse(num):
	'''
	����else����whileѭ��
	Ҳ������ѭ������ʱִ��һ�ε�����
	����չʾ�˽׳˵ļ���1*...*num
	'''
	i,sum=1,1
	while i<=num:
		sum*=i
		i+=1
	else:
		print(sum)
		return sum

def WhileBreak():
	'''
	����break����whileѭ��
	ʵ��һ���Ӽ��̶������������������ǵĺ�
	ֱ����������ʱ��ʹ��break����ѭ��������������������
	'''
	sum,num=0,0
	while(True):
		num=eval(input("�������������������븺��������"))
		if(num<0):
			break
		sum+=num
	print(sum)

def WhileContinue():
	'''
	����continue����whileѭ��
	ʵ�ִ�0��100��ż�����
	���������������ʹ��continue������ǰѭ��
	������һ��ѭ��
	'''
	i,sum=0,0
	while i<100:
		if i%2==1:
			i+=1
			continue
		sum+=i
		i+=1
	print(sum)

def TrangleYangHui():
	'''
	����������
	��ĸ������
	'''
	i=0
	while i<26 :
		j=0
		while j<26-i :
			print(' ',end='')
			j+=1
		j=0
		while j<i :
			print(chr(j+ord('A')),end='')
			j+=1
		while j>=0 :
			print(chr(j+ord('A')),end='')
			j-=1
		print()
		i+=1

def BaijiBaiqian():
	'''
	�ܹ�100��
	����5�ģ�ĸ��С����3��
	ÿ�ּ���Ҫ��
	'''
	count=0
	print("question",5,3,3)
	for i in range(100//5+1):
		for j in range((100-i*5)//3+1):
			for k in range((100-i*5-j*3)//3+1):
				if 100==i*5+j*3+k*3 and i+j+k>0:
					print('anwser:',i,j,k)
				count+=1
	print("times:",count)
					
def main():
	print('whileSegment')
	#print(baseWhile(10))
	#WhileElse(5)
	#WhileBreak()
	#WhileContinue()
	#TrangleYangHui()
	BaijiBaiqian()

if __name__=='__main__':
	main()
