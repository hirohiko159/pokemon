import json
import random

class Bdd ():

  def __init__(self):
        # load le pokedex dans une variable
        with open ("pokedex.json", "r") as f:    
            self.data_pokedex=json.load(f)
        # load les types dans une variable
        with open ("type.json", "r") as f: 
            self.data_type=json.load(f)
        # load la base de donnée joueurs dans une variable
        with open ("joueurs.json", "r") as f:
            self.data_joueurs=json.load(f)
        self.joueurs=[]
  
  #methode pour récupérer un pokemon aleatoire
  def get_random(self):
    return random.choice(self.data_pokedex) 
  
  #methode pour récupérer un joueur (et ses pokemons associés) en fonction de son nom
  def retrieve_joueur(self, nom_joueur):
    #on parcourt les noms dans la bdd
    for i in self.data_joueurs:
        if i ["name"] == nom_joueur:
          self.joueurs.append(i)
          return i
    #si le nom_joueur n est pas dans la bdd
    return False

  #methode pour creer joueur - on lui assigne 3 Pokemons aleatoires
  def create_joueur(self, nom_joueur):
    joueur={
    "name": nom_joueur,
    "Pokemons": [self.get_random(), 
                self.get_random(),
                self.get_random()]
    } 
    self.joueurs.append(joueur)
    return joueur
  
  # methode pour changer pour ajouter/supprimer pokemon selon le resultat du combat determiné par pokemon.py
  def add_pokemon(self, joueur, adversaire, pokemon):
    joueur["Pokemons"].append(pokemon)
    adversaire["Pokemons"].remove(pokemon)
  

  ######### A FAIRE ############
#   #methode supprimer un joueur 
#   def remove(self,nom_joueur):
#     Bdd.joueurs.remove(nom_joueur)
  
#   #methode enregistrer qui enregistre le dictionnaire self.data_joueurs dans le fichier json
#   joueurs=[]
#   date_joueurs.json
  
# #   for i["name"] in joueurs:
    

# Initialise la class ? 
Bdd1=Bdd()
# print(Bdd1.get_random())










########## TEST LORS DU DEVELOPPEMENT - A supprimer ###########

# nom_joueur1=input("quel joueur1? ")
# # joueur1=Bdd1.create_joueur(nom_joueur1)
# joueur1=Bdd1.retrieve_joueur(nom_joueur1)
# nom_joueur2=input("quel joueur2? ")
# # joueur2=Bdd1.create_joueur(nom_joueur2)
# joueur2=Bdd1.retrieve_joueur(nom_joueur2)

# print("Liste Joueurs existe ?", joueurs)

# print("joueur1 : ",joueur1)

# print("joueur2 : ",joueur2)

# Bdd1.add_pokemon(joueur1,joueur2, joueur2["Pokemons"][0])

# print("joueur1 : ",joueur1)

# print("joueur2 : ",joueur2)
