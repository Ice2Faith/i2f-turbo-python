# -- coding: gbk --
import os

'''
函数的定义形式：
def 函数名([参数列表=默认值]):
	函数体
	[return 返回值列表]
从上面你可以看出，支持多个参数或者零个参数，
返回值也可以有多个，并且是可以没有返回值的
参数也是可以有默认值的，但是默认值应该列表后面
可选参数，值必须为空字符串
参数也可以是可变长的参数*号开头，传进去作为列表存在，调用时：12,13,14
两个*号的参数，标识是一个变长的字典，调用时：a=12,b=15
def func():
	a=12
def func(a,b,c):
	return a+b+c,(a+b+c)/3
def func(a,b,c=12):
	pass
def func(a,b,c=''):
	pass
def func(a,b,*args):
	for it in args:
		print(it)
'''
'''
函数的调用：
可以按照函数定义给出的参数位置进行调用
也可以通过参数名指定的键值使用
func(1,2,3)
func(a=1,c=3,b=2)
'''

def Command(mind):
	'''
	调用系统cmd命令行
	'''
	os.system(mind)

def getListMaxMin(ls):
	'''
	获取列表的最大值和最小值
	'''
	if len(ls)==0:
		return None,None
	min=max=ls[0]
	for item in ls:
		if item>max:
			max=item
		if item<min:
			min=item
	return max,min
	
def getSumAvg(a,b):
	return a+b,(a+b)/2

def swap(a,b): #交换值，其实PY中没必要这样使用，直接a,b=b,a交换即可
	return b,a #因此一般使用集合的方式交换才有意义，集合传递是引用传递
	
def getUserInfo(map):
	while True:
		name=input('please input name(input q quit):')
		if name=='q':
			break
		age=int(input('please input %s\'s age:'%name))
		map[name]=age
'''
函数的递归
即函数自身调用它自己
但是，写递归必须要有出口条件
'''
def MultiplySuper(number):
	'''
	递归求阶乘
	'''
	if number<=1 :
		return 1
	return number*MultiplySuper(number-1)
'''
变量作用域
如果函数体内使用了全局变量，那么要在使用之前声明是使用了全局变量
毕竟PY是不需要定义变量的，如果不声明而直接使用，那么就会使用局部变量
x=10
def func():
	global x # 引用全局变量
	x=20 # 这里就将全局变量改为20

def func():
	x=20 # 这里多了一个局部变量，修改不会影响全局变量
'''
	
def main():
	#调用函数
	map={}
	getUserInfo(map)
	print(map)
	
	Command('color f1')
	Command('Pause')
	
	print(getListMaxMin((1,2,5,4,9,-2)))
	print(getSumAvg(b=3,a=5))
	
if __name__=='__main__':
	main()