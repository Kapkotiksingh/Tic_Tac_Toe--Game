# Tic Tac Toe

# Global variables
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Function to print the board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if any player has won
def check_winner():
    global game_over
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            print("Player", board[i], "wins!")
            game_over = True
            print_board()  # Display the final board
            return

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            print("Player", board[i], "wins!")
            game_over = True
            print_board()  # Display the final board
            return

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        print("Player", board[0], "wins!")
        game_over = True
        print_board()  # Display the final board
        return
    if board[2] == board[4] == board[6] != " ":
        print("Player", board[2], "wins!")
        game_over = True
        print_board()  # Display the final board
        return

    # Check for a tie
    if " " not in board:
        print("It's a tie!")
        game_over = True
        print_board()  # Display the final board
        return


# Function to handle a player's turn
def play_turn():
    global current_player
    print_board()
    print("Player", current_player, "turn:")
    
    # Prompt for input and handle errors
    while True:
        try:
            position = int(input("Enter a position (1-9): ")) - 1
            if position < 0 or position > 8:
                raise ValueError
            if board[position] != " ":
                raise ValueError
            break
        except ValueError:
            print("Invalid move. Try again.")

    # Make the move
    board[position] = current_player

    # Check if the game is over
    check_winner()

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"

# Main game loop
def play_game():
    while not game_over:
        play_turn()

# Start the game
play_game()

