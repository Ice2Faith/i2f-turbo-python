# -- coding: gbk --
import sys,time,calendar,random
#导入文件测试

'''
模块
将代码集保存在一个py文件中
形成一个模块

调用时，只需要使用import导入模块即可

导入整个模块：
import 模块文件名
使用时：
模块文件名.方法名

只导入一些函数
from 模块名 import 函数名
使用时：
直接使用函数名即可

当然有的模块名太长，可以给他们取别名，以方便自己使用
import 模块名 as 别名
from 模块名 import 函数名 as 函数别名
使用时：
可以使用源名称，也可以使用定义的别名

导入的内容，部分可以使用通配符*，标识导入某个模块中的所有内容

用例：
import myfunctional
from myfunctional import *

import myclass
from myclass import *
'''

def timeModule():
	# 时间模块的使用,import time
	import time
	utctime=time.time() #获取时间戳
	print(utctime)
	print(time.strftime('%Y-%m-%d %H:%M:%S')) #格式化为字符串返回
	print(time.strftime('%a %b %d %H:%M:%S %Y')) #格式化为字符串返回
	timeStruct=time.localtime() #返回时间结构体，能够方便的获取日期信息
	# timeStruct.tm_year...
	print(timeStruct)
	
def CalendarModule():
	# 日历模块的使用，import calendar
	cal=calendar.month(2020,3) #获取一个这个日期所在的日历的月份
	print(cal) 
	
def randomModule():
	# 随机模块的使用，import random
	print(random.randint(10,100)) #完全闭区间的随机
	print(random.choice([1,5,7,8])) #随机取列表中的一个
	ls=[1,2,3,4,5,6]
	random.shuffle(ls) #洗牌算法
	print(ls)
	rls=random.sample(ls,3) #随机从列表中选取三个形成一个新列表返回
	print(rls)
	
def main():
	timeModule()
	CalendarModule()
	randomModule()
	
if __name__=='__main__':
	main()
	