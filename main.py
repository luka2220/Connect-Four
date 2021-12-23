import numpy as np


# will create the game board using a matrix
def create_board():
    # creates a 6x7 board with all values being 0
    board = np.zeros((6, 7))
    return board


def drop_piece():
    pass


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_rows():
    pass


# main game loop
board = create_board()  # initializing an empty board
game_over = False   # will switch to True if a player connected four
turn = 0    # used to identify which players turn it is (0 = player1, 1 = player2)
print(board)

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6):"))

    # Ask for player 2 input
    else:
        col = int(input("Player 2 Make your Selection (0-6):"))

    turn += 1
    turn = turn % 2
