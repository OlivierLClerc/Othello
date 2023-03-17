# Here the pawn/cell scr

#class Pawn:
#    def __init__(self, ligne_jeton, colonne_jeton, color):
#        self.ligne_jeton = ligne_jeton
#        self.colonne_jeton = colonne_jeton
#        self.value = color
#    
#    def change_value(self, ligne_grid, colonne_grid):
#        self.value = Board.grid[ligne_grid][colonne_grid]
#        
#    def cell_color(self):
#        if self.value==1:
#            print("white")
#        elif self.value==-1:
#            print("black")
#        else:
#            print("empty")
# 
#
#
#
#        
#
#

from player import Joueur

class Pawn:
    def __init__(self, form):
        self.form = form

    
    def pawn_form(self, form):
        if Joueur.couleur == "black":
            self.form = "X"
        elif Joueur.couleur == "white":
            self.form = "O"
        else:
            self.form = " "
        
