#-*-coding:gbk-*-
import socket

'''
客户端主动发起请求
服务器被动接受连接
'''
def TCPServer():
	'''
	使用浏览输入网址：127.0.0.1:8080访问
	'''
	host='127.0.0.1'
	port=8080
	web=socket.socket()
	web.bind((host,port))
	web.listen(5)#Set Max listen link
	print('Wait connect...')
	while True:
		conn,addr=web.accept()
		data=conn.recv(1024)#Accept Max Count
		print(data)
		conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello World')#Send Byte Data
		conn.close()


def main():
	TCPServer()

if __name__=='__main__':
	main()