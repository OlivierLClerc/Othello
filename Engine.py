# Here the mechanics of the game
from Board import Board
from player import Joueur

class Engine:
    def __init__(self, board, joueur_noir, joueur_blanc):
        self.board = board
        self.joueur_noir = joueur_noir
        self.joueur_blanc = joueur_blanc

    def tour_par_tour(self):
        nb_coup_joue = 0
        joueur = self.joueur_noir
        while nb_coup_joue < 64:
            joueur.jouer(self.board)
            nb_coup_joue += 1
            joueur = self.joueur_blanc if joueur == self.joueur_noir else self.joueur_noir

