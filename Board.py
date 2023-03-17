class Board:
    def __init__(self):
        '''
        Construction board as a 8x8 grid
        '''
        self.grid = [[" " for _ in range(8)] for _ in range(8)]


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


