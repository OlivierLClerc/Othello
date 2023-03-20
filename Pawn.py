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



         
    