#-*-coding:utf-8-*-
import wx
'''
extend calss
'''
class myApp(wx.App):
	def OnInit(self):
		frame=wx.Frame(parent=None,title="PyGUImyApp Dev Ice2Faith")
		frame.Show()
		return True
'''
extend calss
'''
class myFrame(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title,pos=(100,100),size=(600,400))
		panel=wx.Panel(self)#建立画板
		font=wx.Font(18,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
		title=wx.StaticText(panel,label='Python StaticText',pos=(100,20))
		title.SetFont(font)
		
def main():
#创建APP的三种方式
#使用子类
	'''
	app=myApp()
	app.MainLoop()
	'''
#直接使用
	'''
	app=wx.App()
	frame=wx.Frame(parent=None,title="PyGUIDirectUse Dev Ice2Faith")
	frame.Show()
	app.MainLoop()
	'''
#使用wx.Frame框架
	'''
	app=wx.App()
	frame=myFrame(parent=None,id=-1,title="PyGUImyFrame Dev Ice2Faith")
	frame.Show()
	app.MainLoop()
	'''
#控件介绍
#文本类StaticText
	app=wx.App()
	frame=myFrame(parent=None,id=-1,title="PyGUIStaticText Dev Ice2Faith")
	frame.Show()
	app.MainLoop()

	
	

if __name__=='__main__':
	main()