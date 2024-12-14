# -- coding: gbk --
#集合，注意，虽然都是以花括号标识，这里要注意
ll={} #这将得到一个空字典
ll=set() #这才能得到一个空集合
#创建、清空与删除
set={0,1,2,5,4,2,6}
print(set)
set.clear()
del set
#空集合和创建
set=set()
del set
set=set(['女娲','甄姬','孙尚香'])
print(set)
#增删元素
set.add('大乔')
if '小乔' in set:
	set.remove('小乔')
	print('移除成功-','小乔')
else:
	print('没有找到')
#并|交&差-运算和对称差集^
set2={'虞姬','王昭君','孙尚香'}
print('并集：',set|set2)
print('交集：',set&set2)
print('差集：',set-set2)
print('对称差集：',set^set2)
