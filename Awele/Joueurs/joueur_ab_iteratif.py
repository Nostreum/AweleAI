#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Wed Jan 21 22:52:20 2015

@author: yohanfargeix
"""
# Importation des modules neccessaires

import sys
sys.path.append("../..")
import game
#from NParties import get_j

#Définission des variables globales (moi non utilisé dans cette version)

PMax = 5 # Profondeur de recherche
moi = 0 # Variable stockant le joueur actuel

nombreDeMatch = 0

# Liste des meilleurs gênes obtenu
# - [0.7672288629213112, 0.3773993848150305, 0.5184497264195141, 0.011809209001408617]
# - [0.5621264773037965, 0.1785297339319972, 0.251396339201298]
# - [0.5710308078815601, 0.47745388662150906, 0.6678035658785807] VS AB
# - [0.6179849809414142, 0.32256654018177866, 0.6530445794355563] VS CHEAT
# - [0.7865342813039222, 0.2983736782734423, 0.41971106976440264]
# - [0.7547233761403045, 0.16765866297744872, 0.6342579902815532]
# - ORACLE : [9.7, 4.650000000000005, 4.699999999999999]

valeurCoeff = [0.5710308078815601, 0.47745388662150906, 0.6678035658785807]
valeurCoeff1 = [1, 0.5, 0.1] # Pondérations des parties pour le joueur 1, lors de l'algorithme de population
valeurCoeff2 = [1, 0.5, 0.1] # Pondérations des parties pour le joueur 2, lors de l'algorithme de population


#Fonction appeler par la fonction joue pour la saisie d'un coup. ELle se contente de lancer décision
#et de retourner le coup joué.

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    global moi
    moi = game.getJoueur(jeu)
    c = decision(jeu, game.getCoupsValides(jeu))

    return [moi-1, c]

def decision(jeu, L):
    ''' jeu*list -> nat
        Retourne un entier correpondant a la meilleur case
    '''
    liste_meilleur_coup = []
    for i in L:
        liste_meilleur_coup.append([i[1],ab_iteratif(jeu)])

    coup = liste_meilleur_coup[0]
    
    for j in liste_meilleur_coup:
        if coup[1] < j[1] and game.getJoueur(jeu) == 2:
            coup = j
        elif coup[1] <= j[1] and game.getJoueur(jeu) == 1:
            coup = j

    return coup[0]

def ab_iteratif(jeu):

    prof = 1

    l = game.getCoupsValides(jeu)

    listeEval = []

    # Stock le coup retourner par chacun des deux alpha béta
    c1 = 0
    c2 = 1

    # Tant que la profondeur et inférieur à 10 ou que les deux coups sont différents
    while (prof < 4) and (c1 != c2):
        # On parcours tout les coups possibles
        for c in l:

            # On copie le jeu 2 fois pour chaque parti
            copie1 = game.getCopieJeu(jeu)

            # On copie la profondeur 
            profC1 = prof 

            c2 = c1

            # On recupére le résultat d'alpha béta à horizon prof et prof+1
            c1 = alpha_beta(copie1, c, -1000, 1000, profC1)

        prof += 1 # On incrémente la profondeur

    # On retourne le max 
    return c1


# Algorithme alpha-beta

def alpha_beta(jeu, coup, alpha, beta, prof):
    ''' jeu*list*nat*nat*nat -> list 

        Algorithme alpha_beta. Parcourt d'arbre à horizon PMax
    '''

    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)

    if(game.finJeu(copie)):
        if game.getGagnant(copie) == moi:
            return 1000
        else:
            return -1000

    if prof == 0:
        return evaluation(jeu)
    else:
        l = game.getCoupsValides(copie) 
        if prof%2 == 0:
            inter = -10000
            for s in l:
                sco = alpha_beta(copie, s, alpha, beta, prof - 1)
                if sco > inter:
                    inter = sco
                    if inter >= beta:
                        break
                    alpha = max(inter, alpha)
            return inter
        else:
            inter = 10000
            for s in l:
                sco = alpha_beta(copie, s, alpha, beta, prof - 1)
                if sco < inter:
                    inter = sco 
                    if inter <= alpha:
                        break
                    beta = min(inter, beta)
            return inter


# Fonction evaluation (pour le moment très basique) :
# Calcule de la différence de point entre les deux joueurs.


def evaluation(jeu):
    ''' jeu -> nat 

        Fonction d'évaluation. Retourne le produit scalaire entre les fonctions d'éval et leurs pondérations
    '''

    return valeurCoeff[0]*f1(jeu) + valeurCoeff[1]*f2(jeu) + valeurCoeff[2]*f3(jeu)
    
    
    '''if (moi == 1 and get_j()<nombreDeMatch/2) or (moi == 2 and get_j()>= nombreDeMatch/2):
        return scalaire([f1(jeu), f2(jeu), f3(jeu)], valeurCoeff1)
    else:
        return scalaire([f1(jeu), f2(jeu), f3(jeu)], valeurCoeff2)'''
    

def f1(jeu):
    ''' jeu -> nat 

        Retourne la différence de score
    '''
    score = game.getScores(jeu)
    
    if moi == 1:
        return score[0]-score[1]
    else:
        return score[1]-score[0]

def f2(jeu):
    diffGraine = 0

    if moi == 1:
        importance = 0.3
    else:
        importance = 0.8

    for i in range(6):
        if moi == 1:
            diffGraine += importance * (game.getCaseVal(jeu, 1, -i%6) - game.getCaseVal(jeu, 0, i))
            importance += 0.1
        else:
            diffGraine += importance * (game.getCaseVal(jeu, 0, i) - game.getCaseVal(jeu, 1, -i%6))
            importance -= 0.1

    return diffGraine

def f3(jeu):
    nombreGraine = 0
    j = game.getJoueur(jeu)

    for i in range(6):
        nombreGraine += game.getCaseVal(jeu, j-1, i)

    return nombreGraine

def f4(jeu):
    mauvaiseCase = 0
    j = game.getJoueur(jeu)

    for i in range(6):
        if (game.getCaseVal(jeu,j-1, i) == 2 or game.getCaseVal(jeu, j-1, i) == 1) and (j == moi):
            mauvaiseCase += 10
        else:
            mauvaiseCase -= 10

    return mauvaiseCase

def f5(jeu):
    krou = 0
    j = game.getJoueur(jeu)

    for i in range(6):
        if (game.getCaseVal(jeu, j-1, i) >= 12) and (krou == 0) and (j == moi):
            krou += 10
        elif (game.getCaseVal(jeu, j-1, i) >= 12) and (krou == 0) and (j != moi):
            krou += 10

    return krou


def scalaire(L2, L):
    ''' list*list -> nat

        Fais le produit scalaire entre deux vecteurs
    '''
    valeur = 0
    i=0
    while i<len(L):
        valeur += L[i]*L2[i]
        i += 1
    return valeur

def change_valeur_coeff(l, i):
    ''' list*nat -> None 

        Modifie valeurCoeff1 et valeurCoeff2
    '''
    global valeurCoeff1

    if i == 1:
        valeurCoeff1 = l
    elif i == 2:
        valeurCoeff2 = l
