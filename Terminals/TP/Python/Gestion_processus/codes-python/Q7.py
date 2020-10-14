#!/usr/bin/python3
import os

ret=os.fork()

if (ret==0):
    # si je suis le fils
    print("je suis le fils")
else:
    # si je suis le pere
    print("je suis le pere et mon fils a pour pid : ",ret)
