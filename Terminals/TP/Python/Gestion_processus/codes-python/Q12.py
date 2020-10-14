#!/usr/bin/python3
import signal,os

def traitement(numero, frame) :
	if numero == 12:
		print ("bonjour bel étranger 2")
	if numero == 10:
		print ("bonjour bel étranger 1")

# quel signal va être traité (SIGUSR1) et par qui (traitement)
signal.signal(signal.SIGUSR1, traitement)
signal.signal(signal.SIGUSR2, traitement)
print(os.getpid())
# boucle infinie
while(True) :
      a=0

