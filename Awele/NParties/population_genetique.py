#!/usr/bin/python
# -*- coding: utf-8 -*-

# On import tous ce dont on à besoin pour le programme
# J'utilise from x import * par simplicité, étant donné que je sais que tous les noms des fonctions seront uniques.

from partie import *
from NParties import *
from random import *
from math import *
from joueur_ab import *

''' CONCEPT DE LA POPULATION GENETIQUE :

	- Chaque joueur est considéré comme un individu.
	- Chaque individu possède un ADN (qui correspond à un vecteur W des pondérations des fonctions d'évaluations)
	- Chaque ADN est composé de gênes (Qui correspondent aux coordonnées des vecteurs W)
	- Un ensemble d'individu forme une population
	- La population évolue en jouant les uns contre les autres. (comme un tournoi)
	- A la fin, on évalue le taux de victoire et on choisit l'individu dominant.
	- On crée n enfants avec des parents aléatoire.
	- Un enfant est créé aléatoirement via les gênes de ses deux parents (on pourrait aussi faire une coupure vectorielle)
	- Pour garantir une part d'aléatoire dans les génes (indispensable dans un système d'évolution de population), on fait muter quelques
	  uns des individus, d'un taux défini ci-dessous dans les variables globales.
	- On garde, à chaque évolution, le meilleur des individus intact dans la prochaine génération (sans aucune mutation donc).
	- On reproduit le proccessu d'évolution, soit à l'infini, soit pour un nombre d'évolution donné.
	- A la fin, on récupére le génome du meilleur individu, celui que l'on utilisera pour notre joueur.

'''

# DEFINISSIONS DES VARIABLES GLOBALES UTILES DANS CE FICHIER

probabliteMutation = 0.3 # La probabilité pour qu'un individu soit muté
tauxDeMutation = 0.15 # Variation epsilon d'un des gênes
taillePopulation = 6 # taille de la population maximal
nombreDeGene = 3 # Nombre de composant des vecteurs W
nombreDeMatch = 10 # Nombre de match
nbEnfants = taillePopulation/2 # Nombre d'enfant par couple

# Dans cette version, tous les individus sont des alpha-béta

joueur1 = 5 # Joueur individu
joueur2 = 3 # Joueur ennemi

def evolutionPopulation():
	''' Fonction qui gére l'évolution de la population 

		Ne retourne rien.
	'''
	global joueur1, joueur2 # Utilisation des variable joueur1 et joueur2

	etat = get_etat_joueur() # On récupére l'état des joueurs

	# Menu qui demande à l'utilisateur quels sont les joueurs.

	print("================== EVOLUTION GENETIQUE DES VECTEURS COEFFICIENTS ====================\n")
	joueur1 = input("Choix des indivus : 0. Random, 1. Humain, 2. Premier Coup, 3. CheatAlgo, 4. Min_Max, 5. A_B : ")
	joueur2 = input("Choix des ennemis : 0. Random, 1. Humain, 2. Premier Coup, 3. CheatAlgo, 4. Min_Max, 5. A_B : ")
	print("=====================================================================================\n\n")

	enregistrementResultat("\n\n\n########## Nouvelle population VS " +str(get_nom_joueur(joueur2)) + " ##########\n") # Nouvelle population dans le fichier

	pop = initialisationPopulation() # Initialisation de la population de façon aléatoire
	affichePopulation(pop) # Affichage de la population de départ

	# Boule infinie (presque...)
	ite = 1
	while ite < 1000:

		print("\n----------------------- EVOLUTION NUMERO "+str(ite)+" -----------------------\n")

		enregistrementResultat("########## Evolution numéro "+str(ite)+" ##########\n")

		sc = [evaluationPopulation(x,pop) for x in pop] # Création d'une liste contenant les évaluations

		b = pop[sc.index(max(sc))] # Retourne le meilleur joueur
		best = [x for x in b] # Création du meilleur individu
		enfant = [] # Initialisation enfant vide

		# Parcourt nbEnfants fois la boucle

		for i in range(nbEnfants):

			r = randint(0, len(sc)-1) # Choisit au hasard une évaluation dans sc
			p1 = pop[r] # On recupere le r ième individus
			p2 = p1 # p2 = p1

			# while p2 == p1 pour garantir que les deux individus seront différents pour le croisement

			while p2 == p1: 

				r = randint(0, len(sc)-1) # Choisit au hasard une évaluation dans sc
				p2 = pop[r] # On récupére le r ième individus

			# On effectue les croisements entre p1 et p2

			enfant.append(croisement(p1, p2)) 

		npop = enfant # La nouvelle population est consituée des enfants

		npop.append(best) # On garde le meilleur dans la population

		# Auquel on ajoute aléatoirement des anciens jusqu'à remplir la population de taillePopulation individus

		while len(npop) < taillePopulation:

			i = randint(0, len(pop)-1) # Choisit au hasard une évaluation dans sc

			sc[i]=0 # On reinitialise l'évaluation à 0
			p = pop[i] # On récupére l'individu correspondant
			pop.remove(pop[i]) # On supprime l'individu i de la population actuelle

			x = random() # Génération d'un nombre aléatoire entre 0 et 1

			if x < probabliteMutation: # Si ce nombre est inférieur à notre probabilité de mutation
				p = mutation(p) # Alors on fait muter l'individu p

			npop.append(p) # et on l'ajoute à notre nouvelle population

		pop = npop # La nouvelle population devient la population actuel
		ite += 1 # On incrémente i de 1

	affichePopulation(pop) # Affichage de la population finale

