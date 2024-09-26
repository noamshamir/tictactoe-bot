import copy
class Board:
    def __init__(self, board=None):
        if board is None:
            board = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]
        self.board = board
        self.compute_score()

    def print_board(self):
        print_board = copy.deepcopy(self.board)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    print_board[i][j] = " "
        print('   ' + '  1     2     3 ')
        print('   ' + '_________________')
        print('  ' + '|     |     |     |')
        print('1 ' + f'|  {print_board[0][0]}  |  {print_board[0][1]}  |  {print_board[0][2]}  |')
        print('  ' + '|_____|_____|_____|')
        print('  ' + '|     |     |     |')
        print('2 ' + f'|  {print_board[1][0]}  |  {print_board[1][1]}  |  {print_board[1][2]}  |')
        print('  ' + '|_____|_____|_____|')
        print('  ' + '|     |     |     |')
        print('3 ' + f'|  {print_board[2][0]}  |  {print_board[2][1]}  |  {print_board[2][2]}  |')
        print('  ' + '|_____|_____|_____|')
        print("")

    def compute_score(self):
        # Check rows, columns, and diagonals for a winner
        board = self.board
        for i in range(3):
            self.score = winner3(board[i][0], board[i][1], board[i][2])
            if self.score is not None:
                return
        for i in range(3):
            self.score = winner3(board[0][i], board[1][i], board[2][i])
            if self.score is not None:
                return
        if winner3(board[0][0], board[1][1], board[2][2]) is not None:
            self.score = winner3(board[0][0], board[1][1], board[2][2])
            return
        if winner3(board[0][2], board[1][1], board[2][0]) is not None:
            self.score = winner3(board[0][2], board[1][1], board[2][0])
            return

        # Check for tie (no empty spaces left)
        for row in board:
            if None in row:
                self.score = None
                return
        self.score = 0  # Tie

    def clear(self, x, y):
        self.board[x][y] = None
        self.compute_score()

    def is_empty(self, x, y):
        return self.board[x][y] is None

    def move(self, x, y):
        if self.board[x][y] is None:
            if self.is_x_turn():
                self.board[x][y] = 'X'
            else:
                self.board[x][y] = 'O'
            self.compute_score()
        else:
            raise Exception(f'Illegal move at {x}, {y}, already occupied.')

    def is_x_turn(self):
        # Determine if it's X's turn by counting Xs and Os
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        return x_count == o_count

def winner3(a, b, c):
    if a == b == c and a is not None:
        return 1 if a == 'X' else -1
    return None