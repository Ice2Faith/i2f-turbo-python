# -- coding: gbk --
import sys,time,calendar,random
#�����ļ�����

'''
ģ��
�����뼯������һ��py�ļ���
�γ�һ��ģ��

����ʱ��ֻ��Ҫʹ��import����ģ�鼴��

��������ģ�飺
import ģ���ļ���
ʹ��ʱ��
ģ���ļ���.������

ֻ����һЩ����
from ģ���� import ������
ʹ��ʱ��
ֱ��ʹ�ú���������

��Ȼ�е�ģ����̫�������Ը�����ȡ�������Է����Լ�ʹ��
import ģ���� as ����
from ģ���� import ������ as ��������
ʹ��ʱ��
����ʹ��Դ���ƣ�Ҳ����ʹ�ö���ı���

��������ݣ����ֿ���ʹ��ͨ���*����ʶ����ĳ��ģ���е���������

������
import myfunctional
from myfunctional import *

import myclass
from myclass import *
'''

def timeModule():
	# ʱ��ģ���ʹ��,import time
	import time
	utctime=time.time() #��ȡʱ���
	print(utctime)
	print(time.strftime('%Y-%m-%d %H:%M:%S')) #��ʽ��Ϊ�ַ�������
	print(time.strftime('%a %b %d %H:%M:%S %Y')) #��ʽ��Ϊ�ַ�������
	timeStruct=time.localtime() #����ʱ��ṹ�壬�ܹ�����Ļ�ȡ������Ϣ
	# timeStruct.tm_year...
	print(timeStruct)
	
def CalendarModule():
	# ����ģ���ʹ�ã�import calendar
	cal=calendar.month(2020,3) #��ȡһ������������ڵ��������·�
	print(cal) 
	
def randomModule():
	# ���ģ���ʹ�ã�import random
	print(random.randint(10,100)) #��ȫ����������
	print(random.choice([1,5,7,8])) #���ȡ�б��е�һ��
	ls=[1,2,3,4,5,6]
	random.shuffle(ls) #ϴ���㷨
	print(ls)
	rls=random.sample(ls,3) #������б���ѡȡ�����γ�һ�����б���
	print(rls)
	
def main():
	timeModule()
	CalendarModule()
	randomModule()
	
if __name__=='__main__':
	main()
	