#-*-coding:gbk-*-
'''
�ֵ��һЩʹ�ð���
'''

def MarketComsuption():
	'''
	���������˵�����
	'''
	list={'ţ��':65,'���':15,'����':39,'����':45,'�ǹ�':24,'ˮ��':35.8}
	list['����']=60
	print("������%d����Ʒ�����ƣ�%.2lfԪ"%(len(list.keys()),sum(list.values())))
	
def BankCardIDCreate():
	'''
	���п���������
	'''
	dict={'610%03d'%i:'000000' for i in range(1,100+1)}
	print('100�����п�������������ʾ��',dict)

def MarketSaleList():
	'''
	��������ˮ�嵥
	'''
	list={'11��24��':{'ţ��':{'����':15,'����':5.5},
					'������':{'����':25,'����':4},
					'�ǹ�':{'����':10,'����':12}
					},
		'11��25��':{'ţ��':{'����':25,'����':5.5},
					'����':{'����':5,'����':6},
					'����':{'����':15,'����':6},
					'���ȳ�':{'����':10,'����':5}
					},
		'11��26��':{'�̲�':{'����':10,'����':5},
					'ţ��':{'����':20,'����':5.5},
					'������':{'����':15,'����':4}
					}
		}
	for date,data in list.items():
		count,money=0,0
		print(date)
		for goods,detail in data.items():
			print(goods,':',end=' ')
			for name,value in detail.items():
				print(name,':',value,end=' ')
				if name=='����':
					count+=value
				if name=='����':
					money+=value
			print()
		print('\t%s��������%d����С�ƣ�%.2lfԪ'%(date,count,money))
	

def main():
	MarketComsuption()
	BankCardIDCreate()
	MarketSaleList()

if __name__=='__main__':
	main()
