#-*-coding:gbk-*-
import sys
import os

# ������һ����̬�������ļ���ʾ
import socket
import re 
from multiprocessing import Process
# �ֱ����׽��֡����򡢶��߳�ģ��

HTML_ROOT_DIR="./Views"
# ���þ�̬�������ĸ�·��

class StaticHttpServer(object):
	def __init__(self):
		self.server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCPЭ�飬��Э��
	def start(self):
		self.server_sock.listen(128) #��������������
		print('�ȴ��ͻ�������...')
		while True:
			client_sock,client_addr=self.server_sock.accept()
			print('�û�[%s,%s]�������˷�����'%client_addr)
			handle_client_process=Process(target=self.handle_client,args=(client_sock,))
			handle_client_process.start()
			client_sock.close()
			
	def handle_client(self,client_sock):
		# ��ȡ��������
		request_data=client_sock.recv(1024)
		print('request data:',request_data)
		request_lines=request_data.splitlines() # �����н��зָ�����
		for line in request_lines:
			print(line)
		request_start_line=request_lines[0] # ����������ͷ
		print('*'*20)
		print(request_start_line.decode('utf-8'))
		
		#ʹ��������ʽ����ȡ������ļ���
		file_name=re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode('utf-8')).group(1)
		# �ж��Ƿ�Ϊ���ļ���
		if '/'==file_name:
			file_name='/index.html'
		
		print("#"*20,file_name)
		try:
			print("$"*20,HTML_ROOT_DIR+file_name)
			file=open(HTML_ROOT_DIR+file_name,'rb')
		except IOError:
			# ��������쳣����û�ҵ��ļ����Ǿ�404
			response_start_line='HTTP/1.1 404 Not Found\r\n'
			response_headers='Server:My PyStatic Server\r\n'
			response_body='The file is not found!'
		else:
			file_data=file.read()
			file.close()
			# ������Ӧ��
			response_start_line='HTTP/1.1 200 OK\r\n'
			response_headers='Server:My PyStatic Server\r\n'
			response_body=file_data.decode('utf-8')
		
		response=response_start_line+response_headers+'\r\n'+response_body
		print('response data:',response)
		client_sock.send(bytes(response,'utf-8'))
		client_sock.close()
		
	def bind(self,port):
		self.server_sock.bind(("",port)) #ʹ��Ĭ��������ַ��һ���˿�

def main():
	print('PyStaticHttpServer')
	httpServer=StaticHttpServer()
	httpServer.bind(8000)
	httpServer.start()

if __name__=='__main__':
	main()
