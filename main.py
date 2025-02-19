def print_grid(board):
    """

        This function prints the grid out to the console.

    :param board: 2D Array of the board layout
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, players):
    """

        This function checks to see if a winner has been declared

    :param board: 2D Array of the board layout
    :param players: Array of the X and Os
    :return: Boolean value representing a winning value
    """
    for i in range(3):
        if all(board[i][j] == players for j in range(3)) or all(board[j][i] == players for j in range(3)):
            return True
    if all(board[i][i] == players for i in range(3)) or all(board[i][2 - i] == players for i in range(3)):
        return True
    return False


def tie(board):
    """

        This function checks to see if a tie has been reached

    :param board: 2D Array of the board layout
    :return: Boolean value representing a tie
    """
    return all(col != " " for row in board for col in row)


def tictactoe():
    """

        This is the main function of the program

    :return: Boolean value representing the successful completion of the program or not.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_grid(board)
    for tries in range(9):
        player = players[tries % 2]
        while 1:
            try:
                col, row = get_input(player)
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


def get_input(player):
    """

        This function gets the user input for where the user wants to place their character

    :param player: Current player in the selection
    :return: position user selected
    """
    row, col = map(int, input(f"P {player}, row col (0-2): ").split())
    return col, row


tictactoe()