#-*-coding:gbk-*-
import socket
'''
�ͻ���������������
������������������
'''
def TCPClient():
	host='127.0.0.1'
	port=8080
	client=socket.socket()
	client.connect((host,port))
	data=input('Please input:')
	client.send(data.encode())
	recvdata=client.recv(1024).decode()
	print('Receive:',recvdata)

def main():
	TCPClient()

if __name__=='__main__':
	main()