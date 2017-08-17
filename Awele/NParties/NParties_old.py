#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 18:39:07 2015

@author: yohanfargeix
"""
import sys
import os
sys.path.append("..")
import awele 
sys.path.append("../..")
import game
game.game=awele
sys.path.append("../1Partie")
import global_variable
import partie
from partie import joue
from partie import change_etat_joueur
from partie import echange_joueur
from partie import enregistrer_dans_fichier
os.chdir("../Donnees")
nombre_victoire_joueur_1 = 0
nombre_victoire_joueur_2 = 0

def NParties():
    global nombre_victoire_joueur_1
    global nombre_victoire_joueur_2
    i = 0
    n = input("Combien de partie ? :")
    print("Choix des joueurs ! 0. Random, 1. Humain, 2. MaxRandom, 3. Horizon1, 4. Horizon3, 5. Horizon3-opti, 6. Horizon 4 ")
    j1 = input("Joueur 1 :")
    j2 = input("Joueur 2 :")
    change_etat_joueur(j1,j2)
        
    while i<n:
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
                
        print("Nombre de victoire : "+str(nombre_victoire_joueur_1)+" , "+str(nombre_victoire_joueur_2))
        enregistrer_dans_fichier(n,nombre_victoire_joueur_1,nombre_victoire_joueur_2)
    
NParties()