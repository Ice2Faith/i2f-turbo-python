#-*-coding:gbk-*-
'''
	����ͷ��
	���糬ʱ
	�������
	��ҳ����
'''
import requests
#�����������������쳣��
from requests import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup

def HeadersSolve():
	'''
	����ͷ����������
	'''
	#�������������ַ
	url='https://www.whatismyip.com/'
	#����ͷ������headers
	headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWedKit/537.36 (KHTML,like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
	#������ҳ���󣬲�ָ��ͷ��
	respond=requests.get(url,headers=headers)
	#��ӡ�����ת��������룩
	print(respond.content.decode('utf-8'))

def BeyondTime():
	'''
	���糬ʱ
	'''
	#ѭ�����ʣ������쳣
	for i in range(50):
		try:
			#���÷���URL�͵ȴ�ʱ��
			respond=requests.get('http://www.baidu.com',timeout=0.1)
			print(respond.status_code)	#������
		except ReadTimeout:#Exception as e:
			#print('Error ',str(e))	#��ӡ�쳣
			print('Time Out')
		except HTTPError:
			print('HTTP Error')
		except RequestException:
			print('Request Exception')
			
def Proxy():
	'''
	�������
	�����������ѯ��ַ��www.xicidaili.com
	'''
	proxy={'http':'183.32.226.35:61234',
			'https':'112.85.168.197:9999'}
	respond=requests.get('https://www.baidu.com',proxies=proxy)
	print(respond.content.decode('utf-8'))
	
def TransHtml():
	'''
	BeautifulSoup4 HTML������
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