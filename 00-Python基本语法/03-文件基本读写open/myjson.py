#-*-coding:gbk-*-
import sys
import os

'''
json��ʽ�ļ��Ķ�д
д��Ϊ�б�������������б�
'''
import json
def WriteJson():
	numbers=[1,2,3,4,{'aa':17}] #ֻ�����б�����ֵ䣬����Ƕ�׵�Ȼ�ǿ��Ե�
	filename='numbers.json'
	with open(filename,'w') as fp:
		json.dump(numbers,fp)
		
def ReadJson():
	filename='numbers.json'
	with open(filename,'r') as fp:
		numbers=json.load(fp)
		print(type(numbers),numbers)
		position=fp.tell() #��õ�ǰ�ļ�ָ��λ��
		print(position)
		# <class 'list'> [1, 2, 3, 4]
		

def main():
	print('myjson')
	WriteJson()
	ReadJson()

if __name__=='__main__':
	main()
