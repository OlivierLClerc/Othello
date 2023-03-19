
from Pawn import Pawn

class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def jouer(self, board):
        #new_pawn=Pawn(self.couleur)
        x = input(f'C\'est au joueur {self.couleur}, entrez la position du coup : ')
        ligne_index = int(x[0])
        col_index = int(x[1])
        valide,opposite_pawn=board.check_valide(ligne_index,col_index,self.couleur)
        while board.grid[ligne_index][col_index] != " ":
            print('Case déjà occupée, veuillez choisir une autre position')
            x = input('Entrez la position du coup : ')
            ligne_index = int(x[0])
            col_index = int(x[1])
        while  valide !=1:
            print('Case non valide, veuillez choisir une autre position')
            x = input('Entrez la position du coup : ')
            ligne_index = int(x[0])
            col_index = int(x[1])
        board.grid[ligne_index][col_index] = Pawn(ligne_index,col_index,self.couleur)
        for i in range(len(opposite_pawn)):
            pawn_to_flip=board.grid[opposite_pawn[i][0]][opposite_pawn[i][1]]
            flip(pawn_to_flip)
