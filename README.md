# pokemon
combat pokemon

Groupe 2 : Florent - Gabriel - Thibault - Thomas - Rania

Ressources: 
- on importe le git https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json (base de donné pokemon)
- on importe le git des faiblesse/force https://github.com/filipekiss/pokemon-type-chart/blob/master/types.json




Deroulement du programme:
  
###### COMBAT #####
On rentre son nom de joueur: soit il est connu et renseigné dans la base de donnée, soit on le crée et on le renseigne dans la bdd 
on lui assigne 3 pokemons aleatoires (from pokedex)

* choix du 1er combattant
Pour chacun des joueurs, un pokemon aléatoire est choisi parmi ceux de son pool

* détermination du 1er dresseur
on compare "speed" du 1er pokemon pour savoir qui va commencer # BDD stats

* Tour classique Joueur 1
on affiche les statistiques de son 1er pokemon et celles de son adversaire:
on lui propose 3 choix (avec un case) attaquer changer de pokemon fuir



Menu choix action
  - attaquer:
    Le pokemon actif du joueur attaque le pokemon adverse,
    on soustrait aux "HP" du pokemon adverse l'"ATTACK" du pokemon attaquant

    si le pokemon attaqué est dans les faiblesses du pokemon attanquant on soustrait "SP.DEFENSE" du pokemon attaqué a l"ATTACK" du pokemon attanquant

  - changer de pokemons
    On montre la liste des pokemons disponibles du joueur.
    Il peut changer de pokemon actif

  - fuir
    Le joueur a 1 chance sur 4 de fuir le combat.
    les joueurs gardent leurs pokemons restant dans une BDD
    la partie est terminé si il fuit
    
A l'issue du tour, if HP pokemon = 0 alors pokemon KO
if pokemon j1 est ko (on peu plus l'utiliser ) then on envoi le suivant
                        
on passe sur le tour du joueur 2 on repete la meme chose



le combat continue tant qu'il reste 2 pokemon non Ko et que personne n'a fuit ( avec des elif)

#### if j1 ou j2 na plus de pokemon partie finie et on importe le resulat sur la base de donnée
                        
 

######  partie gestion de la bdd ########
                        
on enregistre le nom de joueur et on lui attribue 3 pokemons
quand un pokemon est mis Ko ll est transferé chez l'autre joueur
si un joueur perd ses 3 pokemons c'est game over on le suprime de la bdd


###### 

                        
