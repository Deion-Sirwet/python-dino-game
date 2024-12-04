import pygame
import settings
import sprites

pygame.init()

# Functions
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time /= 1000
    score_surf = exit_font.render(f'{current_time:.2f}', False, 'Black')
    score_rect = score_surf.get_rect(center = (400, 170))
    screen.blit(score_surf, score_rect)

def player_animation():
    global player_surf, player_jump_index, player_run_index, player_gravity

    # Check if player is in the air
    if player_pos.y < 385:  # Player is airborne
        # Reset jump animation index for a new jump
        if player_gravity < 0 and player_jump_index >= len(player_jump) - 1:
            player_jump_index = 0  # Start jump animation from the beginning
        
        # Progress through the jump animation frames
        player_jump_index += .6  # Control speed of jump animation
        if player_jump_index >= len(player_jump):  # Clamp index to avoid overshooting
            player_jump_index = len(player_jump) - 1  # Stay on the last jump frame
        
        player_surf = player_jump[int(player_jump_index)]
    else:  # Player is on the ground
        # Reset jump animation index when landing
        player_jump_index = 0

        # Progress through the walk animation frames
        player_run_index += 0.22  # Control speed of walk animation
        if player_run_index >= len(player_run):  # Loop the walk animation
            player_run_index = 0
        
        player_surf = player_run[int(player_run_index)]

# Variables (static)
clock = pygame.time.Clock()
title_y_pos = -50
title_y_max = 50
start_time = 0

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

# Exit message
exit_font = pygame.font.Font('assets/prehistoric_bones.otf', 60)
exit_msg = exit_font.render('Thanks for playing!', False, 'Black')

# Game over message
game_over_msg = exit_font.render('Game Over', False, 'Black')

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

# Player and Stone setup
player = pygame.image.load('assets/sprites/dino/Idle (1).png').convert_alpha()
player = pygame.transform.scale(player, (200, 130))

# Player animation photos (properly scale each sprite individually)
player_run_1 = pygame.image.load('assets/sprites/dino/Run (1).png').convert_alpha()
player_run_1 = pygame.transform.scale(player_run_1, (200, 130))  # Scale independently
player_run_2 = pygame.image.load('assets/sprites/dino/Run (2).png').convert_alpha()
player_run_2 = pygame.transform.scale(player_run_2, (200, 130))  # Scale independently
player_run_3 = pygame.image.load('assets/sprites/dino/Run (3).png').convert_alpha()
player_run_3 = pygame.transform.scale(player_run_3, (200, 130))
player_run_4 = pygame.image.load('assets/sprites/dino/Run (4).png').convert_alpha()
player_run_4 = pygame.transform.scale(player_run_4, (200, 130))
player_run_5 = pygame.image.load('assets/sprites/dino/Run (5).png').convert_alpha()
player_run_5 = pygame.transform.scale(player_run_5, (200, 130))
player_run_6 = pygame.image.load('assets/sprites/dino/Run (6).png').convert_alpha()
player_run_6 = pygame.transform.scale(player_run_6, (200, 130))
player_run_7 = pygame.image.load('assets/sprites/dino/Run (7).png').convert_alpha()
player_run_7 = pygame.transform.scale(player_run_7, (200, 130))
player_run_8 = pygame.image.load('assets/sprites/dino/Run (8).png').convert_alpha()
player_run_8 = pygame.transform.scale(player_run_8, (200, 130))

# Combine all run animations into a list
player_run = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8]
player_run_index = 0

# Player jumping animation frames (scaled independently)
player_jump_1 = pygame.image.load('assets/sprites/dino/Jump (1).png').convert_alpha()
player_jump_1 = pygame.transform.scale(player_jump_1, (200, 130))
player_jump_2 = pygame.image.load('assets/sprites/dino/Jump (2).png').convert_alpha()
player_jump_2 = pygame.transform.scale(player_jump_2, (200, 130))
player_jump_3 = pygame.image.load('assets/sprites/dino/Jump (3).png').convert_alpha()
player_jump_3 = pygame.transform.scale(player_jump_3, (200, 130))
player_jump_4 = pygame.image.load('assets/sprites/dino/Jump (4).png').convert_alpha()
player_jump_4 = pygame.transform.scale(player_jump_4, (200, 130))
player_jump_5 = pygame.image.load('assets/sprites/dino/Jump (5).png').convert_alpha()
player_jump_5 = pygame.transform.scale(player_jump_5, (200, 130))
player_jump_6 = pygame.image.load('assets/sprites/dino/Jump (6).png').convert_alpha()
player_jump_6 = pygame.transform.scale(player_jump_6, (200, 130))
player_jump_7 = pygame.image.load('assets/sprites/dino/Jump (7).png').convert_alpha()
player_jump_7 = pygame.transform.scale(player_jump_7, (200, 130))
player_jump_8 = pygame.image.load('assets/sprites/dino/Jump (8).png').convert_alpha()
player_jump_8 = pygame.transform.scale(player_jump_8, (200, 130))
player_jump_9 = pygame.image.load('assets/sprites/dino/Jump (9).png').convert_alpha()
player_jump_9 = pygame.transform.scale(player_jump_9, (200, 130))
player_jump_10 = pygame.image.load('assets/sprites/dino/Jump (10).png').convert_alpha()
player_jump_10 = pygame.transform.scale(player_jump_10, (200, 130))
player_jump_11 = pygame.image.load('assets/sprites/dino/Jump (11).png').convert_alpha()
player_jump_11 = pygame.transform.scale(player_jump_11, (200, 130))
player_jump_12 = pygame.image.load('assets/sprites/dino/Jump (12).png').convert_alpha()
player_jump_12 = pygame.transform.scale(player_jump_12, (200, 130))
player_jump_index = 0

