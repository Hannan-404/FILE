# 03A1B05432108342864003A1B04003
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
