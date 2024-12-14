#-*-coding:gbk-*-
import sys
import os
'''
基本流程控制
'''
def IfSegment():
	'''
	if 语句的书写规则
	使用冒号引出程序段
	使用缩进控制程序段的归属
	if的判定不需要使用括包含
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
	实现字符转大写
	ord():转整型
	chr():转字符
	'''
	print(chr(ord(a)&~32))

def sort3Number(x,y,z):
	'''
	实现三个数字的比较大小，顺序输出，从小到大
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
	回文数判定
	'''
	num=str(num)
	res=True
	for i in range(len(num)//2) : #for in 也就是foreach,其中的range用来取0-这样一个个数的范围
		if num[i] != num[len(num)-1-i] : #截取字符串的第i个
			res=False
			break
	print(res)
def gradePrint(score):
	'''
	等级判定
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
	x,y,z=eval(input('please input 3 number:'))# 注意，这里的输入方式用逗号分隔
	sort3Number(x,y,z)
	symmetryNumber(12121)
	gradePrint(89)

if __name__=='__main__':
	main()
