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


    def check_playable(self, row, col, board,token):
        #ligne
        for i in range(col + 1, 7):
            while board.grid(row, i).color != token.color:
                self.flip(row, i)
                break
        for i in range(col -1, 0,-1):
            while board.grid(row, i).color != token.color:
                self.flip(row, i)
                break
        #colonne
        for j in range(row + 1, 7):
            while board.grid(row, i).color != token.color:
                self.flip(col, j)
                break
        for j in range(row -1, 0,-1):
            while board.grid(row, i).color != token.color:
                self.flip(col, j)