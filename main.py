from board import board


def reset_board():
    for x in range(len(board)):
        if board[x] == "O" or board[x] == "X":
            board[x] = " "
def player1(board):
    player1_move = input("\nPlayer 1, Where would you like to move: ")
    if player1_move == "1a":
        board[1] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "1b":
        board[5] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "1c":
        board[9] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "2a":
        board[13] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "2b":
        board[17] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "2c":
        board[21] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "3a":
        board[25] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "3b":
        board[29] = "O"
        for x in board:
            print(x, end=" ")
    elif player1_move == "3c":
        board[33] = "O"
        for x in board:
            print(x, end=" ")
    else:
        print("Not a Valid Move")
        player1(board)


def player2(board):
    player2_move = input("\nPlayer 2, Where would you like to move: ")
    if player2_move == "1a":
        board[1] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "1b":
        board[5] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "1c":
        board[9] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "2a":
        board[13] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "2b":
        board[17] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "2c":
        board[21] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "3a":
        board[25] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "3b":
        board[29] = "X"
        for x in board:
            print(x, end=" ")
    elif player2_move == "3c":
        board[33] = "X"
        for x in board:
            print(x, end=" ")
    else:
        print("Not a Valid Move")
        player2(board)

def game_over(board, player_id):
    game_on = False
    go_again = input(f"\nGame Over! Player {player_id} has won. Would you like to play again? (y/n): ")
    if go_again == "y":
        play_game(state=True, board=board)
        board = board
def play_game(state, board):
    print("\nWelcome to Tic-Tac-Toe!")

    reset_board()
    for x in board:
        print(x, end=" ")

    print(
        "\n\nHow To Play: Type A Number for the row you would like to play in, and a letter for the column. Example: 1a correspoonds to the top left corner.")

    game_on = state
    while game_on:
        player1(board)
        if board[1] == "O" and board[5] == "O" and board[9] == "O":
            game_over(board, 1)
        if board[13] == "O" and board[17] == "O" and board[21] == "O":
            game_over(board, 1)
        if board[25] == "O" and board[29] == "O" and board[33] == "O":
            game_over(board, 1)
        if board[1] == "O" and board[13] == "O" and board[25] == "O":
            game_over(board, 1)
        if board[5] == "O" and board[17] == "O" and board[29] == "O":
            game_over(board, 1)
        if board[9] == "O" and board[21] == "O" and board[33] == "O":
            game_over(board, 1)

        if game_on:
            player2(board)
            if board[1] == "X" and board[5] == "X" and board[9] == "X":
                game_over(board, 2)
            if board[13] == "X" and board[17] == "X" and board[21] == "X":
                game_over(board, 2)
            if board[25] == "X" and board[29] == "X" and board[33] == "X":
                game_over(board, 2)
            if board[1] == "X" and board[13] == "X" and board[25] == "X":
                game_over(board, 2)
            if board[5] == "X" and board[17] == "X" and board[29] == "X":
                game_over(board, 2)
            if board[9] == "X" and board[21] == "X" and board[33] == "X":
                game_over(board, 2)


play_game(state=True, board=board)
