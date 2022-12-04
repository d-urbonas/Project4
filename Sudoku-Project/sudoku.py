from constants import *
import pygame
from sudoku_generator import *

board = generate_sudoku(9, 30)
initial_board = board

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)
    draw(screen)
    draw_nums(screen, board)

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

def place_number(value):
    if event.key == pygame.K_num:
        board.mark_square(row, col, value)
        screen.fill(BG_COLOR)
        board.draw()
        pygame.display.update()
def clear(self):
    if event.key == pygame.K_BACKSPACE:
        board.mark_square(row, col, '-')
        screen.fill(BG_COLOR)
        board.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()