# Main script to test and instanciate our objects

from Board import Board
from player import Joueur
from Engine import Engine


my_grid = Board()

Jean_michel=Joueur("jean_mi","black")
Josette=Joueur("josy","white")

new_partie=Engine(my_grid,Jean_michel,Josette)
new_partie.tour_par_tour()

#print(Jean_michel.couleur)
