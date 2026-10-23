
# The 8 ways to win: 3 rows, 3 columns and 2 diagonals (board indexes 0-8)
WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
]


def create_board():
    """Creates a new board: a list of 9 empty squares (" ")."""
    board = []
    for square in range(9):
        board.append(" ")
    return board


def square_label(board, index):
    """Returns the symbol in a square, or its number (1-9) if it is empty."""
    label = board[index]
    if label == " ":
        label = str(index + 1)
    return label


def print_board(board):
    """Prints the board, showing the number of every empty square."""
    for row in range(3):
        cells = []
        for index in range(row * 3, row * 3 + 3):
            cells.append(square_label(board, index))
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")


def choose_player():
    """Prompts the user to choose their player symbol (X or O).

    Returns None if the player typed q to quit.
    """
    while True:
        choice = input("Player 1, choose X or O (or q to exit): ")
        choice = choice.strip().upper()
        if choice == "Q":
            return None
        if choice == "X" or choice == "O":
            print(
                f"Player 1 is {choice}, Player 2 is {switch_player(choice)}.")
            return choice
        print("Invalid input, please make sure to type X or O")


def ask_move(board, player):
    """Asks the current player for their move and updates the board.

    Returns False if the player typed q to quit, otherwise True.
    """
    while True:
        move = input(
            f"Player {player}, choose a square (1-9) (or q to exit): ").strip()
        if move.lower() == "q":
            return False
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input,Please make sure to enter a number from 1 to 9")
        elif board[int(move) - 1] != " ":
            print("That square is taken, choose another")
        else:
            board[int(move) - 1] = player
            return True


def check_winner(board):
    """Checks if there is a winner on the board."""
    for line in WINNING_LINES:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return True
    return False


def check_draw(board):
    """Checks if the game is a draw (no empty spaces left)."""
    for square in board:
        if square == " ":
            return False
    return True


def switch_player(player):
    """Switches the current player from X to O or O to X."""
    if player == "X":
        return "O"
    else:
        return "X"


def game_over(board, player):
    """Prints the result and returns True if the game has ended."""
    if check_winner(board):
        print(f"Player {player} wins!")
        return True
    if check_draw(board):
        print("It's a draw!")
        return True
    return False


def play_turn(board, player):
    """Plays one turn. Returns "quit", "over" (win or draw) or "next"."""
    if not ask_move(board, player):
        return "quit"
    print_board(board)
    if game_over(board, player):
        return "over"
    return "next"


def play_game():
    """Plays one round. Returns "quit" if a player typed q, otherwise "over"."""
    print()
    board = create_board()
    player = choose_player()
    if player is None:
        return "quit"
    while True:
        result = play_turn(board, player)
        if result != "next":
            return result
        player = switch_player(player)


def main():
    """Main function to run the Tic Tac Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    print("Pick a square by typing its number (or q to quit):")
    print_board([str(number) for number in range(1, 10)])
    while True:
        if play_game() == "quit":
            break
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Thanks for playing. Bye!")


# for the terminal  to run the py file is the first thing it search for .
if __name__ == "__main__":
    main()
