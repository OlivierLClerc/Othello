# Here the pawn/cell scr

from player import Joueur

class Pawn:
    def __init__(self, couleur, form=" "):
        self.couleur = couleur
        self.form = form
    if self.couleur == "black":
        self.form = "X"
    elif self.couleur == "white":
        self.form = "O"
    else:
        self.form = " "
        
    def __str__(self):
        return self.form
        