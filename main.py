import pygame
import sys
from objects import Arrow
import constant as c

# Initialize Pygame
pygame.init()

# Set up display

window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Arrow Runner")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up a clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

arrow = Arrow()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if arrow.right:
                    arrow.x += arrow.width
                else :
                    arrow.Arrow_Right()
            if event.key == pygame.K_LEFT:
                if arrow.left:
                    arrow.x -= arrow.width
                else :
                    arrow.Arrow_Left()

            if event.key == pygame.K_UP:
                if arrow.up:
                    arrow.y -= arrow.height
                else :
                    arrow.Arrow_Up()

            if event.key == pygame.K_DOWN:
                if arrow.down:
                    arrow.y += arrow.height
                else :
                    arrow.Arrow_Down()

    # Fill the screen with white
    window.fill(WHITE)
    arrow.draw(window)

    clock.tick(FPS)
    pygame.display.update()


# Quit Pygame
pygame.quit()
sys.exit()
