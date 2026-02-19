def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\n" + "*" * 13)
    for row in board:
        print(f"* {row[0]} | {row[1]} | {row[2]} *")
    print("*" * 13 + "\n")

def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (1-3): ")) - 1
            col = int(input(f"Player {player} - Enter column (1-3): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if row not in range(3) or col not in range(3):
            print("Position out of range.")
            continue

        if board[row][col] != " ":
            print("Cell already taken.")
            continue

        return row, col

def check_win(board, player):

    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def play():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play()
