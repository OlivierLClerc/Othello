class Joueur:
    def __init__(self, code_joueur, couleur):
        self.code_joueur = code_joueur
        self.couleur = couleur

    def jouer(self, board):
        x = input(f'C\'est au joueur {self.couleur}, entrez la position du coup : ')
        ligne_index = int(x[0])
        col_index = int(x[1])
        while board.get_value(ligne_index, col_index) != 0:
            print('Case déjà occupée, veuillez choisir une autre position')
            x = input('Entrez la position du coup : ')
            ligne_index = int(x[0])
            col_index = int(x[1])
        board.set_value(ligne_index, col_index, self.code_joueur)
