import json
import random

class Bdd ():
  joueur=[]
    def __init__(self):
        with open ("pokedex.json", "r") as f:    
            self.data_pokedex=json.load(f)
        with open ("type.json", "r") as f: 
            self.data_type=json.load(f)
        with open ("joueurs.bdd", "r") as f:
            self.data_joueurs=json.load(f)
    #methode pour récupérer un pokemon aleatoire
    def get_random(self):
        return random.choice(self.data_pokedex) 
    #methode récupérer un joueur en fonction d'un nom
    def retrieve_joueur(self, joueur)
        get_attr(self.data_joueurs,joueur)
    #methode pour creer joueur
    def create_joueur(self, nom_joueur)
        joueur={
          "name": nom_joueur,
          "Pokemon1": self.get_random(),
          "Pokemon2": self.get_random(),
          "Pokemon3": self.get_random()
        } 
    #methode "add_Bdd" qui doit ajouter un joueur dans le dictionnaire // un joueur est un dictionnaire de dictionnaire  
    def add_joueur(self, joueur, adversaire)
        Bdd.joueur.append(Bdd(adversaire{"Pokemon1", "Pokemon2", "Pokemon3"})
        humain.humains.append(humain(random.choice(humain.prenoms),random.choice(humain.sexe)))
    
    #methode supprimer un joueur 
    def remove(self,nom_joueur):
        Bdd.joueur.remove(nom_joueur)
    #methode changer un joueur (pour ajouter/supprimer pokemon selon le resultat du combat determiné par pokemon.py)
    #methode enregistrer qui enregistre le dictionnaire self.data dans le fichier json




Bdd1=Bdd()
print(Bdd1.get_random())



