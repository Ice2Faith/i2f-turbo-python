#-*-coding:gbk-*-
import sys
import os
import abc
'''
Լ������
�����ƣ�����ĸ��д
���Ժͷ����У����ڲ�ͬģ��֮��Ҳ����ˣ�
����Ҳ���Ƿ�װ��
	һ���»��߿�ͷ��ʾprotected,�ⲿ���Է���
	�����»��߿�ͷ��ʾprivate���ⲿ�����Է���

����ͨ������.������ ��̬������µ�����

�ຯ��Ӧ�ð���һ��self�������൱�����������е�this
	�����ڲ�����һ��Ҫʹ��self.�ķ�ʽ���з��ʣ��������ʲ���
	Ҳ�����൱�ļ��ߣ�������������һ�����Զ����ϣ�
	�����Լ�д��self�ͺ���
	
���������Լ�ע�⣬ע����һ������������Ҫimport abc
@abc.abstractmethod
def func():
	pass
'''
class Car:
	# ����һ���ڲ�˽�б������ⲿ���ɷ���
	__color='red'
	# ���캯�����������Ϊ
	def __init__(self,speed=4):
		#�ڹ������������һ����Ա���������������ⲿ���޷����ʵ�
		#ֻ��ͨ���ṩ�ķ������з���(�������»��߿�ͷ�ı����������ǿ��Է��ʵ���)
		self.__speed=speed
		print('this object is constructing...')
	# ��������
	def __del__(slef):
		print('this object is destroying...')
		
	#һЩ��ͨ��get/set����
	def setColor(self,color):
		self.__color=color
	# �ṩ�������з����ڲ�����
	def getSpeed(self):
		return self.__speed
	def setSpeed(self,speed):
		self.__speed=speed
	def run(self):
		print('This %s car is running %d km/s.'%(self.__color,self.__speed))
		
	#����װ����--ʵ���ڲ������Ĳ������ơ�ע����ͨ��ע��ķ�ʽʵ�ֵġ�
	#���þ��ǣ���һ�����������γ�Ϊһ���������÷���
	#�ô����ǣ��ⲿ������������һ�������������Լ����Կ��ƣ���C#�е���������
	#���ò�����Ҫcolor(),�������Ա����һ��ʹ��
	#һ����˵����Ҫ������������һ��ʹ�ã�������ʵ���˶�д�Ŀ���
	@property 
	def color(self): #����൱��һ��ֻ������
		return self.__color
	@color.setter #����һ���������ģ�д�뷽����ע��д����@װ����.setter
	def color(self,color):	#����ֻ���������Ҫ��д���ǾͶ�color��setter��������
		self.__color=color
	@color.deleter	#����һ���������ģ�ɾ��������һ����˵����Ҫ
	def color(self):
		del self.color
		print('color has been deleted.')
		
def carTest():
	# ��������
	bmw=Car()
	# ����µĳ�Ա����
	bmw.size=[15,20]
	# ��������
	bmw.setColor('blue')
	# ��Ȼ�������ַ�ʽ���������Ƿ������ڲ���������������ֻ�������һ���µ����ԣ����ڲ������޹�
	# ���Ǽ���ֱ�ӷ��ʵĻ������Ḳ���ڲ��������з���
	# bmw.__color='yellow'
	#����˽�г�Ա�Ƿ��ʲ����ģ��ᷢ�������������ֱ�ӷ���
	# print(bmw.__color)
	
	print(bmw.getSpeed())
	bmw.setSpeed(6)
	# ˽�б����޷�����
	# print(bmw.__speed)
	
	#ʹ������װ����
	bmw.color='blue'
	print(bmw.color)
	
	bmw.run()
	
'''
�������--�̳�
���̳и�ʽ��
	class ����(����):
		û��ָ�������ʱ��Ĭ�Ͼ���Object�Ǹ���
		super().__init__()���е��ø��๹��
		
��̳и�ʽ
	class ����(����1������2...):
		ע�⣬������ø��๹��Ͳ��ܼ򵥵�ʹ��super()
			����1.__init__(self)
			����2.__init__(self)
		ʹ�����Ϸ�ʽ���е���ָ������Ĺ��죬ע�����self�Ǳ����
			��Ȼ�㻹������super()���ǿ��Եģ�������ʱ������һЩ����
			
	ע�⣺����̳и�����ӵ����ͬ�����Ե�ʱ��
		���õ�ʱ��
			���ݣ������б�ĵ�һ������������
			���磺
				class A(B,C)
				��ôͬ���Ľ�������B����ģ�Ҳ���Ǹ����б�B,C�ĵ�һ��B�е�
'''
class Robot:
	def hunt(self):
		print('Robot hunt')
	
class Animal:
	#����Ĺ���
	def __init__(self):
		print('Animal init')

	def speak(self):
		print('Animal speak')

#��������һ�����̳�
class Dog(Animal):
	def __init__(self):
		#���ø���Ĺ���
		super().__init__() #ͨ��super()�õ����࣬�����乹��
		print('Dog init')
	def shout(self):
		print('Dog shout')
	# ������ֱ�ӽ�����д����
	def speak(self):
		print('Dog speak')
		
#��������һ����̳�
class RobotCat(Animal,Robot):
	def __init__(self):
		Animal.__init__(self)
		Robot.__init__(self)
	def hunt(self):
		print('RobotCat hunt')
	def speak(self):
		print('RobotCat speak')

'''
��̬��Ҳ����������ͳһ��������࣬��ӵ�и������ͬ����Ϊ��
�����ǵ��ø��෽����ʱ�򣬼�ʹ�����������ôҲ�ܹ����е���
�����һ����̬
��Python�п�����ô��������
'''
#һ���򵥵Ķ�̬	
#ֻҪ���ݽ�������Animal����������Ķ����ǿ��Խ��е��õ�
def AniSpeak(ani):
	ani.speak()
		
def AnimalTest():
	ani=Animal()
	ani.speak()
	
	dog=Dog()
	dog.speak()
	
	rcat=RobotCat()
	rcat.hunt()
	rcat.speak()
	
	AniSpeak(ani)
	AniSpeak(dog)
	AniSpeak(rcat)
	
'''
�������ļ��е�����
from ģ���� import ���б�
���磺
from AnimalExport import Animal,Dog,Cat
��ʵ�����ģ���ʹ��ʱһ���ģ��Ͳ���ϸ˵��
'''

'''
�ڲ���ļ�ʹ��
����ֱ�ӽ������Ƕ�ף�
�����ⲿ��ʹ���ڲ���ʵ������ʱ����Ҫ��self�޶�,���߼��ⲿ�����޶�
'''
class Tools:
	class InearTool:
		def tell(self):
			print('Tools-InearTool tell')
	def show(self):
		b=Tools.InearTool() #ע�⣬ʵ�����ڲ���ķ�ʽ
		# b=self.InearTool() #ע�⣬ʵ�����ڲ���ķ�ʽ
		b.tell()
		
def InearClassTest():
	a=Tools()
	a.show()
	
	b=Tools.InearTool()
	b.tell()
		
def main():
	print('myoop')
	carTest()
	print('-'*20)
	AnimalTest()
	print('-'*20)
	InearClassTest()
	

if __name__=='__main__':
	main()
