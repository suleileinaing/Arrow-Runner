import pygame
import constant as c
import random

class Arrow():
    def __init__(self):
        self.x = 0
        self.y = c.HEIGHT-50
        self.width = 50
        self.height =  50
        self.image = pygame.image.load('Assets/arrow.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.arrow = self.image
        self.right = True
        self.left = False
        self.up = False
        self.down = False


    def Arrow_Up(self):
        self.up = True
        self.right, self.down, self.left = False, False, False
        self.arrow = pygame.transform.rotate(self.image, +90)

    def Arrow_Down(self):
        self.down = True
        self.right, self.up, self.left = False, False, False
        self.arrow = pygame.transform.rotate(self.image, -90)

    def Arrow_Left(self):
        self.left = True
        self.right, self.down, self.up = False, False, False
        self.arrow = pygame.transform.rotate(self.image, -180)

    def Arrow_Right(self):
        self.right = True
        self.up, self.down, self.left = False, False, False
        self.arrow = self.image

    def draw(self, window):
        window.blit(self.arrow, (self.x, self.y))

class Grass():
    def __init__(self):
        self.width = 50
        self.height =  50
        self.image = pygame.image.load('Assets/grass.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
    def draw(self, window, x, y):
        window.blit(self.image, (x, y))

class Path():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.coordinate = []

        current= (0, c.HEIGHT-self.height)
        end = (c.WIDTH - self.width,0 )
        self.coordinate.append(current)
        while current!= end:
            randint = random.randint (0,1)
            if current[0] == end[0]:
                new = (current[0], current[1]-50)
            if randint == 0 and current[0] != end[0]:
                new = (current[0]+50, current[1])
            else:
                new = (current[0], current[1]-50)
            current = new 
            self.coordinate.append(current)

