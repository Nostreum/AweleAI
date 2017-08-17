# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 17:42:45 2015

@author: yohanfargeix
"""

import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    L = game.getCoupsValides(jeu)
    if game.getJoueur(jeu) == 1:
    	c = L[len(L)-1]
    else:
    	c = L[0]
    return [game.getJoueur(jeu)-1, c[1]]