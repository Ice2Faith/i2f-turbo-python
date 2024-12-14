#-*-coding:gbk-*-
import socket
'''
UDP 服务器
'''
def UDPServer():
	server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server.bind(('127.0.0.1',8888))
	print('UDP Set port 8888')
	data,addr=server.recvfrom(1024)#返回值是一个元组
	data=float(data)*1.8+32
	senddata='EXTemprature:'+str(data)
	print('Recv from %s:%s'%(addr,data))
	server.sendto(senddata.encode(),addr)
	server.close()

def main():
	UDPServer()

if __name__=='__main__':
	main()