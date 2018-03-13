def random_place(board, player):
    possiblestat = possibilities(board)
    possiblestat = random.choice(possiblestat)
    place(board,player,possiblestat)
    return board
    
board = random_place(board,2)
board = create_board()
