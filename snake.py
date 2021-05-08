import pygame
from pygame import *
import sys
import random

# Variables

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GridSize = 20
GRID_WIDTH = SCREEN_HEIGHT / GridSize
GRID_HEIGHT = SCREEN_WIDTH / GridSize

Up = (0, -1)
Down = (0, 1)
Left = (-1, 0)
Right = (1, 0)

pygame.init() # Start PyGame

class snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(Up, Down, Left, Right)
        self.color = random

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point


    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass



class food(object):
    def __init__(self):
        pass

    def random_position(self):
        pass

    def draw(self, surface):
        pass

    def DrawGrid(surface):
        for y in range(0, int(GRID_HEIGHT)):
            for x in range(0, int(GRID_WIDTH)):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x*GridSize, y*GridSize), (GridSize, GridSize))
                    pygame.draw.rect(surface, (93, 216, 228), r)
                else:
                    rr = pygame.Rect((x*GridSize, y*GridSize), (GridSize, GridSize))
                    pygame.draw.rect(surface, (84, 194, 205), rr)
                    

def main():
    clock = pygame.time.clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = Surface.convert()

    snake = snake()
    food - food()

    score = 0
    while(True):
        clock.tick(30)
    screen.blit(surface, (0, 0))
    pygame.display.update()

    main()
