#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Un 2ème exemple d'implémentation de liste chaînées, approche POO
"""
########### Implémentation du TAD liste chaînée ######################

#Ecrire une spécification pour mes différents éléments ci-dessous

class Cellule:
    """ Pour creer une cellule d'une liste chainée. Tout objet de cette classe contient
        la valeur de l'élément et un attribut suivant pour la cellule suivante """
    def __init__(self, v,s):
        self.valeur=v
        self.suivante=s
       
L  = Cellule(1,Cellule(2, Cellule(3,Cellule(4,Cellule(5,None)))))     
     
def longueur(lst):
    """ Cette fonction permet de calculer la longueur de la liste    """
    n=0
    c=lst
    while c is not None :
        n=n+1
        c=c.suivante
    return n

print (longueur(L))

def nieme(n,lst):
    """       """
    if lst is None:
        raise IndexError("indice invalide")
    if n==0:
        return lst.valeur
    else :
        return nieme(n-1, lst.suivante)

print (nieme(1,L))

               
class Liste:
    """Une liste chainée  """
    def __init__(self):
        self.tete=None
        
    def estVide(self):
        return self.tete is None
    
    def ajoute(self,x):
        self.tete=Cellule(x,self.tete)
        
    def __len__(self):
        return longueur(self.tete)
    
    def __getitem__(self,n):
        return nieme(n, self.tete)
