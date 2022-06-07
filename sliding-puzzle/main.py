import pygame
import sys
from puzzle import Puzzle

puzzle_size = int(input("\nHow many squares tall and wide would you like the puzzle to be? "))
puzzle = Puzzle(puzzle_size)

pygame.init()

WIDTH = 750
HEIGHT = WIDTH + 100
screen = pygame.display.set_mode([WIDTH, HEIGHT])

BOARD_WIDTH = WIDTH
BOARD_HEIGHT = WIDTH
SQUARE_WIDTH = BOARD_WIDTH/puzzle_size
SQUARE_HEIGHT = BOARD_HEIGHT/puzzle_size

button_font = pygame.font.Font(None, 40)
square_font = pygame.font.Font(None, 400//puzzle_size)
win_font = pygame.font.Font(None, 50)

LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (105, 105, 105)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

while True:

    screen.fill(LIGHT_GRAY)
    x, y = pygame.mouse.get_pos()

    board = puzzle.board

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                if SQUARE_WIDTH*j < x < SQUARE_WIDTH*j+SQUARE_WIDTH and SQUARE_HEIGHT*i < y < SQUARE_HEIGHT*i+SQUARE_HEIGHT:
                    pygame.draw.rect(screen, BLACK, (SQUARE_WIDTH*j, SQUARE_HEIGHT*i, SQUARE_WIDTH, SQUARE_HEIGHT))
                    pygame.draw.rect(screen, YELLOW, (SQUARE_WIDTH*j+1, SQUARE_HEIGHT*i+1, SQUARE_WIDTH-2, SQUARE_HEIGHT-2))
                else:
                    pygame.draw.rect(screen, BLACK, (SQUARE_WIDTH*j, SQUARE_HEIGHT*i, SQUARE_WIDTH, SQUARE_HEIGHT))
                    pygame.draw.rect(screen, WHITE, (SQUARE_WIDTH*j+1, SQUARE_HEIGHT*i+1, SQUARE_WIDTH-2, SQUARE_HEIGHT-2))

                text = square_font.render(str(board[i][j]), True, BLACK)
                text_rect = text.get_rect(center = (SQUARE_WIDTH*j+SQUARE_WIDTH/2, SQUARE_HEIGHT*i+SQUARE_HEIGHT/2))
                screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, BLACK, (SQUARE_WIDTH*j, SQUARE_HEIGHT*i, SQUARE_WIDTH, SQUARE_HEIGHT))

    pygame.draw.rect(screen, BLACK, (25, BOARD_HEIGHT+25, BOARD_WIDTH/3-50 , 50))
    pygame.draw.rect(screen, DARK_GRAY, (25+1, BOARD_HEIGHT+25+1, BOARD_WIDTH/3-50-2 , 50-2))
    reshuffle_text = button_font.render("Reshuffle", True, WHITE)
    reshuffle_rect = reshuffle_text.get_rect(center = (25+(BOARD_WIDTH/3-50)/2, BOARD_HEIGHT+50))
    screen.blit(reshuffle_text, reshuffle_rect)

    count_text = button_font.render("Moves: " + str(puzzle.get_count()), True, BLACK)
    count_rect = count_text.get_rect(center = (BOARD_WIDTH/3+25+(BOARD_WIDTH/3-50)/2, BOARD_HEIGHT+50))
    screen.blit(count_text, count_rect)

    pygame.draw.rect(screen, BLACK, (BOARD_WIDTH/3*2+25, BOARD_HEIGHT+25, BOARD_WIDTH/3-50, 50))
    pygame.draw.rect(screen, DARK_GRAY, (BOARD_WIDTH/3*2+25+1, BOARD_HEIGHT+25+1, BOARD_WIDTH/3-50-2, 50-2))
    quit_text = button_font.render("Quit", True, WHITE)
    quit_rect = quit_text.get_rect(center = (BOARD_WIDTH/3*2+25+(BOARD_WIDTH/3-50)/2, BOARD_HEIGHT+50))
    screen.blit(quit_text, quit_rect)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:

            if 25 <= x <= BOARD_WIDTH/3-25 and BOARD_HEIGHT+25 <= y <= BOARD_HEIGHT+25+50:
                puzzle.shuffle()

            if BOARD_WIDTH/3*2+25 <= x <= BOARD_WIDTH/3*2+25+BOARD_WIDTH/3-50 and BOARD_HEIGHT+25 <= y <= BOARD_HEIGHT+25+50:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.KEYDOWN:
            
            if 0 <= x <= BOARD_WIDTH and 0 <= y <= BOARD_HEIGHT:
                
                if event.key == pygame.K_a:
                    puzzle.move_left(int(y//SQUARE_HEIGHT), int(x//SQUARE_WIDTH))

                if event.key == pygame.K_d:
                    puzzle.move_right(int(y//SQUARE_HEIGHT), int(x//SQUARE_WIDTH))
                    
                if event.key == pygame.K_w:
                    puzzle.move_up(int(y//SQUARE_HEIGHT), int(x//SQUARE_WIDTH))
                    
                if event.key == pygame.K_s:
                    puzzle.move_down(int(y//SQUARE_HEIGHT), int(x//SQUARE_WIDTH))

    if puzzle.is_win():
        win = True
        
        while win:
            
            screen.fill(LIGHT_GRAY)
            x, y = pygame.mouse.get_pos()
            
            pygame.draw.rect(screen, BLACK, (25, BOARD_HEIGHT+25, BOARD_WIDTH/3-50 , 50))
            pygame.draw.rect(screen, DARK_GRAY, (25+1, BOARD_HEIGHT+25+1, BOARD_WIDTH/3-50-2 , 50-2))
            reshuffle_text = button_font.render("Reshuffle", True, WHITE)
            reshuffle_rect = reshuffle_text.get_rect(center = (25+(BOARD_WIDTH/3-50)/2, BOARD_HEIGHT+50))
            screen.blit(reshuffle_text, reshuffle_rect)

            pygame.draw.rect(screen, BLACK, (BOARD_WIDTH/3*2+25, BOARD_HEIGHT+25, BOARD_WIDTH/3-50, 50))
            pygame.draw.rect(screen, DARK_GRAY, (BOARD_WIDTH/3*2+25+1, BOARD_HEIGHT+25+1, BOARD_WIDTH/3-50-2, 50-2))
            quit_text = button_font.render("Quit", True, WHITE)
            quit_rect = quit_text.get_rect(center = (BOARD_WIDTH/3*2+25+(BOARD_WIDTH/3-50)/2, BOARD_HEIGHT+50))
            screen.blit(quit_text, quit_rect)

            win_text = win_font.render("You completed the puzzle in " + str(puzzle.get_count()) + " moves!", True, BLACK)
            win_rect = win_text.get_rect(center = (BOARD_WIDTH/2, BOARD_HEIGHT/2))
            screen.blit(win_text, win_rect)

            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONUP:

                    if 25 <= x <= BOARD_WIDTH/3-25 and BOARD_HEIGHT+25 <= y <= BOARD_HEIGHT+25+50:
                        puzzle.shuffle()
                        win = False

                    if BOARD_WIDTH/3*2+25 <= x <= BOARD_WIDTH/3*2+25+BOARD_WIDTH/3-50 and BOARD_HEIGHT+25 <= y <= BOARD_HEIGHT+25+50:
                        pygame.quit()
                        sys.exit()
                        
            pygame.display.update()
            
    pygame.display.update()
