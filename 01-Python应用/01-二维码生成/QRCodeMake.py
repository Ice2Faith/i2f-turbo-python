#-*-coding=gbk-*-
import qrcode
import os
import sys
#��ά������
context='www.baidu.com'
#����ͼƬ���Ƽ���ʽ
imgname='qr.png'
#��������в���
if len(sys.argv)<3:
	context=str(input('��������Ҫ������ά�������\n>/ '))
	imgname=str(input('��������Ҫ�����ͼƬ���ƣ���Ҫ����׺(.png/.jpg)\n>/ '))
else:
	context=sys.argv[1]
	imgname=sys.argv[2]
'''
version=None:����Ӧ
box_size:ÿ����������
border:�߽�����
error_correction:ERROR_CORRECT_L:�ݴ���
L:7%
M:15%
Q:25%
H:30%
'''
#���ö�ά���ʽ
qr=qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=2)
qr.make(fit=True)
#�����ά������
qr.add_data(context)
#������ά��
img=qr.make_image()
#�����ά��
img.save(imgname)
#ϵͳ��ʽ�򿪱����ͼƬ
os.startfile(imgname)
