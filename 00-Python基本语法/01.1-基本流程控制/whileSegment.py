#-*-coding:gbk-*-
import sys
import os
'''
循环结构：
while结构
	while boolExp:
		codeSegment
'''
def baseWhile(num):
	'''
	最基本的while循环
	展示一个0+...+num的过程
	'''
	i=0
	sum=0
	while i<=num :
		sum+=i
		i+=1
	return sum

def WhileElse(num):
	'''
	带有else语句的while循环
	也就是在循环结束时执行一次的语句段
	这里展示了阶乘的计算1*...*num
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
	带有break语句的while循环
	实现一个从键盘读入若干正数计算他们的和
	直到遇到负数时，使用break结束循环，输出结果，结束计算
	'''
	sum,num=0,0
	while(True):
		num=eval(input("请输入若干正数，输入负数计算结果"))
		if(num<0):
			break
		sum+=num
	print(sum)

def WhileContinue():
	'''
	带有continue语句的while循环
	实现从0到100的偶数相加
	如果遇到奇数，就使用continue跳过当前循环
	进入下一次循环
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
	输出杨辉三角
	字母金字塔
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
	总共100文
	公鸡5文，母鸡小鸡各3文
	每种鸡都要有
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
