import pygame
import constant as c 
from objects import Arrow, Path, Grass


def HomePage(screen):
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (173, 216, 230)

    # Text
    title_text = c.font_large.render("Welcome to the Arrow Runner!", True, BLACK)

    # Button dimensions
    button_width = 200
    button_height = 50
    button_x = (800 - button_width) // 2
    button_y = 600 // 2

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Home_Page = False
                running = False

            # Detect mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (button_x <= mouse_x <= button_x + button_width and
                        button_y <= mouse_y <= button_y + button_height):
                    game_play(screen)
                    running = False

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw title
        screen.blit(title_text, ((800 - title_text.get_width()) // 2, 100))

        # Draw button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (button_x <= mouse_x <= button_x + button_width and
                button_y <= mouse_y <= button_y + button_height):
            button_color = LIGHT_BLUE
        else:
            button_color = BLUE

        pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
        button_text = c.font_small.render("Start", True, WHITE)
        screen.blit(button_text, ((800 - button_text.get_width()) // 2, button_y + 10))

        # Update display
        pygame.display.update()


def game_play(screen):
    arrow = Arrow(50)
    path = Path()
    grass = Grass()
    clock = pygame.time.Clock()
    FPS = 60 

    timer_started = False
    start_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Play_Page = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if arrow.right and (arrow.x + arrow.width , arrow.y) in path.coordinate:
                    arrow.x += arrow.width
                    if not timer_started:
                        timer_started = True
                        start_time = pygame.time.get_ticks()
                else:
                    arrow.Arrow_Right()
            if event.key == pygame.K_LEFT:
                if arrow.left and (arrow.x - arrow.width , arrow.y) in path.coordinate:
                    arrow.x -= arrow.width
                    if not timer_started:
                        timer_started = True
                        start_time = pygame.time.get_ticks()
                else:
                    arrow.Arrow_Left()

            if event.key == pygame.K_UP:
                if arrow.up and (arrow.x , arrow.y - arrow.height) in path.coordinate:
                    arrow.y -= arrow.height
                    if not timer_started:
                        timer_started = True
                        start_time = pygame.time.get_ticks()
                else:
                    arrow.Arrow_Up()

            if event.key == pygame.K_DOWN:
                if arrow.down and (arrow.x, arrow.y + arrow.height) in path.coordinate:
                    arrow.y += arrow.height
                    if not timer_started:
                        timer_started = True
                        start_time = pygame.time.get_ticks()
                else:
                    arrow.Arrow_Down()

        # Fill the screen with white
        screen.fill(c.WHITE)

        ## from here is test,
        for (x,y) in c.grass_pts:
            if (x,y) not in path.coordinate:
                grass.draw(screen, x,y)

        ## test ened
        arrow.draw(screen)

        if timer_started:
            elapsed_time = pygame.time.get_ticks() - start_time
            timer_text = f"Time: {elapsed_time // 1000}s"
            text = c.font_small.render(timer_text, True, c.WHITE)
            screen.blit(text, (10, 10))

        clock.tick(FPS)
        pygame.display.update()