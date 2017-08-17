#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 18:37:44 2015

@author: yohanfargeix
"""

import sys
import os
sys.path.append("../1Partie")
import partie
os.chdir("../Donnees")

def enregistrer_dans_fichier(n,j1, j2) :
    mon_fichier = open(str(etat_joueur_1)+"-"+str(etat_joueur_2)+".txt", "a")
        
    mon_fichier.write("\nNombre de partie : "+str(n)+", Joueur 1 : "+str(j1)+", Joueur 2 : "+str(j2))
    mon_fichier.close()
