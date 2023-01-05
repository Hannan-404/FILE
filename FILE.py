import os, platform, time, sys
os.system('git pull -q')
bit = platform.architecture()[0]
if bit == '64bit':
 print('64BIT FOUND');time.sleep(1)
 import FILE64
elif bit == '32bit':
 print('32BIT FOUND');time.sleep(1)
 import FILE32
