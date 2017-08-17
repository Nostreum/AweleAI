# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 22:52:20 2015

@author: yohanfargeix
"""
# Importation des modules neccessaires

import sys
sys.path.append("../..")
import game

valeurCoeff = [1, 1, 0.2]

#Définission des variables globales (moi non utilisé dans cette version)

PMax = 4
moi = 0

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
        liste_meilleur_coup.append([i[1],min_max(jeu, i)])

    coup = liste_meilleur_coup[0]
    
    for j in liste_meilleur_coup:
        if coup[1] < j[1] and game.getJoueur(jeu) == 2:
            coup = j
        elif coup[1] <= j[1] and game.getJoueur(jeu) == 1:
            coup = j

    return coup[0]

def min_max(jeu, coup, prof = PMax):

    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    l = game.getCoupsValides(copie)

    if prof == 0  or l == []:
        return evaluation(jeu)
    else:
        if game.getJoueur(copie) == moi:
            inter = -10000
            for s in l:
                inter = max(inter, min_max(copie, s, prof - 1))
            return inter - evaluation(copie)
        else:
            inter = 10000
            for s in l:
                inter = min(inter, min_max(copie, s, prof - 1))
            return inter - evaluation(copie)

'''def alpha_beta_amel(jeu, coup, alpha, beta, prof = 1):
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    l = game.getCoupsValides(copie)

    if(game.finJeu(copie)):
        if game.getGagnant(copie) == moi:
            return 1000
        elif game.getGagnant(copie) == 0:
            return -100
        else:
            return -1000

    if prof >= PMax:
        return evaluation(copie)
    else:
        meilleur = -1000
        for s in l:
            val = -alpha_beta_amel(copie, s, -beta, -alpha, prof+1)
            if val > meilleur:
                meilleur = val
                if meilleur > alpha:
                    alpha = meilleur
                    if alpha >= beta:
                        return meilleur
        return meilleur'''


# Fonction evaluation (pour le moment très basique) :
# Calcule de la différence de point entre les deux joueurs.

def evaluation(jeu):
   

    return 2*f1(jeu)+f2(jeu)

#Différence de score

def f1(jeu):
    score = game.getScores(jeu)
    
    if moi == 1:
        return score[1]-score[0]
    else:
        return score[0]-score[1]

#Pondération des cases

def f2(jeu):
    diffGraine = 0

    if moi == 1:
        importance = 0.3
        for i in range(6):
            diffGraine += importance * (game.getCaseVal(jeu, 1, (-i%6)) - game.getCaseVal(jeu, 0, i))
            importance += 0.1
    else:
        importance = 0.8
        for i in range(6):
            diffGraine += importance * (game.getCaseVal(jeu, 0, i) - game.getCaseVal(jeu, 1, (-i%6)))
            importance -= 0.1

    return diffGraine

#Nombre de graine de notre côté (utile en fin de partie)

def f3(jeu):
    nombreGraine = 0
    j = game.getJoueur(jeu)
    i = 0
    for i in range(6):
        nombreGraine += game.getCaseVal(jeu, j-1, i)

    return nombreGraine/6

#Calcul du produit scalaire entre deux listes

def scalaire(L, L2):
    valeur = 0
    i=0
    while i<len(L):
        valeur += L[i]*L2[i]
        i += 1

    return valeur

''' FONCTION D'ENTRAINEMENT '''
'''
def train(n):
    L = liste des coeff w1
    for i in range(nb):
        train2.param[i]=train1.param[i]
        for j in range(n):
            for w in range(nb):
                while True:
                    train2.param[w] += epsilon
                    v = NParties(nbSimulation)
                    if v[1] > v[0]:
                        train1.param[w] = train2.param[w]
                    else:
                        train2.param[w] -= 2*epsilon
                        v = NParties(nbSimulation)
                        if v[1] > v[0]:
                            train1.param[w] = train2.param[w]
                        else:
                            train2.param[w]=train1.param[w]
                            break
'''
