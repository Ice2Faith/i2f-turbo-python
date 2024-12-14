# -- coding: gbk --
def GetIntegerHex(integer,rmove):
	'''
	将integer十进制数转换为2^rmove进制字符串并返回
	因此支持转换为：2,4,8,16,32进制
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
	返回给定字符串的反转字符串
	'''
	restring='\0'
	slen=len(string)
	slen=slen-1
	while slen>=0:
		restring+=string[slen]
		slen=slen-1
	return restring


#进制转换测试
integer=0
rmove=0
integer=int(input('输入整数>> '))
rmove=int(input('请输入右移位数>> '))
tstring=GetIntegerHex(integer,rmove)
print(str(integer)+'>>'+tstring)
