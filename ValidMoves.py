
def valid_moves(board, piece, row, col):
    valid_moves = []

    # Red pieces move downwards (towards lower rows)
    if piece == 'R':
        # down-left: (row+1, col-1), down-right: (row+1, col+1)
        directions = [(1, -1), (1, 1)]

    # Black pieces move upwards (towards higher rows)
    elif piece == 'B':
        # up-left: (row-1, col-1), up-right: (row-1, col+1)
        directions = [(-1, -1), (-1, 1)]

    else:
        return valid_moves  # If no valid piece, return empty list

    # Loop through each direction and check if the move is within bounds
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the move is within bounds (1 <= row <= 8 and 1 <= col <= 8)
        if 1 <= new_row <= 8 and 1 <= new_col <= 8:
            # Ensure the destination square is empty (no other pieces present)
            if board[new_row - 1][new_col] == '':
                valid_moves.append((new_row, new_col))

    return valid_moves