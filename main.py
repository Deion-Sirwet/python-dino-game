import pygame
import settings
import random
import os

pygame.init()

# Functions
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time /= 1000
    score_surf = exit_font.render(f'{int(current_time)}', False, 'Black')
    score_rect = score_surf.get_rect(center = (400, 170))
    screen.blit(score_surf, score_rect)

def display_high_score():
    # High score font
    hs_font = pygame.font.Font('assets/prehistoric_bones.otf', 30)
    # High score surface
    hs_surf = hs_font.render(f'High Score: {high_score}', False, 'Black')
    hs_score_rect = hs_surf.get_rect(topleft=(120, 10))
    screen.blit(hs_surf, hs_score_rect)

def player_animation():
    global player, player_jump_index, player_run_index, player_gravity

    # Check if player is in the air
    if player_rect.y < 385:  # Player is airborne
        # Reset jump animation index for a new jump
        if player_gravity < 0 and player_jump_index >= len(player_jump) - 1:
            player_jump_index = 0  # Start jump animation from the beginning
        
        # Progress through the jump animation frames
        player_jump_index += .6  # Control speed of jump animation
        if player_jump_index >= len(player_jump):  # Clamp index to avoid overshooting
            player_jump_index = len(player_jump) - 1  # Stay on the last jump frame
        
        player = player_jump[int(player_jump_index)]
    else:  # Player is on the ground
        # Reset jump animation index when landing
        player_jump_index = 0

        # Progress through the walk animation frames
        player_run_index += 0.22  # Control speed of walk animation
        if player_run_index >= len(player_run):  # Loop the walk animation
            player_run_index = 0
        
        player = player_run[int(player_run_index)]

def dead_animation():
    global player_dead_index, player

    # Progress through the death animation frames
    if player_dead_index < len(player_dead):
        player = player_dead[int(player_dead_index)]  # Set player surface to death frame
        player_dead_index += 0.22  # Adjust speed
    else:
        # Stay on the last frame after animation finishes
        player_dead_index = len(player_dead) - 1
        player = player_dead[int(player_dead_index)]  # Ensure player surface stays on last frame

def draw_scrolling_background():
    global bg_x1, bg_x2

    # Move both background images to the left
    bg_x1 -= bg_scroll_speed
    bg_x2 -= bg_scroll_speed

    # If a background image moves completely off the screen, reset it to the right
    if bg_x1 <= -settings.SCREEN_WIDTH:
        bg_x1 = settings.SCREEN_WIDTH
    if bg_x2 <= -settings.SCREEN_WIDTH:
        bg_x2 = settings.SCREEN_WIDTH

    # Draw the two background images
    screen.blit(background, (bg_x1, 0))
    screen.blit(background, (bg_x2, 0))

def draw_scrolling_floor():
    global floor_x1, floor_x2

    # Move both floor images to the left
    floor_x1 -= floor_scroll_speed
    floor_x2 -= floor_scroll_speed

    # If a floor image moves completely off the screen, reset it to the right
    if floor_x1 <= -settings.SCREEN_WIDTH:
        floor_x1 = settings.SCREEN_WIDTH
    if floor_x2 <= -settings.SCREEN_WIDTH:
        floor_x2 = settings.SCREEN_WIDTH

    # Draw the two floor images
    screen.blit(floor, (floor_x1, settings.SCREEN_HEIGHT - 100))  # Adjust Y position to place it at the bottom
    screen.blit(floor, (floor_x2, settings.SCREEN_HEIGHT - 100))

def read_high_score():
    if os.path.exists(high_score_file):
        with open(high_score_file, 'r') as file:
            try:
                return int(file.read())  # Read and return the high score as an integer
            except ValueError:
                return 0  # If the file is empty or contains invalid data, return 0
    return 0  # Return 0 if the file doesn't exist

def save_high_score(score):
    with open(high_score_file, 'w') as file:
        file.write(str(score))  # Save the high score as a string


# Variables (static)
clock = pygame.time.Clock()
title_y_pos = -50
title_y_max = 50
start_time = 0
high_score_file = "high_score.txt"
high_score = read_high_score()

# Set up the game window
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Dino Dashin'")

# Background image scaled
background = pygame.image.load('assets/prehistoric_background.jpg').convert()
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, 500))

# Initialize positions for the scrolling background
bg_x1 = 0  # First background image
bg_x2 = settings.SCREEN_WIDTH  # Second background image starts after the first

bg_scroll_speed = 1  # Background scroll speed (slower for depth effect)

# Floor image scaled
floor = pygame.image.load('assets/floor.jpg').convert()
floor = pygame.transform.scale(floor, (settings.SCREEN_WIDTH, 100))

# Initialize positions for the scrolling floor
floor_x1 = 0  # First floor image
floor_x2 = settings.SCREEN_WIDTH  # Second floor image starts after the first

floor_scroll_speed = 8  # Floor scroll speed (faster to simulate closer perspective)

# Game font and game name
game_font = pygame.font.Font('assets/prehistoric_bones.otf', 80)
game_name = game_font.render('Dino Dashin\'', False, 'Black')

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

# Player
player = pygame.image.load('assets/sprites/dino/Idle (1).png').convert_alpha()
player = pygame.transform.scale(player, (200, 130))
player_rect = player.get_rect()
player_mask = pygame.mask.from_surface(player)
mask_image = player_mask.to_surface()

# Position the player
player_rect.topleft = (300, 385)

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

