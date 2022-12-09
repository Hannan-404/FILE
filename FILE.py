import os
from subprocess import run
uu = run("play", capture_output=True).stderr.decode('ascii')
if 'play FAIL sox' in uu:
 pass
else:
 os.system('pkg install sox -y')
import os, platform, time
try:
 import requests
except:
 os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
 import FILE64
elif bit == '32bit':
 import FILE32
