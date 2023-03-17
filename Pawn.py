# Here the pawn/cell scr


class Pawn:
    def __init__(self, ligne, colonne, couleur):
        self.ligne = ligne
        self.colonne = colonne
        self.couleur = couleur
        self.coord = [ligne, colonne]
        self.adjacent = []
    
    def __str__(self):
        if self.couleur == "black":
            self.form = "X"
        elif self.couleur == "white":
            self.form = "O"
        else:
            self.form = " "
        return self.form
    
    def get_adjacent(self, grid):
        self.adjacent = [[self.ligne-1,self.colonne],[self.ligne+1,self.colonne],
                    [self.ligne,self.colonne+1],[self.ligne,self.colonne-1],
                    [self.ligne-1,self.colonne-1],[self.ligne-1,self.colonne+1],
                    [self.ligne+1,self.colonne-1],[self.ligne+1,self.colonne+1]]
        for cell in self.adjacent:
            if isinstance(grid[cell[0]][cell[1]], Pawn):
                return "OK"
            else:
                return "Pas OK"