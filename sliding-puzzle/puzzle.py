import random
from movecounter import MoveCounter

class Puzzle:
    
    def __init__(self, size):

        self.counter = MoveCounter()
        
        temp = []
        for i in range(1, size*size):
            temp += [i]
        temp += [0]

        self.board = []
        while len(temp) > 0:
            self.board += [temp[0:size]]
            temp = temp[size:]

        while self.is_win():
            self.shuffle()

    def shuffle(self):
        y, x = self.find_blank()
        for i in range(pow(len(self.board), 4)):
            moved = False
            while not moved:
                rand = random.randint(1, 5)
                if rand == 1:
                    if self.move_left(y, x):
                        x -= 1
                        moved = True
                elif rand == 2:        
                    if self.move_right(y, x):
                        x += 1
                        moved = True
                elif rand == 3:
                    if self.move_up(y, x):
                        y -= 1
                        moved = True
                elif rand == 4:
                    if self.move_down(y, x):
                        y += 1
                        moved = True
        self.counter.reset()
                
    def find_blank(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return (i, j)

    def is_win(self):
        num = 1
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == num or self.board[i][j] == 0:
                    num += 1
                else:
                    return False
        return True
    
    def can_move_left(self, row, col):
        if col > 0:
            return self.board[row][col-1] == 0 or self.board[row][col] == 0
        return False

    def move_left(self, row, col):
        if self.can_move_left(row, col):
            temp = self.board[row][col-1]
            self.board[row][col-1] = self.board[row][col]
            self.board[row][col] = temp
            self.counter.increment()
            return True
        return False

    def can_move_right(self, row, col):
        if col < len(self.board) - 1:
            return self.board[row][col+1] == 0 or self.board[row][col] == 0
        return False

    def move_right(self, row, col):
        if self.can_move_right(row, col):
            temp = self.board[row][col+1]
            self.board[row][col+1] = self.board[row][col]
            self.board[row][col] = temp
            self.counter.increment()
            return True
        return False

    def can_move_up(self, row, col):
        if row > 0:
            return self.board[row-1][col] == 0 or self.board[row][col] == 0
        return False

    def move_up(self, row, col):
        if self.can_move_up(row, col):
            temp = self.board[row-1][col]
            self.board[row-1][col] = self.board[row][col]
            self.board[row][col] = temp
            self.counter.increment()
            return True
        return False

    def can_move_down(self, row, col):
        if row < len(self.board) - 1:
            return self.board[row+1][col] == 0 or self.board[row][col] == 0
        return False

    def move_down(self, row, col):
        if self.can_move_down(row, col):
            temp = self.board[row+1][col]
            self.board[row+1][col] = self.board[row][col]
            self.board[row][col] = temp
            self.counter.increment()
            return True
        return False

    def get_count(self):
        return self.counter.count
