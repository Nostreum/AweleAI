# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 22:52:20 2015

@author: yohanfargeix
"""

import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    numero_joueur = game.getJoueur(jeu)
    coup_possible = game.getCoupsValides(jeu)  
    point_resultant = []
    jeu_copie = game.getCopieJeu(jeu)
    
    for i in coup_possible:
        jeu_actuel = jeu_copie
        score_a = game.getScore(jeu_actuel, numero_joueur)
        game.joueCoup(jeu_actuel, i)
        score_b = game.getScore(jeu_actuel, numero_joueur)
        point_resultant.append([i[1],score_b - score_a])
    
    meilleur_coup = point_resultant[0]        
    for ind in point_resultant:
        if meilleur_coup[1] <= ind[1]:
            meilleur_coup[1] = ind[1]

    
    j = meilleur_coup[0]

    return [game.getJoueur(jeu)-1, j]       
                
        