# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 22:52:20 2015

@author: yohanfargeix
"""
# Importation des modules neccessaires

import sys
sys.path.append("../..")
import game

valeurCoeff = [0.3, 0.5, 0.7]

#Définissions des variables globales

PMax = 1
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

    return [game.getJoueur(jeu)-1, c]

# Fonction décision :
# - Création d'une liste de tuples de la forme L = [[a,b], [a,b], ...] contenant l'indice du coup et sa valeur d'estimation
# - Initialisation du coup au premier tuple de L
# - Parcourt de la liste L et détermination du meilleur coup : On incrémente lors de l'égalité si et seulement si
#   c'est au joueur 2 de joué (le but étant de se rapprocher au maximum de la droite pour le J2 et gauche pour le J1)
# - Retourne l'indice du coup à jouer.

def decision(jeu, L):
    ''' jeu*list -> nat
        Retourne un entier correpondant a la meilleur case
    '''
    liste_meilleur_coup = []
    for i in L:
        liste_meilleur_coup.append([i[1],estimation(jeu, i)])

    coup = liste_meilleur_coup[0]

    for j in liste_meilleur_coup:
        if coup[1] < j[1] and game.getJoueur(jeu) == 2:
            coup = j
        elif coup[1] <= j[1] and game.getJoueur(jeu) == 1:
            coup = j

    return coup[0]


# Fonction estimation :
# - Copie du jeu et simulation du coup envoyé par la fonction décision
# - Retourne l'évaluation

def estimation(jeu, coup, prof = 1):
    '''jeu*coup*nat -> nat
        Retourne la moyenne des points gagnés engendré par ce coup (une fois toutes les possibilités envisagé)
    '''
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    return evaluation(copie)

# Fonction evaluation (pour le moment très basique) :
# Calcule de la différence de point entre les deux joueurs.

def evaluation(jeu):
    ''' jeu -> nat 

        Fonction d'évaluation. Retourne le produit scalaire entre les fonctions d'éval et leurs pondérations
    '''

    return valeurCoeff[0]*f1(jeu) + valeurCoeff[1]*f2(jeu) + valeurCoeff[2]*f3(jeu)
    
    '''
    if (moi == 1 and get_j()<nombreDeMatch/2) or (moi == 2 and get_j()>= nombreDeMatch/2):
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
