# -- coding: gbk --
import struct,pickle
'''
先来两个简单的示例
'''
def ReadTextFile(filename):
	'''
	读取一个文本文件内容显示在屏幕上
	'''
	fp=open(filename,'r')
	string='\0'
	while(True):
		string=fp.read()
		print(string)
		if string=='':
			break
	fp.close()
	

def SaveTextToFile(filename):
	'''
	新建一个名为：filename的文件
	在内部输入字符串，知道遇到#号开始的字符串结束输入
	'''
	fp=open(filename,'a+')
	string='0'
	while(True):
		string=input('请输入(#号结束)>> ')
		if string[0]=='#':
			break
		print(string,file=fp)
	fp.close()

'''
#文件保存测试
filename=input('请输入你要保存的文件名称:')
SaveTextToFile(filename)
'''

'''
#读取文件测试
ReadTextFile('01.txt')
'''

'''
文件的打开，需要文件已存在，否则会抛出错误：FileNotFoundError,
可以使用try: ... except FileNotFoundError: ...进行异常处理 
而文件的写入，则不需要考虑是否存在，不存在会自动创建
'''
def ReadFile():
	try:
		# 文件的打开方式，类似C的方式，连打开的模式和C都基本一样，还可以指定编码格式
		fp=open('aaa.txt','r',encoding='utf-8')
		str=fp.read() #这样是整个文件读取完毕
		# 如果使用read(20),这样就可以读取指定字符数的串
		
		print(str)
		pos=fp.tell() # 获取当前文件指针位置
		print(pos)

		fp.seek(0,0) #设置文件指针，参数：偏移，相对值（0：文件头，1：当前，2：文件尾）
		# 这里就设置文件指针指向文件开头，又可以读取了
		# 需要注意，反向的时候，需要用二进制方式打开才行
		
		#文件被打开之后是需要关闭的
		fp.close()
	except FileNotFoundError:
		print('文件不存在')
	
def WriteFile():
	#这里就创建了一个空文件
	fp=open('aaa.txt','w',encoding='utf-8')
	#写入一行文本，并且返回写入的个数
	fp.write('hello,这是Python的文件写入信息\n')
	# 也可以使用writelines()写入一个列表，自动实现换行
	fp.close()

'''
使用with方式进行文件读写
'''
def withOpenFile():
	#使用with方式，文件的关闭是自动关闭的，不需要手动关闭
	#你也可以认为，在with代码块结束的时候，自动关闭
	#但是，依旧要注意文件不存在异常
	with open('aaa.txt','w') as fp:
		fp.write('hello,这是Python的with文件写入信息\n')
	with open('aaa.txt','r') as fp:
		print(fp.read())
'''
全部读取文件并按行分割
'''
def readAllLineSplit():
	# 如果想全部读取，并按照行分割：read().splitlines()，这样得到的就是一个分割好的字符串列表
	# 并且字符串列表是不包含换行符\n的
	fp=open('aaa.txt','r')
	lines=fp.read().splitlines()
	for line in lines:
		print(line)
	fp.close()

'''
逐行读取
'''
def readSingleLine():
	# 如果想一行一行的读取的话，可以使用readline()方法，这样获得一行，是包含换行符的，可以使用strip()方法去除空行
	# 如果到文件结束，就返回空串
	fp=open('aaa.txt','r')
	line=fp.readline()
	while line!='':
		print(line)
		line=fp.readline()
	fp.close()
	'''
	# 还可以写的更简洁
	fp=open('aaa.txt','r')
	for line in fp:
		print(line)
	fp.close()
	'''
	
'''
格式化读取
'''
def readFormat():
	fp=open('aaa.txt','r')
	# 通过逐行读取之后按照规则分割字符串即可
	line=fp.readline().strip()
	valus=line.split()
	#这样就分割好了数据
	fp.close()

'''
二进制的读写，import struct
借助pack和unpack进行打包和解包

也可使用import pickle，这里以种种方式为例，使用struct方式的具体搜索
借助dump和load进行打包和解包
'''
def binaryIOFile():
	fp=open('bbb.bin','wb')
	pickle.dump(12,fp)
	pickle.dump(True,fp)
	pickle.dump(12.125,fp)
	fp.close()
	
	fp=open('bbb.bin','rb')
	a=pickle.load(fp) #返回的是字符串，如果需要，类型强转
	b=pickle.load(fp)
	c=pickle.load(fp)
	print(a,b,c)
	fp.close()
	
def fileSystemOperation():
	os.rename('source.txt','target.txt') #重命名
	os.remove('delete.txt')	#删除文件
	os.mkdir('floder')	#创建文件夹
	os.rmdir('delete dir') #删除文件夹
	fileNamelist=os.listdir('./') #获得文件夹下的文件列表，结果不是绝对路径

def main():
	WriteFile()
	ReadFile()
	withOpenFile()
	binaryIOFile()

if __name__=='__main__':
	main()