#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")
import game
from partie import point
import joueur_ab
import joueur_horizon_un

PMax = 4


def perceptron(jeu):
    W = [0,0,0] # Initialisation d'une liste de coefficient pur les fonctions d'évaluations

    i = 0

    while i < 1000: # Boucle infini ( ou presque )
        while (game.finJeu(jeu)): # Tant que la partie n'est pas terminé
            
