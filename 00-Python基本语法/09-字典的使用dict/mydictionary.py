# -- coding: gbk --
#字典
#创建删除与清空
#key:context(key必须唯一)
dict={'qq':'30017862154','ID':'511401178712110100'}
print(dict)
dict.clear()
print(dict)
del dict
dict={}
del dict
dict=dict()
del dict
#通过映射函数zip利列表、元组创建字典
tuple=(101,102,103,104,105)
list=['jack','mellen','alice','keyle','daivel']
dict=dict(zip(tuple,list))
print(dict)
del dict
del list
del tuple
#对象映射建立
dict=dict(妲己='法师','虞姬'='射手')
print(dict)
del dict
#创建空值字典
list=['妲己','王昭君','亚瑟','后羿']
dict=dict.fromkeys(list)
# 创建一个具有默认值的字典
dict={}.fromkeys(list,'aaa')
print(dict)
del dict
del list
#将一个元组作为键，一个列表作为值
tuple=(101,102,103,104,105)
list=['jack','mellen','alice','keyle','daivel']
dict={tuple:list}
print(dict)
del dict
del list
del tuple
#字典的访问
dict=dict(妲己='法师','虞姬'='射手')
print('妲己是：',dict['妲己'] if '妲己' in dict else '妲己没找到')
print('后羿是：',dict.get('后羿','找不到')) #找键的值，找不到就用给定的默认参数
#遍历
for key in dict.keys(): #遍历键，可以先sorted(dict.keys())进行排序之后输出
	print(dict[key])
for value in dict.values(): #遍历值
	print(value)
for item in dict.items(): #遍历项
	print(item)
for key,value in dict.items(): #遍历项，并分开键值
	print('Key=',key,'Value=',value)
#增删改
dict['杨玉环']='辅助' #不存在键即添加
print(dict)
dict['杨玉环']='法师' #存在即修改
print(dict)
if '后羿' in dict: #判断键是否存在 ，可使用not in dict.values()判断值是否存在
	del dict['杨玉环'] #删除一个键值
	dict.pop('杨玉环') #删除一个键值，会返回删除的键对应的值
	dict.popitem() #随机删除一个元素，同时返回键和值
	dict.clear() #清空字典
	print(dict)
else:
	print("后羿删除无效，不存在！")
dict.update({'伽罗':'射手'}) #更新字典，如果键存在就修改，不存在就添加进去
del dict #删除整个字典
#字典推导式
name=['妲己','王昭君','亚瑟','后羿']
job=['法师','法师','战士','射手']
dict={n:j+'型' for n,j in zip(name,job)}
print(dict)
del dict
del name
del job