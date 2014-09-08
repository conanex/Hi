import telnetlib
import time
import re
import getpass
from datetime import datetime

CODE="big5"
OUTPUTFILE="name"+str(datetime.now())+".txt"
#USER_ID="wclab5566"
#USER_PW="wclab"

USER_ID=input('請輸入帳號: ')
USER_PW=getpass.getpass('請輸入密碼: ')
print(OUTPUTFILE)
'''
print("登入中")
tn =telnetlib.Telnet("ptt.cc")
#time.sleep(1)
#string=tn.read_very_eager().decode('uao_decode','ignore')
#print (string)

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
print("登入成功")

s="\x1b[B";s2="打開";
tn.write( b'\x1b\x5b\x42' );#string=tn.read_until(s2.encode(CODE),10);print(string);

tn.write( b'\x1b\x5b\x42' );#string=tn.read_until(s2.encode(CODE),10);
s="\x1b[C";
tn.write( b'\x1b\x5b\x43' );#tn.write( b'\x0c' );string=tn.read_until(s2.encode(CODE),10);print(string)
s="\x1b[B";
tn.write( b'\x1b\x5b\x42' );#string=tn.read_until(s2.encode(CODE),10);
s="\x1b[C";s2=":";
tn.write( b'\x1b\x5b\x43' );#tn.write( b'\x0c' );string=tn.read_until(s2.encode(CODE),10);

time.sleep(1)
string=tn.read_very_eager().decode('big5','ignore')
#print (string)
print("準備查詢中...")

s="a ";s2="繼續";
tn.write( s.encode('ascii') );#string=tn.read_until(s2.encode(CODE),10);
s=" ";
f = open(OUTPUTFILE,"w")
#f2 = open("output2.txt","w")
i=0;stop=0;pre_stop=0;char_now='a';
while (True):
	#Read ID page
	time.sleep(0.6)
	string=tn.read_very_eager().decode('big5','ignore')
	#print(string);f2.write(string);
	string=re.sub('\x1b[[0-9;]*[mABCDHJKsu]','    ',string);
	string=re.sub('\x08','    ',string);
	string=string.replace('◆ 按空白鍵可列出更多項目','');
	string=string.replace('[按任意鍵繼續]','');
	string=string.replace('【 查詢網友 】','');
	string=string.replace('請輸入使用者代號:','');
	string=string.replace('------------------------------- 相關資訊一覽表 -------------------------------','');
	#f.write(string)
	#print(string)
	string_list=string.split();
	j=0
	while j<len(string_list):
		if char_now != string_list[j]:
			if i>0 and first_name==string_list[j]:
				stop=stop+1
				break
			else:	
				f.write(string_list[j]+'\n')
		j=j+1
	if i==0:
		first_name=string_list[1]
		print ('第一個名字'+first_name)
	
	if stop==pre_stop:	
		#PRESS space and read the buffer
		tn.write( s.encode('ascii') )
		time.sleep(0.6)
		string=tn.read_very_eager().decode('big5','ignore')
		#Ctrl + L
		tn.write( b'\x0c' );
		i=i+1
	else:
		#PRESS Back+space and read the buffer
		if stop==26:
			break
		char_now=chr(97+stop)
		tn.write( b'\x08')
		tn.write( char_now.encode('ascii'))
		tn.write( s.encode('ascii') )
		string=tn.read_very_eager().decode('big5','ignore')
		tn.write( b'\x0c' );
		pre_stop=stop
		i=0


f.close()
#f2.close();
'''
