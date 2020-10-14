#!/usr/bin/python3
import signal,os

def traitement(numero, frame) :
	print("réception d'un signal de numero ",numero)


# quel signal va être traité (SIGUSR1) et par qui (traitement)
signal.signal(signal.SIGUSR1, traitement)
print(os.getpid())
# boucle infinie
while(True) :
      a=0

