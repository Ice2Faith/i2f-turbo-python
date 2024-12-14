#-*-coding:gbk-*-
import socket
'''
TCP 聊天室
'''
def ChatServer():
	host=socket.gethostname()
	port=12345
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((host,port))
	server.listen(1)
	print('Server Wait...')
	sock,addr=server.accept()
	print('Server Built.')
	info=sock.recv(1024).decode()
	while info !='byebye':
		if info:
			print('Accept:%s'%info)
		senddata=input('Your Send:')
		sock.send(senddata.encode())
		if senddata=='byebye':
			break
		info=sock.recv(1024).decode()
	sock.close()
	server.close()
def main():
	ChatServer()

if __name__=='__main__':
	main()