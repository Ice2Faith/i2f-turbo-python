# -- coding: gbk --
def GetIntegerHex(integer,rmove):
	'''
	��integerʮ������ת��Ϊ2^rmove�����ַ���������
	���֧��ת��Ϊ��2,4,8,16,32����
	'''
	if type(integer)!=int or type(rmove)!=int:
		return 'Error values'
	mapping='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	mandnum=(2**rmove)-1
	if mandnum%2==0 or mandnum<2-1 or mandnum>32-1:
		return 'Bad direct hex'
	string='\0'
	while integer!=0:
		string+=mapping[integer&mandnum]
		integer=integer>>rmove
	rstring=ReverseString(string)
	return string
	
def ReverseString(string):
	'''
	���ظ����ַ����ķ�ת�ַ���
	'''
	restring='\0'
	slen=len(string)
	slen=slen-1
	while slen>=0:
		restring+=string[slen]
		slen=slen-1
	return restring


#����ת������
integer=0
rmove=0
integer=int(input('��������>> '))
rmove=int(input('����������λ��>> '))
tstring=GetIntegerHex(integer,rmove)
print(str(integer)+'>>'+tstring)