# Player dead animation frames (scaled independently)
player_dead_1 = pygame.image.load('assets/sprites/dino/Dead (1).png').convert_alpha()
player_dead_1 = pygame.transform.scale(player_dead_1, (200, 130))
player_dead_2 = pygame.image.load('assets/sprites/dino/Dead (2).png').convert_alpha()
player_dead_2 = pygame.transform.scale(player_dead_2, (200, 130))
player_dead_3 = pygame.image.load('assets/sprites/dino/Dead (3).png').convert_alpha()
player_dead_3 = pygame.transform.scale(player_dead_3, (200, 130))
player_dead_4 = pygame.image.load('assets/sprites/dino/Dead (4).png').convert_alpha()
player_dead_4 = pygame.transform.scale(player_dead_4, (200, 130))
player_dead_5 = pygame.image.load('assets/sprites/dino/Dead (5).png').convert_alpha()
player_dead_5 = pygame.transform.scale(player_dead_5, (200, 130))
player_dead_6 = pygame.image.load('assets/sprites/dino/Dead (6).png').convert_alpha()
player_dead_6 = pygame.transform.scale(player_dead_6, (200, 130))
player_dead_7 = pygame.image.load('assets/sprites/dino/Dead (7).png').convert_alpha()
player_dead_7 = pygame.transform.scale(player_dead_7, (200, 130))
player_dead_8 = pygame.image.load('assets/sprites/dino/Dead (8).png').convert_alpha()
player_dead_8 = pygame.transform.scale(player_dead_8, (200, 130))
player_dead_index = 0

# Combine all dead animations into a list
player_dead = [player_dead_1, player_dead_2, player_dead_3, player_dead_4, player_dead_5, player_dead_6, player_dead_7, player_dead_8]

# Stone setup (obstacle)
stone_surf = pygame.image.load('assets/stone.png').convert_alpha()
stone_rect = stone_surf.get_rect()
stone_mask = pygame.mask.from_surface(stone_surf)

obstacle_list = []
min_obstacle_distance = 250  # Adjust this value to control spacing

# Position the stone
stone_rect.topleft = (700, 445)

# Obstacle timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, random.randint(900, 1100))

# Main game loop
running = True
game_active = False
is_dead = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if game_active:
            if not is_dead:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.y >= 385:
                        player_gravity = -18

            # Obstacle logic
            if event.type == obstacle_timer:
                # Create a new obstacle and its mask
                new_stone_rect = stone_surf.get_rect(midtop=(random.randint(800, 1200), 445))
                new_stone_mask = pygame.mask.from_surface(stone_surf)
                
                # Ensure new obstacle is spaced properly
                if not obstacle_list or new_stone_rect.x - obstacle_list[-1]['rect'].x > min_obstacle_distance:
                    # Append a tuple of the rect and mask to the obstacle list
                    obstacle_list.append({'rect': new_stone_rect, 'mask': new_stone_mask})


    # Update the screen (background and floor)
    draw_scrolling_background()
    draw_scrolling_floor()
    screen.blit(game_name, (205, title_y_pos))

    if game_active:
        # Move the stone
        # Update obstacle positions
        for obstacle in obstacle_list[:]:  # Use a copy of the list for safe iteration
            obstacle['rect'].x -= 8  # Move obstacles to the left
            if obstacle['rect'].right < 0:  # Remove off-screen obstacles
                obstacle_list.remove(obstacle)
        
        # Draw obstacles
        for obstacle in obstacle_list:
            screen.blit(stone_surf, obstacle['rect'])

        # Player movement (gravity)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.y >= 385:
            player_rect.y = 385

        if not is_dead:
            # Variables (dynamic)
            mouse_pos = pygame.mouse.get_pos()

            # Score
            display_score()
            display_high_score()

            player_animation()
            screen.blit(player, player_rect)

            # Check for collisions
            for obstacle in obstacle_list:
                offset = (obstacle['rect'].x - player_rect.x, obstacle['rect'].y - player_rect.y)
                if player_mask.overlap(obstacle['mask'], offset):
                    is_dead = True
                    player_dead_index = 0

        else:
            dead_animation()  # Update the death animation frame
            screen.blit(player, player_rect)  # Draw the current frame of the death animation
            screen.blit(game_over_msg, (265, 200))  # Display the "Game Over" message
            display_score()
            display_high_score()
           
            # Set final score
            final_score = int((pygame.time.get_ticks() - start_time) / 1000)

            # Update high score if necessary
            if final_score > high_score:
                high_score = final_score
                save_high_score(high_score)  # Save the new high score

            # Check if the animation has finished
            if int(player_dead_index) >= len(player_dead):
                # After the animation ends, stop the game or reset
                pygame.display.flip()
                pygame.time.delay(1500)  # Optional delay after animation
                game_active = False

    else:
        # Variables (dynamic)
        mouse_pos = pygame.mouse.get_pos()

        # Screen layers
        screen.blit(background, (0, 0))
        screen.blit(floor, (0, 500))
        screen.blit(player, player_rect)
        display_high_score()

        # Game title
        if title_y_pos < title_y_max:
            title_y_pos += 1.5
        screen.blit(game_name, (205, title_y_pos))

        screen.blit(play_but, play_rect)
        if play_rect.collidepoint(mouse_pos):  # Check if mouse is over play button
            if pygame.mouse.get_pressed()[0]:  # Check if mouse is clicked
                game_active = True  # Start the game
                # Optionally, reset any game variables here (like stone position)
                stone_rect.x = 700  # Reset stone position
                player_rect.y = 500  # Reset player position
                player_gravity = 0  # Reset gravity
                is_dead = False # Reset is_dead boolean
                # Reset background positions
                bg_x1 = 0
                bg_x2 = settings.SCREEN_WIDTH
                # Reset floor positions
                floor_x1 = 0
                floor_x2 = settings.SCREEN_WIDTH
                # Reset obstacle list
                obstacle_list = []
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
