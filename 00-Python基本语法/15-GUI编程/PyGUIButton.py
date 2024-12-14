#-*-coding:utf-8-*-
import wx

class myFrame(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title,pos=(100,100),size=(600,400))
		panel=wx.Panel(self)
		self.title=wx.StaticText(panel,label="Login View",pos=(140,20))
		self.label_user=wx.StaticText(panel,label="name:",pos=(50,50))
		self.text_user=wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=wx.TE_LEFT)
		self.label_pwd=wx.StaticText(panel,label="pwd:",pos=(50,90))
		self.text_pwd=wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
		self.button_submit=wx.Button(panel,label='Submit',pos=(105,200))
		self.button_cancel=wx.Button(panel,label='Cancel',pos=(195,200))
		
def main():	
	app=wx.App()
	frame=myFrame(parent=None,id=-1,title="PyGUIButton Dev Ice2Faith")
	frame.Show()
	app.MainLoop()

if __name__=='__main__':
	main()