from playground.designs.tic_tac_toe.board import GameBoard
from playground.designs.tic_tac_toe.cell_values import CellValues
from playground.designs.tic_tac_toe.next_move_heuristic import find_next_move


class Game(GameBoard):
    def __init__(self, n):
        super().__init__(n)

    def is_winning(self, player: CellValues, row: int, col: int) -> bool:
        """player has marked row and col. check if this leads to player winning"""

        # Check row
        win = True
        for j in range(self.size):
            if self.board[row][j] != player.value:
                win = False
                break
        if win:
            return win

        # Check col
        win = True
        for i in range(self.size):
            if self.board[i][col] != player.value:
                win = False
                break
        if win:
            return win

        # Check main diagonal
        if row == col:
            win = True
            for i in range(self.size):
                if self.board[i][i] != player.value:
                    win = False
                    break
            if win:
                return win

        # Check secondary diagonal
        if col == self.size - row - 1:
            win = True
            for i in range(self.size):
                if self.board[i][self.size - i - 1] != player.value:
                    win = False
                    break
            if win:
                return win

        return False

    def move(self, player: CellValues):
        # if board is full, player can't make a move
        if not self.num_empty_cells:
            return

        # find next move
        i, j = find_next_move(self.board, self.size)

        # mark cell
        self.board[i][j] = player.value
        self.num_empty_cells -= 1

        print("Player ", player.value, "'s turn")
        self.print_board()

        # check if player is winning
        if self.is_winning(player, i, j):
            return player.value

    def play(self):
        """Model game play"""
        self.print_board()
        while 1:
            # Player 1
            result = self.move(CellValues.PLAYER1)
            if result:
                return result
            if not self.num_empty_cells:
                return

            # Player 2
            result = self.move(CellValues.PLAYER2)
            if result:
                return result
            if not self.num_empty_cells:
                return
