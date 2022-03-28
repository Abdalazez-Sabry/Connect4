import pygame
from global_variables import SCREEN, SQUARE_SIZE, WHITE, RED


class peice:
    PADDING = 20
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0

        self.x = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.col + SQUARE_SIZE // 2

    def draw(self, screen):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
    def __repr__(self) :
        return str

class button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        global mouse_clicked
        mouse_pos = pygame.mouse.get_pos()
        pressed = False
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.clicked == False:
                    self.clicked = True
                    pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return pressed