# Combine all jump animations into a list
player_jump = [player_jump_1, player_jump_2, player_jump_3, player_jump_4, player_jump_5, player_jump_6, player_jump_7, player_jump_8, player_jump_9, player_jump_10, player_jump_11, player_jump_12]

# Stone setup
stone_surf = pygame.image.load('assets/stone.png').convert_alpha()

# Create masks for the player's and stone's ellipses directly
# Player's ellipse
player_width, player_height = player.get_size()
player_width *= .5
ellipse_surface_player = pygame.Surface((player_width, player_height), pygame.SRCALPHA)
pygame.draw.ellipse(ellipse_surface_player, (255, 255, 255), (0, 0, player_width, player_height))
ellipse_mask_player = pygame.mask.from_surface(ellipse_surface_player)

# Stone's ellipse
stone_width, stone_height = stone_surf.get_size()
ellipse_surface_stone = pygame.Surface((stone_width, stone_height), pygame.SRCALPHA)
pygame.draw.ellipse(ellipse_surface_stone, (255, 255, 255), (0, 0, stone_width, stone_height))
ellipse_mask_stone = pygame.mask.from_surface(ellipse_surface_stone)

# Positions of the player and stone (directly used without rect)
player_pos = pygame.Vector2(300, 385)  # Player position (center)
stone_pos = pygame.Vector2(700, 441)  # Stone position (center)

# Main game loop
running = True
game_active = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_pos.y >= 385:
                player_gravity = -18

    # Update the screen (background and floor)
    screen.blit(background, (0, 0))  # Redraw the background
    screen.blit(floor, (0, 500))
    screen.blit(game_name, (265, title_y_pos))

    if game_active:
        # Variables (dynamic)
        mouse_pos = pygame.mouse.get_pos()

        # Score
        display_score()

        # Move the stone
        stone_pos.x -= 8
        if stone_pos.x <= -100:
            stone_pos.x = 900  # Reset stone position when it goes off-screen

        # Draw the stone
        screen.blit(stone_surf, stone_pos)

        # Draw the stone's collision ellipse (for visualization)
        pygame.draw.ellipse(screen, (255, 0, 0), (stone_pos.x, stone_pos.y, stone_width, stone_height), 2)


        # Draw the player's collision ellipse (for visualization)
        pygame.draw.ellipse(screen, (0, 255, 0), (player_pos.x, player_pos.y, player_width, player_height), 2)

        # Player movement (gravity)
        player_gravity += 1
        player_pos.y += player_gravity
        if player_pos.y >= 385:
            player_pos.y = 385
        player_animation()
        screen.blit(player_surf, player_pos)

        # Check for collision using ellipse masks (overlap)
        offset = (stone_pos.x - player_pos.x, stone_pos.y - player_pos.y)
        if ellipse_mask_player.overlap(ellipse_mask_stone, offset):
            screen.blit(game_over_msg, (265, 200))
            game_active = False
            pygame.display.flip()
            pygame.time.delay(1500)
    
    else:
        # Variables (dynamic)
        mouse_pos = pygame.mouse.get_pos()

        # Screen layers
        screen.blit(background, (0, 0))
        screen.blit(floor, (0, 500))
        screen.blit(stone_surf, stone_pos)
        screen.blit(player, player_pos)

        # Game title
        if title_y_pos < title_y_max:
            title_y_pos += 1.5
        screen.blit(game_name, (265, title_y_pos))

        screen.blit(play_but, play_rect)
        if play_rect.collidepoint(mouse_pos):  # Check if mouse is over play button
            if pygame.mouse.get_pressed()[0]:  # Check if mouse is clicked
                game_active = True  # Start the game
                # Optionally, reset any game variables here (like stone position)
                stone_pos.x = 700  # Reset stone position
                player_pos.y = 500  # Reset player position
                player_gravity = 0  # Reset gravity
                start_time = pygame.time.get_ticks()
                pygame.time.delay(120)  # Optional delay for responsiveness

        # Draw exit button
        screen.blit(exit_but, exit_rect)
        if exit_rect.collidepoint(mouse_pos):  # Check if mouse is over exit button
            if pygame.mouse.get_pressed()[0]:  # Check if mouse is clicked
                screen.blit(play_but, play_rect)
                screen.blit(exit_but_press, exit_rect)
                pygame.display.flip()
                pygame.time.delay(120)

                screen.blit(exit_but, exit_rect)
                screen.blit(exit_msg, (175, 250))
                pygame.display.flip()
                pygame.time.delay(1800)

                running = False

    # Update game screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(settings.FPS)
