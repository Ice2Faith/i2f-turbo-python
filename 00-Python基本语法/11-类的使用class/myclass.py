# -- coding: gbk --
#�����麯��֧��
import abc
#ÿ�����Ա��������Ҫself�������൱��thisָ�룬�Գ�Ա�����ķ���Ҳ��Ҫselfָ��
#����
class Animal:
	_m_foot=4
	_m_weight=5
	def __init__(self,foot=4,weight=5):
		self._m_foot=foot
		self._m_weight=weight
	#�麯������̬ʹ��
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

#�̳�
class Cat(Animal):
	def __init__(self,foot=4,weight=5):
		super().__init__(foot,weight)
	def speak(self):
		print('Cat Speack'+'\tFoot:'+str(self._m_foot)+'\tWeight:'+str(self._m_weight))

#�����
#��̬
def animalSpeak(animal):
	animal.speak()
#�����弰ʹ��
def classUse():
	animal=Animal()
	cat=Cat(4,2)
	animalSpeak(animal)
	animalSpeak(cat)
	
def main():
	classUse()
	
main()