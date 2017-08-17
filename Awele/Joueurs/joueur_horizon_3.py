# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 22:52:20 2015

@author: yohanfargeix
"""
# Importation des modules neccessaires

import sys
sys.path.append("../..")
import game

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
# - Initialisation d'une liste vide sc contenant les estimations pour chaque branche et d'une liste des coups valides une
#   fois la simulation faites.
# - Cas de base : Dans le cas où la profondeur est >= à PMax et si aucun coup n'est valide : on retourne
#   juste l'évaluation
# - Sinon, on parcourt la liste des coups valides et on ajoute à sc la valeur de l'estimation de ce coup
# - Une fois la liste compléte, on calcule la moyenne des points rapporter par ce coup.

def estimation(jeu, coup, prof = 1):
    '''jeu*coup*nat -> nat
        Retourne la moyenne des points gagnés engendré par ce coup (une fois toutes les possibilités envisagé)
    '''
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    sc = []
    l = game.getCoupsValides(copie)

    if (prof >= PMax) or (l == []):
        return evaluation(copie)
    else:
        for c in l:
            sc.append(estimation(copie,c,prof+1))        

    somme = 0
    for i in sc:
        somme += i

    return max(sc)

# Fonction evaluation (pour le moment très basique) :
# Calcule de la différence de point entre les deux joueurs.

def evaluation(jeu):
    ''' jeu -> nat 

        Fonction d'évaluation. Retourne le produit scalaire entre les fonctions d'éval et leurs pondérations
    '''

    return f1(jeu)
    

def f1(jeu):
    ''' jeu -> nat 

        Retourne la différence de score
    '''
    score = game.getScores(jeu)
    
    if moi == 1:
        return score[1]-score[0]
    else:
        return score[0]-score[1]










        