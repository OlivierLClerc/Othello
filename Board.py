class Board:
    def __init__(self):
        '''
        Construction board as a 8x8 grid
        '''
        self.grid = [[0 for _ in range(8)] for _ in range(8)]


    def __str__(self):
        rows = []
        for row in self.grid:
            rows.append(" ".join(str(x) for x in row))
        return "\n".join(rows)

    def add_Pawn(self, ligneJoueur, colonneJoueur, Joueur):
        self.grid[ligneJoueur][colonneJoueur]=Pawn.pawn_form(Joueur.couleur)



#coord = [
#    'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 
#    'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 
#    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 
#    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 
#    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 
#    'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 
#    'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 
#    'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
#]


