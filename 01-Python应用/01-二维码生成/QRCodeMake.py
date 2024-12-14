#-*-coding=gbk-*-
import qrcode
import os
import sys
#二维码内容
context='www.baidu.com'
#保存图片名称及格式
imgname='qr.png'
#检查命令行参数
if len(sys.argv)<3:
	context=str(input('请输入你要制作二维码的内容\n>/ '))
	imgname=str(input('请输入你要保存的图片名称，需要带后缀(.png/.jpg)\n>/ '))
else:
	context=sys.argv[1]
	imgname=sys.argv[2]
'''
version=None:自适应
box_size:每个方块像素
border:边界设置
error_correction:ERROR_CORRECT_L:容错率
L:7%
M:15%
Q:25%
H:30%
'''
#设置二维码格式
qr=qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=2)
qr.make(fit=True)
#传入二维码内容
qr.add_data(context)
#制作二维码
img=qr.make_image()
#保存二维码
img.save(imgname)
#系统方式打开保存的图片
os.startfile(imgname)
