#-*-coding:gbk-*-
import socket
'''
TCP 聊天室
'''
def ChatClient():
	host=socket.gethostname()
	port=12345
	client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((host,port))
	print('Connect Success.')
	info=''
	while info !='byebye':
		senddata=input('Your send:')
		client.send(senddata.encode())
		if senddata=='byebye':
			break
		info=client.recv(1024).decode()
		print('Recv:%s'%info)
	client.close()
	
def main():
	ChatClient()

if __name__=='__main__':
	main()