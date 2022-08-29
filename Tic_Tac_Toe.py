# Global Variables

# Firstly, we would need a board to play the game
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# If game is still going
game_still_going = True

# If game is still going
winner = None

# Whose turn is it
current_player =  "X"

# Display board
def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

def play_game():
    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")



# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1
    
        if board[position] == "-":
            valid = True
        else:
            print("You can't play there. Spot already taken")

    board[position] = player
    display_board()


def check_if_game_over():
    # The criteria which must be met before game can be over
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # To access a global variable outside the function
    global winner
    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # There was a win
        winner = row_winner
    elif column_winner:
        # There was a win
        winner = column_winner
    elif diagonal_winner:
        # There was a win
        winner = diagonal_winner
    else:
        # There was no win
        winner = None
    return

def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():    
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
        
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
        
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

# To flip the player from X to O
def flip_player():
    # To be able to access a global variable in a function
    global current_player

    if current_player == "X":  # If X was first typed, then switch to O.
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return


play_game()