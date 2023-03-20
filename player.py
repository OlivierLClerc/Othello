
from Pawn import Pawn

class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def jouer(self, board):
        #new_pawn=Pawn(self.couleur)
        x = input(f'C\'est au joueur {self.couleur}, entrez la position du coup : ')
        col_index = ord(x[0].lower())-96-1
        ligne_index = int(x[1])-1
        while board.grid[ligne_index][col_index] != " ":
            print('Case déjà occupée, veuillez choisir une autre position')
            x = input('Entrez la position du coup : ')
            col_index = ord(x[0].lower())-96-1
            ligne_index = int(x[1])-1
        while board.check_valide(ligne_index,col_index,self.couleur) == False:
            print('Case non valide, veuillez choisir une autre position')
            x = input('Entrez la position du coup : ')
            col_index = ord(x[0].lower())-96-1
            ligne_index = int(x[1])-1
        board.grid[ligne_index][col_index] = Pawn(ligne_index,col_index,self.couleur)


