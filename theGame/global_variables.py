import sys, pygame
import ctypes
user32 = ctypes.windll.user32


#General
clock = pygame.time.Clock()



#Screen
SCREEN_WIDTH = user32.GetSystemMetrics(0) //2


scale = user32.GetSystemMetrics(0) / 1920
mouse_clicked = False

ROWS, COLS= 6, 7
SQUARE_SIZE = SCREEN_WIDTH // COLS

SCREEN_HIGHT = SCREEN_WIDTH - SQUARE_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

board_image = pygame.image.load("field3.png")
board_image = pygame.transform.scale(board_image, (SQUARE_SIZE, SQUARE_SIZE))

#Background
BACKGROUND_COLOR = pygame.Color(4, 40, 159)

#Rows and Cols
ROWS, COLS= 6, 7
SQUARE_SIZE = SCREEN_WIDTH // COLS

#RGB
RED = (255, 0, 46)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (232, 250, 5)


GRAVITY = 4
peice_counter = []