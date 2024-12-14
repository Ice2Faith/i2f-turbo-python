#-*-coding:gbk-*-
import sys
import os
'''
list 列表容器

'''

def baseList():
	'''
	list的基本用法
	'''
	a=[] #得到一个空列表
	a=[1,2.5,'hello',[1,1,2],(3,4,5)] #得到一个普通列表，列表可以存放任意类型，还可以嵌套
	print(a)
	a=a[0:len(a):2] #取出列表中的偶数项，形成一个新的列表
	print(a)
	print(a[2]) #取出一个下标元素
	b=a+[10,10,10] #连接列表，会形成一个新的列表返回
	print(b)
	b=a*2 #重复列表，相当于复制几分连接上去，会形成一个新的列表返回
	print(b)
	a=[11,12]
	a.append([13,14]) #向列表中添加一个新元素，不管什么只看做一个元素加进去
	print(a)
	a.extend([13,14]) #将一个列表追加到原列表中，如果是一个列表，就连接成列表
	print(a)
	a.insert(2,'hello') #插入指定位置一个元素，指该值插入之后的下标索引，原来的后移
	print(a)
	# 获取元素下标index()，参数：元素[，开始下标[，结束下标]]
	print(a.index('hello')) #获取指定元素的第一个下标
	print(a.index('hello',2)) #获取从下标2开始的第一个个出现的下标
	print(a.index('hello',2,4)) #获取指定元素在某个下标区间的下标
	# 统计元素出现的次数
	print(a.count(13)) # 注意，不会统计子列表，因为子列表相当于一个元素
	# 判断元素是否在其中
	print(14 in a)
	#列表的删除
	del a[2] #删除下标元素
	a.remove(13) #删除第一次出现的元素，如果不存在会报错
	a.pop() #取出最后一个元素
	print(a)
	# 修改元素值
	a[0]='hello'
	print(a)
	del a #删除整个列表
	del b

def usualFunc():
	'''
	list常用函数
	'''
	a=[11,12]
	b=[12,13]
	# print(cmp(a,b)) #py2的使用方式，返回整型值标识大小
	print(a>b) #py3的比较方式，字符串按照字符编码比较
	print(len(a)) #获取列表的长度，实际上是列表的内置函数，内置变量__len__,由于是两个下划线标识的，private不可访问
	print(max(a)) # 获取元素的最大值，但是，列表元素类型需要一致，否则失败
	print(sum(a)) #列表求和，但是不能用于字符串，sum(a,12),这将会再加上一个12
	print(sorted(a)) #排序一个列表，只能是同一类型，默认升序排序，不改变源列表顺序，使用参数：reverse=True改变为降序排序
	a.sort() #内置的排序方法，会覆盖原列表，同样也有reverse参数
	a.reverse() #翻转列表元素
	# 逆转矩阵
	matrix=[[1,2,3,4],[5,6,7,8],[3,10,11,12]]
	tmatrix=[]
	for j in range(4):
		tmatrix.append([row[j] for row in matrix])
	print(tmatrix)


import random
def test():
	'''
	8个学生，随机插入三个班
	'''
	stus=['stu'+str(i) for i in range(8)]
	clas=[[] for i in range(3)]
	for i in stus:
		clas[random.randint(0,2)].extend([i])
	print(clas)
	

def test2():
	'''
	将6个学生平均分配到三个班级
	'''
	stus=['stu'+str(i) for i in range(6)]
	avgclas=[[] for i in range(3)]
	for i in stus:
		ri=random.randint(0,2)
		while len(avgclas[ri])>=2:
			ri=random.randint(0,2)
		avgclas[ri].append(i)
	print(avgclas)
	
def proveList():
	'''
	list的列表推导式
	'''
	a=[i**2 for i in range(100)] #列表推导式，形如：推到体 循环条件
	print(a)
	
import time
def IDParse(id):
	list_id=['350100','福州市','350101','市辖区',
        '350102','鼓楼区',
        '350103','台江区',
        '350104', '仓山区',
        '350105', '马尾区',
        '350111', '晋安区',
        '350121', '闽侯县',
        '350122', '连江县',
        '350123', '罗源县',
        '350124', '闽清县',
        '350125', '永泰县',
        '350128', '平潭县',
        '350181', '福清市',
        '350182', '长乐市']
	city=id[0:6]
	index=list_id.index(city)
	if index<0:
		print('该出生地未支持')
	else:
		print(list_id[index+1])
		tm=time.localtime(time.time())
		print('%d周岁'%(tm.tm_year-int(id[6:10])))
		print('出生日期:%s-%s-%s'%(id[6:10],id[10:12],id[12:14]))
		
def main():
	test()
	test2()
	print('list列表的使用')
	baseList()
	usualFunc()
	proveList()
	IDParse(input('请输入身份证号：'))

if __name__=='__main__':
	main()
