# Here the pawn/cell scr


class Pawn:
    def __init__(self, couleur):
        self.couleur = couleur
        
    def pawn_form(self):
        if self.couleur == "black":
            self.form = "X"
        elif self.couleur == "white":
            self.form = "O"
        else:
            self.form = " "
    
    def __str__(self):
        return self.form
        