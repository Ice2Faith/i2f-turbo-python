#-*-code:utf-8-*-
from PIL import Image
import pytesseract
import re
import sys

def PicOcr(imgName,langType='eng',grayPic=False):
	'''
	input:
		imgName:need to ocr image file name
		langType:default eng(english),set a suitable language type will get well result
		grayPic:default False(close),picture become gray mode
	'''
	img=Image.open(imgName)
	if grayPic==True:
		img=img.convert('L')
		img.save(imgName)
	text=pytesseract.image_to_string(img,langType)
	return text
	
def Main():
	picname=''
	if len(sys.argv)>=2:
		picname=sys.argv[1]
		print('Load File : ',sys.argv[1])
	else:
		picname=str(input('Please input a picture name/path :\n/> '))
	langhelp=['1.English_moden','2.Chinese_Simple','3.Express_Math','4.Chinese_Tradition',
	'5.English_middle','6.Japanese','7.Korean','8.Russia','9.German']
	lang=['eng','chi_sim','equ','chi_tra','enm','jpn','kor','rus','deu']
	print('Language List:\n----------------')
	for item in langhelp:
		print('\t',item)
	print('----------------')
	langtype=int(input('CLMode:Please Choice :\n/> '))
	if langtype>0 and langtype<10:
		gray=int(input('POMode:0.DefaultPic  1.PicToGray :\n/> '))
		if gray>=0 and gray<=1:
			ulang=lang[langtype-1]
			ugray=False
			if gray==1:
				ugray=True
			text=PicOcr(picname,ulang,ugray)
			print('\nOCR:>>>>>>>>>>')
			print(text)
			print('>>>>>>>>>>')
			savef=str(input('Save to File?1.Save else.NotSave:\n>/ '))
			if savef=='1':
				sfname=str(input('Please input save file name:\n>/ '))
				with open(sfname+'_ocr.txt',mode='w',encoding='utf-8') as sf:
					sf.write(text)
					sf.close()
		else:
			print('POMode Error!!')
	else:
		print('CLMode Error!!')

Main()