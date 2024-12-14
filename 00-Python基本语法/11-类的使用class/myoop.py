#-*-coding:gbk-*-
import sys
import os
import abc
'''
约定规则
类名称：首字母大写
属性和方法中（对于不同模块之间也是如此）
（这也就是封装）
	一个下划线开头表示protected,外部可以访问
	两个下划线开头表示private，外部不可以访问

可以通过对象.属性名 动态的添加新的属性

类函数应该包含一个self变量，相当于其他语言中的this
	访问内部变量一定要使用self.的方式进行访问，否则会访问不到
	也就是相当的鸡肋，不像其他语言一样，自动补上，
	不用自己写明self就好了
	
函数还可以加注解，注明是一个抽象函数，需要import abc
@abc.abstractmethod
def func():
	pass
'''
class Car:
	# 定义一个内部私有变量，外部不可访问
	__color='red'
	# 构造函数，可以理解为
	def __init__(self,speed=4):
		#在构造里面添加了一个成员变量，这样做，外部是无法访问的
		#只能通过提供的方法进行访问(仅限有下划线开头的变量，否则还是可以访问到的)
		self.__speed=speed
		print('this object is constructing...')
	# 析构函数
	def __del__(slef):
		print('this object is destroying...')
		
	#一些普通的get/set方法
	def setColor(self,color):
		self.__color=color
	# 提供方法进行访问内部变量
	def getSpeed(self):
		return self.__speed
	def setSpeed(self,speed):
		self.__speed=speed
	def run(self):
		print('This %s car is running %d km/s.'%(self.__color,self.__speed))
		
	#属性装饰器--实现内部变量的操作控制【注意是通过注解的方式实现的】
	#作用就是，将一个方法，修饰成为一个变量的用法，
	#好处就是，外部看起来它就是一个变量，但是自己可以控制，和C#中的属性类似
	#调用不在需要color(),而是像成员变量一样使用
	#一般来说，需要下面两个方法一起使用，这样就实现了读写的控制
	@property 
	def color(self): #这就相当于一个只读变量
		return self.__color
	@color.setter #设置一个修饰器的，写入方法，注意写法：@装饰器.setter
	def color(self,color):	#由于只读，如果需要可写，那就对color的setter进行修饰
		self.__color=color
	@color.deleter	#设置一个修饰器的，删除方法，一般来说不需要
	def color(self):
		del self.color
		print('color has been deleted.')
		
def carTest():
	# 创建对象
	bmw=Car()
	# 添加新的成员变量
	bmw.size=[15,20]
	# 函数调用
	bmw.setColor('blue')
	# 虽然下面这种方式，看起来是访问了内部变量，但是这里只是添加了一个新的属性，和内部变量无关
	# 但是继续直接访问的话，将会覆盖内部变量进行访问
	# bmw.__color='yellow'
	#对于私有成员是访问不到的，会发生错误，这里进行直接访问
	# print(bmw.__color)
	
	print(bmw.getSpeed())
	bmw.setSpeed(6)
	# 私有变量无法访问
	# print(bmw.__speed)
	
	#使用属性装饰器
	bmw.color='blue'
	print(bmw.color)
	
	bmw.run()
	
'''
类的特性--继承
单继承格式：
	class 子类(父类):
		没有指明父类的时候，默认就是Object是父类
		super().__init__()进行调用父类构造
		
多继承格式
	class 子类(父类1，父类2...):
		注意，这里调用父类构造就不能简单的使用super()
			父类1.__init__(self)
			父类2.__init__(self)
		使用以上方式进行调用指定父类的构造，注意参数self是必须的
			当然你还是适用super()还是可以的，但是有时候会出现一些问题
			
	注意：当多继承父类中拥有相同的属性的时候
		调用的时候
			根据，父类列表的第一个父类来决定
			比如：
				class A(B,C)
				那么同名的将会是用B里面的，也就是父类列表B,C的第一个B中的
'''
class Robot:
	def hunt(self):
		print('Robot hunt')
	
class Animal:
	#父类的构造
	def __init__(self):
		print('Animal init')

	def speak(self):
		print('Animal speak')

#这样就是一个单继承
class Dog(Animal):
	def __init__(self):
		#调用父类的构造
		super().__init__() #通过super()拿到父类，调用其构造
		print('Dog init')
	def shout(self):
		print('Dog shout')
	# 子类中直接进行重写即可
	def speak(self):
		print('Dog speak')
		
#这样就是一个多继承
class RobotCat(Animal,Robot):
	def __init__(self):
		Animal.__init__(self)
		Robot.__init__(self)
	def hunt(self):
		print('RobotCat hunt')
	def speak(self):
		print('RobotCat speak')

'''
多态，也就是派生自统一父类的子类，都拥有父类的相同的行为，
当我们调用父类方法的时候，即使是子类对象，那么也能够进行调用
这就是一个多态
在Python中可以这么简单理解就行
'''
#一个简单的多态	
#只要传递进来的是Animal或者其子类的对象都是可以进行调用的
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
从其他文件中导入类
from 模块名 import 类列表
例如：
from AnimalExport import Animal,Dog,Cat
其实这个和模块的使用时一样的，就不详细说了
'''

'''
内部类的简单使用
可以直接进行类的嵌套，
但是外部类使用内部内实例化的时候，需要加self限定,或者加外部类名限定
'''
class Tools:
	class InearTool:
		def tell(self):
			print('Tools-InearTool tell')
	def show(self):
		b=Tools.InearTool() #注意，实例化内部类的方式
		# b=self.InearTool() #注意，实例化内部类的方式
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
