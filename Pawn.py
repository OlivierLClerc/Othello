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

    def flip(self):
        if self.couleur== "black":
            self.couleur=="white"
        else:
            self.couleur="black"



    def check_playable(self, board, row, col):
        playable = 0
        opposite_couleur = 'white' if self.couleur == 'black' else 'black'
        opposite_pawns_tot = []
        opposite_pawns= []
        # row
        found_opposite_pawn = False
        for i in range(col + 1, 7):
            if board.grid[row][i] is not " " and board.grid[row][i].couleur == opposite_couleur:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i] is not " " and board.grid[row][i].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for i in range(col - 1, 0, -1):
            if board.grid[row][i] is not " " and board.grid[row][i].couleur == opposite_couleur:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i] is not " " and board.grid[row][i].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

    # column
        found_opposite_pawn = False
        for j in range(row + 1, 7):
            if board.grid[j][col] is not " " and board.grid[j][col].couleur == opposite_couleur:
                opposite_pawns.append((j, col))
                found_opposite_pawn = True
            elif board.grid[j][col] is not " " and board.grid[j][col].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for j in range(row - 1, 0, -1):
            if board.grid[j][col] is not " " and board.grid[j][col].couleur == opposite_couleur:
                opposite_pawns.append((j, col))
                found_opposite_pawn = True
            elif board.grid[j][col] is not " " and board.grid[j][col].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

    # diagonals
        found_opposite_pawn = False
        for d in range(1, min(7-row, 7-col)):
            if board.grid[row+d][col+d] is not " " and board.grid[row+d][col+d].couleur == opposite_couleur:
                opposite_pawns.append((row+d, col+d))
                found_opposite_pawn = True
            elif board.grid[row+d][col+d] is not " " and board.grid[row+d][col+d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(row, col)):
            if board.grid[row-d][col-d] is not " " and board.grid[row-d][col-d].couleur == opposite_couleur:
                opposite_pawns.append((row-d, col-d))
                found_opposite_pawn = True
            elif board.grid[row-d][col-d] is not " " and board.grid[row-d][col-d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(7-row, col)):
            if board.grid[row+d][col-d] is not " " and board.grid[row+d][col-d].couleur == opposite_couleur:
                opposite_pawns.append((row+d, col-d))
                found_opposite_pawn = True
            elif board.grid[row+d][col-d] is not " " and board.grid[row+d][col-d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(row, 7-col)):
            if board.grid[row-d][col+d] is not " " and board.grid[row-d][col+d].couleur == opposite_couleur:
                opposite_pawns.append((row+d, col-d))
                found_opposite_pawn = True
            elif board.grid[row-d][col+d] is not " " and board.grid[row-d][col+d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break
        print(opposite_pawns_tot,opposite_pawns)
        return playable, opposite_pawns_tot           