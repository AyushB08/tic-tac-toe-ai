# Set up the game board as a list
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = "O"
computer = "X"


# Define a function to print the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    if player == "O":

        position = input("Choose a position from 1-9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        while board[position] != "-":
            position = int(input("Position already taken. Choose a different position: ")) - 1
        board[position] = player

    else:
        position = findBestMove(board)
        board[position] = "X"

    print_board()


# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    if (board[0] == board[1] == board[2] != "-") or \
            (board[3] == board[4] == board[5] != "-") or \
            (board[6] == board[7] == board[8] != "-") or \
            (board[0] == board[3] == board[6] != "-") or \
            (board[1] == board[4] == board[7] != "-") or \
            (board[2] == board[5] == board[8] != "-") or \
            (board[0] == board[4] == board[8] != "-") or \
            (board[2] == board[4] == board[6] != "-"):
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"


def get_value_of_game(board):
    if board[0] == board[1] == board[2] != "-":
        if board[0] == "O":
            return -10
        else:
            return 10

    if board[3] == board[4] == board[5] != "-":
        if board[3] == "O":
            return -10
        else:
            return 10

    if board[6] == board[7] == board[8] != "-":
        if board[6] == "O":
            return -10
        else:
            return 10

    if board[0] == board[3] == board[6] != "-":
        if board[0] == "O":
            return -10
        else:
            return 10

    if board[1] == board[4] == board[7] != "-":
        if board[1] == "O":
            return -10
        else:
            return 10

    if board[2] == board[5] == board[8] != "-":
        if board[2] == "O":
            return -10
        else:
            return 10

    if board[2] == board[4] == board[6] != "-":
        if board[2] == "O":
            return -10
        else:
            return 10


    # Check for a tie
    return 0
    # Game is not over


# Define the main game loop
def play_game():
    print_board()
    current_player = computer
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


def minimax(board, depth):
    value = get_value_of_game(board)
    print(value)
    if value == 10:
        return value

    if value == -10:
        return value

    if not isMovesLeft(board):
        return 0

    if isMovesLeft(board):
        best_val = -100
        for i in range(9):
            if board[i] == "-":
                board[i] = computer
                best_val = max(best_val, minimax(board, depth + 1))
                board[i] = "-"
        return best_val


def isMovesLeft(board):
    for i in range(9):

        if board[i] == "-":
            return True
    return False


def findBestMove(board):
    bestVal = -1000

    bestMove = 0

    for i in range(9):

        if board[i] == "-":
            board[i] = "X"
            value = minimax(board, 0)
            board[i] = "-"

            if value > bestVal:
                bestMove = i
                bestVal = value

    print(bestMove)
    return bestMove


# Start the game
play_game()
