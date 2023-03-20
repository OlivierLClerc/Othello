from Pawn import Pawn

class Board:
    def __init__(self):
        '''
        Construction board as a 8x8 grid
        '''
        #creation de la grid
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
        #creation des pawns initiaux
        self.grid[3][3] = Pawn(3,3,"white")
        self.grid[3][4] = Pawn(3,4,"black")
        self.grid[4][3] = Pawn(4,3,"black")
        self.grid[4][4] = Pawn(4,4,"white")
        

    def __str__(self):
        #print column names
        print('\n     A   B   C   D   E   F   G   H')
        # Define cell boundaries
        hori = "---"
        vert = "|"
        corn = "+"

        # Build string representation of board
        output = ""

        # Add empty horizontal line at the top of the grid
        #output += "\n"
        for i, row in enumerate(self.grid):
            # Add horizontal line at the top of the row
            output += "   " + (corn + hori) * len(row) + corn + "\n"
            #add row number
            output += " " + str(i+1) + " "

      # Add each cell in the row, separated by vertical lines
            for cell in row:
                output += f"{vert} {cell} "

            # Add vertical line at the end of the row
            output += vert + "\n"

        # Add horizontal line at the bottom of the grid
        output +="   " + (corn + hori) * len(row) + corn + "\n"
        
        return output
    

    def check_valide(self, ligne_joueur, colonne_joueur, joueur):
        valide =0
        my_new_pawn = Pawn(ligne_joueur,colonne_joueur,joueur)
<<<<<<< HEAD
        playable, opposite_pawn =  my_new_pawn.check_playable(self, ligne_joueur,colonne_joueur)
=======
        playable,opposite_pawn=my_new_pawn.check_playable(self, ligne_joueur,colonne_joueur)
        #print(opposite_pawn)
>>>>>>> 9a609957794668d3e79bc7fc5423000578a25ab9
        if playable ==1:
            valide =1
            return valide,opposite_pawn
        else:
            valide =0
        return valide,[]

    def is_on_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    #check si le jeton que l'on pose est sur une case adjacente d'un autre jeton
    # X et Y sont les coordonnées du jeton  
    #def is_adjacent(self, X, Y, list_of_pawns):
       # adjacent = [[X-1,Y], [X+1,Y], [X,Y+1], [X,Y-1], [X-1,Y-1], [X-1,Y+1], [X+1,Y-1], [X+1,Y+1]]
        #if adjacent not in list_of_pawns:
          #  return "Not possible"

    