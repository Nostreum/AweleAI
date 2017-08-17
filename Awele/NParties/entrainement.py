''' FONCTION D'ENTRAINEMENT '''
from partie import joue
from partie import change_etat_joueur
from partie import echange_joueur
from partie import enregistrer_dans_fichier
nombre_victoire_joueur_1 = 0
nombre_victoire_joueur_2 = 0
os.chdir("../Donnees")

nbTest = 100

def main(n):
    i = 0

    print " -------------------- AWELE GAME --------------------"
    print " --------------------  WELCOME   --------------------"
    print " ----------------------------------------------------"
        
    while i<n:
        if i == n/2:
            recup = echange_joueur(nombre_victoire_joueur_1, nombre_victoire_joueur_2)
            nombre_victoire_joueur_1 = recup[0]
            nombre_victoire_joueur_2 = recup[1]
        jeu = joue()
        
        if game.getGagnant(jeu) == 1 :
                nombre_victoire_joueur_1 += 1
        elif game.getGagnant(jeu) == 2 :
                nombre_victoire_joueur_2 += 1
        
        i += 1
                
        print("Victoire : "+str(nombre_victoire_joueur_1)+" , "+str(nombre_victoire_joueur_2))
    enregistrer_dans_fichier(n,nombre_victoire_joueur_1,nombre_victoire_joueur_2)
    

def train(n):
    param_j1 = [1, 0.5]
    param_j2 = []
    nbPartie = input("Nombre de partie : ")
    train1 = partie.selectionJoueur(1)
    train2 = partie.selectionJoueur(2)

    for i in range(nbTest):
        train2.param[i]=train1.param[i]
        for j in range(n):
            for w in range(nb):
                while True:
                    train2.param[w] += epsilon
                    v = NParties(nbPartie)
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

train()
