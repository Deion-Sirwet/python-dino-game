import pygame
import settings
import sprites

pygame.init()

# Set up the game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()

# Background image scaled
background = pygame.image.load('assets/prehistoric_background.jpg')
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, 500))

# Floor image scaled
floor = pygame.image.load('assets/floor.jpg')
floor = pygame.transform.scale(floor, (settings.SCREEN_WIDTH, 100))

# Game font and game name
game_font = pygame.font.Font('assets/prehistoric_bones.otf', 60)
game_name = game_font.render('Dino Hop', False, 'Black')
title_y_pos = -50
title_y_max = 50

# Player

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Screen layers
    screen.blit(background, (0, 0))
    screen.blit(floor, (0, 500))

    # Game name animation
    if title_y_pos < title_y_max:
        title_y_pos += 1.5
    screen.blit(game_name, (310, title_y_pos))

    # Update game
    pygame.display.flip()
    pygame.display.update()
    clock.tick(settings.FPS)