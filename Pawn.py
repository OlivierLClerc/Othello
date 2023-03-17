# Here the pawn/cell scr

from player import Joueur

class Pawn:
    def __init__(self, couleur, form=" "):
        self.couleur = couleur
        self.form = form

    
    def pawn_form(self):
        if self.couleur == "black":
            self.form = "X"
        elif self.couleur == "white":
            self.form = "O"
        else:
            self.form = " "
        