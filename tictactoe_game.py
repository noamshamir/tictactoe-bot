from board import Board
from minimax import minimax
import time

board = Board()

# choose if the human plays first or second
while True:
    o_or_x = input("Would you like to go first or second? (x or o): ").lower()
    if o_or_x == "x":
        is_AI_x = False
        break
    elif o_or_x == "o":
        is_AI_x = True
        break
    else:
        print('Please enter either "x" or "o"')

def human():
    while True:
        try:
            x = int(input("X (1-3): ")) - 1
            y = int(input("Y (1-3): ")) - 1
            if board.is_empty(y, x):
                board.move(y, x)
                board.print_board()
                break
            else:
                print("That spot is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")


def ai():
    print("AI is thinking...")
    print("")
    start_time = time.time()
    _, best_move = minimax(board, is_AI_x)
    if best_move is not None:
        board.move(best_move[0], best_move[1])
    end_time = time.time()
    ai_thought_time = round((end_time - start_time), 2)
    print(f"Ai played {best_move[0]}, {best_move[1]} in {str(ai_thought_time)} seconds")
    print("")
    board.print_board()


# main game loop
while board.score is None:
    if is_AI_x:  # ai goes first
        ai()
    else:  # human goes first
        human()

    # check if game has ended after AI or human move
    if board.score is not None:
        if board.score == 1:
            print("X Wins!")
        elif board.score == -1:
            print("O Wins!")
        elif board.score == 0:
            print("It's a Tie!")
        break

    # switch turns
    if is_AI_x:
        human()
    else:
        ai()

    # check again for the result after the switch
    if board.score is not None:
        if board.score == 1:
            print("X Wins!")
        elif board.score == -1:
            print("O Wins!")
        elif board.score == 0:
            print("It's a Tie!")
        break
