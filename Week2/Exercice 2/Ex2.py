def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
    

board = create_board()
place(board, 1, (0,0))
