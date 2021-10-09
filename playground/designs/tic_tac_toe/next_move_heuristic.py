import random
from playground.designs.tic_tac_toe.cell_values import CellValues


def find_next_move(board: list[list[int]], board_size: int):
    # generate an empty cell to fill in next turn
    while 1:  # assumes an empty cell is present
        i = random.randint(0, board_size - 1)
        j = random.randint(0, board_size - 1)
        if board[i][j] == CellValues.EMPTY.value:
            return i, j
