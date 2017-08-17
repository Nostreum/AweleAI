#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 18:39:07 2016

@author: yohanfargeix
"""
import sys
import os
import partie
import importlib
import time
sys.path.append("..")
import awele 
sys.path.append("../..")
import game
game.game=awele
from partie import joue
from partie import change_etat_joueur
from partie import echange_joueur
from partie import enregistrer_dans_fichier
os.chdir("../Donnees")

j = 0

def NParties():
    i = 0

    nombre_victoire_joueur_1 = 0
    nombre_victoire_joueur_2 = 0

    print(" -------------------- AWELE GAME --------------------")
    print(" --------------------  WELCOME   --------------------")
    print(" ----------------------------------------------------")
    n = input("Nombre de partie :")
    #j1 = input("Joueur 1 :")
    #j2 = input("Joueur 2 :")
    s1 = partie.selectionJoueur(1)
    s2 = partie.selectionJoueur(2)
    a=0

    #change_etat_joueur(s1,s2)
        
    aTime = time.time()
    while i<n:
        a += 1
        if i == n/2:
            recup = echange_joueur(nombre_victoire_joueur_1, nombre_victoire_joueur_2)
            nombre_victoire_joueur_1 = recup[0]
            nombre_victoire_joueur_2 = recup[1]
        jeu = joue()
        
        if game.getGagnant(jeu) == 1 :
            nombre_victoire_joueur_1 += 1
        elif game.getGagnant(jeu) == 2 :
            nombre_victoire_joueur_2 += 1
        
        i += 1
        
        if a==10:       
            print("Victoire : "+str(nombre_victoire_joueur_1)+" , "+str(nombre_victoire_joueur_2))
            a=0

    bTime = time.time()
    print("Temps écoulé : " +str(bTime - aTime) + " secs.")
    enregistrer_dans_fichier(n,nombre_victoire_joueur_1,nombre_victoire_joueur_2)

def NParties_genetique(j1, j2, nbParties):
    ''' Simule nbParties entre le j1 et le j2 :

        nat*nat*nat -> Nat*Nat
    '''
    global j

    j = 0

    nombre_victoire_joueur_1 = 0
    nombre_victoire_joueur_2 = 0


    change_etat_joueur(j1, j2)
    
    while j<nbParties:
        if j == nbParties/2:
            recup = echange_joueur(nombre_victoire_joueur_1, nombre_victoire_joueur_2)
            nombre_victoire_joueur_1 = recup[0]
            nombre_victoire_joueur_2 = recup[1]
        jeu = joue()
        
        if game.getGagnant(jeu) == 1:
            nombre_victoire_joueur_1 += 1
        elif game.getGagnant(jeu) == 2:
            nombre_victoire_joueur_2 += 1

        j += 1

    return [nombre_victoire_joueur_2, nombre_victoire_joueur_1]

def get_j():
    return j

NParties()

