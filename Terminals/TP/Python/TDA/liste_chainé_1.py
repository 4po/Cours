#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Un premier exemple d'implémentation de liste chaînées
L represente la liste 
x represente une valeur
"""
################ Implémentation du TAD liste chaînée #####################

#Ecrire une spécification pour chacune des fonctions ci-dessous

def vide():
    """ Cette fonction permet de creer une liste vide  """
    return None

def cons(x,L):
    """ Cette fonction permet de creer une liste """
    return(x,L)
    
def ajoutTete(L,x):
    """ Cette fonction permet d'ajouter un element au debut de la liste   """
    return cons(x,L)

def suppTete(L):
    """ Cette fonction permet de supprimer un element au debut de la liste  """
    return (L[0],L[1])

def estVide(L):
    """ Cette fonction teste si L est vide """
    return L is None

def compte(L):
    """ Cette fonction permet de connaitre le nombre d'elements dans la liste   """
    if estVide(L):
        return 0
    return 1+ compte(L[1])  #Cette fonction est récurssive


################ Tester cette implémentation avec les instructions suivantes ###################

#créer une liste appelée listeV vide
listeV = vide()

#Vérifier que listeV ne contient aucune valeur
print(estVide(listeV))	

#Construire une liste appelée maListe qui contiendra les éléments 5, 4, 3, 2, 1)
maListe= cons(5,cons(4,cons(3,cons(2,cons(1,listeV)))))

#Afficher maListe
print(maListe)

#Afficher le nombre de valeurs de la liste :
print(compte(maListe))

#Ajouter 6 à maListe
maListe = ajoutTete(maListe,6)

#Afficher maListe et nombre de valeurs de la liste :
print(maListe)
print(compte(maListe))

#Supprimer la 1ère valeur de la liste et vérifier en l'affichant :
maListe = suppTete(maListe)
print(maListe)
