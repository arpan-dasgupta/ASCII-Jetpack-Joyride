from board import Board


def gameplay(obj1, obj2):
    # main game function

    game_board = Board()
    moveFunctions = [obj1, obj2]
    players = ['o', 'x']
    curPlayer = 0

    # preliminary print
    game_board.print_board()

    while True:

        winner = game_board.gameOver()
        if game_board.isGameOver:
            if winner == -1:
                print("Draw")
            else:
                print(winner, "wins")
            quit()

        else:
            print(players[curPlayer], "to move")
            # replace this block with bot moves
            # =================================
            while True:
                i, j = input(
                    "Enter space separated row and col number: ").split(" ")
                # add type check if needed
                i, j = int(i), int(j)
                if game_board.check_valid(i, j):
                    break
                print("Invalid Move. Go again.")
            # =================================

            game_board.update(i, j, players[curPlayer])
            game_board.print_board()

            curPlayer = (curPlayer + 1) % 2


gameplay(1, 2)
