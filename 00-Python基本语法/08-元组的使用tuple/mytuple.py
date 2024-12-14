# -- coding: gbk --
#元组
#元组和列表类似
#创建
tuple=()
#元组不能对其部分赋值，只能访问，可以整体重新赋值
tuple=tuple+('test',)	#单元素元组连接必须加逗号
print(tuple)
tuple+=(0,) #追加单个元组，需要加逗号
tuple+=(1,2) #追加一个新元组
print(tuple)
del tuple
#元组和链表的异同点
'''
都是序列
链表是可变序列，元素值可以增删改（写操作）
元组是不可变序列，只能查和整体替换和追加元组（读操作，简单理解为Java中的String）
元组访问速度更快，可以作为字典的键,
相互转换list(tuple),tuple(list)
其他读操作均相同
'''