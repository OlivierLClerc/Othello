# Here the mechanics of the game
from Board import Board

class Engine:
    def __init__(self,board,joueurs1,joueurs2) :
        self.board=Board()
        
    def tour_par_tour():
        nb_coup_joue=0
        joueur= -1 #code pour les noirs
        while nb_coup_joue<65:
            if joueur==-1: #appeler le joueur
                x = input("c'est aux noirs :")
                x.split
                ligne_index=int(x[0])
                col_index= int(x[1])
                #self.board.set_value(ligne_index, col_index, -1)
                self.board.add_pawn(ligne_index, col_index)
                nb_coup_joue+=1
                joueur= 1
            elif joueur==1:
                x = input("c'est aux blancs :")
                x.split
                ligne_index=int(x[0])
                col_index= int(x[1])
                self.board.add_pawn(ligne_index, col_index)
                nb_coup_joue+=1
                joueur= -1

