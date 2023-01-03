#FULL CODING BY HANNAN ANSARI
#Hehe You Can Copy Me But Cant Be Me

import os
Hannan = os.system
try:
	open('/sdcard/aaaaaaa','a')
	os.system('rm -rf /sdcard/aaaaaaa')
except:
	Hannan('termux-setup-storage')
try:
	import requests
except:
	Hannan('pip install requests')
try:
	import gtts
except:
	Hannan('pip install gtts')
import random
Hannan('touch /sdcard/16272.txt')

import requests, re, os, time
urls = 'https://business.facebook.com/business_locations'
requests = requests.Session()
from concurrent.futures import ThreadPoolExecutor as threadspeed
import os, sys, re, time, json, requests
from requests.exceptions import ConnectionError
from time import sleep
Hannan('rm -rf /sdcard/.Your_Dad_Is_Here')
#SHORTCUTS
Hani = print
Hannan = os.system
HANNAN_VIP = []
sepx = []
cutter = []
sepx2 = []
Status = 'None'
logo = '''
\033[1;91m  ███████ ██ ██      ███████ 
\033[1;92m  ██      ██ ██      ██      
\033[1;93m  █████   ██ ██      █████   
\033[1;94m  ██      ██ ██      ██      
\033[1;95m  ██      ██ ███████ ███████ 

\033[1;93m==============================
\033[1;97m Owner  : Hannan AnSari
\033[1;97m Github : Hannan-404
\033[1;97m Tool   : File Making Latest
\033[1;97m Version:\033[1;92m 4.3.5
\033[1;93m==============================
'''

extractheads = {'Host': 'https://graph.facebook.com','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','viewport-width':'980'}

def speed(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)

def LDP():
	import _thread
	_thread.start_new_thread(os.system,('play lahore.mp3 -q',))
	

def TTS(text):
	from gtts import gTTS
	gTTS(text, lang='en', slow=False).save('/data/data/com.termux/files/usr/lib/check.mp3')
	import _thread
	_thread.start_new_thread(os.system,('play /data/data/com.termux/files/usr/lib/check.mp3 -q',))

def TTSS(text):
	import _thread
	_thread.start_new_thread(TTS,(text,))
 
def real_time():
    from time import time
    return str(time()).split('.')[0]



def FILE_MENU():
	Hannan('clear')
	Hani(logo)
	try: 
		token = open('Hannan_KinG007','r').read()
	except (IOError):
		HANNAN_KING()
	try:
		token = open('Hannan_KinG007','r').read()
		cookies = open('Hannan_KinG07','r').read()
		HANNAN_VIP.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me/?&access_token='+HANNAN_VIP[0], cookies={'cookie':cookies})
			sy2 = json.loads(sy.text)['name']
		except Exception as e:
			Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
			Hannan('rm -rf Hannan_KinG007')
			Hannan('rm -rf Hannan_KinG07')
			HANNAN_KING()
	except:
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		Hannan('rm -rf Hannan_KinG007')
		Hannan('rm -rf Hannan_KinG07')
		HANNAN_KING()
	print('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92mActive')
	print()
	Hani('\033[1;91m[\033[1;97m1\033[1;91m] \033[1;97mSimple File Make')
	Hani('\033[1;91m[\033[1;97m2\033[1;91m] \033[1;97mUnlimited File Make With 1 ID')
	Hani('\033[1;91m[\033[1;97m0\033[1;91m] \033[1;97mBack To Menu')
	Hani('')
	o = input('\033[1;93m[\033[1;97m?\033[1;93m] \033[1;97mYour Choice : \033[1;92m')
	if o=='1':
		time.sleep(1);main()
	elif o=='2':
		time.sleep(1);UNLIMITED_MAIN()
	elif o=='0':
		MAIN_MENU()
	else:
		Hani('\033[1;91m[\033[1;97m!\033[1;91m] \033[1;97mWRONG INPUT!');time.sleep(0.5);MAIN_MENU()
		
	

