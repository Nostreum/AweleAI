import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    c=input("Joueur "+str(game.getJoueur(jeu))+": Quelle colonne ?")
    return [game.getJoueur(jeu)-1,c]
