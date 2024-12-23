import pygame
import sys
from objects import Arrow, Grass, Path, Button
import constant as c

# Initialize Pygame
pygame.init()

# Set up display

window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Arrow Runner")

# Set up a clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

#Page
Home_Page = True
Instruction_Page = False
Play_Page = False
GameOver_Page = False
GameWon_Page = False 
nextlevel_error = False

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while Home_Page:
        window.fill(c.WHITE)
        title_text = c.font_small.render("Welcome to the Arrow Runner!", True, c.BLACK)
        window.blit(title_text, ((800 - title_text.get_width()) // 2, 100))

        play_button = Button("PLAY", window, c.HEIGHT//2-50)
        instruction_button = Button ("Game Instruction", window, c.HEIGHT// 2 + 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (play_button.x <= mouse_x <= play_button.x + play_button.width and
                        play_button.y <= mouse_y <= play_button.y + play_button.height):
                    Play_Page = True
                    Home_Page = False
                    arrow = Arrow(50)
                    grass = Grass()
                    path = Path()
                    timer_started = False
                    start_time = 0
                    countdown_time = 10000

                if (instruction_button.x <= mouse_x <= instruction_button.x+ instruction_button.width and
                        instruction_button.y <= mouse_y <= instruction_button.y + instruction_button.height):
                    Instruction_Page = True
                    Home_Page = False
            if event.type == pygame.QUIT:
                Home_Page = False
                running = False

    while Play_Page:     

        if arrow.x == c.WIDTH - arrow.width and arrow.y == 0:
            Play_Page = False
            GameWon_Page = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Play_Page = False
                running = False
            if event.type == pygame.KEYDOWN:
                if not timer_started:
                    timer_started = True
                    start_time = pygame.time.get_ticks()
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
        window.fill(c.WHITE)

        ## from here is test,
        for (x,y) in c.grass_pts:
            if (x,y) not in path.coordinate:
                grass.draw(window, x,y)

        ## test ened
        arrow.draw(window)
        if not timer_started:
            text = f"Level {path.level} // Time: {countdown_time // 1000}s"
            text = c.font_small.render(text, True, c.WHITE)
            window.blit(text, (10, 10))

        if timer_started:
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(countdown_time - elapsed_time, 0) 
            timer_text = f"Level {path.level} // Time: {remaining_time // 1000}s"
        
            if remaining_time == 0:
                Play_Page = False
                GameOver_Page = True

            text = c.font_small.render(timer_text, True, c.WHITE)
            window.blit(text, (10, 10))
        
        clock.tick(FPS)
        pygame.display.update()

    while Instruction_Page:
        window.fill(c.WHITE)
        instruction = """Use Arrows to move the arrow.
You have to reach the end of
the path within the given time.
The arrow uses one move to
change its direction.
(For example, if the arrow is
facing upwards, but you have to
go to the right, the first right
click will change the direction
of the arrow first, and the next
right click will move the arrow.)"""

        lines = instruction.split('\n')
        y = 100
        for line in lines: 
            line_text = c.font_small.render(line, True, c.BLACK)
            window.blit(line_text, ((c.WIDTH - line_text.get_width())//2 , y))
            y += line_text.get_height() + 5

        back_button = Button("BACK", window, c.HEIGHT - 100)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Instruction_Page = False
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (back_button.x <= mouse_x <= back_button.x + back_button.width and
                        back_button.y <= mouse_y <= back_button.y + back_button.height):
                    Home_Page = True
                    Instruction_Page = False

    while GameOver_Page:
        window.fill(c.WHITE)
        gameover_text = c.font_small.render("Game Over!", True, c.BLACK)
        window.blit(gameover_text, ((800 - gameover_text.get_width()) // 2, 100))

        home_button = Button("Go to Home", window, c.HEIGHT-100)
        pygame.display.update()   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameOver_Page = False        
                running = False         
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (home_button.x <= mouse_x <= home_button.x + home_button.width and
                        home_button.y <= mouse_y <= home_button.y + home_button.height):
                    GameOver_Page = False
                    Home_Page = True

    while GameWon_Page:
        window.fill(c.WHITE)
        gamewon_text = c.font_small.render("You won the game", True, c.BLACK)
        window.blit(gamewon_text, ((800 - gamewon_text.get_width()) // 2, 100))

        home_button = Button("Go to Home", window, c.HEIGHT-100)
        nextlevel_button = Button("Next Level", window, c.HEIGHT-200)
        pygame.display.update()   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameWon_Page = False        
                running = False         
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (home_button.x <= mouse_x <= home_button.x + home_button.width and
                        home_button.y <= mouse_y <= home_button.y + home_button.height):
                    GameWon_Page = False
                    Home_Page = True
                if (nextlevel_button.x <= mouse_x <= nextlevel_button.x + nextlevel_button.width and
                        nextlevel_button.y <= mouse_y <= nextlevel_button.y + nextlevel_button.height):
                    if path.level == 3: 
                        GameWon_Page = False
                        nextlevel_error = True
                        
                    else:
                        GameWon_Page = False
                        Play_Page = True
                        arrow = Arrow(50)
                        grass = Grass()
                        path.LevelUp()
                        if path.level == 2:
                            path.coordinate = c.Level2_path
                            timer_started = False
                            start_time = 0
                            countdown_time = 10000
                        if path.level == 3:
                            path.coordinate = c.Level3_path
                            timer_started = False
                            start_time = 0
                            countdown_time = 15000


    while nextlevel_error:
        window.fill(c.WHITE)
        text = c.font_small.render("Sorry, next level is still in progress", True, c.BLACK)
        window.blit(text, ((800 - text.get_width()) // 2, 100))

        home_button = Button("Go to Home", window, c.HEIGHT-100)
        pygame.display.update()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nextlevel_error = False        
                running = False   
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (home_button.x <= mouse_x <= home_button.x + home_button.width 
                    and home_button.y <= mouse_y <= home_button.y + home_button.height):
                    nextlevel_error = False
                    Home_Page = True                     

# Quit Pygame
pygame.quit()
sys.exit()
