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
    print()
    if player == "O":

        position = input("Choose a position from 1-9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        while board[position] != "-":
            position = int(input("Position already taken. Choose a different position: ")) - 1
        board[position] = player
        print()

    else:
        position = findBestMove(board)
        board[position] = "X"

    print_board()


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
    elif not isMovesLeft(board):
        return "tie"
    # Game is not over
    else:
        return "play"


def isMovesLeft(board):
    for i in range(9):
        if board[i] == "-":
            return True
    return False


# Define a function to check if the game is over

# main game loop
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
            if current_player == "O":
                current_player = "X"
            else:
                current_player = "O"


def get_value_of_board(board):
    if board[0] == board[1] == board[2]:
        if board[0] == "O":
            return -10
        if board[0] == "X":
            return 10
    if board[3] == board[4] == board[5]:
        if board[3] == "O":
            return -10
        if board[3] == "X":
            return 10
    if board[6] == board[7] == board[8]:
        if board[6] == "O":
            return -10
        if board[6] == "X":
            return 10

    if board[0] == board[3] == board[6]:
        if board[0] == "O":
            return -10
        if board[0] == "X":
            return 10

    if board[1] == board[4] == board[7]:
        if board[1] == "O":
            return -10
        if board[1] == "X":
            return 10

    if board[2] == board[5] == board[8]:
        if board[2] == "O":
            return -10
        if board[2] == "X":
            return 10

    if board[0] == board[4] == board[8]:
        if board[0] == "O":
            return -10
        if board[0] == "X":
            return 10

    if board[2] == board[4] == board[6]:
        if board[2] == "O":
            return -10
        if board[2] == "X":
            return 10

    return 0


def minimax(board, depth, isComputerPlaying, alpha, beta):
    value = get_value_of_board(board)

    if value == 10 or value == -10:
        return value

    if not isMovesLeft(board):
        return 0

    if isComputerPlaying:


        best_val = -10
        for i in range(9):
            if board[i] == "-":
                board[i] = computer

                best_val = max(best_val, minimax(board, depth + 1, not isComputerPlaying, alpha, beta) - depth)
                board[i] = "-"
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break




    else:
        best_val = 10
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                best_val = min(best_val, minimax(board, depth + 1, not isComputerPlaying, alpha, beta) + depth)
                board[i] = "-"
                beta = min(beta, best_val)
                if beta <= alpha:
                    break
    return best_val


def findBestMove(board):

    bestVal = -10

    bestMove = 0

    for i in range(9):

        if board[i] == "-":
            board[i] = "X"
            value = minimax(board, 0, False, -1000, 1000)
            board[i] = "-"
            if value > bestVal:
                bestMove = i
                bestVal = value

    return bestMove


play_game()
