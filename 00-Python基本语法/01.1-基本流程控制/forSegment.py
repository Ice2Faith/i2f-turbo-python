#-*-coding:gbk-*-
import sys
import os
'''
循环结构：
for结构
	for value in range(squeen):
		CodeSegment
'''
def baseFor():
	'''
	最基本的for循环
	这里演示了输出0-9的数字
	实质上这里的range(10)相当于range(0,10)，这是一个左闭右开区间
	和C语言中的(i=0;i<10;i++)一致
	'''
	for i in range(10):
		print(i)

def ForStep():
	'''
	带有step的for循环
	这里演示了输出0-10中的偶数
	实质上这里的range(0,10,2)相当于
	range(start=0,stop=10,step=2)
	(但是貌似不怎么支持这种写法)，这是一个左闭右开区间
	和C语言中的(i=0;i<10;i+=2)一致
	'''
	for i in range(0,10,2):
		print(i)
		
def ForEnumerate():
	'''
	使用enumerate关键字配合for循环
	实现获取元素的下标
	这里的输出方式就为：0=h 1=e 2=l 3=l 4=o
	
	还可以配合len()使用
	for i in len(str):
	'''
	str="hello"
	for index,value in enumerate(str):
		print(index,value,sep="=")
	
def Table99():
	'''
	嵌套循环
	实现输出乘法表
	'''
	for i in range(1,10):
		for j in range(1,i+1):
			print("%d*%d=%d"%(i,j,i*j),end="\t")
		print("")

def RegTrangle():
	'''
	输出正三角形
	外矩阵大小10row*20col
	'''
	for i in range(10):
		for k in range(10-i):
			print(' ',end='')
		for j in range(i*2-1):
			print('*',end='')
		print()
def TragleYangHui():
	'''
	输出杨辉三角
	字母金字塔
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
