from playground.designs.tic_tac_toe.game import Game


def main():
    n = 4
    tic_tac = Game(n)
    result = tic_tac.play()
    if not result:
        print("DRAW")
    else:
        print("Player ", result, " wins")


main()
