import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Runner")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up a clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Images 
arrow_img = pygame.image.load('Assets/arrow.png')
arrow_img = pygame.transform.scale(arrow_img, (60, 50))


# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    window.fill(WHITE)
    window.blit(arrow_img, (0,HEIGHT - 50))

    clock.tick(FPS)
    pygame.display.update()


# Quit Pygame
pygame.quit()
sys.exit()
