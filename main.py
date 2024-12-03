import pygame
import settings
import sprites

pygame.init()

# Variables (static)
clock = pygame.time.Clock()
title_y_pos = -50
title_y_max = 50

# Set up the game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Background image scaled
background = pygame.image.load('assets/prehistoric_background.jpg')
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, 500))

# Floor image scaled
floor = pygame.image.load('assets/floor.jpg')
floor = pygame.transform.scale(floor, (settings.SCREEN_WIDTH, 100))

# Game font and game name
game_font = pygame.font.Font('assets/prehistoric_bones.otf', 80)
game_name = game_font.render('Dino Hop', False, 'Black')

# Play buttons
play_but = pygame.image.load('assets/buttons/PlayBtn.png')
play_but = pygame.transform.scale(play_but, (100, 50))
play_rect = play_but.get_rect(topleft = (10, 10))

# Exit buttons
exit_but = pygame.image.load('assets/buttons/ExitBtn.png')
exit_but = pygame.transform.scale(exit_but, (100, 50))
exit_rect = exit_but.get_rect(topleft = (690, 10))
exit_but_press = pygame.image.load('assets/buttons/ExitClick.png')
exit_but_press = pygame.transform.scale(exit_but_press, (100, 50))

# Exit message
exit_font = pygame.font.Font('assets/prehistoric_bones.otf', 50)
exit_msg = exit_font.render('Thanks for playing!', False, 'Black')

# Player
player = pygame.image.load('assets/sprites/dino/Idle (1).png')
player = pygame.transform.scale(player, (200, 130))
player_rect = player.get_rect(midbottom = (430, 515))

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Variables (dynamic)
    mouse_pos = pygame.mouse.get_pos()

    # Screen layers
    screen.blit(background, (0, 0))
    screen.blit(floor, (0, 500))

    # Game name animation
    if title_y_pos < title_y_max:
        title_y_pos += 1.5
    screen.blit(game_name, (265, title_y_pos))

    # Player
    screen.blit(player, player_rect)

    # Buttons
    screen.blit(exit_but, exit_rect)
    if exit_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            screen.blit(play_but, play_rect)
            screen.blit(exit_but_press, exit_rect)
            pygame.display.flip()
            pygame.time.delay(120)

            screen.blit(exit_but, exit_rect)
            screen.blit(exit_msg, (210, 250))
            pygame.display.flip()
            pygame.time.delay(2000)

            running = False
            
    screen.blit(play_but, play_rect)

    # Update game
    pygame.display.flip()
    pygame.display.update()
    clock.tick(settings.FPS)