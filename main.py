def print_grid(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, players):
    for i in range(3):
        if all(board[i][j] == players for j in range(3)) or all(board[j][i] == players for j in range(3)):
            return True
    if all(board[i][i] == players for i in range(3)) or all(board[i][2 - i] == players for i in range(3)):
        return True
    return False


def tie(board):
    return all(col != " " for row in board for col in row)


def tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_grid(board)
    for tries in range(9):
        player = players[tries % 2]
        while 1:
            try:
                row, col = map(int, input(f"P {player}, row col (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Nope. Again.")
            except ValueError as ve:
                print("Wrong. 0-2 pls.\n" + str(ve))
        print_grid(board)
        if check_winner(board, player):
            print(f"P {player} wins!")
            return
        if tie(board):
            print("Draw!")
            return
    print("Draw!")


tictactoe()