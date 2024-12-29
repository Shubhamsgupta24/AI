# Defines tictactoe game board which is 3*3 in our case
board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("---------")

# This function checks whether a player has win or not
def check_win():
    # Check for a straight line in rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != " ":
            return board[i]

    # Check for a straight in columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != " ":
            return board[i]

    # Check for a straigh line in diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]

    if " " not in board:
        return "Draw"

    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    result = check_win()
    if result == "X":
        return -1
    if result == "O":
        return 1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI player that is the opposite player tries to minimise max utility
def ai_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# Main game loop
while True:
    print_board()
    
    if " " not in board or check_win():
        break

    player_move = int(input("Enter your move (1-9): ")) - 1

    if 0 <= player_move < 9 and board[player_move] == " ":
        board[player_move] = "X"
    else:
        print("Invalid move. Try again.")
        continue

    if " " not in board or check_win():
        break

    ai_move()

print_board()

# Display game result
result = check_win()
if result == "X":
    print("You win!")
elif result == "O":
    print("AI wins!")
else:
    print("It's a draw!")
