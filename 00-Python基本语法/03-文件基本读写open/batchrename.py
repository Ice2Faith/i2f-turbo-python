#-*-coding:gbk-*-
import os

def main():
	print('batch rename')
	floder='./'
	prefix='prefix-'
	sel=input('1.batch add prefix [prefix-]\n2.batch remove prefix\n')
	if sel!='1' and sel!='2':
		return
	filelist=os.listdir(floder)
	for name in filelist:
		if sel=='1':
			os.rename(floder+name,floder+prefix+name)
		elif sel=='2':
			os.rename(floder+name,floder+name[len(prefix):])

if __name__=='__main__':
	main()
	