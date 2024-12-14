# -- coding: gbk --
#字符串
#编码与解码
string='你好呀，python'
print(string)
stringcode=string.encode(encoding='utf-8',errors='replace')
print(stringcode)
stringret=stringcode.decode('utf-8')
print(stringret)
#字符串连接+
#求长度len(string)，默认字符个数为长度，其他要求进行encode编码后计算
print(len(string))
print(len(string.encode('gbk')))
#字符串截取，使用切片
print(string[2:-1:1])
#截取索引异常
try:
	print(string[15:20])
except IndexError:
	print("指定索引不存在")
#分割与合并
#分割后保存到列表中split(分割标记，最大分割次数=默认不限制)
list=string.split('，')
print(list)
#可迭代对象拼接为字符串：连接符.join(迭代对象)
newstring=' && '.join(list)
print(newstring)
#检索
newstring.index('py') #返回子串的开始位置
newstring.find('py') #查找子串位置，和index一样，只是index如果找不到会报异常
newstring.count('py') #计算子串个数

#用例
print('-'*20)
str1='this is a string test'
str1.replace('is','was') #注意this中的is也会被替换，如果需要的话，需要加前置空格如下
#str1.replace(' is',' was')
print(str1)
strg=str1.split(' ') #分离字符串，根据指定的分离符号，得到一个列表
print(strg)
str1=','.join(strg) #拼接字符串从列表，按照分割符进行合并，这里的分割符直接使用了','
print(str1) #语法为：str=sep.join(list)

#判断单词是否元音字母开头
aeo='aeiouAEIOU'
alist=[input('请输入一个单词:') for i in range(5)]
for word in alist:
	if word[0] in aeo:
		print('元音：',word)