def MAIN_MENU():
	Hannan('clear')
	Hani(logo)
	try:
		open('Hannan_KinG007','r').read()
		token = open('Hannan_KinG007','r').read()
		cookies = open('Hannan_KinG07','r').read()
		HANNAN_VIP.append(token)
		try:
			#Hani('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;93m Checking Cookies Please Wait...')
			sy = requests.get('https://graph.facebook.com/me/?&access_token='+HANNAN_VIP[0], cookies={'cookie':cookies})
			sy2 = json.loads(sy.text)['name']
			Status = 'Active'
		except Exception as e:
			Status = 'Expired'
	except:
		Status = None
	print(f'\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92m{Status}')
	print()
	if Status=='Active':
		logg = 'Create File'
	else:
		logg = 'Login'
	Hani(f'\033[1;91m[\033[1;97m1\033[1;91m] \033[1;97m{logg}')
	Hani('\033[1;91m[\033[1;97m2\033[1;91m] \033[1;97mRemove Duplicate Ids')
	Hani('\033[1;91m[\033[1;97m3\033[1;91m] \033[1;97mRemove Used Links')
	Hani('\033[1;91m[\033[1;97m4\033[1;91m] \033[1;97mChange Cookies')
	Hani('\033[1;91m[\033[1;97m5\033[1;91m] \033[1;97mSolve Login Problem (Video)')
	Hani('\033[1;91m[\033[1;97m6\033[1;91m] \033[1;97mSend Message To Owner')
	Hani('')
	o = input('\033[1;93m[\033[1;97m?\033[1;93m] \033[1;97mYour Choice : \033[1;92m')
	if o=='1':
		FILE_MENU()
	elif o=='2':
		fileName = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;97m Enter File Name :\033[1;92m ')
		os.system('sort -r '+fileName+' | uniq > 123')
		os.system('mv 123 '+fileName)
		print('\033[1;91m[\033[1;97m✓\033[1;91m]\033[1;97m Successfully Removed')
		time.sleep(3);MAIN_MENU()
	elif o=='3':
		from slice import used
		used();MAIN_MENU()
	elif o=='4':
		try:
			os.remove('Hannan_KinG07')
			os.remove('Hannan_KinG007')
		except:pass
		MAIN_MENU()
	elif o=='5':
		Hannan('xdg-open https://www.facebook.com/100083649571009/posts/pfbid0zWgHxVGPmJX9EZg7BEkaPPGqcUZ6AUoGXmzrtwsbT7by2oyGBzgLycpy77HeXA2Ul/?app=fbl')
#		print()
#		Hani('\033[1;91m[\033[1;97m1\033[1;91m] \033[1;97mExtension : Cookie Dough')
#		Hani('\033[1;91m[\033[1;97m2\033[1;91m] \033[1;97mOpen Desktop Mode')
#		Hani('\033[1;91m[\033[1;97m3\033[1;91m] \033[1;97mGo To This Link : www.facebook.com/adsmanager ')
#		Hani('\033[1;91m[\033[1;97m4\033[1;91m] \033[1;97mThen Open Extension Copy Cookie')
#		Hani()
#		input('\033[1;91m[\033[1;97m?\033[1;91m] \033[1;97mBack!')
		MAIN_MENU()
	elif o=='6':
		Hannan('xdg-open https://www.facebook.com/TERMUX.LOVER.143')
		MAIN_MENU()
	else:
		Hani('\033[1;91m[\033[1;97m!\033[1;91m] \033[1;97mWRONG INPUT!');time.sleep(0.5);MAIN_MENU()

	
def GET_TOKEN(HBL_IK_NAYA_KHAWAB):
	head = {'Host': 'www.facebook.com','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','viewport-width':'980'}
	respon = requests.get('https://www.facebook.com/adsmanager/manage/campaigns', headers = head, cookies = {'cookies':HBL_IK_NAYA_KHAWAB})
	find = re.findall('act=(.*?)&nav_source', respon.text)
	for y in find:
		response = requests.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer',headers=head, cookies = {'cookies':HBL_IK_NAYA_KHAWAB})
		token = re.search('(EAAB\w+)', response.text).group(1)
	open('Hannan_KinG007','w').write(token)
	open('Hannan_KinG07','w').write(HBL_IK_NAYA_KHAWAB)
	
def HANNAN_KING():
	try:
		Hannan('clear')
		Hani(logo)
		print('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92mNone')
		print()
		HBL_IK_NAYA_KHAWAB = input('\033[1;93m[\033[1;97m?\033[1;93m] \033[1;97mPaste Cookies : \033[1;91m')
		GET_TOKEN(HBL_IK_NAYA_KHAWAB)
		cookies = HBL_IK_NAYA_KHAWAB
		EAAB = open('Hannan_KinG007','r').read()
		HANNAN_VIP.append(EAAB)
		MAIN_MENU()
	except Exception as e:
		print(e)
		Hannan("rm -f Hannan_KinG007")
		Hannan("rm -f Hannan_KinG07")
		Hani('\033[1;92m[\033[1;97m!\033[1;92m] \033[1;97mCookies Invailed!');time.sleep(2)
		MAIN_MENU()
	



def cut2(fileName):
	if 'Ya' in cutter:
		try:
			for a in sepx2:
				Hannan('cat '+fileName+' | grep "'+a+'" >> /sdcard/16272.txt')
			Hannan('sort -r /sdcard/16272.txt | uniq > '+fileName+'')
			Hannan('rm -rf /sdcard/16272.txt')
		except Exception as e:
			Hani(e)
			pass
		pass
	else:
		pass		


def cut(file):
	if 'Ya' in cutter:
		try:
			for a in sepx:
				Hannan('cat '+file+' | grep "'+a+'" >> /sdcard/16272.txt')
			Hannan('sort -r /sdcard/16272.txt | uniq > '+file+'')
			Hannan('rm -rf /sdcard/16272.txt')
		except Exception as e:
			Hani(e)
			pass
		pass
	else:
		pass

id = []

def DUMP2(fileName):
	Hannan('clear')
	Hani(logo)
	try: 
		token = open('Hannan_KinG007','r').read()
	except (IOError):
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		HANNAN_KING()
	try:
		token = open('Hannan_KinG007','r').read()
		cookies = open('Hannan_KinG07','r').read()
		HANNAN_VIP.append(token)
		try:
			response = requests.get('https://graph.facebook.com/100008352679338?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
			response['friends']['data']
		except Exception as e:
			Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
			Hannan('rm -rf Hannan_KinG007')
			Hannan('rm -rf Hannan_KinG07')
			HANNAN_KING()
	except:
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		Hannan('rm -rf Hannan_KinG007')
		Hannan('rm -rf Hannan_KinG07')
		HANNAN_KING()
	cookies = open('Hannan_KinG07','r').read()
	HANNAN_VIP.append(token)
	print('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92mActive')
	print()
	for line in open('/sdcard/.Your_Dad_Is_Here', 'r').readlines():
		id.append(line.strip())
	total = open('/sdcard/.Your_Dad_Is_Here', 'r').readlines()
	
	Hani('\033[1;93m===============================================')
	Hani('\033[1;91m[\033[1;97m✓\033[1;91m]\033[1;97m Process Has Been Started!')
	Hani('\033[1;91m[\033[1;97m!\033[1;91m]\033[1;97m Ctrl + Z Top Stop Process ')
	Hani('\033[1;93m===============================================')
	try:
		select = ['v2']
		with threadspeed(max_workers=20) as (hannanxd):
			try:
				for xd in range(len(total)):
					if select[0]=='v2':
						hannanxd.submit(startv2,fileName,xd,cookies,HANNAN_VIP)
			except:pass
	except:pass
	

	
def startv2(fileName,xd,cookies,HANNAN_VIP):
	try:
		HaNNaN_XD = random.choice(['\033[1;91m','\033[1;92m','\033[1;94m','\033[1;96m','\033[1;95m'])
		for a in range(1):
			response = requests.get('https://graph.facebook.com/'+id[xd]+'?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
			if response['friends']['data']:
				file = open(fileName, 'a')
				for a in response['friends']['data']:
					if 'Ya' in cutter:
						for y in sepx:
							if y in a['id']:
								file.write(a['id']+"|"+a['name']+'\n')
								sys.stdout.write("\r\033[1;91m•\033[1;93m ====== %s \r"%(len(open(fileName,'r').readlines()))
								);sys.stdout.flush()
					else:
						file.write(a['id']+"|"+a['name']+'\n')
						sys.stdout.write("\r\033[1;91m•\033[1;93m ====== %s \r"%(len(open(fileName,'r').readlines()))
						); sys.stdout.flush()
				file.close()
		
				
			else:
				pass			
	except:pass

def start(fileName,xd,cookies,HANNAN_VIP):
	try:
		HaNNaN_XD = random.choice(['\033[1;91m','\033[1;92m','\033[1;94m','\033[1;96m','\033[1;95m'])
		sys.stdout.write("\r\033[1;91m•\033[1;93m %s %s Checking Friendlist From : %s\r"%(len(open(fileName,'r').readlines()),HaNNaN_XD,id[xd])
		); sys.stdout.flush()
		for a in range(1):
			response = requests.get('https://graph.facebook.com/'+id[xd]+'?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
			if response['friends']['data']:
				file = open(fileName, 'a')
				for a in response['friends']['data']:
					if 'Ya' in cutter:
						for y in sepx:
							if y in a['id']:
								file.write(a['id']+"|"+a['name']+'\n')
					else:
						file.write(a['id']+"|"+a['name']+'\n')
				file.close()
				Hani(HaNNaN_XD+'• Successfully Extracted From : '+id[xd]+'        ')
				sys.stdout.write("\r\033[1;91m•\033[1;93m %s %s Checking Friendlist From : %s\r"%(len(open(fileName,'r').readlines()),HaNNaN_XD,id[xd])
				); sys.stdout.flush()
			else:
				pass			
	except:pass
		
def UNLIMITED_MAIN():
	Hannan('clear')
	Hani(logo)
	try: 
		token = open('Hannan_KinG007','r').read()
	except (IOError):
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		HANNAN_KING()
	try:
		token = open('Hannan_KinG007','r').read()
		cookies = open('Hannan_KinG07','r').read()
		HANNAN_VIP.append(token)
		try:
			response = requests.get('https://graph.facebook.com/100008352679338?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
			response['friends']['data']
		except Exception as e:
			Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
			Hannan('rm -rf Hannan_KinG007')
			Hannan('rm -rf Hannan_KinG07')
			HANNAN_KING()
	except:
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		Hannan('rm -rf Hannan_KinG007')
		Hannan('rm -rf Hannan_KinG07')
		HANNAN_KING()
	cookies = open('Hannan_KinG07','r').read()
	HANNAN_VIP.append(token)
	HANNAN_VIP.append(token)
	print('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92mActive')
	print()
	fileName = input('\033[1;91m[\033[1;97m✓\033[1;91m]\033[1;97m Enter File Name :\033[1;92m ')
	Hannan('touch '+fileName)
	HEHE = input('\033[1;91m[\033[1;97m✓\033[1;91m]\033[1;97m Enter Username/Uid : ')
	try:
		response = requests.get('https://graph.facebook.com/'+HEHE+'?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
		file = open('/sdcard/.Your_Dad_Is_Here', 'a')
		for a in response['friends']['data']:
			file.write(a['id']+'\n')
		file.close()
	except:
		
		Hani('\033[1;91m[\033[1;97m!\033[1;91m]\033[1;97m ID NOT PUBLIC');time.sleep(3)
		UNLIMITED_MAIN()
	p = input('\033[1;95m[\033[1;97m?\033[1;95m] \033[1;97mDo You Want To Seprate Links(y/n)? : ')
	if p=='y':
		cutter.append('Ya')
		pass
	else:
		cutter.append('No')
		DUMP2(fileName)
	limi = int(input('\033[1;95m[\033[1;97m?\033[1;95m] \033[1;97mHow many links you want to seprate : '))
	Hani()
	for a in range(limi):
		xid = input('\033[1;96m[\033[1;97m'+str(a)+'\033[1;96m]\033[1;97m Select Links : \033[1;92m')
		sepx.append(str(xid))
	DUMP2(fileName)
	
	
def main():
	
	Hannan('clear')
	Hani(logo)
	try: 
		token = open('Hannan_KinG007','r').read()
	except (IOError):
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		HANNAN_KING()
	try:
		token = open('Hannan_KinG007','r').read()
		cookies = open('Hannan_KinG07','r').read()
		HANNAN_VIP.append(token)
		try:
			response = requests.get('https://graph.facebook.com/100008352679338?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
			response['friends']['data']
		except Exception as e:
			Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
			Hannan('rm -rf Hannan_KinG007')
			Hannan('rm -rf Hannan_KinG07')
			HANNAN_KING()
	except:
		Hani("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;97mCookies Invalid"); sleep(2)
		Hannan('rm -rf Hannan_KinG007')
		Hannan('rm -rf Hannan_KinG07')
		HANNAN_KING()
	print('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92mActive')
	print()
	fileName = input('\033[1;91m[\033[1;97m✓\033[1;91m]\033[1;97m Enter File Name :\033[1;92m ')
	uu = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;97m Do You Want To Seprate Links?(y/n): ')
	if uu=='n':
		cutter.append('No')
		pass
	elif uu=='y':
		cutter.append('Ya')
		limi = int(input('\033[1;95m[\033[1;97m?\033[1;95m] \033[1;97mHow many links you want to seprate : '))
		Hani()
		for a in range(limi):
			xid = input('\033[1;96m[\033[1;97m'+str(a)+'\033[1;96m]\033[1;97m Select Links : \033[1;92m')
			sepx2.append(str(xid))
	else:
		cutter.append('No')
		pass
	
	time.sleep(1)
	Hannan('clear')
	Hani(logo)
	print('\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Cookie Status: \033[1;92mActive')
	Hani('')
	Hani('\033[1;93m==============================')
	Hani('\033[1;97m            Input Ids ')
	Hani('\033[1;93m==============================')
	DUMP(fileName)

def DUMP(fileName):
	while True:
		token = open('Hannan_KinG007','r').read()
		cookies = open('Hannan_KinG07','r').read()
		HANNAN_VIP.append(token)
		HEHE = input("\033[1;97mid: ")
		if HEHE in ['',' ']:
			
			exit('\033[1;95mYou Tap Enter So Dump Is Completed')
		if '|' in HEHE:
			uid, name = HEHE.split('|')
			try:
				response = requests.get('https://graph.facebook.com/'+uid+'?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
				file = open(fileName , 'a')
				for a in response['friends']['data']:
					file.write(a['id']+"|"+a['name']+'\n')
				file.close()
				Hani('\033[1;92mSuccessfully Extracted From '+uid)
				cut2(fileName)
			except(ConnectionError):
				Hani('\033[1;93mNo Internet Connection')
				pass
			except (KeyError):
				Hani('\033[1;91mNot Public')
				pass
		else:
			try:
				response = requests.get('https://graph.facebook.com/'+HEHE+'?fields=friends.limit(50000)&access_token='+HANNAN_VIP[0],cookies={'cookie': cookies},headers=extractheads).json()
				file = open(fileName , 'a')
				for a in response['friends']['data']:
					file.write(a['id']+"|"+a['name']+'\n')
				file.close()
				Hani('\033[1;92mSuccessfully Extracted From '+HEHE)
				cut2(fileName)
			except(ConnectionError):
				Hani('\033[1;93mNo Internet Connection')
				pass
			except (KeyError):
				Hani('\033[1;91mNot Public')
				pass

def NOTICE():
	try:
		os.system('rm -rf /sdcard/.HANNAN')
		os.system('rm -rf .CheckHehe')
		yy = open('/sdcard/.HannanCMdFileDontDelete','r').read()
	except:
		Hannan('clear')
		Hani(logo)
		Hani('\033[1;93m==============================')
		Hani('\033[1;97m   Follow My GiTHub :/ Biruh')
		Hani('\033[1;93m==============================')
		Hannan('xdg-open https://github.com/Hannan-404')
		Hani()
		input('\033[1;97m Enter To Run Commands !')
		
		o = open('/sdcard/.HannanCMdFileDontDelete','a')
		o.write('Delete Na Krdena Acha Krdena Chal Nai Krna Chal krdena Kuxh Na HoTa Krne se')
		
NOTICE()
MAIN_MENU()
