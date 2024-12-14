#-*-code:utf-8-*-
import pymysql
def CreateTable():
	hcon=pymysql.connect(host='localhost',user='root',password='ltb12315',database='contract',charset='utf8')
	hcur=hcon.cursor()
	hcur.execute('drop table if exists contractlist')
	ctable='''
	create table contractlist
	(
	ID int(10) primary key,
	NAME varchar(20) not null,
	TELF char(11) not null,
	TELS char(11),
	OTHER varchar(50)
	)engine=myisam charset=utf8;
	'''
	hcur.execute(ctable)
	hcur.close()
	hcon.close()
	
def AddInfo(hcon,hcur):
	id=int(input('please input ID: '))
	name=str(input('please input Name: '))
	telf=str(input('please input Tel 1: '))
	tels=str(input('please input Tel 2: '))
	other=str(input('please input other: '))
	sql="insert into contractlist(id,name,telf,tels,other) values(%s,%s,%s,%s,%s)"
	try:
		hcur.execute(sql,(id,name,telf,tels,other))
		hcon.commit()
	except:
		hcon.rollback()
	
def DeleteInfo(hcon,hcur):
	SelectInfo(hcon,hcur)
	did=int(input('please input id of delete: '))
	sql="delete from contractlist where id=%s"
	try:
		hcur.execute(sql,(did,))
		hcon.commit()
	except:
		hcon.rollback()

def UpdateInfo(hcon,hcur):
	SelectInfo(hcon,hcur)
	did=int(input('please input id of update: '))
	
	sqlname="update contractlist set name=%s where id=%s"
	name=str(input('please input Name: '))
	try:
		hcur.execute(sqlname,(name,did))
		hcon.commit()
	except:
		hcon.rollback()
	
	sqltelf="update contractlist set telf=%s where id=%s"
	telf=str(input('please input Tel 1: '))
	try:
		hcur.execute(sqltelf,(telf,did))
		hcon.commit()
	except:
		hcon.rollback()
	
	sqltels="update contractlist set tels=%s where id=%s"
	tels=str(input('please input Tel 2: '))
	try:
		hcur.execute(sqltels,(tels,did))
		hcon.commit()
	except:
		hcon.rollback()
		
	sqlothers="update contractlist set other=%s where id=%s"
	other=str(input('please input other: '))
	try:
		hcur.execute(sqlothers,(other,did))
		hcon.commit()
	except:
		hcon.rollback()
	
	
def SelectInfo(hcon,hcur):
	hcur.execute("select * from contractlist")
	result=hcur.fetchall()
	ptitle=('ID','Name','Tel 1','Tel 2','Other')
	print(ptitle)
	for findex in result:
		print(findex)
		
	print('')

	
def Meau():
	print('1.diaplay')
	print('2.add')
	print('3.update')
	print('4.delete')
	print('5.cls')
	print('0.exit')
	sel=9
	while(sel>5 or sel<0):
		sel=int(input('please choice: '))
	return sel
	
def main():
	#CreateTable()
	hcon=pymysql.connect(host='localhost',user='root',password='ltb12315',database='contract',charset='utf8')
	hcur=hcon.cursor()
	while(True):
		sel=Meau()
		if(sel==1):
			SelectInfo(hcon,hcur)
		elif(sel==2):
			AddInfo(hcon,hcur)
		elif(sel==3):
			UpdateInfo(hcon,hcur)
		elif(sel==4):
			DeleteInfo(hcon,hcur)
		elif(sel==5):
			os.system('cls')
		else:
			break
		print('-------------------------')
	hcur.close()
	hcon.close()
	
if __name__=="__main__":
	main()