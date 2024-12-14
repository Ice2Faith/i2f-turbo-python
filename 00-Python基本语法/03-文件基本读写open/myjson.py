#-*-coding:gbk-*-
import sys
import os

'''
json格式文件的读写
写出为列表，读入进来还是列表
'''
import json
def WriteJson():
	numbers=[1,2,3,4,{'aa':17}] #只能是列表或者字典，这样嵌套当然是可以的
	filename='numbers.json'
	with open(filename,'w') as fp:
		json.dump(numbers,fp)
		
def ReadJson():
	filename='numbers.json'
	with open(filename,'r') as fp:
		numbers=json.load(fp)
		print(type(numbers),numbers)
		position=fp.tell() #获得当前文件指针位置
		print(position)
		# <class 'list'> [1, 2, 3, 4]
		

def main():
	print('myjson')
	WriteJson()
	ReadJson()

if __name__=='__main__':
	main()
