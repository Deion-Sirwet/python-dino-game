import pygame
import settings
import sprites

pygame.init()

# Variables (static)
clock = pygame.time.Clock()
title_y_pos = -50
title_y_max = 40
game_active = False
show_play_but = True

# Set up the game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Background image scaled
background = pygame.image.load('assets/prehistoric_background.jpg').convert()
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, 500))

# Floor image scaled
floor = pygame.image.load('assets/floor.jpg').convert()
floor = pygame.transform.scale(floor, (settings.SCREEN_WIDTH, 100))

# Game font and game name
game_font = pygame.font.Font('assets/prehistoric_bones.otf', 80)
game_name = game_font.render('Dino Hop', False, 'Black')

# Score keeper
score = 0
score_font = pygame.font.Font('assets/prehistoric_bones.otf', 60)
score_surf = score_font.render(str(score), True, 'Black')
score_rect = score_surf.get_rect(center = (400, 150))

# Play buttons
play_but = pygame.image.load('assets/buttons/PlayBtn.png')
play_but = pygame.transform.scale(play_but, (100, 50))
play_rect = play_but.get_rect(topleft = (10, 10))
play_but_press = pygame.image.load('assets/buttons/PlayClick.png')
play_but_press = pygame.transform.scale(play_but_press, (100, 50))

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
player = pygame.image.load('assets/sprites/dino/Idle (1).png').convert_alpha()
player = pygame.transform.scale(player, (200, 130))
player_rect = player.get_bounding_rect()
player_rect.center = (370, 450)

# Player gravity
player_gravity = 0

# Stone
stone_surf = pygame.image.load('assets/stone.png').convert_alpha()
stone_surf = pygame.transform.scale(stone_surf, (100, 100))
stone_rect = stone_surf.get_bounding_rect()
stone_rect.center = (700, 470)

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 515:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -17

            if event.type == pygame.KEYDOWN and player_rect.bottom >= 515:
                if event.key == pygame.K_SPACE:
                    player_gravity = -17

    if game_active:
        # Variables (dynamic)
        mouse_pos = pygame.mouse.get_pos()

        # Screen layers
        screen.blit(background, (0, 0))
        screen.blit(floor, (0, 500))
        screen.blit(score_surf, score_rect)
        stone_rect.x -= 5.8
        screen.blit(stone_surf, stone_rect)

        # Game name animation
        if title_y_pos < title_y_max:
            title_y_pos += 1.5
        screen.blit(game_name, (265, title_y_pos))

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 515:
            player_rect.bottom = 515
        screen.blit(player, player_rect)

        # End game if collision
        if stone_rect.colliderect(player_rect):
            print("Collision")
            # game_active = False

        # Exit button
        screen.blit(exit_but, exit_rect)
        if exit_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                screen.blit(exit_but_press, exit_rect)
                pygame.display.flip()
                pygame.time.delay(120)

                screen.blit(exit_but, exit_rect)
                screen.blit(exit_msg, (210, 250))
                pygame.display.flip()
                pygame.time.delay(2000)

                running = False
                
        # # Play button
        # if show_play_but:
        #     screen.blit(play_but, play_rect)
        #     if play_rect.collidepoint(mouse_pos):
        #         if pygame.mouse.get_pressed()[0]:
        #             game_active = True
        #             screen.blit(play_but_press, play_rect)
        #             pygame.display.flip()
        #             pygame.time.delay(120)
        #             show_play_but = False
        #             stone_x_pos += 1
    else:
        # Variables (dynamic)
        mouse_pos = pygame.mouse.get_pos()

        # Screen layers
        screen.blit(background, (0, 0))
        screen.blit(floor, (0, 500))
        screen.blit(score_surf, score_rect)
        screen.blit(stone_surf, stone_rect)
        # To visualize the new hitbox for debugging
        pygame.draw.rect(screen, (255, 0, 0), stone_rect, 2)

        # Game name animation
        if title_y_pos < title_y_max:
            title_y_pos += 1.5
        screen.blit(game_name, (265, title_y_pos))

        # Player
        screen.blit(player, player_rect)
        # To visualize the new hitbox for debugging
        pygame.draw.rect(screen, (255, 0, 0), player_rect, 2)

        # Exit button
        screen.blit(exit_but, exit_rect)
        if exit_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                screen.blit(exit_but_press, exit_rect)
                pygame.display.flip()
                pygame.time.delay(120)

                screen.blit(exit_but, exit_rect)
                screen.blit(exit_msg, (210, 250))
                pygame.display.flip()
                pygame.time.delay(2000)

                running = False
                
        # Play button
        if show_play_but:
            screen.blit(play_but, play_rect)
            if play_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    game_active = True
                    screen.blit(play_but_press, play_rect)
                    pygame.display.flip()
                    pygame.time.delay(120)
                    show_play_but = False
                
    # Update game
    pygame.display.flip()
    pygame.display.update()
    clock.tick(settings.FPS)