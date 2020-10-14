#!/usr/bin/python3
import os,time

ret=os.fork()

if (ret==0):
    # si je suis le fils
    print("je suis le fils, j'attends 5s")
    time.sleep(5)
    os.kill(os.getppid(),9)
    time.sleep(5)
    print("papa, j'ai pas voulu ça!")
else:
	while 1 :
		# si je suis le pere
		print("je suis le pere , j'attends 1s")
		time.sleep(1)

