def diag_win(board, player):
    win = np.diag(board==player)
    if np.any(win):
        return True
    else:
        return False
    
diag_win(board,1)
