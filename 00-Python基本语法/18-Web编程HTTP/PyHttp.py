#-*-coding:gbk-*-
import sys
import os

'''
	HTTP:
	建立在TCP/IP协议上的超文本传协议
	TCP、IP协议族
	
	HTTP过程：
		客户端：
			应用层（HTTP客户端）-传输层（TCP）-网络层（IP）-链路层（网络）
		服务器：
			网络（链路层）-网络层（IP）-传输层（TCP）-应用层（Http）
		HTTP+TCPHeader+IPHeader+以太网Header
	
	TCP三次握手：
		1.客户端：在吗，服务器 SYN
		2.服务器：在呢 SYN、ACK
		3.客户端：收到 ACK
		
	IP协议：
		在网卡进行工作
		完成MAC--IP地址转换，建立在ARP协议上
		
	DNS服务：
		完成域名到地址的转换
		1.发送端：这个网址的地址是什么？
		2.DNS：地址是...
		3.拿到地址之后的发送端就给目标机器发送访问请求了
		
	HTTP整体流程：
		1.客户端：域名的地址是多少
		2.DNS：地址是...
		3.客户端生成请求报文
		4.通过TCPIP发送请求报文
		5.服务端收到请求并解析请求
		6.返回对应的请求页面
		
	WEB服务器：
		完成端到端的信息传输IP-Port
		1.建立连接
		2.请求过程
		3.应答过程
		
	HTTP协议常用方法：
		GET：请求指定的页面信息，返回实体主体，数据直接在URL中体现
		POST：向指定资源提交数据进行处理，比如表单，文件等，数据被包含在请求体中，可能会导致页面的刷新或者变化
		HEAD：类似于GET，但是这是用于获取报头，响应体中没有内容
		PUT：客户端传送指定的数据代替指定的文档内容
		DELETE：请求服务器删除指定的文档
		OPTIONS:允许客户端查看服务器性能
		
	HTTP状态码含义：
		1**：请求收到，继续处理
		2**：成功，行为被成功接收、理解和采纳
		3**：重定向，为了完成请求，进一步执行的动作
		4**：客户端错误，请求包含语法错误或者无法响应请求
		5**：服务器错误，服务器不能实现一种明显无效的请求
	
	前端基础：
		组成：HTML+JS+CSS
		HTML：
			基本的标签组合而成
		CSS：
			对基本的HTML标签进行修饰美化
			Bootstrap前端框架，能够完成前端的美化和布局
		JavaScript:
			用于对网页元素的操作和逻辑的处理
			是一个工作在浏览器的解释性弱类型语言
			比如常见的输入检查和提示等
	
	Socket套接字
		TCP客户端			TCP服务器
							socket()
							bind()
							listen()
							accept()
		socket()
		connect()
		write()				read()
		read()				write()
		close()
							close()
		整体上来说，服务器要先开启
		分别进行创建套接字，绑定IP，端口
		开启监听
		当客户端创建了套接字并向服务器发起连接之后
		服务器接收客户端
		此后，服务器和客户端便可以进行通信了
		通信结束之后，客户端进行关闭
		一般来说服务器不进行主动的关闭
		如果进行关闭的话，服务器会在将要发送给客户端的信息发送结束之后，
		等待一段时间，如果客户端已经关闭
		断开连接之后，服务器再进行关闭
		
		一般来说，这是一个同步阻塞的过程，因此会使用线程进行解决
		不过也有将这种操作，进行封装，以达到异步操作，从而降低开发难度
		
	多线程模块：
		前面说了，网络来说基本上都是一个同步过程
		因此需要启用线程
		在Python中，提供了多线程模块
		下面是示例代码：
		```python
			from multiprocessing import Process
			
			def syncPrint(num):
				print('hello multiprocess',num)
				
			if __name__=='__main__':
				for i in range(5):
					process=Process(target=syncPrint,args=(i))
					process.start()
		```
		上面的代码中，我们开启了5个线程，分别进行输出
		因此我们也知道了使用过程，首先导入模块：
			from multiprocessing import Process
		其次，通过Process创建一个进程，参数：方法名，参数列表
			process=Process(target=syncPrint,args=(i,))
			这里，target也就是要执行的函数
			args也就是表名使用到的参数列表，他们使用()包裹,也就是一个元组
			原型：Process(target=func,args=(arg1,arg2,...))
			值得注意的是参数部分，如果只有一个参数的时候，可能会出现如下错误：
				in __init__
				self._args = tuple(args)
				TypeError: 'int' object is not iterable
				因此，解决方法，直接将参数转换为列表即可
				process=Process(target=syncPrint,args=([i]))
				也就是这里的差别：args=([i])
				也可以写成(i,)，这个逗号是有必要的，这表名了这是一个元组，仅有一个元素
		
	
	静态服务器：
		提供静态服务
		服务器过程：
			读取HTML
			添加响应头
			添加响应体
		实现：
			
			
'''

# 多线程测试部分 -----------------------------------------------------------------
from multiprocessing import Process
import time # 这里我们加一个延时，来体现线程的作用
def mulproFunc(num):
	time.sleep(5-num) # 因为总共循环5次，这样来说的话，理论上会是倒序输出
	print("mulproFunc",num)
	
def testMultiProcess():
	'''
	多线程测试函数
	'''
	for i in range(0,5):
		pro=Process(target=mulproFunc,args=(i,))
		pro.start()

# 静态服务器测试部分 -----------------------------------------------------------------
# 先运行PyStaticHttpServer
# 然后在浏览器中输入地址：127.0.0.1:8000/index.html
# 即可访问


def testHttp():
	pass

def main():
	print('PyHttp')
	testMultiProcess()

if __name__=='__main__':
	main()
