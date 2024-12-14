#-*-coding:utf-8-*-
import wx

class myFrame(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title,pos=(100,100),size=(400,300))
		panel=wx.Panel(self)
		
		self.button_submit=wx.Button(panel,label='Submit')
		self.button_cancel=wx.Button(panel,label='Cancel')
		
		self.title=wx.StaticText(panel,label="Login View")
		self.label_user=wx.StaticText(panel,label="name:")
		self.text_user=wx.TextCtrl(panel,style=wx.TE_LEFT)
		self.label_pwd=wx.StaticText(panel,label="pwd :")
		self.text_pwd=wx.TextCtrl(panel,style=wx.TE_PASSWORD)
		
		self.sizer_hor_user=wx.BoxSizer(wx.HORIZONTAL)
		self.sizer_hor_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
		self.sizer_hor_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)
		
		self.sizer_hor_pwd=wx.BoxSizer(wx.HORIZONTAL)
		self.sizer_hor_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border=5)
		self.sizer_hor_pwd.Add(self.text_pwd,proportion=1,flag=wx.ALL,border=5)
		
		self.sizer_hor_button=wx.BoxSizer(wx.HORIZONTAL)
		self.sizer_hor_button.Add(self.button_submit,proportion=0,flag=wx.ALL,border=5)
		self.sizer_hor_button.Add(self.button_cancel,proportion=0,flag=wx.ALL,border=5)
		
		self.sizer_ver_all=wx.BoxSizer(wx.VERTICAL)
		self.sizer_ver_all.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
		self.sizer_ver_all.Add(self.sizer_hor_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
		self.sizer_ver_all.Add(self.sizer_hor_pwd,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
		self.sizer_ver_all.Add(self.sizer_hor_button,proportion=0,flag=wx.TOP|wx.ALIGN_CENTER,border=15)
		panel.SetSizer(self.sizer_ver_all)

		
		
def main():	
	app=wx.App()
	frame=myFrame(parent=None,id=-1,title="PyGUIButton Dev Ice2Faith")
	frame.Show()
	app.MainLoop()

if __name__=='__main__':
	main()