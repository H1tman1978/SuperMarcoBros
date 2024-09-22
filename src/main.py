"""
main.py
Entry point for Super Marco Bros game using PyGame.
"""

import sys
import pygame
from menu import show_start_menu
from settings import BACKGROUND_IMAGE, FPS, HEIGHT, WIDTH
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


def load_level(player_selection, level_data, sprites, platforms, enemies, items, all_sprites):
    """Creates the level based on the provided map data."""

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
                        player = Player(marco_animations, x, y)
                    else:
                        player = Player(luca_animations, x, y)
                    all_sprites.add(player)

                case 'E':
                    enemy_type = level_data['enemy_types'][char]
                    if enemy_type == 'slime':
                        from animations import slime_enemy_animations
                        enemy = Enemy(slime_enemy_animations, x, y, 10, 50)
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

    return background_img, player


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

    while game_running:
        if show_menu:
            selected_character = show_start_menu(screen)
            if selected_character is not None:
                show_menu = False
                background_img, player = load_level(selected_character, level1_map, sprites, platforms, enemies, items,
                                                    all_sprites)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Clear the screen by drawing the background first
        screen.blit(background_img, (0, 0))

        # Update game state (player, enemies, etc.)
        all_sprites.update()

        # Check for collisions
        check_collisions(player)

        # Draw all sprites (player, etc.)
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
