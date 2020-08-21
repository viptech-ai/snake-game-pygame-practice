# Imports
import tkinter as tk
import pygame
from tkinter import messagebox

# Class and Function Definitions
class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx = 1, dirny = 0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    x = -1
                    y = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    x = 1
                    y = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_DOWN]:
                    x = 0
                    y = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_UP]:
                    x = 0
                    y = -1  
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns[p]:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)



    def reset(self, pos):
        pass
        
    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for i in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, grid_color, (x,0),(x,w)) # x constant = vertical line
        pygame.draw.line(surface, grid_color, (0,y),(w,y)) # x constant = vertical line
        

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subjecg, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake(snake_color,(10,10))
    
    clock = pygame.time.Clock()
    
    flag = True
    while flag:
        pygame.time.delay(50) # Speed Control
        clock.tick(10) # Lower to speed
        redrawWindow(win)
    
    pass


# Config Params
rows = 0
w = 0
height = 0

grid_color = (255,255,255)
snake_color = (255,0,255)

# Main Code 
cube.rows = rows
cube.w = w

main()