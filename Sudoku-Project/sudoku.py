from constants import *
import pygame
from sudoku_generator import *

game_over = True
gameStarted = False
did_win = False
titleText = None
titleRect = None
subtitleText = None
subtitleRect = None
easyText = None
easyRect = None
mediumText = None
mediumRect = None
hardText = None
hardRect = None
resetText = None
resetRect = None
restartText = None
restartRect = None
exitText = None
exitRect = None

removed = 0
sudoku = None
solved_sudoku = None
initial_sudoku = None
board = None

def startGame():

    global titleText
    global titleRect
    global subtitleText
    global subtitleRect
    global easyText
    global easyRect
    global mediumText
    global mediumRect
    global hardText
    global hardRect
    global resetText
    global resetRect
    global restartText
    global restartRect
    global exitText
    global exitRect
    global game_over
    global did_win
    global gameStarted

    game_over = True
    gameStarted = False
    did_win = False
    gameButton_font = pygame.font.Font(None, 32)
    button_font = pygame.font.Font(None, 40)
    title_font = pygame.font.Font(None, 64)
    subtitle_font = pygame.font.Font(None, 48)
    titleText = title_font.render("Welcome to Sudoku", True, (0, 0, 0))
    titleRect = titleText.get_rect(center=(300, 100))
    subtitleText = subtitle_font.render("Select Game Mode:", True, (0, 0, 0))
    subtitleRect = subtitleText.get_rect(center=(300, 300))
    easyText = button_font.render("easy", True, (255, 255, 255), (255, 165, 0))
    easyRect = easyText.get_rect(center=(200, 450))
    mediumText = button_font.render("medium", True, (255, 255, 255), (255, 165, 0))
    mediumRect = mediumText.get_rect(center=(300, 450))
    hardText = button_font.render("hard", True, (255, 255, 255), (255, 165, 0))
    hardRect = easyText.get_rect(center=(400, 450))
    resetText = gameButton_font.render("Reset", True, (255, 255, 255), (255, 165, 0))
    resetRect = resetText.get_rect(center=(150, 650))
    restartText = gameButton_font.render("Restart", True, (255, 255, 255), (255, 165, 0))
    restartRect = restartText.get_rect(center=(250, 650))
    exitText = gameButton_font.render("Exit", True, (255, 255, 255), (255, 165, 0))
    exitRect = exitText.get_rect(center=(350, 650))


def initialize(cellsToRemove):
    # sets all variables as a global
    # and initializes all of them
    # this method was created so that we can restart
    # the game with a new generated board
    global removed
    global sudoku
    global solved_sudoku
    global initial_sudoku
    global board
    global gameStarted
    global game_over

    gameStarted = True
    game_over = False
    removed = cellsToRemove
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


def resetBoard():
    global board
    global initial_sudoku
    for i, row in enumerate(initial_sudoku):
        for j, col in enumerate(row):
            board[i][j] = col
def main():
    pygame.init()
    startGame()
    global game_over
    global did_win
    global gameStarted
    global board
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    screen.fill(BG_COLOR)
    draw(screen)
    # draw_nums(screen, board)
    row = -1
    col = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    x, y = event.pos
                    row = int(y // SQUARE_SIZE)
                    col = int(x // SQUARE_SIZE)
                    if row < 9 and col < 9:
                        print(row, col)
                        print(board[row][col])
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption('Sudoku')
                        screen.fill(BG_COLOR)
                        draw(screen)
                        draw_nums(screen, board)
                        pygame.draw.line(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                                         (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE), BOX_WIDTH * 5)
                        pygame.draw.line(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                                         (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), BOX_WIDTH * 5)
                        pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE),
                                         (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), BOX_WIDTH * 5)
                        pygame.draw.line(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE),
                                         (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), BOX_WIDTH * 5)
                    else:
                        if resetRect.collidepoint(event.pos):
                            print("reset")
                            resetBoard()
                            screen = pygame.display.set_mode((WIDTH, HEIGHT))
                            pygame.display.set_caption('Sudoku')
                            screen.fill(BG_COLOR)
                            draw(screen)
                            draw_nums(screen, board)
                        elif restartRect.collidepoint(event.pos):
                            print("restart")
                            startGame()
                            screen = pygame.display.set_mode((WIDTH, HEIGHT))
                            pygame.display.set_caption('Sudoku')
                            screen.fill(BG_COLOR)
                            draw(screen)
                            continue
                        elif exitRect.collidepoint(event.pos):
                            pygame.display.quit()
                            pygame.quit()
                            exit()

                else:
                    if easyRect.collidepoint(event.pos):
                        print("easy")
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption('Sudoku')
                        initialize(30)
                        screen.fill(BG_COLOR)
                        draw(screen)
                        draw_nums(screen, board)
                        continue
                    elif mediumRect.collidepoint(event.pos):
                        print("medium")
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption('Sudoku')
                        screen.fill(BG_COLOR)
                        initialize(40)
                        draw(screen)
                        draw_nums(screen, board)
                        continue
                    elif hardRect.collidepoint(event.pos):
                        print("hard")
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption('Sudoku')
                        screen.fill(BG_COLOR)
                        initialize(50)
                        draw(screen)
                        draw_nums(screen, board)
                        continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # restarts game off of this keypress
                    # generates a different board too :)
                    startGame()
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption('Sudoku')
                    screen.fill(BG_COLOR)
                    draw(screen)
                    continue

            if event.type == pygame.KEYDOWN and not game_over:
                if row != -1 and col != -1:
                    sketch_number(screen, event, row, col)
                    if check_if_full():
                        # checks if there are no empty squares
                        if check_if_victory():
                            # checks if the board matches the correct board
                            did_win = True
                        else:
                            did_win = False
                        game_over = True

        if game_over and gameStarted:
            pygame.display.update()
            pygame.time.delay(500)  # small delay before game over screen
            gameStarted = False
            draw_game_over(did_win)
        pygame.display.update()


def draw(screen):
    if not game_over:
        screen.blit(resetText, resetRect)
        screen.blit(restartText, restartRect)
        screen.blit(exitText, exitRect)

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
                    (j * SQUARE_SIZE, HEIGHT-100),
                    BOX_WIDTH * 5
                )
            else:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT-100),
                    BOX_WIDTH
                )
                # for i in range(rows):
                #     for j in range(cols):
                #         cells[i][j].draw(screen)
    else:
        print("game isnt running")
        screen.blit(titleText, titleRect)
        screen.blit(subtitleText, subtitleRect)
        screen.blit(easyText, easyRect)
        screen.blit(mediumText, mediumRect)
        screen.blit(hardText, hardRect)

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
                chip_x_rect = chip_x_surf.get_rect(
                    center=(SQUARE_SIZE * col + SQUARE_SIZE // 2, SQUARE_SIZE * row + SQUARE_SIZE // 2))
                screen.blit(chip_x_surf, chip_x_rect)


def sketch_number(screen, event, row, col):
    global board
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
    global board
    if board == solved_sudoku:
        return True
    return False


def check_if_full():
    for row in board:
        for col in row:
            if col == 0:
                return False

    return True


def draw_game_over(victory):
    # creates the ending game screen
    end_font = pygame.font.Font(None, GAME_OVER_FONT)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    if victory:
        end_text = f"Victory"
    else:
        end_text = f"You Lost"
    end_surf = end_font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75))
    screen.blit(end_surf, end_rect)

    restart_text = "Press r to play again!"
    restart_surf = end_font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))
    screen.blit(restart_surf, restart_rect)


if __name__ == "__main__":
    main()