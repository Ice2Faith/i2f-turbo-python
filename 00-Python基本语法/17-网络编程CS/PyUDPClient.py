#-*-coding:gbk-*-
import socket
'''
UDP �ͻ���
'''
def UDPClient():
	client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	data=input('Please input Temprature:')
	client.sendto(data.encode(),('127.0.0.1',8888))
	print('Exchanged temprature:%s'%client.recv(1024).decode())
	client.close()

def main():
	UDPClient()

if __name__=='__main__':
	main()