def initialisationPopulation():

	''' Fonction qui initialise la population 
		Chaque individus, gêne etc..

		-> List^2
	'''

	pop = [] # Initialisation d'une population vide

	i = 0 # Incrémenteur pour le while 

	while i < taillePopulation: # On parcourt la boucle taillePopulation fois

		j = 0 # Initialisation d'un deuxieme incrémenteur
		indiv = [] # Création d'un individu vide

		while j < nombreDeGene:

			gene = random() # Génération d'un coefficient entre 0 et 1 pour le j ème gêne
			indiv.append(gene) # Ajout de ce coefficient au vecteur
			j += 1 # Incrémentation de j de 1

		indiv = normaliser(indiv) # Normalisation du vecteur
		pop.append(indiv) # Ajout de l'individu à la population
		i += 1 # Incrémentation de i de 1

	return pop # Retourne la population finale crée

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


def evaluationPopulation(p, pop):

	''' Fonction d'évaluation de la population
		Elle simule les parties entre les joueurs 
		+ évaluation de leurs performances

		List*List^2 -> Nat
	'''

	nombreVictoire = 0 # Initialisation du nombre de victoire à 0
	nombreDefaite = 0 # Initialisation du nombre de defaite à 0
	
	change_valeur_coeff(p,1) # On modifie les paramètres du joueur_ab pour coller à celle de l'individu p

	# On parcourt toute la population 

	for i in pop:
		if i != p: # On joue si et seulement si i n'est pas ce même individu (on ne joue pas contre soi même)

			change_valeur_coeff(i,2) # On change les paramètres de joueur_ab pour le deuxieme joueur

			resultat_match = NParties_genetique(joueur1, joueur2, nombreDeMatch) # On joue les parties

			# On incrémente le nombre de victoire et de defaite

			nombreVictoire += resultat_match[0] 
			nombreDefaite += resultat_match[1]

	# Affichage de l'individu, son ratio, et son gêne

	print("|| Individu numéro : "+str(pop.index(p))+", ratio : "+str(nombreVictoire)+"/"+str(nombreDefaite)+", gêne : "+str(p))

	# Ecriture de l'individu, son ratio, et son gêne

	enregistrementResultat("Individu numéro : "+str(pop.index(p))+", ratio : "+str(nombreVictoire)+"/"+str(nombreDefaite)+", gêne : "+str(p)+"\n")

	# On retourne le nombre de victoire normalisée

	return nombreVictoire - nombreDefaite


def mutation(p):

	''' Fonction de mutation d'un gêne de façon aléatoire

		List -> List
	'''

	s = random() # Nombre aléatoire entre 0 et 1
	i = int(random() * len(p)) # Choix d'un gêne aléatoire, de façon proportionnelle

	# On incrémente si s > 0.5, sinon on décrémente
	# Ceci nous permet d'avoir une approche aléatoire et non pas déterministes de l'évolution de la population 

	if s > 0.5:
		p[i] += tauxDeMutation
	elif (s <= 0.5) and (p[i] - tauxDeMutation > 0):
		p[i] -= tauxDeMutation

	# Normalisation du gêne
	normaliser(p)

	# On retourne l'individu une fois muté

	return p

def croisement(p1, p2):

	''' Fonction de croisement entre deux individus :
		Création d'un unique enfant (2 à venir?)

		List * List -> List
	'''

	enfant = [] # Initialisation un gêne enfant vide

	# On parcourt tous les composants du gênes

	for i in range(len(p1)):

		p = random() # Nombre aléatoire entre 0 et 1
		if p<0.5:
			enfant.append(p1[i]) # Attribution du gêne du parent 1
		else:
			enfant.append(p2[i]) # Attribution du gêne du parent 2

	enfant = mutation(enfant) # On fait muter l'enfant

	# Retourne l'enfant

	return enfant

def affichePopulation(l):
	''' Fonction qui se contente d'affiche tous les individus de la population 

		Ne retourne rien.
	'''

	# Quelques print pour une belle présentation

	print("============================== POPULATION ==============================")
	print("========================================================================\n")

	# On parcourt tous les individus

	for i in range(taillePopulation):
		print("|| Individu numéro "+str(i)+" : , Gêne : "+str(l[i])) # On affiche l'individu i et son gêne
		enregistrementResultat("Individu numéro "+str(i)+" : , Gêne : "+str(l[i])+"\n")

	# Esthétique

	print("========================================================================\n")
	print("========================================================================\n")

def enregistrementResultat(chaine):

	fichier = open("resultat_pop_gene.txt","a")
	fichier.write(chaine)
	fichier.close()




