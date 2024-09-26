def minimax(board, is_maximizing):
    best_move = None

    # Base case: return score if the game is over
    if board.score is not None:
        return board.score, best_move

    if is_maximizing:
        best_score = -float('inf')  # Maximizing starts with the worst possible score
    else:
        best_score = float('inf')  # Minimizing starts with the highest possible score

    # Loop through all cells to check for possible moves
    for i in range(3):
        for j in range(3):
            if board.is_empty(i, j):
                board.move(i, j)  # Make a move
                score, _ = minimax(board, not is_maximizing)  # Recur with the new board state
                board.clear(i, j)  # Undo the move (backtrack)

                if is_maximizing:
                    if score > best_score:  # Maximizing tries to get the highest score
                        best_score = score
                        best_move = (i, j)
                else:
                    if score < best_score:  # Minimizing tries to get the lowest score
                        best_score = score
                        best_move = (i, j)

    return best_score, best_move