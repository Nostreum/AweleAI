#!/usr/local/bin/python
import sys
import os
import global_variable
sys.path.append("..")
import awele 
sys.path.append("../..")
import game
game.game=awele
sys.path.append("../Joueurs")
import joueur_humain
import joueur_random
import joueur_maxrandom
import joueur_horizon_un
import joueur_horizon_3
import joueur_horizon_n_opti
import joueur_horizon_4
import joueur_minmax
import joueur_ab
joueur1=joueur_random
joueur2=joueur_random
etat_joueur_1 = 3
etat_joueur_2 = 0
os.chdir("../Donnees")


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    joueur=game.getJoueur(jeu)

    
    if joueur == 1:
        joueur = joueur1
    else:
        joueur=joueur2

    coup=joueur.saisieCoup(game.getCopieJeu(jeu))
    while(not (game.coupValide(jeu,coup))):
        print("Probleme avec le coup saisi, recommencez"+str(coup))
        coup=joueur.saisieCoup(game.getCopieJeu(jeu))
    return coup


def joue():
    """ void-> jeu
        Joue une partie
    """
    global joueur1
    global joueur2
    global etat_joueur_1
    global etat_joueur_2
    
    jeu=game.initialiseJeu()
    it=0     
    
    joueur1 = joueur_random
    joueur2 = joueur_random
    
    while (it<4) and (not game.finJeu(jeu)):
        coup=saisieCoup(jeu)
        game.joueCoup(jeu, coup)
        it+=1
    
    if etat_joueur_1 == 1:
        joueur1 = joueur_humain
    elif etat_joueur_1 == 2:
        joueur1 = joueur_maxrandom
    elif etat_joueur_1 == 3:
        joueur1 = joueur_horizon_un
    elif etat_joueur_1 == 4:
        joueur1 = joueur_horizon_3
    elif etat_joueur_1 == 5:
        joueur1 = joueur_horizon_n_opti
    elif etat_joueur_1 == 6:
        joueur1 = joueur_horizon_4
    elif etat_joueur_1 == 7:
        joueur1 = joueur_minmax
    elif etat_joueur_1 == 8:
        joueur1 = joueur_ab
    
    if etat_joueur_2 == 1:
        joueur2 = joueur_humain
    elif etat_joueur_2 == 2:
        joueur2 = joueur_maxrandom
    elif etat_joueur_2 == 3:
        joueur2 = joueur_horizon_un
    elif etat_joueur_2 == 4:
        joueur2 = joueur_horizon_3
    elif etat_joueur_2 == 5:
        joueur2 = joueur_horizon_n_opti
    elif etat_joueur_2 == 6:
        joueur2 = joueur_horizon_4
    elif etat_joueur_2 == 7:
        joueur2 = joueur_minmax
    elif etat_joueur_2 == 8:
        joueur2 = joueur_ab

    while (it<100) and (not game.finJeu(jeu)):
        coup=saisieCoup(jeu)
        game.joueCoup(jeu, coup)
        it+=1

    #print("Gagnant="+str(game.getGagnant(jeu))+" : "+str(game.getScores(jeu)))
            
    return jeu     

    
def echange_joueur(nombre_victoire_joueur_1, nombre_victoire_joueur_2):
    
    global etat_joueur_1
    global etat_joueur_2

    inter = etat_joueur_1
    etat_joueur_1 = etat_joueur_2
    etat_joueur_2 = inter

    print("J1 : "+str(etat_joueur_1)+" J2 : "+str(etat_joueur_2))
        
    inter_val2 = nombre_victoire_joueur_1
    inter_val1 = nombre_victoire_joueur_2
    return [inter_val1, inter_val2]

def change_etat_joueur(j1,j2):
    global etat_joueur_1
    global etat_joueur_2

    etat_joueur_1 = j1
    etat_joueur_2 = j2

    print("Etat : "+str(etat_joueur_1)+"    "+str(etat_joueur_2))
    
def get_etat_joueur():
    return [etat_joueur_1, etat_joueur_2]
    
def enregistrer_dans_fichier(n,j1, j2) :
    mon_fichier = open(str(etat_joueur_1)+"-"+str(etat_joueur_2)+".txt", "a")
        
    mon_fichier.write("\nNombre de partie : "+str(n)+", Joueur 1 : "+str(j1)+", Joueur 2 : "+str(j2))
    mon_fichier.close()
