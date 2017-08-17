#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import random
import importlib

sys.path.append("..")

import awele 
sys.path.append("../..")

import game
game.game=awele
sys.path.append("../Joueurs")

L = ["joueur_random",
"joueur_humain",
"joueur_maxrandom",
"joueur_horizon_4",
"joueur_minmax",
"joueur_ab",
"joueur_horizon_un",
"joueur_horizon_3"
]

etat_joueur_1 = 0
etat_joueur_2 = 0

def selectionJoueur(n):
    global L
    global joueur1
    global joueur2
    global nbJoueur
    global etat_joueur_1
    global etat_joueur_2

    for i in range(len(L)):
        print str(i) + " : " + str(L[i]) + "\n";

    if n == 1 : 
        s = input("Joueur 1 ? ")
        joueur1 = importlib.import_module(L[s])
        etat_joueur_1 = s
    else:
        s = input("Joueur 2 ? ")
        joueur2 = importlib.import_module(L[s])
        etat_joueur_2 = s

    return s

os.chdir("../Donnees")

def saisieCoup(jeu):

    """ jeu -> coup

        Retourne un coup a jouer

    """

    joueur=game.getJoueur(jeu)

    if joueur == 1:
        joueur = joueur1
    else:
        joueur=joueur2

    coup = joueur.saisieCoup(game.getCopieJeu(jeu))

    while(not (game.coupValide(jeu,coup))):
        print("Joueur : "+str(game.getJoueur(jeu)) + "Probleme avec le coup saisi, recommencez"+str(coup))
        coup=joueur.saisieCoup(game.getCopieJeu(jeu))

    return coup

def joue():

    """ void-> jeu

        Joue une partie

    """
    global L

    jeu = game.initialiseJeu()
    it=0     


    while (it<4) and (not game.finJeu(jeu)):
        coup=random.choice(game.getCoupsValides(jeu))
        game.joueCoup(jeu, coup)
        it+=1 

    while (it<100) and (not game.finJeu(jeu)):
        coup=saisieCoup(jeu)
        game.joueCoup(jeu, coup)
        it+=1

    gagnant = game.getGagnant(jeu)

    if gagnant == 1:
        gagnant = L[etat_joueur_1]
    elif gagnant == 2:
        gagnant = L[etat_joueur_2]
    else:
        gagnant = "Egalite"

    #print("Gagnant="+gagnant+" : "+str(game.getScores(jeu)))
            
    return jeu       


def echange_joueur(nombre_victoire_joueur_1, nombre_victoire_joueur_2):
    global joueur1
    global joueur2
    global etat_joueur_1
    global etat_joueur_2

    inter = joueur1
    joueur1 = joueur2
    joueur2 = inter

    inter = etat_joueur_1
    etat_joueur_1 = etat_joueur_2
    etat_joueur_2 = inter

    inter_val2 = nombre_victoire_joueur_1
    inter_val1 = nombre_victoire_joueur_2

    return [inter_val1, inter_val2]

def change_etat_joueur(j1,j2):

    global etat_joueur_1
    global etat_joueur_2
    global joueur1 
    global joueur2 


    joueur1 = importlib.import_module(L[j1])
    joueur2 = importlib.import_module(L[j2])

    etat_joueur_1 = j1
    etat_joueur_2 = j2

    

def get_etat_joueur():
    return [etat_joueur_1, etat_joueur_2]

def get_nom_joueur(numJ):
    if numJ == 1:
        return L[etat_joueur_1]
    else:
        return L[etat_joueur_2]

def enregistrer_dans_fichier(n,j1, j2) :
    mon_fichier = open(str(L[etat_joueur_1])+"-"+str(L[etat_joueur_2])+".txt", "a")

    mon_fichier.write("\nNombre de partie : "+str(n)+", Joueur 1 : "+str(j1)+", Joueur 2 : "+str(j2))

    mon_fichier.close()

