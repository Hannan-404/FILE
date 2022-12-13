import os, platform, time
try:
 import requests
except:
 os.system('pip install requests')
os.system('git pull -q')

uu = os.popen('play').read()

if 'Usage summary' in uu:
 pass
else:
 print(uu)
 os.system('pkg install sox -y')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
 import FILE64
elif bit == '32bit':
 import FILE32
