def print_board(board):
    """function that prints the game board returns None"""

    # print the header (column numbers so to speak)
    print('0 1 2 3 4 5 6')

    # print the content of the board
    for row in board:
        print(' '.join(row))


def move_piece(board, col, player):
    """Three parameters:
    1) board -> 2d array that stores all of the values for our connect 4 board
    2) col -> integer ranging from 0 -> 6 inclusive indicating which column the player wants to place their piece in
    3) player -> integer either 0 or 1 indicates the player 0 => player 'X' and 1 => player 'O'

    move_piece(board, col, player) -> returns an updated board with the new piece in its location or it returns
    None if there is a "full column error"
    """

    # move down the column that the player has chosen and when there is no available space (meaning there is a
    # piece in that position) place a piece on unit above (unless no more space in the column)
    for row in range(6):
        # check that the current piece isn't blank
        if board[row][col] in ['X', 'O']:
            # there is a piece in this location now we must check that it isn't in the top row because if so
            # then there isn't anymore space in the column
            if row - 1 < 0:
                # no space in column therefore we throw an error "full column error" and return none
                print('There is no more space in this column')
                return None
            else:
                # we set the piece one higher to the player's piece and break out of our loop
                board[row - 1][col] = ['X', 'O'][player]
                break
        # if the piece was blank we check if it is the bottom piece in our grid. If it is we must place it no
        # matter what
        elif row == 5:
            # last row and from the above check we know that this is a blank space
            board[row][col] = ['X', 'O'][player]

    # return the updated board
    return board


def check_win(board):
    """function checks all possible combinations where either player can win
    1) The player won horizontally
    2) The player won vertically
    3) The player won diagonally

    returns either 'X', 'O', 'draw', or None (winner, draw, or game is still in progress and nobody has won yet)
    """
    # check row wins
    for row in board:
        for col in range(4):
            if row[col] == row[col + 1] == row[col + 2] == row[col + 3] != '.':
                return "Player " + row[col] + " Wins!"
    # check column wins
    for row in range(3):
        for col in range(7):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != '.':
                return "Player " + board[row][col] + " Wins!"
    # check positive diagonal wins
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != '.':
                return "Player " + board[row][col] + " Wins!"
    # check negative diagonal wins
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] != '.':
                return "Player " + board[row][col] + " Wins!"


# create a blank 2d array that is a blank connect 4 grid
b = [['.' for i in range(7)] for j in range(6)]

# receive player names that aren't empty
player0 = input('Player X, enter your name: ')

# check that the name isn't blank (that includes enters, blank spaces, and tabs)
while player0.strip() == '':
    # ask for a name again
    player0 = input('Player X, enter your name again: ')

# do the same for player one
player1 = input('Player O, enter your name: ')

while player1.strip() == '':
    # ask for a name again
    player1 = input('Player O, enter your name again: ')

# players is a dictionary that holds the information about our players (makes the code easier to read later on)
players = {
    # key: id (0 or 1) -> value: dictionary that holds the player name and player piece through the keys
    # 'name': player name,
    # 'piece': player piece (either X or O)
    0: {'name': player0, 'piece': 'X'},
    1: {'name': player1, 'piece': 'O'},
}

# create
current_player = 0
do_we_print_board = True

# main game loop
while True:
    # at the start of each turn print the current board unless we are told not to
    if do_we_print_board:
        # We print the board meaning that there was no "full column error" and it is the next person's turn
        print()
        print_board(b)
        print()
    else:
        # There was a "full column error" therefore we just reset the do_we_print_board
        do_we_print_board = True

    # ask the current player which column he or she would like to place his or her piece in
    player_column = int(
        input("{}, you're {}. What column do you want to play in? ".format(players[current_player]['name'],
                                                                           players[current_player]['piece'])))

    # check that the player has entered a valid column if not ask again
    while player_column < 0 or player_column > 6:
        print('INVALID COLUMN')
        player_column = int(
            input("{}, you're {}. What column do you want to play in? ".format(players[current_player]['name'],
                                                                               players[current_player]['piece'])))

    # we have a valid column therefore we move add a piece
    result = move_piece(b, player_column, current_player)

    # check if player has placed in a full column
    if result:
        # there is a result (no errors) so we update our board and switch moves
        if check_win(b):
            print_board(b)
            print(check_win(b))
            break
        b = result
        current_player = (current_player + 1) % 2
    else:
        # there was an error (full column error) therefore
        do_we_print_board = False
