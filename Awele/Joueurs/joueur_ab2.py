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

PMax = 5
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
        liste_meilleur_coup.append([i[1],alpha_beta(jeu, i, -1000, 1000)])

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

def alpha_beta(jeu, coup, alpha, beta, prof = 1):
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

    if prof >= PMax:
        return evaluation(jeu)
    else:
        l = game.getCoupsValides(copie) 
        if prof%2 == 0:
            inter = -10000
            for s in l:
                sco = alpha_beta(copie, s, alpha, beta, prof + 1)
                if sco > inter:
                    inter = sco
                    if inter >= beta:
                        break
                    alpha = max(inter, alpha)
            return inter
        else:
            inter = 10000
            for s in l:
                sco = alpha_beta(copie, s, alpha, beta, prof + 1)
                if sco < inter:
                    inter = sco 
                    if inter <= alpha:
                        break
                    beta = min(inter, beta)
            return inter


# Fonction evaluation (pour le moment très basique) :
# Calcule de la différence de point entre les deux joueurs.

def evaluation(jeu):
    val_f1 = f1(jeu)
    val_f2 = f2(jeu)
    #print("J1 : " + str(val_f1)+" J2 :"+str(val_f2))
    
    return 2*val_f1 + val_f2

def f1(jeu):
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
