#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importation des modules neccessaires
import random
from math import *
import sys
sys.path.append("..")
import awele 
sys.path.append("../..")
import game
game.game=awele
sys.path.append("../Joueurs")
import joueur_horizon_un as etudiant
import joueur_ab as oracle
import joueur_random as joueur_alea

#Definissions des différents joueurs utilisés
rand_joueur = joueur_alea
eleve = etudiant
maitre = oracle
alpha = 0.1

print("--------------- PERCEPTRON STARTING -----------------\n")
nbParties = input("Combien de parties souhaitez vous effectuer ? : ")

def perceptron():
	# nbparties 
    for i in range(nbParties):

        jeu = game.initialiseJeu() # Initialisation du jeu

        while (not(game.finJeu(jeu))): # Tant que la partie n'est pas terminé

            coup_maitre = maitre.saisieCoup( jeu ) # Coup qu'aurait joué le maitre

            jeu2 = game.getCopieJeu(jeu) # On copie le jeu

            game.joueCoup(jeu2, coup_maitre) # On fait jouer le maitre sur la copie

            eleve.moi = (maitre.moi+1)%2 # On echange les joueurs

            score_coup_eleve = [eleve.f1(jeu2),eleve.f2(jeu2),eleve.f3(jeu2)] # Tableau contenant les evaluations de l'éléve

            m = max(maitre.valeurCoeff) # Le maximum des coefficients

            listeCoupValide = game.getCoupsValides(jeu) # Listes des coups valides

            valCoeffEleve = eleve.valeurCoeff # Listes des coefficients des fonctions d'évalutions pour l'éléve
            normaliser(valCoeffEleve)

            ind=0 # Variable d'incrémentation pour parcourir la liste des coefficients

            for c in listeCoupValide: # On parcourt la liste des coups valides

                if maitre.valeurCoeff[ind] < m: # Si le coeffcients à l'indice ind est inférieur au coefficient max

                    jeu3 = game.getCopieJeu(jeu) # On recopie encore une fois le jeu

                    game.joueCoup(jeu3,c) # On simule le coup c

                    score_coup_eleve2 = [eleve.f1(jeu3),eleve.f2(jeu3),eleve.f3(jeu3)] # On recupére les évaluations de l'éléve

                    # Point x/y sur le graphe

                    o = 0 
                    s = 0

                    # Mise à jour des points

                    for i in range(len(score_coup_eleve)):
                        o += valCoeffEleve[i]*score_coup_eleve[i]
                        s += valCoeffEleve[i]*score_coup_eleve2[i]
                        normaliser(valCoeffEleve)

                    # Si on est bien placé par rapport à la droite

                    if (o-s)<1:
                        for j in range(len(score_coup_eleve2)):
                            valCoeffEleve[j] -=   alpha * (score_coup_eleve2[j] - score_coup_eleve[j]) # Mise à jour des coeffs de l'éléve
                            normaliser(valCoeffEleve)

                	ind += 1 # On incrémente pour le coeffcient suivant

            jeu = jeu2 # On reprends le jeu d'avant

            # Et on joue un coup random pour continuer le game

            if(not(game.finJeu(jeu))):
                c = rand_joueur.saisieCoup(jeu)
                game.joueCoup(jeu,c)
                game.changeJoueur(jeu)

        print eleve.valeurCoeff # Affichage des coefficients

def normaliser(p):
    ''' Fonction qui normalise un vecteur de gêne d'un individu 
        (c-à-d la somme de tous les gênes vaut 1 => || W || = 1)

        List -> List
    '''
    norme = 0 # Initialisation de la variable norme

    # Formule de la norme en dimension n : ||W|| = sqrt( x1^2 + x2^2 + ... + xN^2) avec W = (x1, x2, ..., xN)
    # Somme des composants du vecteur 

    for i in p:
        norme += i*i

    norme = sqrt(norme) # On prends la racine pour calculer la norme 

    # On divise chaque coefficient par la norme, pour normaliser le vecteur (si la norme est > 1)

    if norme > 1.0:
        for i in range(len(p)):
            p[i] = p[i] / norme

    # On retourne l'individu une fois normalisé

    return p


perceptron() # Lance la fonction