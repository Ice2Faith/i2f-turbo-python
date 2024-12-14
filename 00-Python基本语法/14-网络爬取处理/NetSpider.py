#-*-coding:gbk-*-
'''
	处理头部
	网络超时
	代理服务
	网页解析
'''
import requests
#导入网络请求三种异常类
from requests import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup

def HeadersSolve():
	'''
	处理头部网络请求
	'''
	#国外请求测试网址
	url='https://www.whatismyip.com/'
	#请求头部处理，headers
	headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWedKit/537.36 (KHTML,like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
	#发起网页请求，并指定头部
	respond=requests.get(url,headers=headers)
	#打印结果（转换编码解码）
	print(respond.content.decode('utf-8'))

def BeyondTime():
	'''
	网络超时
	'''
	#循环访问，捕获异常
	for i in range(50):
		try:
			#设置访问URL和等待时间
			respond=requests.get('http://www.baidu.com',timeout=0.1)
			print(respond.status_code)	#请求码
		except ReadTimeout:#Exception as e:
			#print('Error ',str(e))	#打印异常
			print('Time Out')
		except HTTPError:
			print('HTTP Error')
		except RequestException:
			print('Request Exception')
			
def Proxy():
	'''
	代理服务
	代理服务器查询网址：www.xicidaili.com
	'''
	proxy={'http':'183.32.226.35:61234',
			'https':'112.85.168.197:9999'}
	respond=requests.get('https://www.baidu.com',proxies=proxy)
	print(respond.content.decode('utf-8'))
	
def TransHtml():
	'''
	BeautifulSoup4 HTML解析库
	'''
	respond=requests.get('http://www.baidu.com')
	soup=BeautifulSoup(respond.content.decode('utf-8'),features='lxml')
	#print(soup)#content
	#print(soup.title)#title
	#print(soup.prettify())#format
	print(soup.find('title').text)#get title
	

def main():
	#HeadersSolve()
	#BeyondTime()
	#Proxy()
	TransHtml()
	
if __name__=='__main__':
	main()