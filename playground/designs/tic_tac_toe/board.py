from playground.designs.tic_tac_toe.cell_values import CellValues


class GameBoard:
    def __init__(self, n: int):
        """Initialize an empty n*n board"""
        self.size = n
        self.board = [[CellValues.EMPTY.value] * n for _ in range(n)]
        self.num_empty_cells = n * n

    def print_board(self):
        """Print board in current state"""
        for i in range(self.size):
            print(" ".join(self.board[i]))
        print("\n")
