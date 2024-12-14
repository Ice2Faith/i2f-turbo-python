#-*-coding:gbk-*-
import sys
import os
'''
所有异常基类都是Exception
包含在exceptions模块中
'''
'''
常见异常
未申明的变量：NameError
除数为0：ZeroDivisionError
语法错误：SyntaxError
索引错误：IndexError
键错误：KeyError
文件找不到：FileNotFoundError
'''
def baseCatchExcept():
	'''
	基本结构
		try:
			尝试运行代码块
		except 异常名称 as 别名:
			异常处理代码块，可以通过别名拿到异常
		except 其他异常
			其他异常处理
		else:
			没有发生异常时运行的代码块
			隐含了一个 if except ... else ... 
		finally:
			不管是否出现异常，最终都运行的代码块
		
	如果不需要捕获指定的异常
		try:
			...
		except:
			...
		
	或者不需要别名
		try:
			...
		except 异常名:
			...
	
	多个异常的简写
		try:
			...
		except (异常名1，异常名2...) as err:
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
		# 使用locals()返回当前作用域中的变量名，
		# 这样来进行判定也可以,这种的好处是不用在try之前申明变量
		# if 'fp' in locals(): 
			# fp.close()
			
def ZeroDivErrTest():
	'''
	除数为0的处理
	'''
	try:
		num1=eval(input('请输入第一个数：'))
		num2=eval(input('请输入第二个数：'))
		div=num1/num2
		print('%d/%d=%d'%(num1,num2,div))
	except Exception as err:
		print('异常描述：',str(err))
	else:
		print('没有发生异常')
	finally:
		print('最终处理块')

def main():
	print('myexcept')
	baseCatchExcept()
	ZeroDivErrTest()

if __name__=='__main__':
	main()
