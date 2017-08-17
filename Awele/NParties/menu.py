#!/usr/bin/python
# -*- coding: utf-8 -*-

from NParties import *
from population_genetique import *

def menu():
	choix = input("Que souhaitez vous faire : \n1. Simuler NParties \n2. Simulation Population\n: ")

	if choix == 1:
		NParties()
	elif choix == 2:
		evolutionPopulation()

menu()