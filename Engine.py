# Here the mechanics of the game
from Board import Board
from player import Joueur

class Engine:
    def __init__(self):
        pass

    def tour_par_tour(self):
        print('Bienvenue dans votre partie d\'Othello')
        board = Board()
        name_black = input('Choisir un nom pour le joueur noir :')
        name_white = input('Choisir un nom pour le joueur blanc :')
        joueur_black = Joueur(name_black, "black")
        joueur_white = Joueur(name_white, "white")
        nb_coup_joue = 0
        joueur = joueur_black
        print(str(board))
        while nb_coup_joue < 64:
            joueur.jouer(board)
            nb_coup_joue += 1
            joueur = joueur_white if joueur == joueur_black else joueur_black
            print(str(board))


    def check_playable(self, row, col, board,token):
        #ligne
        for i in range(col + 1, 7):
            while board.grid(row, i).color != token.color:
                self.flip(row, i)
                break
        for i in range(col -1, 0,-1):
            while board.grid(row, i).color != token.color:
                self.flip(row, i)
                break
        #colonne
        for j in range(row + 1, 7):
            while board.grid(row, i).color != token.color:
                self.flip(col, j)
                break
        for j in range(row -1, 0,-1):
            while board.grid(row, i).color != token.color:
                self.flip(col, j)