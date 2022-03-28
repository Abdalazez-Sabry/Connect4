import sys, pygame
from tkinter import Button
from turtle import Screen
from global_variables import*
from board import*
from peice import*
from functions import *

pygame.init()

def build_matrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    return matrix

play_again_image = pygame.image.load("play_again.png")
quit_image = pygame.image.load("quit.png")
red_won = pygame.image.load("red_won.png")
yellow_won = pygame.image.load("yellow_won.png")


play_again_button = button(SCREEN_WIDTH // 4 - play_again_image.get_width() // (2/scale), SCREEN_HIGHT // 2 - play_again_image.get_height() // 2, play_again_image, scale)
quit_button = button(SCREEN_WIDTH // 1.25 - quit_image.get_width()// (2/scale), SCREEN_HIGHT // 2 - quit_image.get_height()//2, quit_image, scale)
end_game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HIGHT))
end_game_surface.fill((10, 10, 10))

#Display
pygame.display.set_caption("Connect 4")

grid = build_matrix(7, 6)




def main():
    the_board = board()
    global grid
    
    round = 0
    Run = True
    play = True
    new_peice = False
    
    delay_time = 90
    

    while Run:
        current_time = pygame.time.get_ticks()
        SCREEN.fill(BACKGROUND_COLOR)
        the_board.draw_squares()
        
        #Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and play == True and get_rows_and_cols(grid)[1] > 0 :
                if event.button == 1:
                    read_the_input(grid, round)
                    if check_if_has_won(grid, round) or draw(round, grid):
                        play = False
                        start_time = current_time + delay_time
                    round += 1
            
                    
        print_the_peices(grid)
        
        if not play:
            if current_time >= start_time:
                end_game_surface.set_alpha(200)
                SCREEN.blit(end_game_surface, (0, 0))
                if play_again_button.draw():
                    play = True
                    grid = build_matrix(7, 6)
                    round = 0


                if quit_button.draw():
                    pygame.quit()
                    sys.exit()
                if not draw(round, grid):
                    winner = red_won if round % 2 == 0 else yellow_won
                    SCREEN.blit(winner, (int(SCREEN_WIDTH // 2 - winner.get_width() // 2) , int(SCREEN_HIGHT // 2 - winner.get_height() * 2 )))

        pygame.display.update()
        #Only 60 frames
        pygame.display.flip()
        clock.tick(60)

        
main()