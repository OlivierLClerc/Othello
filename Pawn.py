# Here the pawn/cell scr


class Pawn:
    def __init__(self, ligne, colonne, couleur):
        self.couleur = couleur
        self.ligne = ligne
        self.colonne = colonne
        self.adjacent = [[self.ligne-1,self.colonne],[self.ligne+1,self.colonne],
                    [self.ligne,self.colonne+1],[self.ligne,self.colonne-1],
                    [self.ligne-1,self.colonne-1],[self.ligne-1,self.colonne+1],
                    [self.ligne+1,self.colonne-1],[self.ligne+1,self.colonne+1]]
    
    def __str__(self):
        if self.couleur == "black":
            self.form = "X"
        elif self.couleur == "white":
            self.form = "O"
        return self.form

    def check_playable(self,board, row, col):
        playable = 0
        opposite_color = 'white' if self.color == 'black' else 'black'
        opposite_pawns_tot = []
        opposite_pawns= []
        # row
        for i in range(col + 1, 7):
            if board.grid[row][i].color == opposite_color:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for i in range(col - 1, 0, -1):
            if board.grid[row][i].color == opposite_color:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

    # column
        found_opposite_pawn = False
        for j in range(row + 1, 7):
            if board.grid[j][col].color == opposite_color:
                opposite_pawns.append((j, col))
                found_opposite_pawn = True
            elif board.grid[j][col].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for j in range(row - 1, 0, -1):
            if board.grid[j][col].color == opposite_color:
                opposite_pawns.append((j, col))
                found_opposite_pawn = True
            elif board.grid[j][col].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

    # diagonals
        found_opposite_pawn = False
        for d in range(1, min(7-row, 7-col)):
            if board.grid[row+d][col+d].color == opposite_color:
                opposite_pawns.append((row+d, col+d))
                found_opposite_pawn = True
            elif board.grid[row+d][col+d].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(row, col)):
            if board.grid[row-d][col-d].color == opposite_color:
                opposite_pawns.append((row-d, col-d))
                found_opposite_pawn = True
            elif board.grid[row-d][col-d].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(7-row, col)):
            if board.grid[row+d][col-d].color == opposite_color:
                opposite_pawns.append((row+d, col-d))
                found_opposite_pawn = True
            elif board.grid[row+d][col-d].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(row, 7-col)):
            if board.grid[row-d][col+d].color == opposite_color:
                opposite_pawns.append((row+d, col-d))
                found_opposite_pawn = True
            elif board.grid[row-d][col+d].color == self.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        return playable, opposite_pawns_tot        