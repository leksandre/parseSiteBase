import subprocess
import time
import random
import psutil
import os
import sys
p = psutil.Process(os.getpid())
p.nice(18)


siteGenDiv20s = sys.argv
siteGenDiv20s.pop(0)
print('siteGenDiv20s',siteGenDiv20s)
siteGenDiv20=int(siteGenDiv20s[0])

while True:
    subprocess.run(["python3.6", "./finderg_Site.py",str(siteGenDiv20)]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./finderg_Site.py",str(siteGenDiv20)]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./finderg_Site.py",str(siteGenDiv20)]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./finderg_Site.py",str(siteGenDiv20)]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./finderg_Site.py",str(siteGenDiv20)]) 
    time.sleep(1)
    subprocess.run(["python3.6", "./finderg_Site.py",str(siteGenDiv20)]) 
    
    time.sleep(random.randint(1,10))
