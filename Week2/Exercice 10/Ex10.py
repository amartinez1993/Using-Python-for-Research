def play_game():
    board = create_board()
    win = 0
    while win == 0:
        for player in [1,2]:
            random_place(board,player)
            win = evaluate(board)
            if win == 1 or win == 2 or win == -1:
                break
    return win
    
play_game()
