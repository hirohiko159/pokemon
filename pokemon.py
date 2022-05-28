#!/usr/bin/env python
from re import A

from sys import version
#import BDD
#import player
#import pokemon
import random
import os
import bdd


######## tentative infructueuse ###############
#clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#clearConsole()

# class game():
#     def __init__(self):
#         print (" ##################  let's fight some pokemons #################")
#     def affichage_pokemon (self, player) :
#         player.attribution_pokemon()
#         return
#     def menu (self):
#         print("pokegoooooooooooooooo")
# g = game ()
# j1 = player.joueur ()
# print (j1.name)
# print (g.affichage_pokemon)
# j2 = player.joueur ()
# print (g.affichage_pokemon)
#class game():
#    def __init_(self):
#       self.joueurs=[{},{}]
#       self.joueur_actif=0
#   def init_bdd() -> va chercher les joueurs, qui va chercher les pokemons
#   def start() -> demarre la partie#  def stop() -> quand la partie se termine, on enregistre les dicos

# creation des listes pour les joueurs (remplace les classes)
# le joueur1 a plusieurs attributs:
# noms[0]
# joueur[0]
# bateaux[0]
# points[0]

#definition des fonctions
def presenter (pokemon) : #creation fonction pour presenter les pokemon
    print (pokemon ['name']['french'])
    print (pokemon ['base']['HP'])
def presenter_joueur (players) : #creation fonction pour presenter les joueurs
    print (players['name'])
def show_pokemon (players):
    for i in range(len(players["Pokemons"])):
        print (players ["Pokemons"][i]["name"]["french"])
def attaque (poke1 , poke2) :
    poke2['base']['HP']-= poke1['base']['Attack']/2
fuite = False #initialisation des variables
i=0

#recuperation des joueurs 1 et 2
name_j1=input("Entrez le nom du joueur 1 : ") 
j1=bdd.Bdd1.retrieve_joueur(name_j1)
if j1 == False:
    j1=bdd.Bdd1.create_joueur(name_j1) # si le joueur n'existe pas on le creer
name_j2=input("Entrez le nom du joueur 2 : ")
j2=bdd.Bdd1.retrieve_joueur(name_j2)
if j2 == False:
    j2=bdd.Bdd1.create_joueur(name_j2)

joueurs = [j1,j2] # creation de la liste des joueurs

print (" ##################  vous entrer en combat pokemon  #################")
tour= j1 #creation de variables pour gerer le tour par tour
attente= j2
pokemon_joueur = random.choice (tour["Pokemons"])# on selectionne un pokemon actif chez les deux joueurs
pokemon_adversaire = random.choice (attente["Pokemons"]) 
while pokemon_adversaire ['base']['HP'] > 0 and pokemon_joueur ['base'] ['HP'] >0 and fuite==False : #condition de fin de partie
    print ("")
    presenter_joueur (tour)  #on aficche le joueur et le pokemon
    presenter (pokemon_joueur) 

    print ("")
    print("")
    presenter_joueur (attente)
    presenter (pokemon_adversaire)
    print ("")

    print("1) attaque")
    print("2) changer de pokemon")
    print("3) fuir")
    reponse =''
    if reponse not in ['1','2','3'] : 
        reponse = input ("que voulez vous faire (1,2,3) ")
    if reponse in ['1']:
            attaque (pokemon_joueur , pokemon_adversaire) 
            print("\n"*50)
    if reponse in ['2'] :
      show_pokemon (tour)
      # ne fonctionne que si le joueur possede 3 Pokemon!!
      choix= input ("quelle pokemons voulez vous choisir (a, b, c)")
      if choix in ['a']:
        pokemon_joueur=tour["Pokemons"][0]
      if choix in ['b']:
        pokemon_joueur=tour["Pokemons"][1]
      if choix in ['c']:
        pokemon_joueur=tour["Pokemons"][2]
    if reponse in ['3'] :
        print ("vous prenez la fuite") 
        fuite=True
        
    inter=pokemon_adversaire 
    pokemon_adversaire=pokemon_joueur #on alterne avec un inter pour gerer le tour par tour
    pokemon_joueur=inter
    inter= attente
    attente= tour
    tour= inter 
print ("######### Partie Finie #############")
#annoncer le gagnant
#faire une liste d epokemon pour en avoir 3
    
  
