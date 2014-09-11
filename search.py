import telnetlib
import time
import re
import random
import sys
from datetime import datetime

CODE="big5"
USER_ID=""
USER_PW=""
INFILENAME="data/name.txt"
OUTFILENAME="data/record.txt"

input_file = open(INFILENAME,"r")
#output_file = open(OUTFILENAME,"w")

def people_info(string):
	global info;global ID;
	
	ID=None;nickname=None;

	if re.search('ＩＤ暱稱',string)!=None:
		ob=re.search('《ＩＤ暱稱》(?p<id>\w*).*\((?P<nick>.*)\).*《',string)
		ID=ob.group(1)
		nickname=ob.group(2)
	if re.serach('經濟狀況',string)!=None:
		ob=re.search('《經濟狀況》(?P<f>\S*)',string)
		economic=ob.group(1)
	if re.serach('登入次數',string)!=None:
		ob=re.search('《登入次數》(?P<f>\d*)',string)
		log_num=ob.group(1)
	
	if re.serach('有效文章',string)!=None:
		ob=re.search('《有效文章》(?P<f>\d*)',string)
		article_num=ob.group(1)
	
	if re.serach('\(退:',string)!=None:
		ob=re.search('《經濟狀況》(?P<f>\S*)',string)
		bad_arcitle=ob.group(1)

	
	'''
	temp_string=re.search('《ＩＤ暱稱》.*《經濟狀況》',string).group(0)
	temp_string=re.sub('《經濟狀況》','',temp_string)
	temp_string=re.sub('《ＩＤ暱稱》','',temp_string)
	nickname=re.search('\((?P<nick>.*)\)',temp_string).group(1)
	#print(nickname)
	temp_string=re.sub('\(.*\)','',temp_string)
	ID=temp_string.split()[0]

	#string_list=string.split()
	#ID=re.sub('《ＩＤ暱稱》','',string_list[0])
	string=re.sub('《ＩＤ暱稱》.*《','',string)
	string_list=string.split();index=0;
	
	for test in string_list:
		print(test)
	'''
	


	'''
	for i in range(1,len(string_list)):
		if re.search('經濟狀況》',string_list[i]):
			index=i;
			break;

	economic=re.sub('經濟狀況》','',string_list[index])
	log_num=re.sub('《登入次數》','',string_list[index+1])
	article_num=re.sub('《有效文章》','',string_list[index+4])
	bad_article=re.sub('\(退:','',string_list[index+6]);bad_article=re.sub('\)','',bad_article);
	
	current_state=re.sub('《目前動態》','',string_list[index+7])
	mail=re.sub('《私人信箱》','',string_list[index+8])
	last_log=re.sub('《上次上站》','',string_list[index+9]);last_log=last_log+" "+string_list[index+10]+" "+string_list[index+11];
	last_ip=re.sub('《上次故鄉》','',string_list[index+12])
	five_in_a_Row=string_list[index+16]+string_list[index+17]+string_list[index+18]+string_list[index+19]+string_list[index+20]+string_list[index+21]
	chinese_chess=string_list[index+23]+string_list[index+24]+string_list[index+25]+string_list[index+26]+string_list[index+27]+string_list[index+28]
	
	signature_line=""
	
	'''
	for  i in range(index+29,len(string_list)):
		signature_line=signature_line+" "+string_list[i]
	info= ID+'\t'+nickname+'\t'+economic+'\t'+log_num+'\t'+article_num+'\t'+bad_article+'\t'+current_state+'\t'+mail+'\t'+last_log+'\t'+last_ip+'\t'+five_in_a_Row+'\t'+chinese_chess+'\t'+signature_line+'\n'
##############################################################################################################################
def login():
	global tn;
	tn =telnetlib.Telnet("ptt.cc")
	s="註冊:"
	string=tn.read_until(s.encode(CODE),10)

	s=USER_ID + "\r" 
	tn.write( s.encode('ascii') )
	s="密碼:"
	string=tn.read_until(s.encode(CODE),10 )
	s=USER_PW + '\r'
	tn.write( s.encode('ascii') )

	s="請按任意鍵繼續"
	string=tn.read_until(s.encode(CODE),10)
	tn.write(b'\r')

	s="打開"
	string=tn.read_until(s.encode(CODE),10)


	s="\x1b[B";s2="打開";
	tn.write( b'\x1b\x5b\x42' );

	tn.write( b'\x1b\x5b\x42' );
	s="\x1b[C";
	tn.write( b'\x1b\x5b\x43' );
	s="\x1b[B";
	tn.write( b'\x1b\x5b\x42' );
#########################################################################################################################################################

login()

string='查詢時間\tＩＤ\t暱稱\t經濟狀況\t登入次數\t有效文章\t劣文\t目前動態\t私人信箱\t上次上站\t上次故鄉\t五子棋\t象棋戰績\t簽名檔\n'
#output_file.write(string)
name='ak84333331'
for letter in input_file:
	
	#name=letter.strip()
	while (True):
		error=0;
	
		try:
			tn.write( b'\x1b\x5b\x43' );
		except:
			e = sys.exc_info()[0]
			print(e)
			print('Log in again!!')
			login()
			continue

		try:
			s='請輸入使用者代號:'
			string=tn.read_until(s.encode(CODE),30).decode('big5','ignore')
		except:
			e = sys.exc_info()[0]
			print(e)
			print('Log in again!!')
			login()
			continue

		now_time=str(datetime.now())
		try:
			tn.write( (name+'\r').encode('ascii') )
		except:
			e = sys.exc_info()[0]
			print(e)
			print('Log in again!!')
			login()
			continue
		try:
			s='請按任意鍵繼續'
			string=tn.read_until(s.encode(CODE),30).decode('big5','ignore')
		except:
			e = sys.exc_info()[0]
			print(e)
			print('Log in again!!')
			login()
			continue

		#time.sleep(5)
		#print(string.find('請按任意鍵繼續'))
		if string.find('請按任意鍵繼續')==-1:
			error=1
		else:
			string=re.sub('\x1b[[0-9;]*[mABCDHJKsu]','    ',string);
			string=re.sub('\x0d','\n',string);
			string=string.replace('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     請按任意鍵繼續','')	
			people_info(string)
			if ID!=name:
				error=2;#print('ID:'+ID+' name:'+name)
		
		if error==1:
			#output_file.write(now_time+'\t'+name+'\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\n')
			break
		elif error==2:
			#output_file.write(now_time+'\t'+name+'\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\n')
			try:
				tn.write( b'\r' )
				break
			except:
				e = sys.exc_info()[0]
				print(e)
				print('Log in again!!')
				login()
				break
		else:
			#output_file.write(now_time+'\t'+info)
			try:
				tn.write( b'\r' )
				break
			except:
				e = sys.exc_info()[0]
				print(e)
				print('Log in again!!')
				login()
				break;
	print(error)
	print(ID)
	print(name)
	break
	#time.sleep()
	

input_file.close()
#output_file.close()


