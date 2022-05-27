
                        #!/usr/bin/env python

from sys import version
#import BDD
#import player
#import pokemon
import random
import os

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

 #   def start() -> demarre la partie
  #  def stop() -> quand la partie se termine, on enregistre les dicos



# creation des listes pour les joueurs (remplace les classes)
# le joueur1 a plusieurs attributs:
# noms[0]
# joueur[0]
# bateaux[0]
# points[0]



poke1 = {
    
    "id": 1,
    "name": {
      "english": "Bulbasaur",
      "japanese": "フシギダネ",
      "chinese": "妙蛙种子",
      "french": "Bulbizarre"
    },
    "type": [
      "Grass",
      "Poison"
    ],
    "base": {
      "HP": 45,
      "Attack": 49,
      "Defense": 49,
      "Sp. Attack": 65,
      "Sp. Defense": 65,
      "Speed": 45
    }
  }

poke2 = {
    
    "id": 2,
    "name": {
      "english": "Ivysaur",
      "japanese": "フシギソウ",
      "chinese": "妙蛙草",
      "french": "Herbizarre"
    },
    "type": [
      "Grass",
      "Poison"
    ],
    "base": {
      "HP": 60,
      "Attack": 62,
      "Defense": 63,
      "Sp. Attack": 80,
      "Sp. Defense": 80,
      "Speed": 60
    }  
    
}

poke3 = {
    "id": 10,
    "name": {
      "english": "Caterpie",
      "japanese": "キャタピー",
      "chinese": "绿毛虫",
      "french": "Chenipan"
    },
    "type": [
      "Bug"
    ],
    "base": {
      "HP": 45,
      "Attack": 30,
      "Defense": 35,
      "Sp. Attack": 20,
      "Sp. Defense": 20,
      "Speed": 45
    }
  }


poke4 = {
    "id": 35,
    "name": {
      "english": "Clefairy",
      "japanese": "ピッピ",
      "chinese": "皮皮",
      "french": "Mélofée"
    },
    "type": [
      "Fairy"
    ],
    "base": {
      "HP": 70,
      "Attack": 45,
      "Defense": 48,
      "Sp. Attack": 60,
      "Sp. Defense": 65,
      "Speed": 35
    }
  }


j1 = {
  "name": "Thomas",
  "Pokemons" : [poke1,poke2] 
}

j2 = {
  "name": "Ranya",
    "Pokemons" : [poke3,poke4]
}

joueurs = [j1,j2]
i=0

print (" ##################  vous entrer en combat pokemon  #################")
def presenter (pokemon) :
    print (pokemon ['name']['french'])
    print (pokemon ['base']['HP'])
def presenter_joueur (players) :
    print (players['name'])
#def swap_pokemon ()
#j1 = vdd
def attaque (poke1 , poke2) :
    poke2['base']['HP']-= poke1['base']['Attack']/2

tour= j1
attente= j2
pokemon_adversaire = random.choice (attente["Pokemons"])
pokemon_joueur = random.choice (attente["Pokemons"])    
while pokemon_adversaire ['base']['HP'] > 0 and pokemon_joueur ['base'] ['HP'] >0 :
    print ("")
    presenter_joueur (tour)
    presenter (pokemon_joueur)
    print ("")
    print("")
    presenter_joueur (attente)
    presenter (pokemon_adversaire)
    print ("")

    if version[0] == "3":
        raw_input = input
    
    print("1) attaque")
    print("2) changer de pokemon")
    print("3) fuir")
    reponse =''
    
    
    if reponse not in ['1','2','3'] :
        reponse = raw_input("que voulez vous faire (1,2,3) ")
        
    if reponse in ['1',]:
            attaque (pokemon_joueur , pokemon_adversaire)
            print("\n"*50)
            
            #print ( pokemon_adversaire "prend " )
    #if reponse in ['2'] :
        
    if reponse in ['3'] :
        print ("vous prenez la fuite")
        break  
    inter=pokemon_adversaire 
    pokemon_adversaire=pokemon_joueur
    
    pokemon_joueur=inter
    
    
    inter= attente
    attente= tour
    tour= inter 
        
print ("######### Partie Finie #############")
                
#annoncer le gagnant
#faire jouer lautre joueur
#clear la console
#faire une liste d epokemon pour en avoir 3 
