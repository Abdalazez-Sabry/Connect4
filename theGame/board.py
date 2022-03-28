import pygame
from global_variables import *


class board:
    def __init__(self):
        self.board = []
        self.red_left = self.blue_left = 21
    def draw_squares(self):          
        for row in range(COLS):
            for col in range(ROWS):
                SCREEN.blit(board_image, (row*SQUARE_SIZE, col*SQUARE_SIZE,))