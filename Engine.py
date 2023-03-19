# Here the mechanics of the game

class Engine:
    def __init__(self, board, joueur_noir, joueur_blanc):
        self.board = board
        self.joueur_noir = joueur_noir
        self.joueur_blanc = joueur_blanc

    def tour_par_tour(self):
        nb_coup_joue = 0
        joueur = self.joueur_noir
        while nb_coup_joue < 64:
            joueur.jouer(self.board)
            nb_coup_joue += 1
            joueur = self.joueur_blanc if joueur == self.joueur_noir else self.joueur_noir
            print(str(self.board))


    def check_playable(self,board, row, col,token):
        playable = 0
        opposite_color = 'white' if token.color == 'black' else 'black'
        opposite_pawns_tot = []
        opposite_pawns= []
        # row
        for i in range(col + 1, 7):
            if board.grid[row][i].color == opposite_color:
                opposite_pawns.append((row, i))
                found_opposite_pawn = True
            elif board.grid[row][i].color == token.color and found_opposite_pawn:
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
            elif board.grid[row][i].color == token.color and found_opposite_pawn:
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
            elif board.grid[j][col].color == token.color and found_opposite_pawn:
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
            elif board.grid[j][col].color == token.color and found_opposite_pawn:
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
            elif board.grid[row+d][col+d].color == token.color and found_opposite_pawn:
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
            elif board.grid[row-d][col-d].color == token.color and found_opposite_pawn:
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
            elif board.grid[row+d][col-d].color == token.color and found_opposite_pawn:
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
            elif board.grid[row-d][col+d].color == token.color and found_opposite_pawn:
                playable = 1
                opposite_pawns_tot.append(opposite_pawns)
                break
            else:
                opposite_pawns=[]
                break

        return playable, opposite_pawns_tot           