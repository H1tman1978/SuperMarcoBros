"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import sys

import pygame

from camera import Camera
from menu import show_start_menu
from settings import FPS, HEIGHT, WIDTH
from src.animations import luca_animations, marco_animations
from src.enemy import Enemy
from src.item import Item
from src.level_maps import level1_map
from src.platform_blocks import Platform
from src.player import Player
from src.sprite_loader import sprites

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Marco Bros")

# Set up the game clock
clock = pygame.time.Clock()

# Placeholder for sprite groups
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


def celebration():
    """Handles the celebration after the player wins the level."""
    celebration_running = True
    celebration_start_time = pygame.time.get_ticks()

    # Simple celebration animation (like flashing text)
    while celebration_running:
        screen.fill((0, 0, 0))  # Fill the screen with black

        # Show "Level Complete" message
        font = pygame.font.Font(None, 74)
        text = font.render("Level Complete!", True, (255, 255, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        # Celebration runs for 3 seconds before transitioning to end credits
        if pygame.time.get_ticks() - celebration_start_time > 3000:
            celebration_running = False

        pygame.display.flip()
        clock.tick(FPS)

    show_end_credits()


def show_end_credits():
    """Displays end credits after the celebration."""
    credits_running = True
    credits_text = [
        "Thanks for Playing!",
        "Created by Anthony Rolfe",
        "",
        "Music by Telaron and HorrorPen",
        "",
        "Graphics by",
        "Kenney Vleugels (www.kenney.nl)",
        "and Anthony Rolfe",
        "",
        "Lead Coding by Anthony Rolfe",
        "",
        "Additional Coding by",
        "chatGPT and JetBrains AI Assistant"
    ]

    # Set the starting position for scrolling credits
    y_offset = HEIGHT

    while credits_running:
        screen.fill((0, 0, 0))  # Clear the screen with black

        # Draw each line of the credits text
        font = pygame.font.Font(None, 48)
        for i, line in enumerate(credits_text):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_offset + i * 60))

        y_offset -= 2  # Scroll the text upwards

        # Allow the player to skip the credits by pressing the spacebar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    credits_running = False

        pygame.display.flip()
        clock.tick(FPS)

    # Allow the player to exit or restart the game after credits
    show_restart_screen()


def show_restart_screen():
    """Shows a screen that allows the player to restart the game or exit."""
    restart_running = True
    while restart_running:
        screen.fill((0, 0, 0))  # Clear the screen with black

        # Display restart/exit options
        font = pygame.font.Font(None, 74)
        text_restart = font.render("Press R to Restart", True, (255, 255, 255))
        text_exit = font.render("Press Q to Quit", True, (255, 255, 255))
        screen.blit(text_restart, (WIDTH // 2 - text_restart.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(text_exit, (WIDTH // 2 - text_exit.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_running = False
                    main()  # Restart the game by calling the main function
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def check_for_win():
    """Check if all enemies are killed, and if so, trigger the celebration."""
    if len(enemies) == 0:  # If the enemies group is empty
        celebration()


def load_level(player_selection, level_data, sprites, platforms, enemies, items, all_sprites):
    """Creates the level based on the provided map data."""

    # Calculate the total level width
    level_width = len(level_data['layout'][0]) * 32
    level_height = len(level_data['layout']) * 32

    # Load background image
    background_img = pygame.image.load(level_data['background_img']).convert()
    player = None

    # Loop through each row and column in the layout to create objects
    for row_idx, row in enumerate(level_data['layout']):
        for col_idx, char in enumerate(row.split(',')):
            x = col_idx * 32  # Assuming each tile is 32x32 pixels
            y = row_idx * 32

            # Use match/case to handle the different characters
            match char:
                case 'p':
                    platform_image = sprites.get('dirt')
                    platform = Platform(x, y, 32, 32, platform_image)
                    platforms.add(platform)
                    all_sprites.add(platform)

                case 'P':
                    if player_selection == 'Marco':
                        player = Player(marco_animations, x, y, level_width, level_height)
                    else:
                        player = Player(luca_animations, x, y, level_width, level_height)
                    all_sprites.add(player)

                case 'E':
                    enemy_type = level_data['enemy_types'][char]
                    if enemy_type == 'slime':
                        from animations import slime_enemy_animations
                        enemy = Enemy(slime_enemy_animations, x, y, 5, 200, platforms)
                        enemies.add(enemy)
                        all_sprites.add(enemy)

                case 'i':
                    item_type = level_data['item_types'][char]
                    if item_type == 'bad_shroom':
                        item = Item(sprites.get('mushroomBrown'), x, y, animated=False)
                        items.add(item)
                        all_sprites.add(item)

                case _:
                    pass

    # Set up the camera for this level (width and height should match the map's size)
    level_width = len(level_data['layout'][0]) * 32
    level_height = len(level_data['layout']) * 32
    camera = Camera(level_width, level_height)

    return background_img, player, camera


def check_collisions(player):
    """Handle all collisions in the game."""
    platform_collisions = pygame.sprite.spritecollide(player, platforms, False)
    if platform_collisions:
        if player.velocity_y > 0:  # If the player is falling
            player.rect.bottom = platform_collisions[0].rect.top
            player.velocity_y = 0
            player.is_jumping = False

    enemy_collision = pygame.sprite.spritecollide(player, enemies, False)
    if enemy_collision:
        if player.velocity_y > 0:
            enemy_collision[0].kill()  # Defeat enemy
        else:
            print("Player hit by enemy!")

    item_collision = pygame.sprite.spritecollide(player, items, True)
    if item_collision:
        print("Bad shroom collected!")
        player.reverse_controls()


def main():
    """Main game loop."""
    show_menu = True
    selected_character = ''
    game_running = True

    # Load level once after character selection
    background_img = None
    player = None
    camera = None

    while game_running:
        if show_menu:
            selected_character = show_start_menu(screen)
            if selected_character is not None:
                show_menu = False
                background_img, player, camera = load_level(selected_character, level1_map, sprites, platforms, enemies,
                                                            items,
                                                            all_sprites)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Update the camera to follow the player
        camera.update(player)

        # Clear the screen by drawing the background first
        screen.blit(background_img, (0, 0))

        # Update game state (player, enemies, etc.)
        all_sprites.update()

        # Check for collisions
        check_collisions(player)

        # Draw all sprites with the camera applied
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))

        # Check if all enemies are defeated
        check_for_win()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
