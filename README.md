# AweleAI

This project is an AI for the Awele game (https://en.wikipedia.org/wiki/Oware). 
To launch, go to Awele/NParties folder and start menu.py script. 

## Players

All differents AI are inside the "Joueurs" folder. Here a quick explanation : 

  - joueur_humain : Human player
  - joueur_random : Random player 
  - joueur_maxrandom : Always plays the max hit
  - joueur_mega_max / joueur_minmax : maxrandom amelioration
  - joueur_horizon_X : X-level tree research
  - joueur_ab : Alpha-Beta algorithm
  - joueur_neuronne : Neural Network (TODO)

## Learning phase

All different learning method are inside the NParties folder. This phase try to determine the best value for the evaluation
functions coefficient.

  - entrainement : gradient regression
  - oracle : learn from master
  - population_genetique : genetic algorithm
  - neuronne : Neural Network 
  
## Data

Data are saved in the "Donnees" folder.

## Other

  - game.py : Contain all functions to handle a game
  - awele.py : Coutain all functions to play a game
