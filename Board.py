from Engine import Engine
from Pawn import Pawn
class Board:
    def __init__(self):
        '''
        Construction board as a 8x8 grid
        '''
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
        self.grid[3][3] = Pawn(3,3,"white")
        self.grid[3][4] = Pawn(3,4,"black")
        self.grid[4][3] = Pawn(4,3,"black")
        self.grid[4][4] = Pawn(4,4,"white")


    def __str__(self):
        # Define cell boundaries
        hori = "---"
        vert = "|"
        corn = "+"

        # Build string representation of board
        output = ""

        # Add empty horizontal line at the top of the grid
        output += "\n"
        
        for row in self.grid:
            # Add horizontal line at the top of the row
            output += (corn + hori) * len(row) + corn + "\n"

      # Add each cell in the row, separated by vertical lines
            for cell in row:
                output += f"{vert} {cell} "

            # Add vertical line at the end of the row
            output += vert + "\n"

        # Add horizontal line at the bottom of the grid
        output += (corn + hori) * len(row) + corn + "\n"
        
        return output
    
    def check_valide(self, ligne_joueur, colonne_joueur, joueur):
        valide =0
        my_new_pawn = Pawn(ligne_joueur,colonne_joueur,joueur)
        playable,opposite_pawn=my_new_pawn.check_playable(self, ligne_joueur,colonne_joueur)
        print(opposite_pawn)
        if playable ==1:
            for cell in my_new_pawn.adjacent:
                if isinstance(self.grid[cell[0]][cell[1]], Pawn):
                    if my_new_pawn.couleur != self.grid[cell[0]][cell[1]].couleur:
                        valide =1
                        return valide,opposite_pawn
        return valide,[]



    #check si le jeton que l'on pose est sur une case adjacente d'un autre jeton
    # X et Y sont les coordonnées du jeton  
    #def is_adjacent(self, X, Y, list_of_pawns):
       # adjacent = [[X-1,Y], [X+1,Y], [X,Y+1], [X,Y-1], [X-1,Y-1], [X-1,Y+1], [X+1,Y-1], [X+1,Y+1]]
        #if adjacent not in list_of_pawns:
          #  return "Not possible"






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


