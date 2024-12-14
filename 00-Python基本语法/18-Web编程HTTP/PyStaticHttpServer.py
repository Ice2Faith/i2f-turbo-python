#-*-coding:gbk-*-
import sys
import os

# 下面是一个静态服务器的简单演示
import socket
import re 
from multiprocessing import Process
# 分别导入套接字、正则、多线程模块

HTML_ROOT_DIR="./Views"
# 设置静态服务器的根路径

class StaticHttpServer(object):
	def __init__(self):
		self.server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP协议，流协议
	def start(self):
		self.server_sock.listen(128) #设置最大监听数量
		print('等待客户端连接...')
		while True:
			client_sock,client_addr=self.server_sock.accept()
			print('用户[%s,%s]连接上了服务器'%client_addr)
			handle_client_process=Process(target=self.handle_client,args=(client_sock,))
			handle_client_process.start()
			client_sock.close()
			
	def handle_client(self,client_sock):
		# 获取请求数据
		request_data=client_sock.recv(1024)
		print('request data:',request_data)
		request_lines=request_data.splitlines() # 按照行进行分割请求
		for line in request_lines:
			print(line)
		request_start_line=request_lines[0] # 解析请求报文头
		print('*'*20)
		print(request_start_line.decode('utf-8'))
		
		#使用正则表达式，提取请求的文件名
		file_name=re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode('utf-8')).group(1)
		# 判断是否为根文件名
		if '/'==file_name:
			file_name='/index.html'
		
		print("#"*20,file_name)
		try:
			print("$"*20,HTML_ROOT_DIR+file_name)
			file=open(HTML_ROOT_DIR+file_name,'rb')
		except IOError:
			# 如果发生异常，则没找到文件，那就404
			response_start_line='HTTP/1.1 404 Not Found\r\n'
			response_headers='Server:My PyStatic Server\r\n'
			response_body='The file is not found!'
		else:
			file_data=file.read()
			file.close()
			# 构造响应体
			response_start_line='HTTP/1.1 200 OK\r\n'
			response_headers='Server:My PyStatic Server\r\n'
			response_body=file_data.decode('utf-8')
		
		response=response_start_line+response_headers+'\r\n'+response_body
		print('response data:',response)
		client_sock.send(bytes(response,'utf-8'))
		client_sock.close()
		
	def bind(self,port):
		self.server_sock.bind(("",port)) #使用默认主机地址绑定一个端口

def main():
	print('PyStaticHttpServer')
	httpServer=StaticHttpServer()
	httpServer.bind(8000)
	httpServer.start()

if __name__=='__main__':
	main()
