def row_win(board, player):
    win = np.all(board==player,axis=1)
    if np.any(win):
        return True
    else:
        return False
    
row_win(board,1)
