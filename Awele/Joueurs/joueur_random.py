# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 09:26:46 2015

@author: 3300080
"""

import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """

    return random.choice(game.getCoupsValides(jeu))
