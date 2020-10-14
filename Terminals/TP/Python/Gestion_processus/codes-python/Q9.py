#!/usr/bin/python3
import os,time

ret=os.fork()

if (ret==0):
    # si je suis le fils
    print("je suis le fils, j'attends 5s")
    time.sleep(5)
    print("le fils est mort")
else:
    # si je suis le pere
    print("je suis le pere , j'attends 10s")
    time.sleep(10)
    print("le pere est mort")
