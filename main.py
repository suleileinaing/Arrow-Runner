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

#Constants 
arrow_x = 0
arrow_y = HEIGHT - 50

arrow_w = 50
arrow_h = 50

# Images 
arrow_img = pygame.image.load('Assets/arrow.png')
arrow_img = pygame.transform.scale(arrow_img, (arrow_w, arrow_h))

arrow_img_right = arrow_img 
arrow_img_up = pygame.transform.rotate(arrow_img, +90)
arrow_img_down = pygame.transform.rotate(arrow_img, -90)
arrow_img_left = pygame.transform.rotate(arrow_img, -180)


#Arrow Facing
face_right = True
face_left = False
face_up = False
face_down = False 

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if face_right:
                    arrow_x += arrow_w
                else :
                    arrow_img = arrow_img_right
                    face_right = True
                    face_down, face_left, face_up = False, False, False
            
            if event.key == pygame.K_LEFT:
                if face_left:
                    arrow_x -= arrow_w
                else :
                    arrow_img = arrow_img_left
                    face_left = True
                    face_down, face_right, face_up = False, False, False

            if event.key == pygame.K_UP:
                if face_up:
                    arrow_y -= arrow_h
                else :
                    arrow_img = arrow_img_up
                    face_up = True
                    face_down, face_left, face_right = False, False, False

            if event.key == pygame.K_DOWN:
                if face_down:
                    arrow_y += arrow_h
                else :
                    arrow_img = arrow_img_down
                    face_down = True
                    face_right, face_left, face_up = False, False, False

    # Fill the screen with white
    window.fill(WHITE)
    window.blit(arrow_img, (arrow_x, arrow_y))

    clock.tick(FPS)
    pygame.display.update()


# Quit Pygame
pygame.quit()
sys.exit()
