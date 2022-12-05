from constants import *
import pygame
from sudoku_generator import *

removed = 30
sudoku = SudokuGenerator(9, removed)
sudoku.fill_values()
solved_sudoku = [["-" for j in range(9)] for i in range(9)]
for i, row in enumerate(sudoku.get_board()):
    for j, col in enumerate(row):
        solved_sudoku[i][j] = col
sudoku.remove_cells()
initial_sudoku = [["-" for j in range(9)] for i in range(9)]
for i, row in enumerate(sudoku.get_board()):
    for j, col in enumerate(row):
        initial_sudoku[i][j] = col
board = sudoku.get_board()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)
    draw(screen)
    draw_nums(screen, board)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = int(y // SQUARE_SIZE)
                col = int(x // SQUARE_SIZE)
                print(row, col)
                print(board[row][col])
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption('Sudoku')
                screen.fill(BG_COLOR)
                draw(screen)
                draw_nums(screen, board)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE +SQUARE_SIZE, row * SQUARE_SIZE), BOX_WIDTH * 5)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), BOX_WIDTH * 5)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE +SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), BOX_WIDTH * 5)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), BOX_WIDTH * 5)
            if event.type == pygame.KEYDOWN:
                sketch_number(screen, event, row, col)
                if check_if_victory():
                    # checks if board == to a finished board after every sketch
                    game_over == True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # figure out how to restart the game off of this keypress I don't quite know how
                    pass
        if game_over:
            pygame.display.update()
            pygame.time.delay(500) # small delay before game over screen
            draw_game_over() 
        pygame.display.update()


def draw(screen):
    for i in range(1, BOARD_ROWS):
        if i % 3 == 0:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                BOX_WIDTH * 5
            )
        else:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                BOX_WIDTH
            )
    for j in range(1, BOARD_COLS):
        if j % 3 == 0:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, HEIGHT),
                BOX_WIDTH * 5
            )
        else:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, HEIGHT),
                BOX_WIDTH
            )
            # for i in range(rows):
            #     for j in range(cols):
            #         cells[i][j].draw(screen)

def draw_nums(screen, board):
    # draw a text, 1. define a surface, 2. define the location of the text
    num_font = pygame.font.Font(None, CHIP_FONT)
    dict = {
    1: num_font.render('1', 0, CROSS_COLOR),
    2: num_font.render('2', 0, CROSS_COLOR),
    3: num_font.render('3', 0, CROSS_COLOR),
    4: num_font.render('4', 0, CROSS_COLOR),
    5: num_font.render('5', 0, CROSS_COLOR),
    6: num_font.render('6', 0, CROSS_COLOR),
    7: num_font.render('7', 0, CROSS_COLOR),
    8: num_font.render('8', 0, CROSS_COLOR),
    9: num_font.render('9', 0, CROSS_COLOR),
    }
    # draw a text, 1. define a surface, 2. define the location of the text

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] != 0:
                chip_x_surf = dict[board[row][col]]
                chip_x_rect = chip_x_surf.get_rect(center=(SQUARE_SIZE * col + SQUARE_SIZE // 2, SQUARE_SIZE * row + SQUARE_SIZE // 2))
                screen.blit(chip_x_surf, chip_x_rect)


def sketch_number(screen, event, row, col):
    if initial_sudoku[row][col] != 0:
        return None
    else:
        if event.key == pygame.K_1:
            board[row][col] = 1
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_2:
            board[row][col] = 2
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_3:
            board[row][col] = 3
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_4:
            board[row][col] = 4
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_5:
            board[row][col] = 5
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_6:
            board[row][col] = 6
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_7:
            board[row][col] = 7
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_8:
            board[row][col] = 8
            print(board)
            draw_nums(screen, board)
        if event.key == pygame.K_9:
            board[row][col] = 9
            print(board)
            draw_nums(screen, board)

def enter_number():
    pass

def clear(self):
    if event.key == pygame.K_BACKSPACE:
        board.mark_square(row, col, '-')
        screen.fill(BG_COLOR)
        board.draw()
        pygame.display.update()
        
        
def check_if_victory():
    # checks to see if the player has won sudoku
    if board == solved_sudoku:
        return True
    return False


def draw_game_over():
    # creates the ending game screen
    screen.fill(BG_COLOR)
    end_text = "Victory"
    end_surf = font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75))
    screen.blit(end_surf, end_rect)

    restart_text = "Press r to play again!"
    restart_surf = font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))
    screen.blit(restart_surf, restart_rect)

if __name__ == "__main__":
    main()
