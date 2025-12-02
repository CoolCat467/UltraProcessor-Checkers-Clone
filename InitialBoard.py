
def initial_board():
    board = [
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},

    ]

    # Place red pieces ('W') on rows 1, 2, 3
    row = 0
    while row < 3:
        col = 1
        while col < 9:
            if (row + col) % 2 == 1:  # Check if the square is dark (for white pieces)
                board[row][col] = 'R'  # Place red piece

            col = col + 1
        row = row + 1

    # Place black pieces ('W') on rows 6, 7, 8
    row = 5
    while row < 8:
        col = 1
        while col < 9:
            if (row + col) % 2 == 1:  # Check if the square is dark (for white pieces)
                board[row][col] = 'B'  # Place red piece

            col = col + 1
        row = row + 1


    print("Initializing starter board..")
    for row in board:
        print(row)

    return board
