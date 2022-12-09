import os, platform, time
try:
 import requests
except:
 os.system('pip install requests')
os.system('git pull -q')
os.system('pkg install sox 2>/dev/null')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
 import FILE64
elif bit == '32bit':
 import FILE32
