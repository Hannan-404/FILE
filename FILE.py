#   46HCRAAYTRIDC3C1369F8G72191410526625SSB
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
    import Hannan
