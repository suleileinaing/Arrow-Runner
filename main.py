import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Button color
LIGHT_BLUE2 = (173, 200, 230)       # Hover color

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arrow Run")

# Set up font
font = pygame.font.Font(None, 28)

# Button texts and their rectangles
button_texts = ["Play", "How to play", "Quit"]
buttons = []

# Create button rectangles
for i, text in enumerate(button_texts):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + i * 50))
    button_rect = pygame.Rect(text_rect.x - 5, text_rect.y - 5, text_rect.width + 10, text_rect.height + 10)
    buttons.append((button_rect, text_surface, text_rect))

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 30

main_menu = True
game_play = False
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if main_menu: 
                for i, (button_rect, _, _) in enumerate(buttons):
                    if button_rect.collidepoint(mouse_pos):
                        if i == 0:
                            game_play = True
                            main_menu = False
                        elif i == 1:
                            print("How to play button clicked!")
                        elif i == 2:
                            running = False  # Quit button clicked

    # Fill the screen with a color
    screen.fill(WHITE)

    if main_menu:
        mouse_pos = pygame.mouse.get_pos()
        for button_rect, text_surface, text_rect in buttons:
            # Change color on hover
            if button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, LIGHT_BLUE2, button_rect)
            else:
                pygame.draw.rect(screen, LIGHT_BLUE, button_rect)
            # Draw the text
            screen.blit(text_surface, text_rect)

    elif game_play:
        play_text = font.render("Playing the Game!", True, BLACK)
        play_text_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(play_text, play_text_rect)
        
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
sys.exit()
