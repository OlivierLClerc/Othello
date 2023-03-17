def get_adjacent(pawn, grid)
    adjacent = [[pawn.ligne-1,pawn.colonne],[pawn.ligne+1,pawn.colonne],
                        [pawn.ligne,pawn.colonne+1],[pawn.ligne,pawn.colonne-1],
                        [pawn.ligne-1,pawn.colonne-1],[pawn.ligne-1,pawn.colonne+1],
                        [pawn.ligne+1,pawn.colonne-1],[pawn.ligne+1,pawn.colonne+1]]
    for cell in adjacent:
        if isinstance(grid[cell[0]][cell[1]], pawn):
            return "OK"
        else:
            return "Pas OK"