# -- coding: gbk --
import random
#列表
# 赋值
llist=['测试',12,125.13,['aaa',12]]
# 取值，切片，区间【1，3）上，每间隔为2的值取出
pl=llist[1:3:2]
del llist
#空列表
list=[]
list+=['测试']
list.append(2019)
list+=[7]
list+=[17]
list.append('列表的测试')
#遍历列表
for item in list:
	print(item,end='\t')
print()
#带索引方式遍历列表
for index,item in enumerate(list):
	print(str(index)+'\t'+str(item))
list2=['hello',2019,'welcome','python']
#导入列表
list.extend(list2)
print(list)
#修改列表元素
list[0]='列表测试'
print(list)
#删除列表元素
#根据位置
del list[-1]
print(list)
#根据值，需要唯一
list.remove('welcome')
print(list)
#插入指定位置一个值
list.insert(-1,'python')
print(list)
#统计出现次数
print(str(list.count(2019)))
#查询首次下标
print(str(list.index(2019)))
#求和
listint=[5,12,7,6,13,15,24,37,3]
print('Sum='+str(sum(listint,0)))
#排序
print('原本排列：',listint)
listint.sort(reverse=True)
print('降序排列：',listint)
liststr=['Cat','Animal','Dog','Brid','alter']
print('原本排列：',liststr)
#不区分大小写排序
liststr.sort(key=str.lower,reverse=False)
print('升序排列：',liststr)
#排序并创建新列表
liststr2=['Cat','Animal','Dog','Brid','alter']
print('原本排列：',liststr2)
listsorted=sorted(liststr2,key=str.lower,reverse=False)
print('升序排列：',listsorted)
#列表推导式--快速生成列表
listcreate=[str('new_'+item) for item in liststr2]
print('New List:',listcreate)

randomnumber=[random.randint(0,100) for i in range(10)]
print('Random Number:',randomnumber)
#二维列表
arr=[]
for i in range(1,5):
	arr.append([])	#为内层创建空列表
	for j in range(1,5):
		arr[i-1].append(i*j)
print(arr)
#列表的删除
del list
del list2
del listcreate
del listint
del listsorted
del liststr
del liststr2