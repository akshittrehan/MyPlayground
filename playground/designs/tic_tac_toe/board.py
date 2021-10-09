class Board:
    def __init__(self, n: int):
        """Initialize an empty n*n board"""
        self.size = n
        self.EMPTY = "-"
        self.PLAYER1 = "X"
        self.PLAYER2 = "O"
        self.board = [[self.EMPTY] * n for _ in range(n)]
        self.solved = False
        self.num_empty_cells = n * n

    def print_board(self):
        """Print board in current state"""
        for i in range(self.size):
            print(" ".join(self.board[i]))
        print("\n")

    def check_winner(self, val):
        """Check if board is solved for val (1 for one player and -1 for other)"""

        # check rows
        for i in range(self.size):  # check if all values of this row are val
            found = True
            for j in range(self.size):
                if self.board[i][j] != val:
                    found = False
                    break
            if found:
                return True

        # check cols
        for i in range(self.size):  # check if all values of this column are val
            found = True
            for j in range(self.size):
                if self.board[j][i] != val:
                    found = False
                    break
            if found:
                return True

        # check main diagonal
        found = True
        for i in range(self.size):
            if self.board[i][i] != val:
                found = False
                break
        if found:
            return True

        # check secondary diagonal
        found = True
        for i in range(self.size):
            if self.board[i][self.size - i - 1] != val:
                found = False
                break
        return found
