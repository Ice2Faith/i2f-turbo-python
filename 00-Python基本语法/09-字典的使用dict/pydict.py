#-*-coding:gbk-*-
'''
字典的一些使用案例
'''

def MarketComsuption():
	'''
	超市消费账单计算
	'''
	list={'牛奶':65,'面包':15,'可乐':39,'饼干':45,'糖果':24,'水果':35.8}
	list['可乐']=60
	print("您购买%d件物品，共计：%.2lf元"%(len(list.keys()),sum(list.values())))
	
def BankCardIDCreate():
	'''
	银行卡密码生成
	'''
	dict={'610%03d'%i:'000000' for i in range(1,100+1)}
	print('100个银行卡及密码如下所示：',dict)

def MarketSaleList():
	'''
	超市日流水清单
	'''
	list={'11月24日':{'牛奶':{'数量':15,'单价':5.5},
					'方便面':{'数量':25,'单价':4},
					'糖果':{'数量':10,'单价':12}
					},
		'11月25日':{'牛奶':{'数量':25,'单价':5.5},
					'咖啡':{'数量':5,'单价':6},
					'饼干':{'数量':15,'单价':6},
					'火腿肠':{'数量':10,'单价':5}
					},
		'11月26日':{'奶茶':{'数量':10,'单价':5},
					'牛奶':{'数量':20,'单价':5.5},
					'方便面':{'数量':15,'单价':4}
					}
		}
	for date,data in list.items():
		count,money=0,0
		print(date)
		for goods,detail in data.items():
			print(goods,':',end=' ')
			for name,value in detail.items():
				print(name,':',value,end=' ')
				if name=='数量':
					count+=value
				if name=='单价':
					money+=value
			print()
		print('\t%s卖出货物%d件，小计：%.2lf元'%(date,count,money))
	

def main():
	MarketComsuption()
	BankCardIDCreate()
	MarketSaleList()

if __name__=='__main__':
	main()
