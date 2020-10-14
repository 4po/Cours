#!/usr/bin/python3
import time
from os import getpid
pid = str(getpid())

with open('test.txt','w') as fichier :
    for i in range (50) :
        fichier.write(pid+' : '+str(i) + '\n')
        time.sleep(1.8)
        fichier.flush()
