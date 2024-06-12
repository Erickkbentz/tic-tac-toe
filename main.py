import time
import os

board_matrix = [[" " for i in range(3)] for j in range(3)]
current_player = ""

def print_board():
    os.system('clear')
    for row in board_matrix:
        print("|" + "|".join(row) + "|")


def update_board(row, col, player):
    if board_matrix[row][col] == " ":
        board_matrix[row][col] = player
        print_board()
    else:
        print("Invalid move. Try again!")

def check_winner(player):
    # Check rows
    for i in range(3):
        if board_matrix[i][0] == board_matrix[i][1] == board_matrix[i][2] == player:
            return True
    
    # Check columns
    for i in range(3):
        if board_matrix[0][i] == board_matrix[1][i] == board_matrix[2][i] == player:
            return True

    # Check diagonals
    if board_matrix[0][0] == board_matrix[1][1] == board_matrix[2][2] == player:
        return True
    if board_matrix[0][2] == board_matrix[1][1] == board_matrix[2][0] == player:
        return True

    return False


def get_initial_player():
    while True:
        initial_player = str(input("Enter your choice of player (X or O): "))
        if initial_player == "X" or initial_player == "O":
            return initial_player
        else:
            print("Invalid choice. Try again! Choose options X or O.")


def get_row_col():
    while True:
        row = int(input("Enter row for your move: "))
        col = int(input("Enter column for your move: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid row or column. Try again!")
        elif board_matrix[row][col] != " ":
            print("Invalid move. Try again!") 
        else:
            return row, col
        

def play_game():
    current_player = get_initial_player()

    while True:
        print("Current Player: ", current_player)
        row, col = get_row_col()
        update_board(row, col, current_player)

        if check_winner(current_player):
            print("Player ", current_player, " wins!")
            break

        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    play_game()