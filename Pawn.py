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
            self.form== "O"
        else:
            self.couleur="black"
            self.form = "X"


   
    def check_playable(self,board, row, col):
        for t in range(0,8):
            step = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        playable = 0
<<<<<<< HEAD
        opposite_color = 'white' if self.couleur== 'black' else 'black'
        opposite_pawns = []
        opposite_pawns_tot= []
        for t in range(8):
            found_opposite_pawn = False
            row_step, col_step = step[t]
            for i in range(1, 8):
                check_row, check_col = row + i*row_step, col + i*col_step
                if not board.is_on_board(check_row, check_col):
                    break
                curr_piece = board.grid[check_row][check_col]
                if curr_piece != " ":
                    if curr_piece.couleur == opposite_color:
                        opposite_pawns.append((check_row, check_col))
                        found_opposite_pawn = True
                    elif curr_piece.couleur == self.couleur and found_opposite_pawn:
                        playable = 1
                        for t in range(len(opposite_pawns)):
                            opposite_pawns_tot.append(opposite_pawns[t])
                        break
                    else:
                        opposite_pawns = []
                        break
            
        print(opposite_pawns_tot,opposite_pawns)
        return playable, opposite_pawns_tot  



         
    
=======
        opposite_couleur = 'white' if self.couleur == 'black' else 'black'
        opposite_pawns_tot = []
        opposite_pawns= []
        # row
        found_opposite_pawn = False
        for i in range(col + 1, 7):
            if board.grid[row][i] != " " and board.grid[row][i].couleur == opposite_couleur:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i] != " " and board.grid[row][i].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for i in range(col - 1, 0, -1):
            if board.grid[row][i] != " " and board.grid[row][i].couleur == opposite_couleur:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i] != " " and board.grid[row][i].couleur == self.couleur and found_opposite_pawn:
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
            if board.grid[j][col] != " " and board.grid[j][col].couleur == opposite_couleur:
                opposite_pawns.append((j, col))
                found_opposite_pawn = True
            elif board.grid[j][col] != " " and board.grid[j][col].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for j in range(row - 1, 0, -1):
            if board.grid[j][col] != " " and board.grid[j][col].couleur == opposite_couleur:
                opposite_pawns_tot.append(opposite_pawns[t])
                found_opposite_pawn = True
            elif board.grid[j][col] !=  " " and board.grid[j][col].couleur == self.couleur and found_opposite_pawn:
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
            if board.grid[row+d][col+d] != " " and board.grid[row+d][col+d].couleur == opposite_couleur:
                opposite_pawns.append((row+d, col+d))
                found_opposite_pawn = True
            elif board.grid[row+d][col+d] != " " and board.grid[row+d][col+d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(row, col)):
            if board.grid[row-d][col-d] != " " and board.grid[row-d][col-d].couleur == opposite_couleur:
                opposite_pawns.append((row-d, col-d))
                found_opposite_pawn = True
            elif board.grid[row-d][col-d] != " " and board.grid[row-d][col-d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(7-row, col)):
            if board.grid[row+d][col-d] != " " and board.grid[row+d][col-d].couleur == opposite_couleur:
                opposite_pawns.append((row+d, col-d))
                found_opposite_pawn = True
            elif board.grid[row+d][col-d] != " " and board.grid[row+d][col-d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break

        found_opposite_pawn = False
        for d in range(1, min(row, 7-col)):
            if board.grid[row-d][col+d] != " " and board.grid[row-d][col+d].couleur == opposite_couleur:
                opposite_pawns.append((row+d, col-d))
                found_opposite_pawn = True
            elif board.grid[row-d][col+d] != " " and board.grid[row-d][col+d].couleur == self.couleur and found_opposite_pawn:
                playable = 1
                for t in range(len(opposite_pawns)):
                    opposite_pawns_tot.append(opposite_pawns[t])
                break
            else:
                opposite_pawns=[]
                break
        #print(opposite_pawns_tot,opposite_pawns)
        return playable, opposite_pawns_tot           
>>>>>>> a5870dfcddbcf22a166ad7fefa8d253851285c19
