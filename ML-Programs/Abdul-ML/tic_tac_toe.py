def print_board(board):
    """
    Print the Tic Tac Toe board in a formatted way.

    Args:
        board (list): The current state of the board as a list of 9 elements.
    """
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    """
    Check if the given player has won the game.

    Args:
        board (list): The current state of the board as a list of 9 elements.
        player (str): The current player's symbol ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal combinations
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical combinations
        [0, 4, 8], [2, 4, 6]              # Diagonal combinations
    ]
    return any(board[c[0]] == board[c[1]] == board[c[2]] == player for c in win_combos)

def is_draw(board):
    """
    Check if the game is a draw.

    Args:
        board (list): The current state of the board as a list of 9 elements.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return ' ' not in board

def get_player_move(board, current_player):
    """
    Get the player's move and validate the input.

    Args:
        board (list): The current state of the board as a list of 9 elements.
        current_player (str): The current player's symbol ('X' or 'O').

    Returns:
        int: The validated move index (0-8).
    """
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ' or not (0 <= move <= 8):
                raise ValueError
            return move
        except (ValueError, IndexError):
            print("Invalid move. Try again.")

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.
    """
    # Initialize the board and the starting player
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    # Game loop
    while True:
        # Get the current player's move
        move = get_player_move(board, current_player)

        # Update the board and display it
        board[move] = current_player
        print_board(board)

        # Check for a winner or a draw
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
