import json
import random

class Bdd ():

  def __init__(self):
        with open ("pokedex.json", "r") as f:    
            self.data_pokedex=json.load(f)
        with open ("type.json", "r") as f: 
            self.data_type=json.load(f)
        with open ("joueurs.json", "r") as f:
            self.data_joueurs=json.load(f)
        self.joueurs=[]
  
  #methode pour récupérer un pokemon aleatoire
  def get_random(self):
    return random.choice(self.data_pokedex) 
  
  #methode pour récupérer un joueur (et ses pokemons associés) en fonction d'un nom
  def retrieve_joueur(self, nom_joueur):
    for i in self.data_joueurs:
        if i ["name"] == nom_joueur:
          self.joueurs.append(i)
          return i
    return False

  #methode pour creer joueur
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
  
#   #methode supprimer un joueur 
#   def remove(self,nom_joueur):
#     Bdd.joueurs.remove(nom_joueur)
  
#   #methode enregistrer qui enregistre le dictionnaire self.data_joueurs dans le fichier json
#   joueurs=[]
#   date_joueurs.json
  
# #   for i["name"] in joueurs:
    




Bdd1=Bdd()
# print(Bdd1.get_random())

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


