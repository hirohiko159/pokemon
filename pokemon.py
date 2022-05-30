#!/usr/bin/env python
from re import A

from sys import version
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
#creation fonction pour presenter les pokemon
def presenter (pokemon) : 
    print (pokemon ['name']['french'])
    print (pokemon ['base']['HP'])
#creation fonction pour presenter les joueurs
def presenter_joueur (players) : 
    print (players['name'])
# Affichage des Pokemon d un joueur - liste complete
def show_pokemon (players):
    for i in range(len(players["Pokemons"])):
        print (players ["Pokemons"][i]["name"]["french"])
# Action Attaque lors d un combat
def attaque (poke1 , poke2) :
    poke2['base']['HP']-= poke1['base']['Attack']/4
#initialisation des variables
fuite = False 
i=0
reussite=0

#recuperation des joueurs 1 et 2
name_j1=input("Entrez le nom du joueur 1 : ") 
j1=bdd.Bdd1.retrieve_joueur(name_j1)
if j1 == False:
    # si le joueur n'existe pas on le crée
    j1=bdd.Bdd1.create_joueur(name_j1) 

name_j2=input("Entrez le nom du joueur 2 : ")
j2=bdd.Bdd1.retrieve_joueur(name_j2)
if j2 == False:
    j2=bdd.Bdd1.create_joueur(name_j2)

# creation de la liste des joueurs
joueurs = [j1,j2] 

print (" ##################  vous entrer en combat pokemon  #################")

#creation de variables pour gerer le tour par tour
tour= j1 
attente= j2
pokemon_joueur = random.choice (tour["Pokemons"])# on selectionne un pokemon actif chez les deux joueurs
pokemon_adversaire = random.choice (attente["Pokemons"]) 

# Combat de Pokemon - boucle While
while pokemon_adversaire ['base']['HP'] > 0 and pokemon_joueur ['base'] ['HP'] >0 and fuite==False : #condition de fin de partie
    print ("")
   #on affiche le joueur et le pokemon
    presenter_joueur (tour)  
    presenter (pokemon_joueur) 

    print ("")
    print("")
    # affichage des joueurs et de leur Pokemon actif
    presenter_joueur (attente)
    presenter (pokemon_adversaire)
    print ("")
    
    #Affiche du menu d'actions
    print("1) attaque")
    print("2) changer de pokemon")
    print("3) fuir")
    reponse =''
    if reponse not in ['1','2','3'] : 
        reponse = input ("que voulez vous faire (1,2,3) ")
    # Option 1 = Attaque   
    if reponse in ['1']:
            attaque (pokemon_joueur , pokemon_adversaire) 
            # gestion du cas ou un Pokemon est KO
            if pokemon_adversaire['base']['HP'] < 0:
                print(" Votre Pokemon ", pokemon_adversaire ['name']['french'], "est K.O. !" )
                #il faut faire un remove!!!
                bdd.Bdd1.add_pokemon(tour, attente, pokemon_adversaire)
                #afficher les nouvelles equipes
                print("Liste Pokemon j2")
                show_pokemon(attente)
                print("Liste Pokemon j1")
                show_pokemon(tour)
                # Pb si on active un Pokemon KO gagné lors d un tour précédent. HP = 0 fin du combat!
                pokemon_adversaire = random.choice (attente["Pokemons"])
                # Pb de boucle infinie si TOUS les Pokemon sont KO
                # while pokemon_adversaire['base']['HP'] < 0:
                #     pokemon_adversaire = random.choice (attente["Pokemons"])
                print(pokemon_adversaire ['name']['french'], " entre dans le combat !!")
            print("\n"*5)
    # Option 2 = Swap de Pokemon
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
    # Option 3 = Fuite
    if reponse in ['3'] :
        print ("vous prenez la fuite") 
        reussite=random.choice(range(4))
        if reussite == 0:
            fuite=True
            print("Reussite! Vous prenez la fuite")
        else:
            print("Echec! Le combat continue")
    #on alterne avec un inter pour gérer le tour par tour
    inter=pokemon_adversaire 
    pokemon_adversaire=pokemon_joueur #on alterne avec un inter pour gerer le tour par tour
    pokemon_joueur=inter
    inter= attente
    attente= tour
    tour= inter 
    
    
print ("######### Partie Finie #############")
#annoncer le gagnant
#faire une liste de pokemon pour en avoir 3
    
  

