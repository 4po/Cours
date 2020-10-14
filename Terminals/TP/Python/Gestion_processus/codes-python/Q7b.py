#!/usr/bin/python3
import os

ret=os.fork()

if (ret==0):
    # si je suis le fils
    print("je suis le fils",os.getpid()," mon pere est ",os.getppid())
else:
    # si je suis le pere
    print("je suis le pere et mon fils a pour pid : ",ret, "et moi ",os.getpid())
