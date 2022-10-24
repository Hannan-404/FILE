#   46HCRAAYTRIDC3C1369F8G72191410526625SSB
#   BXB-H105265X9D8FE110E==
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
