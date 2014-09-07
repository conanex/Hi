import telnetlib
import time
import re

CODE="big5"
USER_ID="wclab5566"
USER_PW="wclab"
INFILENAME="name_test.txt"
OUTFILENAME="record.txt"

input_file = open(INFILENAME,"r")
output_file = open(OUTFILENAME,"w")

def people_info(string):
	string_list=string.split()
	
	ID=re.sub(('《ＩＤ暱稱》','',string_list[0])
	
	economic=re.sub(('《經濟狀況》','',string_list[2])
	log_num=re.sub(('','',string_list[3])
	article_num=re.sub(('','',string_list[])
	bad_article=re.sub(('','',string_list[])
	current_state=re.sub(('','',string_list[])
	mail=re.sub(('','',string_list[])
	last_log=re.sub(('','',string_list[])
	last_ip=re.sub(('','',string_list[])
	five_in_a_Row=re.sub(('','',string_list[])
	chinese_chess=re.sub(('','',string_list[])
	signature_line=re.sub(('','',string_list[])
	
	output_file.write(string_list[0])
	string_list[0]
	
	for element in string_list:
		
		print(element)


tn =telnetlib.Telnet("ptt.cc")
s="註冊:"
string=tn.read_until(s.encode(CODE),10)
#print (string)
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
#s=string.decode("big5",'ignore')
#print (s)


s="\x1b[B";s2="打開";
tn.write( b'\x1b\x5b\x42' );#string=tn.read_until(s2.encode(CODE),10);print(string);

tn.write( b'\x1b\x5b\x42' );#string=tn.read_until(s2.encode(CODE),10);
s="\x1b[C";
tn.write( b'\x1b\x5b\x43' );#tn.write( b'\x0c' );string=tn.read_until(s2.encode(CODE),10);print(string)
s="\x1b[B";
tn.write( b'\x1b\x5b\x42' );#string=tn.read_until(s2.encode(CODE),10);

#time.sleep(1)
#string=tn.read_very_eager().decode('big5','ignore')

for letter in input_file:
	tn.write( b'\x1b\x5b\x43' );
	s='請輸入使用者代號:'
	string=tn.read_until(s.encode(CODE),10).decode('big5','ignore')
	
	
	name=letter.strip()
	name=name+"\r"
	
	tn.write( name.encode('ascii') )
	s='請按任意鍵繼續'
	string=tn.read_until(s.encode(CODE),10).decode('big5','ignore')
	string=re.sub('\x1b[[0-9;]*[mABCDHJKsu]','    ',string);
	string=re.sub('\x0d','\n',string);

	
	people_info(string)
	output_file.write(string)
	tn.write( b'\r' )

	

input_file.close()
output_file.close()


