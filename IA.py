import random
class IA(joueur):
    def __init__(self,nom,couleur) : #initialise le poids est la taille
        super().__init__(nom, couleur)
        coups_jouables = []


def IA_debile(self,board,token):
    coups_jouables = []

# boucle sur toutes les cases du plateau
    for row in range(board.num_rows):
        for col in range(board.num_cols):
        # vérifie si un coup est jouable sur la case actuelle et stocke sa longueur opposite_pawns_tot
            playable, opposite_pawns_tot = token.check_playable(board, row, col)
            if playable == 1:
            # stocke l'information dans la liste des coups jouables avec la longueur opposite_pawns_tot
                coups_jouables.append(((row, col), len(opposite_pawns_tot)))

# affiche la liste des coups jouables et leur longueur opposite_pawns_tot
    print(coups_jouables)

# trier la liste des coups jouables en fonction de la longueur de opposite_pawns_tot
    coups_jouables_tries = sorted(coups_jouables, key=lambda x: x[2], reverse=True)

# sélectionner un coup aléatoire avec la plus grande longueur de opposite_pawns_tot
    meilleur_coup = None
    if coups_jouables_tries:
        max_length = coups_jouables_tries

        import random

# trier la liste des coups jouables par longueur opposite_pawns_tot décroissante
    coups_jouables_tries = sorted(coups_jouables, key=lambda x: x[1], reverse=True)

# prendre le premier élément de la liste triée pour obtenir le coup avec la plus grande longueur opposite_pawns_tot
    meilleur_coup, longueur_max = coups_jouables_tries[0]

# chercher tous les coups qui ont la même longueur opposite_pawns_tot que le meilleur coup
    coups_max = [coup for coup in coups_jouables_tries if coup[1] == longueur_max]

# choisir un coup de manière aléatoire parmi les coups max
    meilleur_coup_aleatoire = random.choice(coups_max)
    ligne_index, col_index = meilleur_coup_aleatoire 
# afficher le meilleur coup et sa longueur opposite_pawns_tot
#print("Meilleur coup :", meilleur_coup, "avec une longueur opposite_pawns_tot de", longueur_max)
#print("Meilleur coup aléatoire :", meilleur_coup_aleatoire[0], "avec une longueur opposite_pawns_tot de", longueur_max)

    return ligne_index, col_index