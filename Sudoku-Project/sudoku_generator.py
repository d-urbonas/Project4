import math,random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [["-" for j in range(row_length)] for i in range(row_length)]  # sets up board in 2d-list wiht dashes as placeholders
        self.box_length = int(math.sqrt(row_length))  # takes sqrt of now_length and converts to int
        return None

    def get_board(self):
        return self.board  # this is the 2d list containing each row in a sublist

    def print_board(self):  # helps for debugging by displaying the board as it would be played
        for row in self.board:
            for col in row:
                print(col,end="  ")
            print()
        print()

    def valid_in_row(self, row, num):
        if num in self.get_board()[row]:  # checks if num is already in row, returns false if so
            return False
        return True

    def valid_in_col(self, col, num):
        for i in range(0, 9):  # checks the column (col) by iteraing through each row (i)
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):  # range is +3 as end is non-inclusive
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):  # checks if the row column and box are a valid, therfore guess is valid
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and \
                self.valid_in_box(row - row % 3, col - col % 3, num):
            return True  # using modulus division we can go from a value in any box to the top lef corner of the box allowing us to use valid box function
        return False

    def fill_box(self, row_start, col_start):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                while True:
                    num = random.randint(1,9)  # generates random number. if that number is valid it is inserted into the cell
                    if self.valid_in_box(row_start, col_start, num):
                        self.board[row][col] = num
                        break
        return None

    def fill_diagonal(self):  # fills the diaganol bozes from top left to bottom right. ie starting positions (0,0), (3,3) and (6,6)
        for i in range(0,7,3):
            self.fill_box(i,i)
        return None

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        i = 0
        while i < self.removed_cells:  # ensures proper num of cells are removed
            while True:
                row = random.randint(0,8)
                col = random.randint(0,8)  # generates random cell and replaces it with zero after ensuring that cell is not already 0
                if self.board[row][col] != 0:
                    self.board[row][col] = 0
                    break
            i += 1
        return None

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

