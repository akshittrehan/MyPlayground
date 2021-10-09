import random
from playground.designs.tic_tac_toe.board import Board


def get_next_move(board: Board):
    # generate an empty cell to fill in next turn
    while 1:  # assumes an empty cell is present
        i = random.randint(0, board.size - 1)
        j = random.randint(0, board.size - 1)
        if board.board[i][j] == board.EMPTY:
            return i, j


def player_action(board: Board, player):
    move = get_next_move(board)
    board.board[move[0]][move[1]] = player

    board.print_board()

    # check if board is solved
    if board.check_winner(player):
        return player


def play(n: int):
    """
    Play tic tac toe with 2 players on a n * n board
    :param n: int
    :return: winner if any
    """

    board = Board(n)
    board.print_board()
    while 1:
        # Player 1
        result = player_action(board, board.PLAYER1)
        if result:
            return result
        board.num_empty_cells -= 1

        board.print_board()

        if not board.num_empty_cells:
            return None

        # Player 2
        result = player_action(board, board.PLAYER2)
        if result:
            return result
        board.num_empty_cells -= 1

        board.print_board()

        if not board.num_empty_cells:
            return None


def main():
    n = 3
    result = play(n)
    if not result:
        print("DRAW")
        return
    print("Player ", result, " wins")


main()
