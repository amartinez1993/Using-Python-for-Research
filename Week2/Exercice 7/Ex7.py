def col_win(board, player):
    win = np.all(board==player,axis=0)
    if np.any(win):
        return True
    else:
        return False
    
col_win(board,1)
