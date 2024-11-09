import pygame
import sys
from objects import Arrow, Grass, Path
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
grass = Grass()
path = Path()
path.Level1()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if arrow.right and (arrow.x + arrow.width , arrow.y) in path.coordinate:
                    arrow.x += arrow.width
                else:
                    arrow.Arrow_Right()
            if event.key == pygame.K_LEFT:
                if arrow.left and (arrow.x - arrow.width , arrow.y) in path.coordinate:
                    arrow.x -= arrow.width
                else:
                    arrow.Arrow_Left()

            if event.key == pygame.K_UP:
                if arrow.up and (arrow.x , arrow.y - arrow.height) in path.coordinate:
                    arrow.y -= arrow.height
                else:
                    arrow.Arrow_Up()

            if event.key == pygame.K_DOWN:
                if arrow.down and (arrow.x, arrow.y + arrow.height) in path.coordinate:
                    arrow.y += arrow.height
                else:
                    arrow.Arrow_Down()

    # Fill the screen with white
    window.fill(WHITE)

    ## from here is test,
    for (x,y) in c.grass_pts:
        if (x,y) not in path.coordinate:
            grass.draw(window, x,y)

    ## test ened
    arrow.draw(window)

    clock.tick(FPS)
    pygame.display.update()


# Quit Pygame
pygame.quit()
sys.exit()
