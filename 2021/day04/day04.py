import pathlib
from dataclasses import dataclass
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.marks = np.zeros((5, 5))
        self.win = False

    def mark(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.marks[i][j] = 1

    def check_win(self):
        for i in range(5):
            if sum(list(self.marks[i, :])) == 5:
                self.win = True
            if sum(list(self.marks[:, i])) == 5:
                self.win = True
        return self.win

    def get_unmarked(self):
        return [
            self.board[i][j]
            for i in range(5)
            for j in range(5)
            if self.marks[i][j] == 0
        ]


bingo_boards = []
board = np.zeros((5, 5))
i = 0

with open(WORKDIR + "/input") as f:
    read_numbers = [int(x) for x in f.readline().split(",")]
    for line in f:
        if line.strip() == "":
            i = 0
            bingo_boards.append(BingoBoard(board))
            board = np.zeros((5, 5))
            continue
        board[i, :] = np.array([int(x) for x in line.strip().split()])
        i += 1


def find_first_winner(read_numbers, bingo_boards):
    for number in read_numbers:
        for bb in bingo_boards:
            bb.mark(number)
            if bb.check_win():
                return number, sum(bb.get_unmarked())


winning_number, unmarked_sum = find_first_winner(read_numbers, bingo_boards)

print(winning_number * unmarked_sum)

# ----------- PART 2 -------------------
def find_last_winner(read_numbers, bingo_boards):
    for number in read_numbers:
        for bb in bingo_boards:
            bb.mark(number)
            bb.check_win()
        if len(bingo_boards) == 1 and bingo_boards[0].win:
            return number, sum(bingo_boards[0].get_unmarked())
        bingo_boards = [bb for bb in bingo_boards if not bb.win]


winning_number, unmarked_sum = find_last_winner(read_numbers, bingo_boards)

print(winning_number * unmarked_sum)
