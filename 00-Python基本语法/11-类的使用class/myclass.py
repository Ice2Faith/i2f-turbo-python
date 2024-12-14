# -- coding: gbk --
#引入虚函数支持
import abc
#每个类成员函数都需要self参数，相当于this指针，对成员变量的访问也需要self指定
#基类
class Animal:
	_m_foot=4
	_m_weight=5
	def __init__(self,foot=4,weight=5):
		self._m_foot=foot
		self._m_weight=weight
	#虚函数，多态使用
	@abc.abstractmethod
	def speak(self):
		print('Animal Speack'+'\tFoot:'+str(self._m_foot)+'\tWeight:'+str(self._m_weight))
	def GetFoot(self):
		return self._m_foot
	def GetWeight(self):
		return self._m_weight
	def SetFoot(self,foot):
		self._m_foot=foot
	def SetWeight(self,weight):
		self._m_weight=weight

#继承
class Cat(Animal):
	def __init__(self,foot=4,weight=5):
		super().__init__(foot,weight)
	def speak(self):
		print('Cat Speack'+'\tFoot:'+str(self._m_foot)+'\tWeight:'+str(self._m_weight))

#类测试
#多态
def animalSpeak(animal):
	animal.speak()
#对象定义及使用
def classUse():
	animal=Animal()
	cat=Cat(4,2)
	animalSpeak(animal)
	animalSpeak(cat)
	
def main():
	classUse()
	
main()