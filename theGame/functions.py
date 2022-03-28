from glob import glob
import pygame
from global_variables import GRAVITY, RED, BLUE, SCREEN, peice_counter, board_image
from peice import *

round = 0

current_row = 0
current_col = 0



def display_peice(row, col, player):
    color = RED if player == "red" else BLUE
    the_peice = peice(row, col, color)

    peice_counter.append(the_peice.draw(SCREEN))

def get_rows_and_cols(grid):
    (mouse_pos_x, s)= pygame.mouse.get_pos()
    row = mouse_pos_x//SQUARE_SIZE

    col = 0
    for idx, i in enumerate (grid[row]):
        if i == 0:
            col += 1
        else:
            break
    return row, col

def read_the_input(grid, round):
    global current_row, current_col

    row, col = get_rows_and_cols(grid)


    current_row = row
    current_col = col
  
    if current_col >= 1:
        if round % 2 == 0:
            grid[row][col - 1] = "blue"
        else:
            grid[row][col - 1] = "red"


def print_the_peices(grid):
    for idx, i in enumerate(grid):
        for idx2, j in enumerate(i):
            if j == "blue":
                display_peice(idx, idx2, "blue")
            elif j == "red":
                display_peice(idx, idx2, "red")


def has_won(round):

    winner = "Yellow" if round % 2== 0 else "Red"
  
def draw(round, grid):
    if round < 41:
        return False
    else:
        for i in grid:
            for j in i:
                if j == 0:
                    return False
    return True



def check_if_has_won(grid, round):
    global current_row, current_col, WTF

    check_row = 0

    current_col -= 1
    same_color_peice_counter = 0
    

    #check right and lift
    for i in range (1, 7 - current_row ):
        if grid[current_row+i][current_col] == grid [current_row][current_col]:
            same_color_peice_counter += 1
        else:
            break

            
    for i in range (current_row, 0, -1):

        if grid[check_row + i - 1][current_col] == grid [current_row][current_col]:
            same_color_peice_counter += 1
        else:
            break
    if same_color_peice_counter >= 3:
        has_won(round)
        return True
    
    #check top and down 
    
    same_color_peice_counter = 0

    for i in range (1, 6- current_col):


        if grid[current_row ][current_col + i] == grid[current_row][current_col]:
           same_color_peice_counter += 1
        else:
            break

    if same_color_peice_counter >= 3:
        has_won(round)
        return True
    

    #diagonale
    #right
    check_col = current_col
    check_row = current_row

    same_color_peice_counter = 0

    while check_row < 6 and check_col > 0:
        check_row += 1
        check_col -= 1
        if grid[check_row][check_col] == grid[current_row][current_col]:
           same_color_peice_counter += 1
        else:
            break

    check_col = current_col
    check_row = current_row

    while check_row > 0 and check_col < 5:
        check_row -= 1
        check_col += 1
        if grid[check_row][check_col] == grid[current_row][current_col]:
           same_color_peice_counter += 1
        else:
            break
        
    
    if same_color_peice_counter >= 3:
        has_won(round)
        return True

    #left
    check_col = current_col
    check_row = current_row

    same_color_peice_counter = 0

    while check_row > 0 and check_col > 0:
        check_row -= 1
        check_col -= 1
        if grid[check_row][check_col] == grid[current_row][current_col]:
           same_color_peice_counter += 1
        else:
            break
    
    check_col = current_col
    check_row = current_row

    while check_row < 6 and check_col < 5:
        check_row += 1
        check_col += 1
        if grid[check_row][check_col] == grid[current_row][current_col]:
           same_color_peice_counter += 1
        else:
            break


    if same_color_peice_counter >= 3:
        has_won(round)
        return True
    
    return False

def play_again():
    pass